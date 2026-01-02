"""
Calculation Engine Service

Generic calculation orchestration service that routes KPI calculations
to dynamic handlers based on metadata definitions.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from typing import List, Dict, Any, Optional
from datetime import datetime
from pydantic import BaseModel
import logging

from .orchestrator import CalculationOrchestrator
from .base_handler import CalculationParams, CalculationResult
from .handlers.dynamic_handler import DynamicCalculationHandler
from .handlers.set_based_handler import SetBasedCalculationHandler, SetBasedCalculationEngine
from .engine.set_operations import SET_BASED_KPI_REGISTRY
from .stream_processor import StreamProcessor
from .clients import DatabaseClient, MessagingClientWrapper
from .config import get_settings

logger = logging.getLogger(__name__)

# Global instances
orchestrator = None
stream_processor = None
db_client = None
msg_client = None
set_based_engine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    global orchestrator, stream_processor, db_client, msg_client, set_based_engine
    
    settings = get_settings()
    
    # Initialize backend clients
    db_client = DatabaseClient(
        base_url=settings.database_service_url,
        service_name="calculation_engine"
    )
    logger.info("DatabaseClient initialized")
    
    msg_client = MessagingClientWrapper(
        redis_url=settings.redis_url,
        service_name="calculation_engine"
    )
    await msg_client.connect()
    logger.info("MessagingClient connected")
    
    # Initialize orchestrator
    orchestrator = CalculationOrchestrator()
    
    # Register Generic Dynamic Handler
    # In a fully generic system, we might iterate over active value chains from metadata
    # For now, we register a dynamic handler that can handle any generic request
    dynamic_handler = DynamicCalculationHandler(
        value_chain_code="GENERIC", # or iterate and register for specific domains
        database_service_url=settings.database_service_url,
        messaging_service_url=settings.messaging_service_url,
        metadata_service_url=settings.metadata_service_url,
        cache_enabled=settings.cache_enabled,
        cache_ttl=settings.cache_ttl
    )
    
    # Register for specific domains if needed, or use a catch-all strategy in orchestrator
    # Here we register it for common domains to ensure routing works
    orchestrator.register_handler("SUPPLY_CHAIN", dynamic_handler)
    orchestrator.register_handler("SALES", dynamic_handler)
    orchestrator.register_handler("CRM", dynamic_handler)
    
    # Register Set-Based Calculation Handler for complex KPIs (uses pub/sub)
    set_based_handler = SetBasedCalculationHandler(
        value_chain_code="SET_BASED",
        redis_url=settings.redis_url,
        cache_enabled=settings.cache_enabled,
        cache_ttl=settings.cache_ttl
    )
    orchestrator.register_handler("SET_BASED", set_based_handler)
    
    # Register set-based KPIs in the KPI-to-handler map
    for kpi_code in SET_BASED_KPI_REGISTRY.keys():
        orchestrator.kpi_to_handler_map[kpi_code] = "SET_BASED"
    
    # Initialize standalone set-based engine for direct API access (uses pub/sub)
    set_based_engine = SetBasedCalculationEngine(
        redis_url=settings.redis_url
    )
    
    # Load KPI mappings
    await orchestrator.load_kpi_mappings(settings.metadata_service_url)
    
    # Initialize stream processor
    stream_processor = StreamProcessor(
        orchestrator=orchestrator,
        database_client=db_client,
        messaging_client=msg_client,
        redis_url=settings.redis_url
    )
    await stream_processor.start()
    
    logger.info("Calculation Engine initialized")
    logger.info(f"Registered handlers: {list(orchestrator.handlers.keys())}")
    logger.info("Stream processor started")
    
    yield
    
    # Cleanup
    if stream_processor:
        await stream_processor.stop()
        logger.info("Stream processor stopped")
    
    if set_based_engine:
        await set_based_engine.close()
        logger.info("SetBasedCalculationEngine closed")
    
    if msg_client:
        await msg_client.disconnect()
        logger.info("MessagingClient disconnected")
    
    if db_client:
        await db_client.close()
        logger.info("DatabaseClient closed")
    
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


# ============================================================================
# SET-BASED CALCULATION ENDPOINTS
# ============================================================================

@app.get("/set-based/kpis")
async def list_set_based_kpis():
    """
    List all available set-based KPIs.
    
    Returns:
        List of set-based KPI definitions with code, name, description, unit
    """
    if not set_based_engine:
        raise HTTPException(status_code=503, detail="Set-based engine not initialized")
    
    return {
        "kpis": set_based_engine.list_available_kpis(),
        "count": len(SET_BASED_KPI_REGISTRY)
    }


@app.post("/set-based/calculate/{kpi_code}")
async def calculate_set_based_kpi(
    kpi_code: str,
    period_start: datetime,
    period_end: datetime,
    filters: Dict[str, Any] = None
):
    """
    Calculate a set-based KPI.
    
    Set-based KPIs require multiple intermediate sets to produce a result.
    Example: Churn Rate requires StartPeriodCustomers, EndPeriodCustomers,
    and LostCustomers sets.
    
    Args:
        kpi_code: The KPI code (e.g., "CHURN_RATE", "RETENTION_RATE")
        period_start: Start of the calculation period
        period_end: End of the calculation period
        filters: Optional additional filters
        
    Returns:
        Calculation result with value, metadata, and SQL breakdown
    """
    if not set_based_engine:
        raise HTTPException(status_code=503, detail="Set-based engine not initialized")
    
    try:
        result = await set_based_engine.calculate(
            kpi_code=kpi_code,
            period_start=period_start,
            period_end=period_end,
            filters=filters
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Set-based calculation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/set-based/explain/{kpi_code}")
async def explain_set_based_kpi(
    kpi_code: str,
    period_start: datetime,
    period_end: datetime
):
    """
    Get explanation of how a set-based KPI would be calculated.
    
    Returns the SQL and step breakdown without executing the calculation.
    Useful for understanding the calculation logic and debugging.
    
    Args:
        kpi_code: The KPI code
        period_start: Start of the calculation period
        period_end: End of the calculation period
        
    Returns:
        Explanation with SQL, parameters, and step breakdown
    """
    if not set_based_engine:
        raise HTTPException(status_code=503, detail="Set-based engine not initialized")
    
    try:
        explanation = await set_based_engine.explain(
            kpi_code=kpi_code,
            period_start=period_start,
            period_end=period_end
        )
        return explanation
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Set-based explanation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/set-based/definition/{kpi_code}")
async def get_set_based_kpi_definition(kpi_code: str):
    """
    Get the full definition of a set-based KPI.
    
    Returns the complete definition including all steps, set definitions,
    aggregations, and the final formula.
    
    Args:
        kpi_code: The KPI code
        
    Returns:
        Full KPI definition
    """
    from .engine.set_operations import get_set_based_kpi_definition as get_def
    
    kpi_def = get_def(kpi_code)
    if not kpi_def:
        raise HTTPException(status_code=404, detail=f"Set-based KPI not found: {kpi_code}")
    
    return kpi_def.model_dump()


@app.get("/set-based/metrics")
async def get_set_based_metrics():
    """
    Get performance metrics for the set-based calculation engine.
    
    Returns metrics for monitoring SLA compliance:
    - total_calculations: Total calculations performed
    - cache_hits/misses: Cache performance
    - avg_calculation_time_ms: Average response time
    - max_calculation_time_ms: Maximum response time
    - sla_violations: Calculations exceeding 1000ms
    - sla_compliance_rate: Percentage meeting <1s SLA
    
    Target SLA: <1000ms per calculation
    """
    if not set_based_engine:
        raise HTTPException(status_code=503, detail="Set-based engine not initialized")
    
    return {
        "sla_target_ms": 1000,
        "metrics": set_based_engine.get_metrics()
    }


@app.post("/set-based/cache/clear")
async def clear_set_based_cache():
    """Clear the set-based calculation result cache."""
    if not set_based_engine:
        raise HTTPException(status_code=503, detail="Set-based engine not initialized")
    
    set_based_engine.clear_cache()
    return {"status": "cache_cleared"}


class NLPConversionRequest(BaseModel):
    """Request model for NLP to set-based definition conversion."""
    nlp_definition: str
    kpi_code: str
    kpi_name: str
    base_entity: str
    unit: str = "Number"
    metadata: Optional[Dict[str, Any]] = None
    register: bool = False


@app.post("/set-based/convert-nlp")
async def convert_nlp_to_sets(request: NLPConversionRequest):
    """
    Convert a natural language KPI definition to a set-based calculation definition.
    
    This endpoint parses NLP definitions like:
    "(Number of Customers Lost During Period / Number of Customers at Start of Period) * 100"
    
    And converts them into structured set-based definitions with:
    - Set definitions (FILTER, EXCEPT, INTERSECT, UNION)
    - Aggregations (COUNTROWS, SUMX, AVERAGEX)
    - Final formula
    
    Supports common patterns:
    - Churn Rate (lost/churned entities)
    - Retention Rate (retained entities)
    - Growth Rate (new entities)
    - Generic ratio patterns
    
    Args:
        request: NLPConversionRequest with:
            - nlp_definition: Natural language definition
            - kpi_code: Code for the KPI (e.g., "CHURN_RATE")
            - kpi_name: Human-readable name
            - base_entity: Primary entity table (e.g., "customers")
            - unit: Unit of measurement (default: "Number")
            - metadata: Optional additional metadata
            - register: If True, persist to metadata service AND register in memory
            
    Returns:
        SetBasedKPIDefinition as JSON
        
    Example:
        POST /set-based/convert-nlp
        {
            "nlp_definition": "(Number of Customers Lost During Period / Number of Customers at Start of Period) * 100",
            "kpi_code": "CUSTOMER_CHURN",
            "kpi_name": "Customer Churn Rate",
            "base_entity": "customers",
            "unit": "Percentage",
            "register": true
        }
    """
    from .engine.nlp_to_sets_converter import convert_nlp_to_set_definition
    import httpx
    
    settings = get_settings()
    
    try:
        definition = await convert_nlp_to_set_definition(
            nlp_definition=request.nlp_definition,
            kpi_code=request.kpi_code,
            kpi_name=request.kpi_name,
            base_entity=request.base_entity,
            unit=request.unit,
            metadata=request.metadata,
            llm_service_url=settings.conversation_service_url if hasattr(settings, 'conversation_service_url') else None,
            register=request.register
        )
        
        persisted = False
        
        # If registered, persist to metadata service for durability
        if request.register:
            # Add to orchestrator's KPI map (in-memory)
            if orchestrator:
                orchestrator.kpi_to_handler_map[request.kpi_code.upper()] = "SET_BASED"
            
            # Persist to metadata service
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    # Build the metric definition payload
                    metric_payload = {
                        "kind": "metric_definition",
                        "code": request.kpi_code.upper(),
                        "name": request.kpi_name,
                        "description": request.nlp_definition,
                        "formula": request.nlp_definition,
                        "unit": request.unit,
                        "calculation_type": "set_based",
                        "set_based_definition": definition.model_dump(),
                        "metadata_": request.metadata or {},
                        "required_objects": [request.base_entity]
                    }
                    
                    response = await client.post(
                        f"{settings.metadata_service_url}/api/v1/metadata/definitions",
                        json=metric_payload
                    )
                    
                    if response.status_code in (200, 201):
                        persisted = True
                        logger.info(f"Persisted set-based KPI {request.kpi_code} to metadata service")
                    else:
                        logger.warning(f"Failed to persist to metadata service: {response.status_code}")
                        
            except Exception as e:
                logger.warning(f"Failed to persist to metadata service: {e}")
        
        return {
            "success": True,
            "registered": request.register,
            "persisted": persisted,
            "definition": definition.model_dump()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"NLP conversion failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/set-based/convert-nlp/preview")
async def preview_nlp_conversion(request: NLPConversionRequest):
    """
    Preview the SQL that would be generated from an NLP definition.
    
    Converts the NLP definition and generates the SQL without executing.
    Useful for validating the conversion before registering.
    
    Args:
        request: Same as convert-nlp endpoint
        
    Returns:
        Definition and generated SQL preview
    """
    from .engine.nlp_to_sets_converter import convert_nlp_to_set_definition
    from .engine.set_operations import SetBasedSQLGenerator
    
    settings = get_settings()
    
    try:
        definition = await convert_nlp_to_set_definition(
            nlp_definition=request.nlp_definition,
            kpi_code=request.kpi_code,
            kpi_name=request.kpi_name,
            base_entity=request.base_entity,
            unit=request.unit,
            metadata=request.metadata,
            llm_service_url=settings.conversation_service_url if hasattr(settings, 'conversation_service_url') else None,
            register=False  # Never register in preview
        )
        
        # Generate SQL preview
        sql_generator = SetBasedSQLGenerator()
        sample_start = datetime(2024, 1, 1)
        sample_end = datetime(2024, 1, 31)
        
        sql, params = sql_generator.generate_sql(
            kpi_def=definition,
            period_start=sample_start,
            period_end=sample_end
        )
        
        return {
            "success": True,
            "definition": definition.model_dump(),
            "sql_preview": sql,
            "sample_parameters": {
                k: v.isoformat() if isinstance(v, datetime) else v
                for k, v in params.items()
            },
            "steps_summary": [
                {
                    "step": step.step_number,
                    "name": step.name,
                    "type": "set_definition" if step.set_definition else 
                            "aggregation" if step.aggregation else "formula"
                }
                for step in definition.steps
            ]
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"NLP preview failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# STREAM PROCESSING ENDPOINTS
# ============================================================================

@app.post("/stream/subscribe")
async def subscribe_to_kpi_stream(
    kpi_code: str,
    entity_id: str,
    period: str,
    calculation_params: Dict[str, Any] = None
):
    """
    Subscribe to a KPI data stream for real-time calculation.
    
    Args:
        kpi_code: KPI code to calculate
        entity_id: Entity ID for the KPI
        period: Time period ('minute', 'hour', 'day')
        calculation_params: Optional additional parameters for calculation
        
    Returns:
        Subscription details
    """
    if not stream_processor:
        raise HTTPException(status_code=503, detail="Stream processor not initialized")
    
    try:
        subscription = await stream_processor.subscribe_to_stream(
            kpi_code=kpi_code,
            entity_id=entity_id,
            period=period,
            calculation_params=calculation_params
        )
        return subscription
    except Exception as e:
        logger.error(f"Failed to subscribe to stream: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/stream/unsubscribe")
async def unsubscribe_from_kpi_stream(stream_key: str):
    """
    Unsubscribe from a KPI data stream.
    
    Args:
        stream_key: Stream key (kpi_code:entity_id:period)
        
    Returns:
        Unsubscription status
    """
    if not stream_processor:
        raise HTTPException(status_code=503, detail="Stream processor not initialized")
    
    try:
        success = await stream_processor.unsubscribe_from_stream(stream_key)
        return {
            "stream_key": stream_key,
            "unsubscribed": success
        }
    except Exception as e:
        logger.error(f"Failed to unsubscribe from stream: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stream/status")
async def get_stream_status():
    """
    Get status of stream processor and active subscriptions.
    
    Returns:
        Stream processor status
    """
    if not stream_processor:
        raise HTTPException(status_code=503, detail="Stream processor not initialized")
    
    try:
        status = await stream_processor.get_status()
        return status
    except Exception as e:
        logger.error(f"Failed to get stream status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
