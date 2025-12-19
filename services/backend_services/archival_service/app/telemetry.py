"""
Telemetry module for the Archival Service.

This module provides OpenTelemetry instrumentation and utilities for distributed tracing
and correlation ID propagation across service boundaries.
"""

import functools
import inspect
import logging
from contextlib import asynccontextmanager
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, cast

from fastapi import FastAPI, Request, Response

try:
    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    import grpc
    from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
    from opentelemetry.instrumentation.redis import RedisInstrumentor
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter, SpanExportResult
    from opentelemetry.sdk.trace.sampling import ParentBased, Sampler, SamplingResult, TraceIdRatioBased
    from opentelemetry.trace import SpanKind, Status, StatusCode
    from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
    OPENTELEMETRY_AVAILABLE = True
except ImportError:
    OPENTELEMETRY_AVAILABLE = False
    # Define dummy classes/functions if OTel is not available
    class SpanKind:
        SERVER = "SERVER"
        CLIENT = "CLIENT"
        PRODUCER = "PRODUCER"
        CONSUMER = "CONSUMER"
        INTERNAL = "INTERNAL"
    
    class Status:
        def __init__(self, status_code, description=None): pass
        
    class StatusCode:
        OK = "OK"
        ERROR = "ERROR"
        
    class trace:
        @staticmethod
        def get_tracer(name): return DummyTracer()
        @staticmethod
        def get_current_span(): return DummySpan()
        
        class SpanContext:
            def __init__(self, trace_id=0, span_id=0, is_remote=False, trace_flags=0, trace_state=None):
                self.trace_id = trace_id
                self.span_id = span_id
                self.is_remote = is_remote
                self.trace_flags = trace_flags
                self.trace_state = trace_state
                
        class TraceFlags:
            SAMPLED = 0x01
            DEFAULT = 0x00

    class DummySpan:
        def set_attribute(self, key, value): pass
        def set_status(self, status): pass
        def record_exception(self, e): pass
        def __enter__(self): return self
        def __exit__(self, exc_type, exc_val, exc_tb): pass
        def get_span_context(self): return trace.SpanContext()
        
    class DummyTracer:
        def start_as_current_span(self, name, kind=None): return DummySpan()

    # Dummy base classes for inheritance
    class Sampler:
        def should_sample(self, parent_context, trace_id, name, kind=None, attributes=None, links=None):
            return SamplingResult(SamplingDecision.DROP, None)
        def get_description(self): return "DummySampler"

    class SpanExporter:
        def export(self, spans): return SpanExportResult.SUCCESS
        def shutdown(self): pass
        def force_flush(self, timeout_millis=30000): return SpanExportResult.SUCCESS
        
    class SamplingResult:
        def __init__(self, decision, trace_state): pass
        
    class SamplingDecision:
        RECORD_AND_SAMPLE = 1
        DROP = 0
        
    class SpanExportResult:
        SUCCESS = 1
        FAILURE = 0

# Type variables for function decorators
F = TypeVar("F", bound=Callable[..., Any])
AsyncF = TypeVar("AsyncF", bound=Callable[..., Any])

# Global tracer instance
_tracer = None
logger = logging.getLogger(__name__)

def initialize_telemetry(
    service_name: str,
    otlp_endpoint: Optional[str] = None,
    resource_attributes: Optional[Dict[str, Any]] = None,
    trace_sample_rate: float = 0.1,
    export_interval_ms: int = 15000,
    auto_instrument: bool = True
) -> None:
    """
    Initialize OpenTelemetry tracing for the service.
    
    Args:
        service_name: Name of the service for identification in traces
        otlp_endpoint: OTLP exporter endpoint (e.g., http://observability_service:4317)
        resource_attributes: Additional resource attributes to include with all spans
        trace_sample_rate: Sampling rate for traces (0.0 to 1.0)
        auto_instrument_packages: Whether to automatically instrument common packages
    """
    global _tracer
    
    # Create resource with service information
    attributes = {
        "service.name": service_name,
        "service.namespace": "archival",
        "service.instance.id": service_name,
        "service.version": "1.0.0",
    }
    
    # Add custom resource attributes if provided
    if resource_attributes:
        attributes.update(resource_attributes)
    
    # Create resource
    resource = Resource.create(attributes)
    
    # Defer sampling decision to a custom exporter that filters based on error status.
    sampler = ParentBased(root=ErrorSampler(fallback_sampler=TraceIdRatioBased(trace_sample_rate)))
    
    # Create trace provider with resource and sampler
    trace_provider = TracerProvider(resource=resource, sampler=sampler)
    
    # Add OTLP exporter if endpoint is provided
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
    
    # Set global trace provider
    trace.set_tracer_provider(trace_provider)
    
    # Create tracer for this service
    _tracer = trace.get_tracer(f"{service_name}-tracer")
    
    # Auto-instrument common packages if enabled
    if auto_instrument:
        AioHttpClientInstrumentor().instrument()
        HTTPXClientInstrumentor().instrument()
        RedisInstrumentor().instrument()
    
    logger.info(f"OpenTelemetry tracing initialized for {service_name}")

def instrument_fastapi(app: FastAPI) -> None:
    """
    Instrument a FastAPI application with OpenTelemetry.
    
    Args:
        app: FastAPI application instance to instrument
    """
    FastAPIInstrumentor.instrument_app(app, tracer_provider=trace.get_tracer_provider())
    logger.info("FastAPI application instrumented with OpenTelemetry")

def extract_correlation_id(request: Request) -> Optional[str]:
    """
    Extract correlation ID from request headers.
    
    Args:
        request: FastAPI request object
        
    Returns:
        Correlation ID if found, None otherwise
    """
    return extract_correlation_id_from_headers(request.headers)


def extract_correlation_id_from_headers(headers: Dict[str, str]) -> Optional[str]:
    """
    Extract correlation ID from headers dictionary.
    
    Args:
        headers: Dictionary of headers
        
    Returns:
        Correlation ID if found, None otherwise
    """
    # Check common correlation ID header names in priority order
    for header in ["X-Correlation-ID", "X-Request-ID", "X-Trace-ID", "traceparent"]:
        if header.lower() in {k.lower(): k for k in headers}:
            actual_key = {k.lower(): k for k in headers}[header.lower()]
            return headers[actual_key]
    return None

def extract_trace_context(headers: Dict[str, str]) -> Optional[trace.SpanContext]:
    """
    Extract trace context from headers.
    
    Args:
        headers: Dictionary of headers
        
    Returns:
        SpanContext if valid context found, None otherwise
    """
    try:
        carrier = {}
        for k, v in headers.items():
            carrier[k.lower()] = v
        
        ctx = TraceContextTextMapPropagator().extract(carrier=carrier)
        return ctx
    except Exception as e:
        logger.debug(f"Failed to extract trace context: {e}")
        return None

def inject_trace_context(headers: Dict[str, str]) -> None:
    """
    Inject current trace context into headers.
    
    Args:
        headers: Dictionary of headers to inject context into
    """
    try:
        TraceContextTextMapPropagator().inject(carrier=headers)
    except Exception as e:
        logger.debug(f"Failed to inject trace context: {e}")

def add_span_attributes(attributes: Dict[str, Any]) -> None:
    """
    Add attributes to the current active span.
    
    Args:
        attributes: Dictionary of attributes to add
    """
    current_span = trace.get_current_span()
    if current_span:
        for key, value in attributes.items():
            if value is not None:
                current_span.set_attribute(key, str(value))

def trace_method(name: Optional[str] = None, kind: Optional[str] = None) -> Callable[[F], F]:
    """
    Decorator to trace a method or function.
    
    Args:
        name: Name of the span (defaults to function name)
        kind: SpanKind (SERVER, CLIENT, PRODUCER, CONSUMER, INTERNAL)
        
    Returns:
        Decorated function
    """
    def decorator(func: F) -> F:
        span_name = name or func.__qualname__
        span_kind = _get_span_kind(kind)
        
        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            if not _tracer:
                return func(*args, **kwargs)
            
            with _tracer.start_as_current_span(span_name, kind=span_kind) as span:
                try:
                    result = func(*args, **kwargs)
                    span.set_status(Status(StatusCode.OK))
                    return result
                except Exception as e:
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    span.record_exception(e)
                    raise
        
        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            if not _tracer:
                return await func(*args, **kwargs)
            
            with _tracer.start_as_current_span(span_name, kind=span_kind) as span:
                try:
                    result = await func(*args, **kwargs)
                    span.set_status(Status(StatusCode.OK))
                    return result
                except Exception as e:
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    span.record_exception(e)
                    raise
        
        if inspect.iscoroutinefunction(func):
            return cast(F, async_wrapper)
        return cast(F, sync_wrapper)
    
    return decorator

@asynccontextmanager
async def traced_span(name: str, kind: Optional[str] = None, attributes: Optional[Dict[str, Any]] = None):
    """
    Async context manager for creating a traced span.
    
    Args:
        name: Name of the span
        kind: SpanKind (SERVER, CLIENT, PRODUCER, CONSUMER, INTERNAL)
        attributes: Initial attributes for the span
        
    Yields:
        Active span
    """
    if not _tracer:
        yield None
        return
    
    span_kind = _get_span_kind(kind)
    with _tracer.start_as_current_span(name, kind=span_kind) as span:
        if attributes:
            for key, value in attributes.items():
                if value is not None:
                    span.set_attribute(key, str(value))
        try:
            yield span
            span.set_status(Status(StatusCode.OK))
        except Exception as e:
            span.set_status(Status(StatusCode.ERROR, str(e)))
            span.record_exception(e)
            raise

def _get_span_kind(kind: Optional[str]) -> SpanKind:
    """
    Convert string span kind to SpanKind enum.
    
    Args:
        kind: String representation of span kind
        
    Returns:
        SpanKind enum value
    """
    if not kind:
        return SpanKind.INTERNAL
    
    kind_map = {
        "SERVER": SpanKind.SERVER,
        "CLIENT": SpanKind.CLIENT,
        "PRODUCER": SpanKind.PRODUCER,
        "CONSUMER": SpanKind.CONSUMER,
        "INTERNAL": SpanKind.INTERNAL
    }
    
    return kind_map.get(kind.upper(), SpanKind.INTERNAL)


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
        if parent_span_context and parent_span_context.is_remote:
            decision = (
                SamplingDecision.RECORD_AND_SAMPLE
                if parent_span_context.trace_flags & trace.TraceFlags.SAMPLED
                else SamplingDecision.DROP
            )
            return SamplingResult(decision, parent_span_context.trace_state)
        
        # For root spans, use the fallback sampler to make a decision.
        # This allows TraceIdRatioBased to function correctly for new traces.
        return self._fallback_sampler.should_sample(
            parent_context, trace_id, name, kind, attributes, links
        )

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
