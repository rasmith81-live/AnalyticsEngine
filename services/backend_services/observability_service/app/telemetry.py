"""
Telemetry module for Observability Service

This module provides OpenTelemetry instrumentation for the Observability Service.
It includes utilities for distributed tracing, metrics, and logging.
"""

import functools
import inspect
import uuid
from typing import Dict, Any, Optional, Callable, TypeVar, cast, Union, Dict, Any
import contextvars
from fastapi import FastAPI, Request

# Import Context directly to ensure it's always available
from opentelemetry.context.context import Context
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

from .logging import get_logger

logger = get_logger(__name__)

# Import other OpenTelemetry modules if available
try:
    import opentelemetry
    from opentelemetry import trace
    from opentelemetry.trace import SpanKind, Tracer, Status, StatusCode
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.sampling import ParentBased, TraceIdRatioBased
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    import grpc
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor
    from opentelemetry.instrumentation.asyncpg import AsyncPGInstrumentor
    from opentelemetry.instrumentation.redis import RedisInstrumentor

    OPENTELEMETRY_AVAILABLE = True
except ImportError as e:
    OPENTELEMETRY_AVAILABLE = False
    logger.error(f"Failed to import OpenTelemetry modules: {e}. Telemetry will be disabled.")

# Type variables for function decorators
F = TypeVar('F', bound=Callable[..., Any])
T = TypeVar('T')

# Context variable to store correlation ID
correlation_id_var = contextvars.ContextVar("correlation_id", default=None)


def initialize_telemetry(
    service_name: str,
    otlp_endpoint: str,
    resource_attributes: Optional[Dict[str, str]] = None
) -> bool:
    """
    Initialize OpenTelemetry for distributed tracing.
    
    Args:
        service_name: Name of the service
        otlp_endpoint: OpenTelemetry collector endpoint
        resource_attributes: Additional resource attributes
        
    Returns:
        bool: True if initialization was successful, False otherwise
    """
    if not OPENTELEMETRY_AVAILABLE:
        logger.warning("OpenTelemetry packages not available, skipping initialization")
        return False
    
    try:
        # Create resource with service information
        attributes = {
            "service.name": service_name,
            "service.namespace": "observability",
            "service.instance.id": str(uuid.uuid4())
        }
        
        # Add additional resource attributes if provided
        if resource_attributes:
            attributes.update(resource_attributes)
        
        resource = Resource.create(attributes)
        
        # Configure sampling to respect parent decisions and sample 10% of new traces
        sampler = ParentBased(root=TraceIdRatioBased(0.1))

        # Create tracer provider
        tracer_provider = TracerProvider(resource=resource, sampler=sampler)
        
        # The Observability Service should not export its own telemetry.
        # It only needs a TracerProvider to create spans for its internal operations.
        logger.info("Skipping OTLP exporter setup for observability_service.")
        
        # Set tracer provider
        trace.set_tracer_provider(tracer_provider)
        
        # Initialize instrumentation for common libraries
        AioHttpClientInstrumentor().instrument()
        AsyncPGInstrumentor().instrument()
        RedisInstrumentor().instrument()
        
        logger.info(f"OpenTelemetry initialized for service {service_name} with endpoint {otlp_endpoint}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to initialize OpenTelemetry: {str(e)}")
        return False


def instrument_fastapi(app: FastAPI) -> None:
    """
    Instrument a FastAPI application with OpenTelemetry.
    
    Args:
        app: FastAPI application to instrument
    """
    if not OPENTELEMETRY_AVAILABLE:
        logger.warning("OpenTelemetry packages not available, skipping FastAPI instrumentation")
        return
    
    try:
        FastAPIInstrumentor.instrument_app(
            app,
            excluded_urls="health,metrics",
            tracer_provider=trace.get_tracer_provider()
        )
        logger.info("FastAPI application instrumented with OpenTelemetry")
    except Exception as e:
        logger.error(f"Failed to instrument FastAPI application: {str(e)}")


def extract_correlation_id_from_headers(headers: Dict[str, str]) -> Optional[str]:
    """
    Extract correlation ID from request headers.
    
    Args:
        headers: Request headers
        
    Returns:
        Optional[str]: Correlation ID if found, None otherwise
    """
    # Check for correlation ID in various header formats
    for header in ["X-Correlation-ID", "X-Correlation-Id", "x-correlation-id"]:
        if header in headers:
            return headers[header]
    
    return None


def set_correlation_id(correlation_id: Optional[str] = None) -> str:
    """
    Set correlation ID in context.
    
    Args:
        correlation_id: Correlation ID to set
        
    Returns:
        str: Correlation ID (generated if not provided)
    """
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())
    
    correlation_id_var.set(correlation_id)
    return correlation_id


def get_correlation_id() -> Optional[str]:
    """
    Get correlation ID from context.
    
    Returns:
        Optional[str]: Correlation ID if set, None otherwise
    """
    return correlation_id_var.get()


def add_span_attributes(attributes: Dict[str, Any]) -> None:
    """
    Add attributes to the current span.
    
    Args:
        attributes: Attributes to add
    """
    if not OPENTELEMETRY_AVAILABLE:
        return
    
    try:
        current_span = trace.get_current_span()
        for key, value in attributes.items():
            if value is not None:
                current_span.set_attribute(key, str(value))
    except Exception as e:
        logger.debug(f"Failed to add span attributes: {str(e)}")


def trace_method(name: Optional[str] = None, kind: Optional[str] = None) -> Callable[[F], F]:
    """
    Decorator to trace a method with OpenTelemetry.
    
    Args:
        name: Name of the span
        kind: Kind of span (SERVER, CLIENT, PRODUCER, CONSUMER, INTERNAL)
        
    Returns:
        Callable: Decorated function
    """
    def decorator(func: F) -> F:
        if not OPENTELEMETRY_AVAILABLE:
            return func
        
        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            # Get span name from function name if not provided
            span_name = name or f"{func.__module__}.{func.__qualname__}"
            
            # Get tracer
            tracer = trace.get_tracer(func.__module__)
            
            # Get correlation ID from kwargs or context
            correlation_id = kwargs.get("correlation_id") or get_correlation_id()
            
            # Start span
            with tracer.start_as_current_span(span_name) as span:
                # Add span attributes
                span.set_attribute("function.name", func.__qualname__)
                span.set_attribute("function.module", func.__module__)
                
                if kind:
                    span.set_attribute("span.kind", kind)
                
                if correlation_id:
                    span.set_attribute("correlation_id", correlation_id)
                
                # Call function
                try:
                    result = await func(*args, **kwargs)
                    return result
                except Exception as e:
                    # Record exception
                    span.record_exception(e)
                    span.set_attribute("error", True)
                    span.set_attribute("error.message", str(e))
                    raise
        
        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            # Get span name from function name if not provided
            span_name = name or f"{func.__module__}.{func.__qualname__}"
            
            # Get tracer
            tracer = trace.get_tracer(func.__module__)
            
            # Get correlation ID from kwargs or context
            correlation_id = kwargs.get("correlation_id") or get_correlation_id()
            
            # Start span
            with tracer.start_as_current_span(span_name) as span:
                # Add span attributes
                span.set_attribute("function.name", func.__qualname__)
                span.set_attribute("function.module", func.__module__)
                
                if kind:
                    span.set_attribute("span.kind", kind)
                
                if correlation_id:
                    span.set_attribute("correlation_id", correlation_id)
                
                # Call function
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    # Record exception
                    span.record_exception(e)
                    span.set_attribute("error", True)
                    span.set_attribute("error.message", str(e))
                    raise
        
        # Use appropriate wrapper based on function type
        if inspect.iscoroutinefunction(func):
            return cast(F, async_wrapper)
        else:
            return cast(F, sync_wrapper)
    
    return decorator


def extract_context_from_request(request: Request) -> Context:
    """
    Extract OpenTelemetry context from request headers.
    
    Args:
        request: FastAPI request
        
    Returns:
        Union[Dict[str, Any], object]: OpenTelemetry context or empty dict if not available
    """
    if not OPENTELEMETRY_AVAILABLE:
        return {}
    
    try:
        # Extract context from request headers
        carrier = {}
        for key, value in request.headers.items():
            carrier[key] = value
        
        # Extract correlation ID
        correlation_id = extract_correlation_id_from_headers(carrier)
        if correlation_id:
            set_correlation_id(correlation_id)
        
        # Extract trace context
        return TraceContextTextMapPropagator().extract(carrier=carrier)
    except Exception as e:
        logger.debug(f"Failed to extract context from request: {str(e)}")
        return {}
