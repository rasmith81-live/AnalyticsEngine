"""
Calculation Engine Service

Generic calculation orchestration service that routes KPI calculations
to domain-specific handlers (SCOR, CRM, Sales, etc.).
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from typing import List, Dict, Any
import logging

from .orchestrator import CalculationOrchestrator
from .base_handler import CalculationParams, CalculationResult
from .handlers.scor_handler import SCORCalculationHandler
# from .handlers.crm_handler import CRMCalculationHandler
# from .handlers.sales_handler import SalesCalculationHandler
from .config import get_settings

logger = logging.getLogger(__name__)

# Global orchestrator instance
orchestrator = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    global orchestrator
    
    settings = get_settings()
    
    # Initialize orchestrator
    orchestrator = CalculationOrchestrator()
    
    # Register SCOR handler
    scor_handler = SCORCalculationHandler(
        database_service_url=settings.database_service_url,
        messaging_service_url=settings.messaging_service_url,
        metadata_service_url=settings.metadata_service_url,
        cache_enabled=settings.cache_enabled,
        cache_ttl=settings.cache_ttl
    )
    orchestrator.register_handler("SUPPLY_CHAIN", scor_handler)
    
    # Register CRM handler
    # crm_handler = CRMCalculationHandler(...)
    # orchestrator.register_handler("CRM", crm_handler)
    
    # Register Sales handler
    # sales_handler = SalesCalculationHandler(...)
    # orchestrator.register_handler("SALES", sales_handler)
    
    # Load KPI mappings
    await orchestrator.load_kpi_mappings(settings.metadata_service_url)
    
    logger.info("Calculation Engine initialized")
    logger.info(f"Registered handlers: {list(orchestrator.handlers.keys())}")
    
    yield
    
    # Cleanup
    logger.info("Calculation Engine shutting down")


# Create FastAPI app
app = FastAPI(
    title="Calculation Engine Service",
    description="Generic KPI calculation orchestration service",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "calculation_engine",
        "handlers": list(orchestrator.handlers.keys()) if orchestrator else []
    }


@app.post("/calculate", response_model=CalculationResult)
async def calculate_kpi(params: CalculationParams):
    """
    Calculate a single KPI.
    
    Args:
        params: Calculation parameters
        
    Returns:
        CalculationResult
    """
    try:
        result = await orchestrator.calculate_single(params)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Calculation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/calculate/batch", response_model=List[CalculationResult])
async def calculate_batch(params_list: List[CalculationParams]):
    """
    Calculate multiple KPIs in parallel.
    
    Args:
        params_list: List of calculation parameters
        
    Returns:
        List of CalculationResults
    """
    try:
        results = await orchestrator.calculate_batch(params_list)
        return results
    except Exception as e:
        logger.error(f"Batch calculation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/calculate/dashboard", response_model=Dict[str, CalculationResult])
async def calculate_dashboard(dashboard_config: Dict[str, Any]):
    """
    Calculate all KPIs for a dashboard.
    
    Args:
        dashboard_config: Dashboard configuration
        
    Returns:
        Dictionary of KPI code to CalculationResult
    """
    try:
        results = await orchestrator.calculate_dashboard(dashboard_config)
        return results
    except Exception as e:
        logger.error(f"Dashboard calculation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/handlers")
async def get_handlers():
    """Get information about registered handlers."""
    return orchestrator.get_handler_stats()


@app.get("/kpis/{value_chain_code}")
async def get_kpis_for_value_chain(value_chain_code: str):
    """
    Get all KPIs for a specific value chain.
    
    Args:
        value_chain_code: Value chain identifier
        
    Returns:
        List of KPI codes
    """
    kpis = [
        kpi_code
        for kpi_code, vc_code in orchestrator.kpi_to_handler_map.items()
        if vc_code == value_chain_code
    ]
    
    return {
        "value_chain": value_chain_code,
        "kpi_count": len(kpis),
        "kpis": kpis
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
