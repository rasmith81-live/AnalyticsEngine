from fastapi import FastAPI, HTTPException, Body, UploadFile, File, Query
from typing import Dict, Any, List
import os
import httpx
from .industry_knowledge_base import NAICClassificationIterator
from .semantic_mapping import KPIDecomposer
from .similarity_engine import SimilarityEngine
from .excel_processor import KPIExcelProcessor

app = FastAPI(title="Metadata Ingestion Service", version="0.1.0")

# Configuration
BUSINESS_METADATA_URL = os.getenv("BUSINESS_METADATA_URL", "http://business_metadata:8000")

# Initialize Engines
naic_iterator = NAICClassificationIterator()
kpi_decomposer = KPIDecomposer(entity_resolution_service_url="http://entity-resolution-service")
similarity_engine = SimilarityEngine()
excel_processor = KPIExcelProcessor()

# In-memory storage for import sessions (Note: Use Redis in production)
import_cache: Dict[str, List[Dict[str, Any]]] = {}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "metadata_ingestion_service"}

# ... (Industry Knowledge and Semantic Mapping endpoints remain the same) ...

# Industry Knowledge Endpoints
@app.get("/knowledge/industries", response_model=List[Dict[str, Any]])
async def list_industries():
    """List available industry classifications."""
    results = []
    async for industry in naic_iterator.iterate_industries():
        results.append(industry)
    return results

@app.get("/knowledge/industries/{code}/value-chain")
async def get_industry_value_chain(code: str):
    """Get standard value chain for an industry."""
    return await naic_iterator.generate_value_chain_set(code)

@app.get("/knowledge/industries/{code}/kpis")
async def get_industry_kpis(code: str):
    """Get best practice KPIs for an industry."""
    return await naic_iterator.generate_best_practice_kpis(code)

# Semantic Mapping Endpoints
@app.post("/mapping/decompose")
async def decompose_kpi(
    formula: str = Body(..., embed=True)
):
    """Decompose a KPI formula into components."""
    try:
        # 1. Decompose
        decomposed = await kpi_decomposer.decompose_formula(formula)
        
        # 2. Resolve (Mocked in decomposer currently)
        attributes = decomposed.get("identified_attributes", [])
        resolved = await kpi_decomposer.resolve_components(attributes)
        
        return {
            "decomposed": decomposed,
            "resolved_components": resolved
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/mapping/check-similarity")
async def check_kpi_similarity(
    new_kpi: Dict[str, Any] = Body(..., description="Candidate KPI definition"),
    existing_kpis: List[Dict[str, Any]] = Body(..., description="List of existing KPIs to compare against")
):
    """
    Check for potential duplicates/similar KPIs based on name and description.
    Returns a list of matches with similarity scores.
    """
    try:
        matches = similarity_engine.find_potential_duplicates(new_kpi, existing_kpis)
        return {"matches": matches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Similarity check failed: {str(e)}")

# Excel Import Endpoints
import uuid

# ... (rest of imports)

@app.post("/import/upload")
async def upload_excel(file: UploadFile = File(...)):
    """
    Upload and process an Excel/CSV file containing KPI definitions.
    Returns parsed KPIs, validation errors, and similarity warnings.
    """
    try:
        # 1. Parse File
        valid_kpis_data, parser_errors = excel_processor.parse_stream(file.file, file.filename)
        
        # 2. Validate & Enhance (Mocking existing KPIs for now)
        # In a real scenario, we would fetch existing KPIs from Business Metadata Service
        existing_kpis_mock = [] 
        
        # Generate Import ID
        import_id = str(uuid.uuid4())
        
        results = {
            "importId": import_id,
            "totalRows": len(valid_kpis_data) + len(parser_errors),
            "validRows": 0,
            "errors": parser_errors,
            "preview": [],
            "duplicates": []
        }
        
        final_valid_kpis = []
        
        for kpi in valid_kpis_data:
            # Perform additional validation if needed
            # Check for duplicates
            duplicates = similarity_engine.find_potential_duplicates(kpi, existing_kpis_mock)
            
            row_data = {
                "Name": kpi.get("name"),
                "Formula": kpi.get("formula"),
                "Code": kpi.get("code"),
                "Metadata": kpi.get("metadata")
            }
            
            if duplicates:
                results["duplicates"].append({
                    "kpi": row_data,
                    "matches": duplicates
                })
            
            final_valid_kpis.append(kpi)
            results["preview"].append(row_data)

        results["validRows"] = len(final_valid_kpis)
        
        # Cache valid KPIs for commit
        if final_valid_kpis:
            import_cache[import_id] = final_valid_kpis
        
        # We limit preview to top 20
        results["preview"] = results["preview"][:20]
        
        return results

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")

@app.post("/import/{import_id}/commit")
async def commit_import(
    import_id: str,
    user: str = Query("system", description="User performing the commit")
):
    """
    Commit a previously uploaded import session to the metadata repository.
    """
    if import_id not in import_cache:
        raise HTTPException(status_code=404, detail="Import session not found or expired")
    
    kpis_to_commit = import_cache[import_id]
    if not kpis_to_commit:
        raise HTTPException(status_code=400, detail="No valid KPIs to commit")
        
    try:
        # Call Business Metadata Service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BUSINESS_METADATA_URL}/api/v1/metadata/definitions/bulk",
                json=kpis_to_commit,
                params={"created_by": user},
                timeout=30.0
            )
            
            if response.status_code != 201:
                raise HTTPException(
                    status_code=response.status_code, 
                    detail=f"Metadata service error: {response.text}"
                )
            
            result = response.json()
            
        # Clear cache on success
        del import_cache[import_id]
        
        return {
            "success": True,
            "count": len(kpis_to_commit),
            "ids": result.get("ids", [])
        }
            
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Failed to connect to Metadata Service: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Commit failed: {str(e)}")

