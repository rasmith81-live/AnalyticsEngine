"""
Database Service - OpenTelemetry distributed tracing integration.

This module provides utilities for:
- Initializing OpenTelemetry for distributed tracing
- Instrumenting FastAPI applications
- Adding trace context propagation
- Creating and managing spans
- Adding custom attributes to spans
"""

import os
import logging
from typing import Dict, Optional, Any, Callable, TypeVar, cast
import functools
import inspect
from contextlib import contextmanager

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.trace.status import Status, StatusCode
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

# Setup logging
logger = logging.getLogger(__name__)

# Global tracer instance
tracer = None

# Type variables for function decorators
F = TypeVar('F', bound=Callable[..., Any])
AsyncF = TypeVar('AsyncF', bound=Callable[..., Any])

def initialize_telemetry(
    service_name: str,
    otlp_endpoint: Optional[str] = None,
    resource_attributes: Optional[Dict[str, str]] = None,
    auto_instrument_packages: bool = True
) -> None:
    """
    Initialize OpenTelemetry for distributed tracing.
    
    Args:
        service_name: Name of the service
        otlp_endpoint: OTLP exporter endpoint (e.g., "http://observability_service:4317")
        resource_attributes: Additional resource attributes for the service
        auto_instrument_packages: Whether to automatically instrument common packages
    """
    global tracer
    
    # Create resource attributes
    attributes = {
        "service.name": service_name,
        "service.namespace": "multiMicroservicePattern",
        "deployment.environment": os.environ.get("DEPLOYMENT_ENVIRONMENT", "development"),
    }
    
    # Add custom resource attributes if provided
    if resource_attributes:
        attributes.update(resource_attributes)
    
    # Create resource
    resource = Resource.create(attributes)
    
    # Create TracerProvider
    trace_provider = TracerProvider(resource=resource)
    
    # Configure OTLP exporter if endpoint is provided
    if otlp_endpoint:
        otlp_exporter = OTLPSpanExporter(endpoint=otlp_endpoint)
        span_processor = BatchSpanProcessor(otlp_exporter)
        trace_provider.add_span_processor(span_processor)
        logger.info(f"OTLP exporter configured with endpoint: {otlp_endpoint}")
    else:
        logger.warning("No OTLP endpoint provided. Traces will not be exported.")
    
    # Set global trace provider
    trace.set_tracer_provider(trace_provider)
    
    # Create tracer
    tracer = trace.get_tracer(f"{service_name}-tracer")
    
    # Auto-instrument packages if enabled
    if auto_instrument_packages:
        # These will be initialized when the respective clients are created
        AioHttpClientInstrumentor().instrument()
        HTTPXClientInstrumentor().instrument()
        RedisInstrumentor().instrument()
        # SQLAlchemy instrumentation is done when the engine is created
        
    logger.info(f"OpenTelemetry initialized for service: {service_name}")

def instrument_fastapi(app):
    """
    Instrument a FastAPI application with OpenTelemetry.
    
    Args:
        app: FastAPI application instance
    """
    try:
        FastAPIInstrumentor.instrument_app(app, tracer_provider=trace.get_tracer_provider())
        logger.info("FastAPI application instrumented with OpenTelemetry")
    except Exception as e:
        logger.warning(f"Failed to instrument FastAPI application: {str(e)}")

def instrument_sqlalchemy(engine):
    """
    Instrument SQLAlchemy with OpenTelemetry.
    
    Args:
        engine: SQLAlchemy engine instance
    """
    try:
        SQLAlchemyInstrumentor().instrument(
            engine=engine,
            tracer_provider=trace.get_tracer_provider()
        )
        logger.info("SQLAlchemy instrumented with OpenTelemetry")
    except Exception as e:
        logger.warning(f"Failed to instrument SQLAlchemy: {str(e)}")

def extract_correlation_id_from_headers(headers):
    """
    Extract correlation ID from request headers.
    
    Args:
        headers: HTTP request headers
        
    Returns:
        Correlation ID if found, None otherwise
    """
    # Check common correlation ID header names
    for header_name in ["x-correlation-id", "x-request-id", "request-id"]:
        if header_name in headers:
            return headers[header_name]
    return None

def inject_trace_context(headers: Dict[str, str], correlation_id: Optional[str] = None) -> Dict[str, str]:
    """
    Inject trace context into headers for distributed tracing.
    
    Args:
        headers: HTTP headers dictionary to inject context into
        correlation_id: Optional correlation ID to include
        
    Returns:
        Updated headers with trace context
    """
    # Create a copy of the headers to avoid modifying the original
    headers_copy = headers.copy()
    
    # Get the current span context
    span_context = trace.get_current_span().get_span_context()
    
    # Inject trace context into headers
    TraceContextTextMapPropagator().inject(headers_copy)
    
    # Add correlation ID if provided
    if correlation_id:
        headers_copy["x-correlation-id"] = correlation_id
    
    return headers_copy

def add_span_attributes(attributes: Dict[str, Any]) -> None:
    """
    Add attributes to the current active span.
    
    Args:
        attributes: Dictionary of attributes to add
    """
    span = trace.get_current_span()
    if span and hasattr(span, "set_attribute"):
        for key, value in attributes.items():
            if value is not None:  # Only add non-None values
                span.set_attribute(key, str(value))

def trace_method(name: Optional[str] = None, kind: str = "INTERNAL"):
    """
    Decorator to trace a method or function.
    
    Args:
        name: Optional name for the span (defaults to function name)
        kind: Span kind (SERVER, CLIENT, PRODUCER, CONSUMER, INTERNAL)
    """
    def decorator(func: F) -> F:
        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                # Get span name from function if not provided
                span_name = name if name else func.__name__
                
                # If tracer is not initialized, just execute the function without tracing
                if tracer is None:
                    logger.debug(f"Tracer not initialized, skipping span for {span_name}")
                    return await func(*args, **kwargs)
                
                # Set span kind
                span_kind = None
                if kind == "SERVER":
                    span_kind = trace.SpanKind.SERVER
                elif kind == "CLIENT":
                    span_kind = trace.SpanKind.CLIENT
                elif kind == "PRODUCER":
                    span_kind = trace.SpanKind.PRODUCER
                elif kind == "CONSUMER":
                    span_kind = trace.SpanKind.CONSUMER
                else:
                    span_kind = trace.SpanKind.INTERNAL
                
                try:
                    # Start a new span
                    with tracer.start_as_current_span(span_name, kind=span_kind) as span:
                        # Add function name as attribute
                        span.set_attribute("function.name", func.__name__)
                        
                        # Add class name if it's a method
                        if args and hasattr(args[0], "__class__"):
                            span.set_attribute("class.name", args[0].__class__.__name__)
                        
                        try:
                            # Execute the function
                            result = await func(*args, **kwargs)
                            return result
                        except Exception as e:
                            # Record error in span
                            span.set_status(Status(StatusCode.ERROR))
                            span.record_exception(e)
                            # Re-raise the exception
                            raise
                except Exception as e:
                    # If there's an error with the tracer, just execute the function
                    logger.debug(f"Error in tracer for {span_name}: {str(e)}")
                    return await func(*args, **kwargs)
                    
            return cast(F, async_wrapper)
        else:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Get span name from function if not provided
                span_name = name if name else func.__name__
                
                # If tracer is not initialized, just execute the function without tracing
                if tracer is None:
                    logger.debug(f"Tracer not initialized, skipping span for {span_name}")
                    return func(*args, **kwargs)
                
                # Set span kind
                span_kind = None
                if kind == "SERVER":
                    span_kind = trace.SpanKind.SERVER
                elif kind == "CLIENT":
                    span_kind = trace.SpanKind.CLIENT
                elif kind == "PRODUCER":
                    span_kind = trace.SpanKind.PRODUCER
                elif kind == "CONSUMER":
                    span_kind = trace.SpanKind.CONSUMER
                else:
                    span_kind = trace.SpanKind.INTERNAL
                
                try:
                    # Start a new span
                    with tracer.start_as_current_span(span_name, kind=span_kind) as span:
                        # Add function name as attribute
                        span.set_attribute("function.name", func.__name__)
                        
                        # Add class name if it's a method
                        if args and hasattr(args[0], "__class__"):
                            span.set_attribute("class.name", args[0].__class__.__name__)
                        
                        try:
                            # Execute the function
                            result = func(*args, **kwargs)
                            return result
                        except Exception as e:
                            # Record error in span
                            span.set_status(Status(StatusCode.ERROR))
                            span.record_exception(e)
                            # Re-raise the exception
                            raise
                except Exception as e:
                    # If there's an error with the tracer, just execute the function
                    logger.debug(f"Error in tracer for {span_name}: {str(e)}")
                    return func(*args, **kwargs)
                    
            return cast(F, wrapper)
    return decorator

@contextmanager
def create_span(name: str, kind: str = "INTERNAL", attributes: Optional[Dict[str, Any]] = None):
    """
    Context manager to create a new span.
    
    Args:
        name: Name for the span
        kind: Span kind (SERVER, CLIENT, PRODUCER, CONSUMER, INTERNAL)
        attributes: Optional attributes to add to the span
    """
    # If tracer is not initialized, just yield None
    if tracer is None:
        logger.debug(f"Tracer not initialized, skipping span for {name}")
        yield None
        return
        
    # Set span kind
    span_kind = None
    if kind == "SERVER":
        span_kind = trace.SpanKind.SERVER
    elif kind == "CLIENT":
        span_kind = trace.SpanKind.CLIENT
    elif kind == "PRODUCER":
        span_kind = trace.SpanKind.PRODUCER
    elif kind == "CONSUMER":
        span_kind = trace.SpanKind.CONSUMER
    else:
        span_kind = trace.SpanKind.INTERNAL
    
    try:
        # Start a new span
        with tracer.start_as_current_span(name, kind=span_kind) as span:
            # Add attributes if provided
            if attributes:
                for key, value in attributes.items():
                    if value is not None:  # Only add non-None values
                        span.set_attribute(key, str(value))
            try:
                yield span
            except Exception as e:
                # Record error in span
                span.set_status(Status(StatusCode.ERROR))
                span.record_exception(e)
                # Re-raise the exception
                raise
    except Exception as e:
        # If there's an error with the tracer, just yield None
        logger.debug(f"Error in tracer for {name}: {str(e)}")
        yield None
