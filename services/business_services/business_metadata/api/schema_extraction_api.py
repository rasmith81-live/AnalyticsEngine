"""
Schema Extraction API Endpoints

Provides REST API for extracting table schemas from EntityDefinitions.
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from pathlib import Path

from ..services.schema_extractor import SchemaExtractor
from ..dependencies import get_database_manager, get_event_publisher
from ..repositories.metadata_query_repository import MetadataQueryRepository

router = APIRouter(prefix="/metadata/schemas", tags=["Schema Extraction"])


class SchemaExtractionRequest(BaseModel):
    """Request model for schema extraction."""
    entity_codes: Optional[List[str]] = Field(
        None,
        description="List of entity codes to extract. If None, extracts all entities."
    )
    module_code: Optional[str] = Field(
        None,
        description="Module code to filter entities (e.g., 'ASCM_SCOR')"
    )
    output_dir: str = Field(
        default="schemas",
        description="Output directory for schema JSON files"
    )


class SchemaExtractionResponse(BaseModel):
    """Response model for schema extraction."""
    success: bool
    total_entities: int
    successful_extractions: int
    failed_extractions: int
    success_rate: float
    output_directory: str
    results: List[Dict[str, Any]]
    failed_entities: List[Dict[str, Any]] = []


@router.post("/extract", response_model=SchemaExtractionResponse)
async def extract_schemas(
    request: SchemaExtractionRequest
):
    """
    Extract table schemas from entity definitions.
    
    This endpoint extracts table_schema from EntityDefinitions and generates
    JSON files that can be consumed by CQRS schema scripts.
    
    **Use Cases**:
    - Extract schemas for specific entities
    - Extract all schemas for a module
    - Extract all schemas in the system
    - Automated schema generation when entities are created/updated
    
    **Examples**:
    ```json
    // Extract specific entities
    {
        "entity_codes": ["SCOR_PROCESS", "SCOR_METRIC"]
    }
    
    // Extract all SCOR entities
    {
        "module_code": "ASCM_SCOR"
    }
    
    // Extract all entities
    {}
    ```
    """
    try:
        # Initialize schema extractor
        output_path = Path(request.output_dir)
        extractor = SchemaExtractor(output_dir=output_path)
        
        # Get database manager for querying entities
        db_manager = get_database_manager()
        
        results = []
        
        # Extract schemas based on request parameters
        if request.entity_codes:
            # Extract specific entities
            for entity_code in request.entity_codes:
                result = await extractor.extract_schema_by_code(
                    entity_code=entity_code,
                    get_entity_func=lambda code: _get_entity_by_code(db_manager, code)
                )
                results.append(result)
        
        elif request.module_code:
            # Extract all entities in module
            results = await extractor.extract_schemas_by_module(
                module_code=request.module_code,
                get_entities_by_module_func=lambda module: _get_entities_by_module(db_manager, module)
            )
        
        else:
            # Extract all entities
            results = await extractor.extract_all_schemas(
                get_all_entities_func=lambda: _get_all_entities(db_manager)
            )
        
        # Generate summary
        summary = extractor.get_extraction_summary(results)
        
        return SchemaExtractionResponse(
            success=summary["failed_extractions"] == 0,
            total_entities=summary["total_entities"],
            successful_extractions=summary["successful_extractions"],
            failed_extractions=summary["failed_extractions"],
            success_rate=summary["success_rate"],
            output_directory=summary["output_directory"],
            results=results,
            failed_entities=summary["failed_entities"]
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Schema extraction failed: {str(e)}"
        )


@router.get("/extract/{entity_code}")
async def extract_schema_by_code(
    entity_code: str
):
    """
    Extract schema for a specific entity by code.
    
    **Path Parameters**:
    - `entity_code`: Entity code (e.g., 'SCOR_PROCESS')
    
    **Returns**:
    - Schema JSON
    - Output file path
    - Entity metadata
    """
    try:
        output_path = Path("schemas")
        extractor = SchemaExtractor(output_dir=output_path)
        db_manager = get_database_manager()
        
        result = await extractor.extract_schema_by_code(
            entity_code=entity_code,
            get_entity_func=lambda code: _get_entity_by_code(db_manager, code)
        )
        
        return result
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/list")
async def list_extracted_schemas(
    output_dir: str = Query(default="schemas", description="Directory to search for schemas")
):
    """
    List all extracted schema files.
    
    **Query Parameters**:
    - `output_dir`: Directory where schemas are stored (default: 'schemas')
    
    **Returns**:
    - List of schema files with metadata
    """
    try:
        schema_path = Path(output_dir)
        
        if not schema_path.exists():
            return {
                "schemas": [],
                "count": 0,
                "output_directory": str(schema_path)
            }
        
        # Find all JSON files
        schema_files = list(schema_path.rglob("*.json"))
        
        schemas = []
        for file_path in schema_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    import json
                    schema_data = json.load(f)
                    
                    schemas.append({
                        "file_path": str(file_path),
                        "file_name": file_path.name,
                        "table_name": schema_data.get("table_name"),
                        "class_name": schema_data.get("class_name"),
                        "entity_code": schema_data.get("_metadata", {}).get("entity_code"),
                        "entity_name": schema_data.get("_metadata", {}).get("entity_name"),
                        "module": schema_data.get("_metadata", {}).get("module"),
                        "column_count": len(schema_data.get("columns", []))
                    })
            except Exception:
                # Skip files that can't be parsed
                continue
        
        return {
            "schemas": schemas,
            "count": len(schemas),
            "output_directory": str(schema_path)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Helper functions for database queries
async def _get_entity_by_code(db_manager, entity_code: str):
    """Get entity by code from database."""
    query_repo = MetadataQueryRepository(db_manager)
    entity = await query_repo.get_entity_by_code(entity_code)
    return entity


async def _get_entities_by_module(db_manager, module_code: str):
    """Get all entities for a module from database."""
    query_repo = MetadataQueryRepository(db_manager)
    entities = await query_repo.get_entities_by_module(module_code)
    return entities


async def _get_all_entities(db_manager):
    """Get all entities from database."""
    query_repo = MetadataQueryRepository(db_manager)
    entities = await query_repo.get_all_entities()
    return entities
