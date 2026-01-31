# =============================================================================
# Observability Setup
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""OpenTelemetry configuration for multi_agent_service."""

import os
import logging
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger(__name__)

# Check if OpenTelemetry is available
try:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
    from opentelemetry.instrumentation.redis import RedisInstrumentor
    from opentelemetry.sdk.resources import Resource
    OTEL_AVAILABLE = True
except ImportError:
    OTEL_AVAILABLE = False
    logger.warning("OpenTelemetry not available - tracing disabled")


SERVICE_NAME = "multi_agent_service"

tracer = None


def setup_observability(app):
    """
    Configure OpenTelemetry for the service.
    
    Sets up:
    - Trace provider with OTLP exporter
    - FastAPI instrumentation
    - HTTPX client instrumentation
    - Redis instrumentation
    """
    global tracer
    
    if not OTEL_AVAILABLE:
        logger.warning("OpenTelemetry not available - skipping setup")
        return
    
    enable_tracing = os.getenv("ENABLE_DISTRIBUTED_TRACING", "true").lower() == "true"
    if not enable_tracing:
        logger.info("Distributed tracing disabled by configuration")
        return
    
    try:
        resource = Resource.create({
            "service.name": SERVICE_NAME,
            "service.version": os.getenv("SERVICE_VERSION", "1.0.0"),
            "deployment.environment": os.getenv("ENVIRONMENT", "development")
        })
        
        provider = TracerProvider(resource=resource)
        
        otlp_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")
        if otlp_endpoint:
            exporter = OTLPSpanExporter(
                endpoint=otlp_endpoint,
                insecure=os.getenv("OTEL_EXPORTER_OTLP_INSECURE", "false").lower() == "true"
            )
            provider.add_span_processor(BatchSpanProcessor(exporter))
        
        trace.set_tracer_provider(provider)
        tracer = trace.get_tracer(SERVICE_NAME)
        
        FastAPIInstrumentor.instrument_app(app)
        HTTPXClientInstrumentor().instrument()
        RedisInstrumentor().instrument()
        
        logger.info(f"OpenTelemetry configured for {SERVICE_NAME}")
        
    except Exception as e:
        logger.error(f"Failed to configure OpenTelemetry: {e}")


def get_tracer():
    """Get the configured tracer."""
    global tracer
    if tracer is None and OTEL_AVAILABLE:
        tracer = trace.get_tracer(SERVICE_NAME)
    return tracer


def traced(span_name: str = None):
    """
    Decorator to add tracing to a function.
    
    Usage:
        @traced("my_operation")
        async def my_function():
            pass
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def async_wrapper(*args, **kwargs) -> Any:
            t = get_tracer()
            if t is None:
                return await func(*args, **kwargs)
            
            name = span_name or func.__name__
            with t.start_as_current_span(name) as span:
                try:
                    result = await func(*args, **kwargs)
                    return result
                except Exception as e:
                    span.record_exception(e)
                    raise
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs) -> Any:
            t = get_tracer()
            if t is None:
                return func(*args, **kwargs)
            
            name = span_name or func.__name__
            with t.start_as_current_span(name) as span:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    span.record_exception(e)
                    raise
        
        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator


def add_span_attributes(attributes: dict):
    """Add attributes to the current span."""
    if not OTEL_AVAILABLE:
        return
    
    span = trace.get_current_span()
    if span:
        for key, value in attributes.items():
            span.set_attribute(key, value)
