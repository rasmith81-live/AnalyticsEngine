"""
Metrics middleware for the API Gateway service.
Collects and exposes Prometheus metrics.
"""
import time
from typing import Callable

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.core.logging import get_logger
from app.core.metrics import (
    setup_metrics_endpoint,
    record_request_count,
    record_request_latency,
    record_request_size,
    record_response_size,
    increment_active_requests,
    decrement_active_requests,
    set_circuit_state,
    set_rate_limit_remaining,
    record_http_traffic
)

logger = get_logger(__name__)

# Metrics are now defined in app.core.metrics

def setup_metrics(app: FastAPI) -> None:
    """
    Set up Prometheus metrics for the application.
    
    Args:
        app: FastAPI application
    """
    # Add metrics endpoint
    setup_metrics_endpoint(app)
    logger.info("Prometheus metrics initialized")

class MetricsMiddleware(BaseHTTPMiddleware):
    """
    Middleware that collects Prometheus metrics.
    """
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and collect metrics.
        
        Args:
            request: FastAPI request
            call_next: Next middleware or endpoint handler
            
        Returns:
            Response from downstream
        """
        # Extract service from path
        service = "unknown"
        try:
            _, service, *_ = request.url.path.strip("/").split("/")
        except ValueError:
            pass
        
        # Get endpoint for metrics
        endpoint = request.url.path
        method = request.method
        
        # Track request size
        request_size = 0
        if "content-length" in request.headers:
            request_size = int(request.headers.get("content-length", 0))
        await record_request_size(method, endpoint, request_size)
        
        # Track active requests
        await increment_active_requests(method, endpoint)
        
        # Track request latency
        start_time = time.time()
        
        try:
            # Process the request
            response = await call_next(request)
            
            # Record metrics
            status_code = response.status_code
            await record_request_count(method, endpoint, str(status_code))
            
            # Track response size
            response_size = 0
            if "content-length" in response.headers:
                response_size = int(response.headers.get("content-length", 0))
            await record_response_size(method, endpoint, response_size)
            
            # Track HTTP traffic from UI to API Gateway for SCADA visualization
            # Determine source based on Origin/Referer header
            origin = request.headers.get("origin", "") or request.headers.get("referer", "")
            source = "demo_config_ui" if "localhost:3000" in origin or "demo_config" in origin else "external_client"
            await record_http_traffic(
                source=source,
                target="api_gateway",
                method=method,
                endpoint=endpoint,
                request_bytes=request_size,
                response_bytes=response_size
            )
            
            return response
            
        except Exception as e:
            # Record error metrics
            await record_request_count(method, endpoint, "500")
            raise e
            
        finally:
            # Record latency and decrement active requests
            await record_request_latency(method, endpoint, time.time() - start_time)
            await decrement_active_requests(method, endpoint)
