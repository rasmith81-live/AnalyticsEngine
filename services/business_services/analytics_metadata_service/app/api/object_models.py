"""
Object Model API Endpoints
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, Any

from ..loader import get_loader

router = APIRouter(prefix="/object-models", tags=["Object Models"])


@router.get("/", response_model=Dict[str, Any])
async def list_object_models(
    limit: Optional[int] = Query(None, description="Limit number of results"),
    offset: int = Query(0, description="Offset for pagination")
):
    """
    List all object models.
    
    Args:
        limit: Maximum number of results
        offset: Pagination offset
        
    Returns:
        Dictionary with object models and metadata
    """
    loader = get_loader()
    models_dict = loader.get_all_object_models()
    
    # Convert to list for pagination
    models_list = list(models_dict.values())
    total = len(models_list)
    
    # Apply pagination
    if limit:
        models_list = models_list[offset:offset + limit]
    else:
        models_list = models_list[offset:]
    
    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "count": len(models_list),
        "object_models": models_list
    }


@router.get("/{model_code}", response_model=Dict[str, Any])
async def get_object_model(model_code: str):
    """
    Get object model definition by code.
    
    Args:
        model_code: Object model code (e.g., "ORDER", "CUSTOMER")
        
    Returns:
        Object model definition dictionary
        
    Raises:
        HTTPException: If object model not found
    """
    loader = get_loader()
    model = loader.get_object_model(model_code)
    
    if not model:
        raise HTTPException(
            status_code=404,
            detail=f"Object model not found: {model_code}"
        )
    
    return model


@router.get("/{model_code}/schema")
async def get_object_model_schema(model_code: str):
    """
    Get table schema for an object model.
    
    Args:
        model_code: Object model code
        
    Returns:
        Table schema definition (for dynamic table creation)
    """
    loader = get_loader()
    model = loader.get_object_model(model_code)
    
    if not model:
        raise HTTPException(
            status_code=404,
            detail=f"Object model not found: {model_code}"
        )
    
    table_schema = model.get("table_schema")
    
    if not table_schema:
        raise HTTPException(
            status_code=404,
            detail=f"No table schema defined for: {model_code}"
        )
    
    return {
        "model_code": model_code,
        "table_name": model.get("table_name"),
        "table_schema": table_schema
    }


@router.get("/{model_code}/relationships")
async def get_object_model_relationships(model_code: str):
    """
    Get UML relationships for an object model.
    
    Args:
        model_code: Object model code
        
    Returns:
        UML relationship definitions
    """
    loader = get_loader()
    model = loader.get_object_model(model_code)
    
    if not model:
        raise HTTPException(
            status_code=404,
            detail=f"Object model not found: {model_code}"
        )
    
    schema_definition = model.get("schema_definition", "")
    
    return {
        "model_code": model_code,
        "schema_definition": schema_definition
    }


@router.get("/{model_code}/modules")
async def get_object_model_modules(model_code: str):
    """
    Get modules that use this object model.
    
    Args:
        model_code: Object model code
        
    Returns:
        List of module codes
    """
    loader = get_loader()
    model = loader.get_object_model(model_code)
    
    if not model:
        raise HTTPException(
            status_code=404,
            detail=f"Object model not found: {model_code}"
        )
    
    metadata = model.get("metadata_", {})
    modules = metadata.get("modules", [])
    
    return {
        "model_code": model_code,
        "modules": modules,
        "count": len(modules)
    }
