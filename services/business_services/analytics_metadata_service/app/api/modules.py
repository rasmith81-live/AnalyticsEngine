"""
Module API Endpoints
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, Any

from ..loader import get_loader

router = APIRouter(prefix="/modules", tags=["Modules"])


@router.get("/", response_model=Dict[str, Any])
async def list_modules(
    limit: Optional[int] = Query(None, description="Limit number of results"),
    offset: int = Query(0, description="Offset for pagination")
):
    """
    List all modules.
    
    Args:
        limit: Maximum number of results
        offset: Pagination offset
        
    Returns:
        Dictionary with modules and metadata
    """
    loader = get_loader()
    modules_dict = loader.get_all_modules()
    
    # Convert to list for pagination
    modules_list = list(modules_dict.values())
    total = len(modules_list)
    
    # Apply pagination
    if limit:
        modules_list = modules_list[offset:offset + limit]
    else:
        modules_list = modules_list[offset:]
    
    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "count": len(modules_list),
        "modules": modules_list
    }


@router.get("/{module_code}", response_model=Dict[str, Any])
async def get_module(module_code: str):
    """
    Get module definition by code.
    
    Args:
        module_code: Module code (e.g., "ASCM_SCOR", "SALES_MANAGEMENT")
        
    Returns:
        Module definition dictionary
        
    Raises:
        HTTPException: If module not found
    """
    loader = get_loader()
    module = loader.get_module(module_code)
    
    if not module:
        raise HTTPException(
            status_code=404,
            detail=f"Module not found: {module_code}"
        )
    
    return module


@router.get("/{module_code}/kpis")
async def get_module_kpis(module_code: str):
    """
    Get all KPIs for a module.
    
    Args:
        module_code: Module code
        
    Returns:
        List of KPI codes and definitions
    """
    loader = get_loader()
    module = loader.get_module(module_code)
    
    if not module:
        raise HTTPException(
            status_code=404,
            detail=f"Module not found: {module_code}"
        )
    
    # Get KPI codes from module
    kpi_codes = module.get("associated_kpis", [])
    
    # Get full KPI definitions
    kpis = []
    for kpi_code in kpi_codes:
        kpi = loader.get_kpi(kpi_code)
        if kpi:
            kpis.append(kpi)
    
    return {
        "module_code": module_code,
        "kpi_count": len(kpis),
        "kpis": kpis
    }


@router.get("/{module_code}/object-models")
async def get_module_object_models(module_code: str):
    """
    Get all object models for a module.
    
    Args:
        module_code: Module code
        
    Returns:
        List of object model codes and definitions
    """
    loader = get_loader()
    module = loader.get_module(module_code)
    
    if not module:
        raise HTTPException(
            status_code=404,
            detail=f"Module not found: {module_code}"
        )
    
    # Get object model codes from module
    model_codes = module.get("associated_object_models", [])
    
    # Get full object model definitions
    models = []
    for model_code in model_codes:
        model = loader.get_object_model(model_code)
        if model:
            models.append(model)
    
    return {
        "module_code": module_code,
        "object_model_count": len(models),
        "object_models": models
    }
