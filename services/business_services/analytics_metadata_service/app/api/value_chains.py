"""
Value Chain API Endpoints
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, Any

from ..loader import get_loader

router = APIRouter(prefix="/value-chains", tags=["Value Chains"])


@router.get("/", response_model=Dict[str, Any])
async def list_value_chains(
    limit: Optional[int] = Query(None, description="Limit number of results"),
    offset: int = Query(0, description="Offset for pagination")
):
    """
    List all value chains.
    
    Args:
        limit: Maximum number of results
        offset: Pagination offset
        
    Returns:
        Dictionary with value chains and metadata
    """
    loader = get_loader()
    vcs_dict = loader.get_all_value_chains()
    
    # Convert to list for pagination
    vcs_list = list(vcs_dict.values())
    total = len(vcs_list)
    
    # Apply pagination
    if limit:
        vcs_list = vcs_list[offset:offset + limit]
    else:
        vcs_list = vcs_list[offset:]
    
    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "count": len(vcs_list),
        "value_chains": vcs_list
    }


@router.get("/{value_chain_code}", response_model=Dict[str, Any])
async def get_value_chain(value_chain_code: str):
    """
    Get value chain definition by code.
    
    Args:
        value_chain_code: Value chain code (e.g., "SUPPLY_CHAIN", "SALES")
        
    Returns:
        Value chain definition dictionary
        
    Raises:
        HTTPException: If value chain not found
    """
    loader = get_loader()
    vc = loader.get_value_chain(value_chain_code)
    
    if not vc:
        raise HTTPException(
            status_code=404,
            detail=f"Value chain not found: {value_chain_code}"
        )
    
    return vc


@router.get("/{value_chain_code}/modules")
async def get_value_chain_modules(value_chain_code: str):
    """
    Get all modules for a value chain.
    
    Args:
        value_chain_code: Value chain code
        
    Returns:
        List of module codes and definitions
    """
    loader = get_loader()
    vc = loader.get_value_chain(value_chain_code)
    
    if not vc:
        raise HTTPException(
            status_code=404,
            detail=f"Value chain not found: {value_chain_code}"
        )
    
    # Get all modules and filter by value chain
    all_modules = loader.get_all_modules()
    modules = []
    
    for module_code, module in all_modules.items():
        # Check if module belongs to this value chain
        module_value_chains = module.get("value_chains", [])
        if isinstance(module_value_chains, list):
            if value_chain_code in module_value_chains:
                modules.append(module)
        elif module.get("value_chain_code") == value_chain_code:
            modules.append(module)
    
    return {
        "value_chain_code": value_chain_code,
        "module_count": len(modules),
        "modules": modules
    }


@router.get("/{value_chain_code}/kpis")
async def get_value_chain_kpis(value_chain_code: str):
    """
    Get all KPIs for a value chain.
    
    Args:
        value_chain_code: Value chain code
        
    Returns:
        List of KPI codes and definitions
    """
    loader = get_loader()
    vc = loader.get_value_chain(value_chain_code)
    
    if not vc:
        raise HTTPException(
            status_code=404,
            detail=f"Value chain not found: {value_chain_code}"
        )
    
    # Search KPIs by value chain
    kpis = loader.search_kpis(value_chain_code=value_chain_code)
    
    return {
        "value_chain_code": value_chain_code,
        "kpi_count": len(kpis),
        "kpis": kpis
    }


@router.get("/{value_chain_code}/object-models")
async def get_value_chain_object_models(value_chain_code: str):
    """
    Get all object models for a value chain.
    
    Args:
        value_chain_code: Value chain code
        
    Returns:
        List of object model codes and definitions
    """
    loader = get_loader()
    vc = loader.get_value_chain(value_chain_code)
    
    if not vc:
        raise HTTPException(
            status_code=404,
            detail=f"Value chain not found: {value_chain_code}"
        )
    
    # Get modules for this value chain
    module_codes = vc.get("associated_modules", [])
    
    # Collect all object models from modules
    all_models = {}
    for module_code in module_codes:
        module = loader.get_module(module_code)
        if module:
            model_codes = module.get("associated_object_models", [])
            for model_code in model_codes:
                if model_code not in all_models:
                    model = loader.get_object_model(model_code)
                    if model:
                        all_models[model_code] = model
    
    return {
        "value_chain_code": value_chain_code,
        "object_model_count": len(all_models),
        "object_models": list(all_models.values())
    }
