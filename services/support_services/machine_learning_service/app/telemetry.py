"""
Telemetry module for distributed tracing with OpenTelemetry.

This module provides functionality for:
- Initializing OpenTelemetry tracing
- Configuring trace exporters
- Adding custom span attributes
- Propagating correlation IDs across service boundaries
"""

import logging
import os
from typing import Dict, Any, Optional, List, Callable
from functools import wraps
import inspect
import uuid

# OpenTelemetry imports
try:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.sampling import Decision, ParentBased, Sampler, SamplingResult, TraceIdRatioBased
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter, SpanExportResult
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    import grpc
    from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor
    from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
    from opentelemetry.instrumentation.redis import RedisInstrumentor
    from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
    from opentelemetry.trace import SpanKind, Status, StatusCode
    OPENTELEMETRY_AVAILABLE = True
except ImportError:
    OPENTELEMETRY_AVAILABLE = False
    # Define dummy classes and constants
    class SpanKind:
        INTERNAL = "INTERNAL"
        CLIENT = "CLIENT"
        SERVER = "SERVER"
        PRODUCER = "PRODUCER"
        CONSUMER = "CONSUMER"
        
    class StatusCode:
        OK = "OK"
        ERROR = "ERROR"
        UNSET = "UNSET"
        
    class Status:
        def __init__(self, status_code, description=None):
            pass

    class Sampler:
        pass
        
    class SpanExporter:
        pass

# Configure logging
logger = logging.getLogger(__name__)

# Global tracer instance
tracer = None

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
    
    if not OPENTELEMETRY_AVAILABLE:
        logger.info("OpenTelemetry not available, skipping initialization")
        return

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
    else:
        logger.warning("No OTLP endpoint provided. Traces will not be exported.")
    
    # Set global trace provider
    trace.set_tracer_provider(trace_provider)
    
    # Create tracer
    tracer = trace.get_tracer(f"{service_name}-tracer")
    
    # Auto-instrument packages if enabled
    if auto_instrument_packages:
        # These will be initialized when the respective clients are created
        try:
            AioHttpClientInstrumentor().instrument()
            HTTPXClientInstrumentor().instrument()
            RedisInstrumentor().instrument()
        except Exception as e:
            logger.warning(f"Failed to auto-instrument packages: {e}")
        # SQLAlchemy instrumentation is done when the engine is created
        
    logger.info(f"OpenTelemetry initialized for service: {service_name}")

def instrument_fastapi(app):
    """
    Instrument a FastAPI application with OpenTelemetry.
    
    Args:
        app: FastAPI application instance
    """
    if not OPENTELEMETRY_AVAILABLE:
        return

    FastAPIInstrumentor.instrument_app(
        app,
        tracer_provider=trace.get_tracer_provider(),
        excluded_urls="health,metrics",  # Exclude health check and metrics endpoints
    )
    logger.info("FastAPI application instrumented with OpenTelemetry")

def extract_correlation_id_from_headers(headers: Dict[str, str]) -> str:
    """
    Extract correlation ID from request headers or generate a new one.
    
    Args:
        headers: Request headers
        
    Returns:
        str: Correlation ID
    """
    correlation_id = headers.get("X-Correlation-ID")
    if not correlation_id:
        correlation_id = str(uuid.uuid4())
    return correlation_id

def inject_trace_context(headers: Dict[str, str]) -> Dict[str, str]:
    """
    Inject current trace context into headers for propagation.
    
    Args:
        headers: Headers dictionary to inject context into
        
    Returns:
        Dict[str, str]: Headers with injected trace context
    """
    # Get current span context
    current_context = trace.get_current_span().get_span_context()
    
    # Create a new headers dict if None was provided
    if headers is None:
        headers = {}
        
    if not OPENTELEMETRY_AVAILABLE:
        if "X-Correlation-ID" not in headers:
            headers["X-Correlation-ID"] = str(uuid.uuid4())
        return headers
    
    # Inject trace context into headers
    TraceContextTextMapPropagator().inject(headers)
    
    # Ensure correlation ID is present
    if "X-Correlation-ID" not in headers:
        headers["X-Correlation-ID"] = str(uuid.uuid4())
    
    return headers

def trace_method(name: Optional[str] = None, kind: SpanKind | str = SpanKind.INTERNAL):
    """
    Decorator to trace a method or function.
    
    Args:
        name: Optional name for the span (defaults to function name)
        kind: Span kind (default: INTERNAL)
        
    Returns:
        Callable: Decorated function
    """
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            if not OPENTELEMETRY_AVAILABLE or not tracer:
                return await func(*args, **kwargs)
            
            # Get span name from function name if not provided
            span_name = name or func.__name__
            
            # Extract correlation ID from kwargs if available
            correlation_id = kwargs.get("correlation_id")

            # Resolve span kind if it's a string
            actual_kind = kind
            if isinstance(kind, str):
                actual_kind = getattr(SpanKind, kind.upper(), SpanKind.INTERNAL)
            
            # Start span
            with tracer.start_as_current_span(span_name, kind=actual_kind) as span:
                # Add function arguments as span attributes
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                for param_name, param_value in bound_args.arguments.items():
                    # Skip 'self' parameter and complex objects
                    if param_name != "self" and isinstance(param_value, (str, int, float, bool)):
                        span.set_attribute(f"arg.{param_name}", str(param_value))
                
                # Add correlation ID as span attribute if available
                if correlation_id:
                    span.set_attribute("correlation_id", correlation_id)
                
                try:
                    result = await func(*args, **kwargs)
                    span.set_status(Status(StatusCode.OK))
                    return result
                except Exception as e:
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    span.record_exception(e)
                    raise
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            if not OPENTELEMETRY_AVAILABLE or not tracer:
                return func(*args, **kwargs)
            
            # Get span name from function name if not provided
            span_name = name or func.__name__
            
            # Extract correlation ID from kwargs if available
            correlation_id = kwargs.get("correlation_id")

            # Resolve span kind if it's a string
            actual_kind = kind
            if isinstance(kind, str):
                actual_kind = getattr(SpanKind, kind.upper(), SpanKind.INTERNAL)
            
            # Start span
            with tracer.start_as_current_span(span_name, kind=actual_kind) as span:
                # Add function arguments as span attributes
                sig = inspect.signature(func)
                bound_args = sig.bind(*args, **kwargs)
                for param_name, param_value in bound_args.arguments.items():
                    # Skip 'self' parameter and complex objects
                    if param_name != "self" and isinstance(param_value, (str, int, float, bool)):
                        span.set_attribute(f"arg.{param_name}", str(param_value))
                
                # Add correlation ID as span attribute if available
                if correlation_id:
                    span.set_attribute("correlation_id", correlation_id)
                
                try:
                    result = func(*args, **kwargs)
                    span.set_status(Status(StatusCode.OK))
                    return result
                except Exception as e:
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    span.record_exception(e)
                    raise
        
        # Return appropriate wrapper based on function type
        if inspect.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    
    return decorator

def add_span_attributes(attributes: Dict[str, Any]) -> None:
    """
    Add attributes to the current active span.
    
    Args:
        attributes: Dictionary of attributes to add
    """
    if not OPENTELEMETRY_AVAILABLE:
        return

    current_span = trace.get_current_span()
    if current_span:
        for key, value in attributes.items():
            if isinstance(value, (str, int, float, bool)):
                current_span.set_attribute(key, value)
            else:
                current_span.set_attribute(key, str(value))

def start_span(name: str, kind: SpanKind = SpanKind.INTERNAL, attributes: Optional[Dict[str, Any]] = None):
    """
    Start a new span.
    
    Args:
        name: Span name
        kind: Span kind
        attributes: Optional span attributes
        
    Returns:
        Span: New span
    """
    if not OPENTELEMETRY_AVAILABLE or not tracer:
        return None
    
    span = tracer.start_span(name, kind=kind)
    
    if attributes:
        for key, value in attributes.items():
            if isinstance(value, (str, int, float, bool)):
                span.set_attribute(key, value)
            else:
                span.set_attribute(key, str(value))
    
    return span

def get_current_span_context():
    """
    Get the current span context.
    
    Returns:
        SpanContext: Current span context
    """
    if not OPENTELEMETRY_AVAILABLE:
        return None
    return trace.get_current_span().get_span_context()

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
