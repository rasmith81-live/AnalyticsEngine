from fastapi import FastAPI, HTTPException, Body, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any, List, Optional
from contextlib import asynccontextmanager
import os
import sys
from pathlib import Path
import httpx

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.messaging_client import MessagingClient
from .industry_knowledge_base import NAICClassificationIterator
from .semantic_mapping import KPIDecomposer
from .similarity_engine import SimilarityEngine
from .excel_processor import KPIExcelProcessor
from .decomposition_orchestrator import DecompositionOrchestrator

# Global instances
messaging_client: Optional[MessagingClient] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    global messaging_client
    
    # Initialize messaging client
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    messaging_client = MessagingClient(
        redis_url=redis_url,
        service_name="metadata_ingestion_service",
        pool_size=5
    )
    await messaging_client.connect()
    logger.info("MessagingClient connected")
    
    yield
    
    # Cleanup
    if messaging_client:
        await messaging_client.disconnect()
        logger.info("MessagingClient disconnected")

app = FastAPI(
    title="Metadata Ingestion Service",
    version="0.1.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
BUSINESS_METADATA_URL = os.getenv("BUSINESS_METADATA_URL", "http://business_metadata:8000")

# Initialize Engines
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

naic_iterator = NAICClassificationIterator()
kpi_decomposer = KPIDecomposer(entity_resolution_service_url="http://entity_resolution_service:8000")
similarity_engine = SimilarityEngine()
excel_processor = KPIExcelProcessor()
decomposition_orchestrator = DecompositionOrchestrator(
    business_metadata_url="http://business_metadata:8000",
    entity_resolution_url="http://entity_resolution_service:8000"
)

# TODO: Replace with Redis for production
# In-memory storage for import sessions (Note: Use Redis in production)
import_cache: Dict[str, List[Dict[str, Any]]] = {}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "metadata_ingestion_service"}

@app.get("/debug/config")
async def get_running_config():
    """
    Returns the actual configuration values the running service is using.
    Used by E2E tests to verify container code matches project code.
    """
    return {
        "service": "metadata_ingestion_service",
        "entity_resolution_url": decomposition_orchestrator.entity_resolution_url,
        "business_metadata_url": decomposition_orchestrator.business_metadata_url,
        "kpi_decomposer_url": kpi_decomposer.entity_resolution_url,
        "env_entity_resolution_url": os.getenv("ENTITY_RESOLUTION_SERVICE_URL", "not_set"),
        "expected_entity_resolution_url": "http://entity_resolution_service:8000",
        "config_matches": decomposition_orchestrator.entity_resolution_url == "http://entity_resolution_service:8000"
    }

@app.post("/debug/test-entity-resolution")
async def test_entity_resolution_connectivity(payload: Dict[str, Any] = None):
    """
    Debug endpoint to test internal connectivity to Entity Resolution Service.
    This helps catch Docker DNS issues (e.g., wrong service names).
    """
    entity_resolution_url = os.getenv(
        "ENTITY_RESOLUTION_SERVICE_URL",
        "http://entity_resolution_service:8000"
    )
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            # Test health endpoint
            health_response = await client.get(f"{entity_resolution_url}/health")
            health_ok = health_response.status_code == 200
            
            # Test semantic extraction endpoint
            extract_response = await client.post(
                f"{entity_resolution_url}/api/v1/entity-resolution/semantic/extract",
                json={"text": payload.get("text", "test"), "name": "connectivity_test"}
            )
            extract_ok = extract_response.status_code == 200
            
            return {
                "reachable": health_ok and extract_ok,
                "entity_resolution_url": entity_resolution_url,
                "health_check": {"status": health_response.status_code, "ok": health_ok},
                "semantic_extract": {"status": extract_response.status_code, "ok": extract_ok}
            }
    except Exception as e:
        return {
            "reachable": False,
            "entity_resolution_url": entity_resolution_url,
            "error": str(e),
            "error_type": type(e).__name__
        }

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
    Automatically extracts entities and math expressions using spaCy NLP (no OpenAI).
    Use /import/{id}/enrich for additional AI enrichment with LLM.
    """
    try:
        # 1. Parse File (fast - no LLM)
        valid_kpis_data, parser_errors = excel_processor.parse_stream(file.file, file.filename)
        
        # Generate Import ID
        import_id = str(uuid.uuid4())
        
        # Initialize KPI decomposer for spaCy-based extraction (no OpenAI)
        from app.semantic_mapping import KPIDecomposer
        kpi_decomposer = KPIDecomposer(entity_resolution_service_url="")
        
        # Collect all extracted entities for ontology
        all_entities = set()
        
        results = {
            "importId": import_id,
            "totalRows": len(valid_kpis_data) + len(parser_errors),
            "validRows": 0,
            "errors": parser_errors,
            "preview": [],
            "duplicates": [],
            "enriched": False,  # Flag to indicate LLM enrichment status
            "ontology_sync": {  # Initialize empty so manual add works
                "value_chains_created": [],
                "modules_created": [],
                "entities_created": [],
                "relationships_created": [],
                "errors": []
            }
        }
        
        final_valid_kpis = []
        
        for kpi in valid_kpis_data:
            # Generate code
            kpi_name = kpi.get("name", "")
            kpi["code"] = kpi.get("code") or kpi_name.upper().replace(" ", "_").replace("-", "_")
            
            # Extract entities and math expression from formula using spaCy (no OpenAI)
            formula = kpi.get("formula")
            math_expression = None
            formula_entities = []
            
            if formula:
                try:
                    decomposed = await kpi_decomposer.decompose_formula(formula)
                    math_expression = decomposed.get("math_expression")
                    formula_entities = decomposed.get("identified_attributes", [])
                    
                    # Store in KPI data
                    kpi["math_expression"] = math_expression
                    kpi["required_objects"] = formula_entities
                    
                    # Add to metadata
                    if "metadata" not in kpi:
                        kpi["metadata"] = {}
                    kpi["metadata"]["decomposition"] = {
                        "math_expression": math_expression,
                        "formula_entities": formula_entities,
                        "extraction_method": decomposed.get("extraction_method", "spacy")
                    }
                    
                    # Collect entities for ontology
                    all_entities.update(formula_entities)
                    
                    logger.info(f"Formula decomposition for '{kpi_name}': entities={formula_entities}, math='{math_expression}'")
                except Exception as e:
                    logger.warning(f"Formula decomposition failed for '{kpi_name}': {e}")
            
            row_data = {
                "Name": kpi.get("name"),
                "Formula": kpi.get("formula"),
                "Code": kpi.get("code"),
                "MathExpression": math_expression,
                "RequiredObjects": formula_entities,
                "Metadata": kpi.get("metadata", {})
            }
            
            final_valid_kpis.append(kpi)
            results["preview"].append(row_data)

        results["validRows"] = len(final_valid_kpis)
        
        # Add extracted entities to ontology_sync
        results["ontology_sync"]["entities_created"] = sorted(list(all_entities))
        
        # Cache valid KPIs for enrichment and commit
        if final_valid_kpis:
            import_cache[import_id] = final_valid_kpis
        
        # Add all KPI codes
        results["allKpiCodes"] = [kpi.get("code") or kpi.get("name") for kpi in final_valid_kpis]
        
        # Limit preview to top 20
        results["preview"] = results["preview"][:20]
        
        logger.info(f"Upload complete: {len(final_valid_kpis)} KPIs parsed with spaCy extraction. Import ID: {import_id}. Entities: {len(all_entities)}")
        
        return results

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to process file: {str(e)}")


@app.post("/import/{import_id}/enrich")
async def enrich_import(import_id: str):
    """
    Optional AI enrichment step - extracts entities, value chains, modules using LLM.
    Call this after upload to enrich KPIs with AI-extracted metadata.
    """
    if import_id not in import_cache:
        raise HTTPException(status_code=404, detail="Import session not found or expired")
    
    kpis = import_cache[import_id]
    
    if not kpis:
        raise HTTPException(status_code=400, detail="No KPIs to enrich")
    
    try:
        logger.info(f"Starting AI enrichment for {len(kpis)} KPIs...")
        
        # Run LLM-based decomposition for all KPIs
        enriched_kpis = []
        for kpi in kpis:
            try:
                enriched_kpi = await decomposition_orchestrator.decompose_kpi(kpi)
                enriched_kpis.append(enriched_kpi)
            except Exception as decomp_error:
                logger.warning(f"Decomposition failed for KPI '{kpi.get('name')}': {decomp_error}")
                enriched_kpis.append(kpi)  # Use original if decomposition fails
        
        # Update cache with enriched KPIs
        import_cache[import_id] = enriched_kpis
        
        # Synchronize ontology (create value chains, modules, entities)
        ontology_sync_summary = {}
        try:
            logger.info(f"Synchronizing ontology for {len(enriched_kpis)} KPIs...")
            ontology_sync_summary = await decomposition_orchestrator.sync_ontology(enriched_kpis)
            logger.info(f"Ontology sync complete: {ontology_sync_summary}")
        except Exception as sync_error:
            logger.error(f"Ontology sync failed: {sync_error}", exc_info=True)
            ontology_sync_summary = {
                "status": "failed",
                "errors": [str(sync_error)],
                "message": "Enrichment complete but ontology sync failed"
            }
        
        # Build preview from enriched KPIs
        preview = []
        for kpi in enriched_kpis[:20]:
            preview.append({
                "Name": kpi.get("name"),
                "Formula": kpi.get("formula"),
                "Code": kpi.get("code"),
                "MathExpression": kpi.get("math_expression"),
                "RequiredObjects": kpi.get("required_objects", []),
                "Metadata": kpi.get("metadata", {})
            })
        
        return {
            "importId": import_id,
            "enriched": True,
            "kpiCount": len(enriched_kpis),
            "preview": preview,
            "ontology_sync": ontology_sync_summary,
            "allKpiCodes": [kpi.get("code") or kpi.get("name") for kpi in enriched_kpis]
        }
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"AI enrichment failed: {str(e)}")

from pydantic import BaseModel

class OntologyEdits(BaseModel):
    """Edited ontology items from the UI."""
    value_chains_created: Optional[List[str]] = None
    modules_created: Optional[List[str]] = None
    entities_created: Optional[List[str]] = None
    relationships_created: Optional[List[str]] = None
    errors: Optional[List[str]] = None

class CommitRequest(BaseModel):
    """Request body for commit with optional edited ontology."""
    ontology: Optional[OntologyEdits] = None

@app.post("/import/{import_id}/commit")
async def commit_import(
    import_id: str,
    user: str = Query("system", description="User performing the commit"),
    body: Optional[CommitRequest] = Body(None)
):
    """
    Commit a previously uploaded import session to the metadata repository.
    Accepts optional edited ontology in request body to create value chains, modules, entities.
    """
    if import_id not in import_cache:
        raise HTTPException(status_code=404, detail="Import session not found or expired")
    
    kpis_to_commit = import_cache[import_id]
    
    if not kpis_to_commit:
        raise HTTPException(status_code=400, detail="No valid KPIs to commit")
    
    # If ontology edits provided, sync them first
    ontology_sync_result = {}
    if body and body.ontology:
        logger.info(f"Processing edited ontology: {body.ontology}")
        try:
            # Use the edited ontology for sync
            edited_ontology = {
                "value_chains": body.ontology.value_chains_created or [],
                "modules": body.ontology.modules_created or [],
                "entities": body.ontology.entities_created or [],
                "relationships": body.ontology.relationships_created or []
            }
            ontology_sync_result = await decomposition_orchestrator.sync_edited_ontology(edited_ontology, user)
            logger.info(f"Edited ontology sync complete: {ontology_sync_result}")
        except Exception as sync_error:
            logger.error(f"Edited ontology sync failed: {sync_error}", exc_info=True)
            ontology_sync_result = {"status": "failed", "error": str(sync_error)}
    
    # Debug logging
    logger.info(f"Committing {len(kpis_to_commit)} KPIs")
    if kpis_to_commit:
        logger.info(f"First KPI keys: {list(kpis_to_commit[0].keys())}")
        logger.info(f"First KPI has 'id': {'id' in kpis_to_commit[0]}")
        
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
        
        # Create relationships for all KPIs (graph architecture)
        logger.info(f"Creating relationships for {len(kpis_to_commit)} KPIs...")
        try:
            rel_result = await decomposition_orchestrator.sync_ontology(kpis_to_commit)
            logger.info(f"Relationships created: {len(rel_result.get('relationships_created', []))}")
        except Exception as rel_error:
            logger.warning(f"Relationship creation failed (non-fatal): {rel_error}")
            
        # Clear cache
        del import_cache[import_id]
        
        # Publish event that KPIs were imported
        if messaging_client:
            try:
                await messaging_client.publish_event(
                    topic="metadata.kpis.imported",
                    event_type="kpis.bulk_imported",
                    data={
                        "import_id": import_id,
                        "count": len(kpis_to_commit),
                        "created_by": "system"
                    }
                )
            except Exception:
                pass  # Event publishing is optional
            
            logger.info(f"Published metadata.kpis.imported event for import {import_id}")
        
        return {
            "status": "success",
            "message": f"Successfully committed {len(kpis_to_commit)} KPIs to metadata repository",
            "kpi_count": len(kpis_to_commit)
        }
            
    except httpx.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Failed to connect to Metadata Service: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Commit failed: {str(e)}")

