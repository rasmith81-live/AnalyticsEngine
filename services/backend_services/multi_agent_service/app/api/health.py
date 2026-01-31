# =============================================================================
# Health Check Endpoints
# =============================================================================
"""Health check endpoints for the multi-agent service."""

from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from datetime import datetime

from ..metrics import (
    active_sessions,
    PROMETHEUS_AVAILABLE
)

router = APIRouter()


class ContractHealth(BaseModel):
    """Contract enforcement health status."""
    enforcement_enabled: bool
    total_violations_1h: int = 0
    hard_stops_1h: int = 0
    escalations_1h: int = 0


class BlackboardHealth(BaseModel):
    """Blackboard component health."""
    status: str
    active_sessions: int = 0
    pending_tasks: int = 0
    pending_reviews: int = 0
    error: Optional[str] = None


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    service: str
    version: str
    timestamp: str
    components: Dict[str, Any]
    contracts: Optional[ContractHealth] = None


class DetailedHealthResponse(BaseModel):
    """Detailed health check response with metrics."""
    status: str
    service: str
    version: str
    timestamp: str
    uptime_seconds: float
    components: Dict[str, Any]
    contracts: ContractHealth
    metrics_available: bool


# Track service start time
_service_start_time = datetime.utcnow()


@router.get("/health", response_model=HealthResponse)
async def health_check(request: Request) -> HealthResponse:
    """Check the health of the service and its components."""
    components = {}
    
    # Check blackboard store
    blackboard_health = await _check_blackboard_health(request)
    components["blackboard_store"] = blackboard_health.model_dump()
    
    # Check contract enforcement
    contract_health = _get_contract_health()
    
    # Overall status
    all_healthy = all(
        c.get("status") == "healthy" 
        for c in components.values()
    )
    
    return HealthResponse(
        status="healthy" if all_healthy else "degraded",
        service="multi_agent_service",
        version="0.1.0",
        timestamp=datetime.utcnow().isoformat(),
        components=components,
        contracts=contract_health
    )


@router.get("/health/detailed", response_model=DetailedHealthResponse)
async def detailed_health_check(request: Request) -> DetailedHealthResponse:
    """Get detailed health status including metrics."""
    components = {}
    
    # Check blackboard store
    blackboard_health = await _check_blackboard_health(request)
    components["blackboard_store"] = blackboard_health.model_dump()
    
    # Check Redis connectivity
    components["redis"] = await _check_redis_health(request)
    
    # Contract health
    contract_health = _get_contract_health()
    
    # Calculate uptime
    uptime = (datetime.utcnow() - _service_start_time).total_seconds()
    
    # Overall status
    all_healthy = all(
        c.get("status") == "healthy" 
        for c in components.values()
    )
    
    return DetailedHealthResponse(
        status="healthy" if all_healthy else "degraded",
        service="multi_agent_service",
        version="0.1.0",
        timestamp=datetime.utcnow().isoformat(),
        uptime_seconds=uptime,
        components=components,
        contracts=contract_health,
        metrics_available=PROMETHEUS_AVAILABLE
    )


@router.get("/ready")
async def readiness_check(request: Request) -> Dict[str, str]:
    """Check if the service is ready to handle requests."""
    if hasattr(request.app.state, 'blackboard_store'):
        try:
            # Verify store is actually working
            store = request.app.state.blackboard_store
            await store.list_sessions()
            return {"status": "ready"}
        except Exception:
            return {"status": "not_ready", "reason": "blackboard_store_error"}
    return {"status": "not_ready", "reason": "not_initialized"}


@router.get("/live")
async def liveness_check() -> Dict[str, str]:
    """Check if the service is alive."""
    return {"status": "alive"}


async def _check_blackboard_health(request: Request) -> BlackboardHealth:
    """Check blackboard store health."""
    if not hasattr(request.app.state, 'blackboard_store'):
        return BlackboardHealth(status="not_initialized")
    
    try:
        store = request.app.state.blackboard_store
        sessions = await store.list_sessions()
        
        # Count pending tasks and reviews across sessions
        pending_tasks = 0
        pending_reviews = 0
        
        for session_id in sessions[:10]:  # Sample first 10 sessions
            try:
                blackboard = await store.load_blackboard(session_id)
                if blackboard:
                    pending_tasks += len([t for t in blackboard.tasks if t.status == "open"])
                    pending_reviews += len([
                        a for a in blackboard.artifacts 
                        if a.review_status == "pending"
                    ])
            except Exception:
                pass
        
        return BlackboardHealth(
            status="healthy",
            active_sessions=len(sessions),
            pending_tasks=pending_tasks,
            pending_reviews=pending_reviews
        )
    except Exception as e:
        return BlackboardHealth(
            status="unhealthy",
            error=str(e)
        )


async def _check_redis_health(request: Request) -> Dict[str, Any]:
    """Check Redis connectivity."""
    if not hasattr(request.app.state, 'blackboard_store'):
        return {"status": "not_initialized"}
    
    try:
        store = request.app.state.blackboard_store
        # Ping Redis
        if hasattr(store, '_redis') and store._redis:
            await store._redis.ping()
            return {"status": "healthy"}
        return {"status": "unknown"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


def _get_contract_health() -> ContractHealth:
    """Get contract enforcement health status."""
    import os
    
    enforcement_enabled = os.getenv("CONTRACT_ENFORCEMENT_ENABLED", "false").lower() == "true"
    
    return ContractHealth(
        enforcement_enabled=enforcement_enabled,
        total_violations_1h=0,
        hard_stops_1h=0,
        escalations_1h=0
    )
