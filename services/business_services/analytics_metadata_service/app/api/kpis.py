"""
KPI API Endpoints
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Dict, Any

from ..loader import get_loader

router = APIRouter(prefix="/kpis", tags=["KPIs"])


@router.get("/", response_model=Dict[str, Any])
async def list_kpis(
    module: Optional[str] = Query(None, description="Filter by module code"),
    value_chain: Optional[str] = Query(None, description="Filter by value chain code"),
    industry: Optional[str] = Query(None, description="Filter by industry code"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    offset: int = Query(0, description="Offset for pagination")
):
    """
    List all KPIs with optional filters.
    
    Args:
        module: Filter by module code
        value_chain: Filter by value chain code
        industry: Filter by industry code
        limit: Maximum number of results
        offset: Pagination offset
        
    Returns:
        Dictionary with KPIs and metadata
    """
    loader = get_loader()
    
    # Get filtered or all KPIs
    if module or value_chain or industry:
        kpis = loader.search_kpis(
            module_code=module,
            value_chain_code=value_chain,
            industry_code=industry
        )
        kpis_dict = {kpi["code"]: kpi for kpi in kpis}
    else:
        kpis_dict = loader.get_all_kpis()
    
    # Convert to list for pagination
    kpis_list = list(kpis_dict.values())
    total = len(kpis_list)
    
    # Apply pagination
    if limit:
        kpis_list = kpis_list[offset:offset + limit]
    else:
        kpis_list = kpis_list[offset:]
    
    return {
        "total": total,
        "offset": offset,
        "limit": limit,
        "count": len(kpis_list),
        "kpis": kpis_list
    }


@router.get("/{kpi_code}", response_model=Dict[str, Any])
async def get_kpi(kpi_code: str):
    """
    Get KPI definition by code.
    
    Args:
        kpi_code: KPI code (e.g., "PERFECT_ORDER_FULFILLMENT")
        
    Returns:
        KPI definition dictionary
        
    Raises:
        HTTPException: If KPI not found
    """
    loader = get_loader()
    kpi = loader.get_kpi(kpi_code)
    
    if not kpi:
        raise HTTPException(
            status_code=404,
            detail=f"KPI not found: {kpi_code}"
        )
    
    return kpi


@router.get("/{kpi_code}/required-objects")
async def get_kpi_required_objects(kpi_code: str):
    """
    Get required object models for a KPI.
    
    Args:
        kpi_code: KPI code
        
    Returns:
        List of required object model codes
    """
    loader = get_loader()
    kpi = loader.get_kpi(kpi_code)
    
    if not kpi:
        raise HTTPException(
            status_code=404,
            detail=f"KPI not found: {kpi_code}"
        )
    
    required_objects = kpi.get("required_objects", [])
    
    return {
        "kpi_code": kpi_code,
        "required_objects": required_objects,
        "count": len(required_objects)
    }


@router.get("/{kpi_code}/formula")
async def get_kpi_formula(kpi_code: str):
    """
    Get KPI calculation formula.
    
    Args:
        kpi_code: KPI code
        
    Returns:
        Formula information
    """
    loader = get_loader()
    kpi = loader.get_kpi(kpi_code)
    
    if not kpi:
        raise HTTPException(
            status_code=404,
            detail=f"KPI not found: {kpi_code}"
        )
    
    return {
        "kpi_code": kpi_code,
        "name": kpi.get("name"),
        "formula": kpi.get("formula"),
        "calculation_logic": kpi.get("calculation_logic"),
        "unit": kpi.get("unit")
    }


@router.get("/{kpi_code}/benchmarks")
async def get_kpi_benchmarks(kpi_code: str):
    """
    Get benchmarks for a KPI.
    
    Args:
        kpi_code: KPI code
        
    Returns:
        Benchmark information
    """
    loader = get_loader()
    kpi = loader.get_kpi(kpi_code)
    
    if not kpi:
        raise HTTPException(
            status_code=404,
            detail=f"KPI not found: {kpi_code}"
        )
    
    benchmarks = kpi.get("benchmarks", {})
    
    return {
        "kpi_code": kpi_code,
        "benchmarks": benchmarks
    }
