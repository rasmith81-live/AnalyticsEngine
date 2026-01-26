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

# Setup logging
logger = logging.getLogger(__name__)

# OpenTelemetry imports
from opentelemetry import trace, metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.sampling import Decision, ParentBased, Sampler, SamplingResult, TraceIdRatioBased
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter, SpanExportResult
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
import grpc
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.trace.status import Status, StatusCode

# Optional instrumentation imports
# We'll check if these are available at runtime
FastAPIInstrumentor = None
AioHttpClientInstrumentor = None
HTTPXClientInstrumentor = None
RedisInstrumentor = None
SQLAlchemyInstrumentor = None

try:
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
except ImportError:
    logger.warning("FastAPI instrumentation not available")

try:
    from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor
except ImportError:
    logger.warning("AioHttp instrumentation not available")

try:
    from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
except ImportError:
    logger.warning("HTTPX instrumentation not available")

try:
    from opentelemetry.instrumentation.redis import RedisInstrumentor
except ImportError:
    logger.warning("Redis instrumentation not available")

try:
    from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
except ImportError:
    logger.warning("SQLAlchemy instrumentation not available")

# Global tracer and metric exporter instances
tracer = None
otlp_metric_exporter: Optional[OTLPMetricExporter] = None

# Type variables for function decorators
F = TypeVar('F', bound=Callable[..., Any])
AsyncF = TypeVar('AsyncF', bound=Callable[..., Any])

def initialize_telemetry(
    service_name: str,
    otlp_endpoint: Optional[str] = None,
    resource_attributes: Optional[Dict[str, str]] = None,
    auto_instrument_packages: bool = True,
    trace_sample_rate: float = 0.1,
    export_interval_ms: int = 15000
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
    
    # Defer sampling decision to a custom exporter that filters based on error status.
    sampler = ParentBased(root=ErrorSampler(fallback_sampler=TraceIdRatioBased(trace_sample_rate)))

    # Create TracerProvider
    trace_provider = TracerProvider(resource=resource, sampler=sampler)
    
    # Configure OTLP exporter if endpoint is provided
    if otlp_endpoint:
        base_exporter = None
        try:
            # Attempt to create secure credentials from the certificate file
            with open('/certs/server.crt', 'rb') as f:
                cert_bytes = f.read()
            credentials = grpc.ssl_channel_credentials(root_certificates=cert_bytes)
            base_exporter = OTLPSpanExporter(
                endpoint=otlp_endpoint,
                credentials=credentials
            )
            logger.info(f"OTLP exporter configured with secure endpoint: {otlp_endpoint}")
        except (FileNotFoundError, ImportError):
            logger.warning("TLS certificate not found or grpc not installed. Falling back to insecure OTLP exporter.")
            base_exporter = OTLPSpanExporter(endpoint=otlp_endpoint, insecure=True)
        
        otlp_exporter = ErrorFilteringExporter(base_exporter)
        span_processor = BatchSpanProcessor(
            otlp_exporter, schedule_delay_millis=export_interval_ms
        )
        trace_provider.add_span_processor(span_processor)
        logger.info(f"OTLP trace exporter configured with endpoint: {otlp_endpoint}")

        # Configure OTLP Metric Exporter
        metric_exporter = OTLPMetricExporter(
            endpoint=otlp_endpoint,
            credentials=credentials if 'credentials' in locals() and credentials is not None else None,
            insecure=True if 'credentials' not in locals() or credentials is None else False
        )
        metric_reader = PeriodicExportingMetricReader(metric_exporter)
        meter_provider = MeterProvider(
            resource=resource,
            metric_readers=[metric_reader]
        )
        metrics.set_meter_provider(meter_provider)
        logger.info(f"OTLP metric exporter configured with endpoint: {otlp_endpoint}")
    else:
        logger.warning("No OTLP endpoint provided. Traces will not be exported.")
    
    # Set global trace provider
    trace.set_tracer_provider(trace_provider)
    
    # Create tracer
    tracer = trace.get_tracer(f"{service_name}-tracer")
    
    # Auto-instrument packages if enabled
    if auto_instrument_packages:
        # These will be initialized when the respective clients are created
        if AioHttpClientInstrumentor:
            try:
                AioHttpClientInstrumentor().instrument()
                logger.info("AioHttp client instrumented with OpenTelemetry")
            except Exception as e:
                logger.warning(f"Failed to instrument AioHttp client: {str(e)}")
                
        if HTTPXClientInstrumentor:
            try:
                HTTPXClientInstrumentor().instrument()
                logger.info("HTTPX client instrumented with OpenTelemetry")
            except Exception as e:
                logger.warning(f"Failed to instrument HTTPX client: {str(e)}")
                
        if RedisInstrumentor:
            try:
                RedisInstrumentor().instrument()
                logger.info("Redis client instrumented with OpenTelemetry")
            except Exception as e:
                logger.warning(f"Failed to instrument Redis client: {str(e)}")
                
        # SQLAlchemy instrumentation is done when the engine is created
        
    logger.info(f"OpenTelemetry initialized for service: {service_name}")

def instrument_fastapi(app):
    """
    Instrument a FastAPI application with OpenTelemetry.
    
    Args:
        app: FastAPI application instance
    """
    if not FastAPIInstrumentor:
        logger.warning("FastAPI instrumentation not available, skipping instrumentation")
        return
        
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
        
    Note: SQLAlchemy instrumentation is disabled for async engines as it causes
    greenlet context issues with async session operations. The instrumentation
    uses sync context managers that break the async greenlet spawn context.
    """
    if not SQLAlchemyInstrumentor:
        logger.warning("SQLAlchemy instrumentation not available, skipping instrumentation")
        return
    
    # Skip instrumentation for async engines - causes greenlet_spawn errors
    if hasattr(engine, 'sync_engine'):
        logger.info("Async engine detected. Skipping SQLAlchemy instrumentation to avoid greenlet context issues.")
        return
        
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
                
                # Start a new span if tracer is available
                if tracer is not None:
                    try:
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
                                # Record exception on span
                                span.set_status(Status(StatusCode.ERROR))
                                span.record_exception(e)
                                raise
                    except Exception as e:
                        logger.warning(f"Error creating span for {span_name}: {str(e)}")
                        return await func(*args, **kwargs)
                else:
                    # Execute function without tracing
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
                
                # Start a new span if tracer is available
                if tracer is not None:
                    try:
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
                else:
                    # Execute function without tracing
                    return func(*args, **kwargs)
                    
            return cast(F, wrapper)
    return decorator

class ErrorSampler(Sampler):
    """
    A sampler that defers the sampling decision for root spans, allowing a downstream
    exporter to decide based on error status. It respects parent sampling decisions.
    """
    def __init__(self, fallback_sampler: Sampler):
        self._fallback_sampler = fallback_sampler

    def should_sample(
        self, parent_context, trace_id, name, kind=None, attributes=None, links=None
    ) -> SamplingResult:
        # If there is a parent context, defer to the parent's decision
        parent_span_context = trace.get_current_span(parent_context).get_span_context()
        if parent_span_context is not None and parent_span_context.is_remote:
            return SamplingResult(parent_span_context.trace_flags)
        
        # This sampler is designed to be a root sampler. The ParentBased sampler that
        # wraps it will handle parent-based decisions. For root spans, we always
        # sample to allow the exporter to make the final filtering decision.
        return SamplingResult(Decision.RECORD_AND_SAMPLE)

    def get_description(self) -> str:
        return "ErrorSampler"


class ErrorFilteringExporter(SpanExporter):
    """
    A span exporter that filters traces, exporting only those that contain errors.
    """
    def __init__(self, underlying_exporter: SpanExporter):
        self._underlying_exporter = underlying_exporter

    def export(self, spans) -> SpanExportResult:
        spans_by_trace_id = {}
        for span in spans:
            trace_id = span.context.trace_id
            if trace_id not in spans_by_trace_id:
                spans_by_trace_id[trace_id] = []
            spans_by_trace_id[trace_id].append(span)

        errored_spans = []
        for trace_id, trace_spans in spans_by_trace_id.items():
            has_error = any(span.status.status_code == StatusCode.ERROR for span in trace_spans)
            if has_error:
                errored_spans.extend(trace_spans)

        if not errored_spans:
            return SpanExportResult.SUCCESS

        return self._underlying_exporter.export(errored_spans)

    def shutdown(self):
        self._underlying_exporter.shutdown()

    def force_flush(self, timeout_millis: int = 30000) -> SpanExportResult:
        return self._underlying_exporter.force_flush(timeout_millis)

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
