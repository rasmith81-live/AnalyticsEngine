"""
Metrics adapter for the API Gateway.
Provides metrics collection via the Messaging Service.
"""
from typing import Dict, Any, Optional, Callable
import time
import functools
from fastapi import FastAPI, Request, Response

from app.core.config import settings
from app.core.logging import get_logger
from app.clients.messaging import MessagingClient

logger = get_logger(__name__)

# Messaging service client instance
_messaging_client = None


async def get_messaging_client() -> MessagingClient:
    """
    Get or create messaging service client instance.
    
    Returns:
        MessagingServiceClient instance
    """
    global _messaging_client
    
    if _messaging_client is None:
        _messaging_client = MessagingClient()
        logger.info(f"Created messaging service client for {settings.MESSAGING_SERVICE_URL}")
    
    return _messaging_client


def setup_metrics_endpoint(app: FastAPI, path: str = "/metrics") -> None:
    """
    Set up metrics endpoint that proxies to the messaging service metrics.
    
    Args:
        app: FastAPI application
        path: Metrics endpoint path
    """
    from fastapi import APIRouter
    
    metrics_router = APIRouter()
    
    @metrics_router.get(path)
    async def get_metrics():
        # This endpoint will proxy metrics requests to the messaging service
        # The messaging service will handle the actual metrics collection and exposition
        from fastapi.responses import PlainTextResponse
        import httpx
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{settings.MESSAGING_SERVICE_URL}/metrics")
                return PlainTextResponse(content=response.text, status_code=response.status_code)
        except Exception as e:
            logger.error(f"Failed to get metrics from messaging service: {str(e)}")
            return PlainTextResponse(content="# Error fetching metrics from messaging service\n", status_code=500)
    
    app.include_router(metrics_router)
    logger.info(f"Metrics endpoint set up at {path} (proxied to messaging service)")


def track_endpoint_execution(func: Callable) -> Callable:
    """
    Decorator to track endpoint execution metrics via messaging service.
    
    Args:
        func: Function to decorate
        
    Returns:
        Decorated function
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract request object
        request = None
        for arg in args:
            if isinstance(arg, Request):
                request = arg
                break
        
        if not request:
            for _, value in kwargs.items():
                if isinstance(value, Request):
                    request = value
                    break
        
        if not request:
            # If no request object found, just call the function
            return await func(*args, **kwargs)
        
        # Get endpoint and method
        endpoint = request.url.path
        method = request.method
        
        # Track request latency
        start_time = time.time()
        
        try:
            # Call the function
            response = await func(*args, **kwargs)
            
            # Record metrics via messaging service
            client = await get_messaging_client()
            status_code = response.status_code if hasattr(response, "status_code") else 200
            
            # Record request count
            await client.record_metric(
                "api_gateway_request_count",
                1.0,
                {"method": method, "endpoint": endpoint, "status_code": str(status_code)}
            )
            
            # Record request latency
            await client.record_metric(
                "api_gateway_request_latency_seconds",
                time.time() - start_time,
                {"method": method, "endpoint": endpoint}
            )
            
            return response
            
        except Exception as e:
            # Record error metrics via messaging service
            try:
                client = await get_messaging_client()
                
                # Record request count with error
                await client.record_metric(
                    "api_gateway_request_count",
                    1.0,
                    {"method": method, "endpoint": endpoint, "status_code": "500"}
                )
                
                # Record request latency
                await client.record_metric(
                    "api_gateway_request_latency_seconds",
                    time.time() - start_time,
                    {"method": method, "endpoint": endpoint}
                )
            except Exception as metric_error:
                logger.warning(f"Failed to record error metrics: {str(metric_error)}")
            
            # Re-raise the original exception
            raise
    
    return wrapper


def track_service_call(service: str, endpoint: str) -> Callable:
    """
    Decorator to track service call metrics via messaging service.
    
    Args:
        service: Service name
        endpoint: Endpoint path
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Track service call latency
            start_time = time.time()
            
            try:
                # Call the function
                response = await func(*args, **kwargs)
                
                # Record service response time via messaging service
                client = await get_messaging_client()
                await client.record_metric(
                    "api_gateway_service_response_time_seconds",
                    time.time() - start_time,
                    {"service": service, "endpoint": endpoint}
                )
                
                return response
                
            except Exception as e:
                # Record error metrics via messaging service
                try:
                    client = await get_messaging_client()
                    
                    # Record service error
                    await client.record_metric(
                        "api_gateway_service_errors",
                        1.0,
                        {"service": service, "error_type": type(e).__name__}
                    )
                    
                    # Record service response time
                    await client.record_metric(
                        "api_gateway_service_response_time_seconds",
                        time.time() - start_time,
                        {"service": service, "endpoint": endpoint}
                    )
                except Exception as metric_error:
                    logger.warning(f"Failed to record service error metrics: {str(metric_error)}")
                
                # Re-raise the original exception
                raise
        
        return wrapper
    
    return decorator


# Helper functions for common metrics
async def record_cache_hit(endpoint: str):
    """
    Record a cache hit for an endpoint.
    
    Args:
        endpoint: Endpoint path
    """
    client = await get_messaging_client()
    await client.record_metric("api_gateway_cache_hits", 1.0, {"endpoint": endpoint})


async def record_cache_miss(endpoint: str):
    """
    Record a cache miss for an endpoint.
    
    Args:
        endpoint: Endpoint path
    """
    client = await get_messaging_client()
    await client.record_metric("api_gateway_cache_misses", 1.0, {"endpoint": endpoint})


async def record_rate_limit_hit(client_id: str, endpoint: str):
    """
    Record a rate limit hit.
    
    Args:
        client_id: Client identifier
        endpoint: Endpoint path
    """
    client = await get_messaging_client()
    await client.record_metric("api_gateway_rate_limit_hits", 1.0, {"client_id": client_id, "endpoint": endpoint})


async def set_circuit_breaker_state(service: str, state: int):
    """
    Set circuit breaker state.
    
    Args:
        service: Service name
        state: Circuit breaker state (0=closed, 1=open, 2=half-open)
    """
    client = await get_messaging_client()
    await client.record_metric("api_gateway_circuit_breaker_state", float(state), {"service": service})


# Alias for backward compatibility
async def set_circuit_state(service: str, state: int):
    """
    Alias for set_circuit_breaker_state.
    
    Args:
        service: Service name
        state: Circuit breaker state (0=closed, 1=open, 2=half-open)
    """
    return await set_circuit_breaker_state(service, state)


async def set_rate_limit_remaining(client_id: str, endpoint: str, remaining: int):
    """
    Set rate limit remaining count.
    
    Args:
        client_id: Client identifier
        endpoint: Endpoint path
        remaining: Remaining requests count
    """
    client = await get_messaging_client()
    await client.record_metric(
        "api_gateway_rate_limit_remaining",
        float(remaining),
        {"client_id": client_id, "endpoint": endpoint}
    )


async def record_request_count(method: str, endpoint: str, status_code: str):
    """
    Record a request count metric.
    
    Args:
        method: HTTP method
        endpoint: Endpoint path
        status_code: HTTP status code
    """
    client = await get_messaging_client()
    await client.record_metric(
        "api_gateway_request_count",
        1.0,
        {"method": method, "endpoint": endpoint, "status_code": status_code}
    )


async def record_request_latency(method: str, endpoint: str, duration: float):
    """
    Record a request latency metric.
    
    Args:
        method: HTTP method
        endpoint: Endpoint path
        duration: Request duration in seconds
    """
    client = await get_messaging_client()
    await client.record_metric(
        "api_gateway_request_latency_seconds",
        duration,
        {"method": method, "endpoint": endpoint}
    )


async def record_request_size(method: str, endpoint: str, size: int):
    """
    Record a request size metric.
    
    Args:
        method: HTTP method
        endpoint: Endpoint path
        size: Request size in bytes
    """
    client = await get_messaging_client()
    await client.record_metric(
        "api_gateway_request_size_bytes",
        float(size),
        {"method": method, "endpoint": endpoint}
    )


async def record_response_size(method: str, endpoint: str, size: int):
    """
    Record a response size metric.
    
    Args:
        method: HTTP method
        endpoint: Endpoint path
        size: Response size in bytes
    """
    client = await get_messaging_client()
    await client.record_metric(
        "api_gateway_response_size_bytes",
        float(size),
        {"method": method, "endpoint": endpoint}
    )


async def increment_active_requests(method: str, endpoint: str):
    """
    Increment active requests counter.
    
    Args:
        method: HTTP method
        endpoint: Endpoint path
    """
    client = await get_messaging_client()
    await client.record_metric(
        "api_gateway_active_requests",
        1.0,
        {"method": method, "endpoint": endpoint, "action": "increment"}
    )


async def decrement_active_requests(method: str, endpoint: str):
    """
    Decrement active requests counter.
    
    Args:
        method: HTTP method
        endpoint: Endpoint path
    """
    client = await get_messaging_client()
    await client.record_metric(
        "api_gateway_active_requests",
        -1.0,
        {"method": method, "endpoint": endpoint, "action": "decrement"}
    )
