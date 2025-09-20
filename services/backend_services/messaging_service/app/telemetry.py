"""
Telemetry module for messaging service.

This module provides OpenTelemetry instrumentation for the messaging service,
including trace context propagation, span creation, and attribute management.
"""

import asyncio
import functools
import json
import logging
import uuid
from contextlib import contextmanager
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, cast

from fastapi import Request, Response
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
from opentelemetry.sdk.trace.sampling import Decision, ParentBased, Sampler, SamplingResult, TraceIdRatioBased
from opentelemetry.trace import SpanKind, Status, StatusCode
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

# Type variables for function decorators
F = TypeVar("F", bound=Callable[..., Any])
T = TypeVar("T")

# Configure logger
logger = logging.getLogger(__name__)

# Global tracer instance
_tracer = None

# Correlation ID header name
CORRELATION_ID_HEADER = "X-Correlation-ID"


def initialize_telemetry(
    service_name: str,
    otlp_endpoint: Optional[str] = None,
    resource_attributes: Optional[Dict[str, str]] = None,
    trace_sample_rate: float = 0.1,
    auto_instrument_packages: bool = True,
    max_retry_attempts: int = 3,
    retry_delay_seconds: float = 5.0,
    max_export_batch_size: int = 50,
    export_timeout_seconds: float = 5.0,
    schedule_delay_millis: int = 10000
) -> None:
    """
    Initialize OpenTelemetry for the messaging service.

    Args:
        service_name: Name of the service
        otlp_endpoint: OpenTelemetry collector endpoint (e.g., localhost:4317)
        resource_attributes: Additional resource attributes
        trace_sample_rate: Sampling rate for traces (0.0 to 1.0)
        auto_instrument_packages: Whether to auto-instrument packages
        max_retry_attempts: Maximum number of retry attempts for OTLP exporter
        retry_delay_seconds: Delay between retry attempts in seconds
        max_export_batch_size: Maximum batch size for OTLP exporter
        export_timeout_seconds: Timeout for OTLP exporter in seconds
        schedule_delay_millis: Schedule delay in milliseconds for batch processor
    """
    global _tracer

    try:
        attributes = {"service.name": service_name}
        if resource_attributes:
            attributes.update(resource_attributes)
        # Defer sampling decision to a custom exporter that filters based on error status.
        sampler = ParentBased(root=ErrorSampler(fallback_sampler=TraceIdRatioBased(trace_sample_rate)))
        trace_provider = TracerProvider(resource=Resource.create(attributes), sampler=sampler)

        if otlp_endpoint:
            try:
                endpoint_url = otlp_endpoint.replace("https://", "").replace("http://", "")
                use_secure_connection = otlp_endpoint.startswith("https://") or ":4317" in endpoint_url

                base_exporter = None
                if use_secure_connection:
                    logger.info("Attempting to configure secure OTLP exporter.")
                    try:
                        with open('/certs/server.crt', 'rb') as f:
                            cert_bytes = f.read()
                        credentials = grpc.ssl_channel_credentials(root_certificates=cert_bytes)
                        base_exporter = OTLPSpanExporter(
                            endpoint=endpoint_url,
                            credentials=credentials,
                            insecure=False
                        )
                        logger.info(f"OTLP exporter configured with secure endpoint: {endpoint_url}")
                    except FileNotFoundError:
                        logger.error(
                            "Certificate file not found for secure OTLP connection. "
                            "Falling back to an insecure connection."
                        )
                        base_exporter = OTLPSpanExporter(endpoint=endpoint_url, insecure=True)
                    except Exception as e:
                        logger.error(f"Failed to create secure OTLP exporter due to: {e}. Falling back to insecure.")
                        base_exporter = OTLPSpanExporter(endpoint=endpoint_url, insecure=True)
                else:
                    logger.info(f"OTLP exporter configured with insecure endpoint: {endpoint_url}")
                    base_exporter = OTLPSpanExporter(endpoint=endpoint_url, insecure=True)

                otlp_exporter = ErrorFilteringExporter(base_exporter)

                span_processor = BatchSpanProcessor(
                    otlp_exporter,
                    max_queue_size=1000,
                    max_export_batch_size=max_export_batch_size,
                    schedule_delay_millis=schedule_delay_millis,
                    export_timeout_millis=int(export_timeout_seconds * 1000)
                )
                trace_provider.add_span_processor(span_processor)

            except Exception as e:
                logger.warning(f"Failed to initialize OTLP exporter: {e}. Tracing will be limited.")

        trace.set_tracer_provider(trace_provider)
        _tracer = trace.get_tracer(f"{service_name}-tracer")

        if auto_instrument_packages:
            instrumentation_packages = {
                "AioHttpClient": AioHttpClientInstrumentor,
                "HTTPXClient": HTTPXClientInstrumentor,
                "Redis": RedisInstrumentor,
            }
            for name, instrumentor_class in instrumentation_packages.items():
                try:
                    instrumentor_class().instrument()
                    logger.debug(f"{name} instrumentation enabled")
                except Exception as e:
                    logger.warning(f"Failed to instrument {name}: {e}")

        logger.info(f"OpenTelemetry initialized for {service_name}.")

    except Exception as e:
        logger.error(f"Failed to initialize tracing: {e}. Service will continue without tracing.")
        trace_provider = TracerProvider()
        trace.set_tracer_provider(trace_provider)
        _tracer = trace.get_tracer(f"{service_name}-tracer-fallback")


def instrument_fastapi(app):
    """
    Instrument FastAPI application with OpenTelemetry.
    
    Args:
        app: FastAPI application instance
    """
    try:
        FastAPIInstrumentor.instrument_app(app, tracer_provider=trace.get_tracer_provider())
        logger.info("FastAPI instrumentation enabled")
    except Exception as e:
        logger.warning(f"Failed to instrument FastAPI: {str(e)}. Application will continue without FastAPI instrumentation.")
    logger.info("FastAPI application instrumented with OpenTelemetry")


def get_tracer():
    """Get the global tracer instance."""
    global _tracer
    if _tracer is None:
        _tracer = trace.get_tracer("messaging-service-tracer")
    return _tracer


def extract_correlation_id_from_headers(headers: Optional[Dict[str, str]] = None) -> Optional[str]:
    """
    Extract correlation ID from headers dictionary in a case-insensitive manner.
    
    Args:
        headers: Dictionary of headers
        
    Returns:
        Correlation ID string or None if not found
    """
    if not headers:
        return None
        
    # Check for correlation ID in headers (case-insensitive)
    correlation_id_keys = ["X-Correlation-ID", "x-correlation-id", "X-CORRELATION-ID"]
    
    # Try exact matches first
    for key in correlation_id_keys:
        if key in headers:
            return headers[key]
    
    # Try case-insensitive match
    for header_name, header_value in headers.items():
        if header_name.lower() == "x-correlation-id":
            return header_value
    
    return None


def extract_correlation_id(request: Optional[Request] = None, headers: Optional[Dict[str, str]] = None) -> str:
    """
    Extract correlation ID from request or headers, or generate a new one.
    
    Args:
        request: FastAPI request object
        headers: Dictionary of headers
        
    Returns:
        Correlation ID string
    """
    # Check if correlation ID is in request state
    if request and hasattr(request, "state") and hasattr(request.state, "correlation_id"):
        return request.state.correlation_id
    
    # Check request headers using the helper function
    if request and hasattr(request, "headers"):
        correlation_id = extract_correlation_id_from_headers(request.headers)
        if correlation_id:
            return correlation_id
    
    # Check provided headers using the helper function
    if headers:
        correlation_id = extract_correlation_id_from_headers(headers)
        if correlation_id:
            return correlation_id
    
    # Generate new correlation ID if not found
    return str(uuid.uuid4())


def inject_trace_context(headers: Dict[str, str], correlation_id: Optional[str] = None) -> Dict[str, str]:
    """
    Inject trace context into headers for distributed tracing.
    
    Args:
        headers: Dictionary of headers to inject into
        correlation_id: Optional correlation ID to include
        
    Returns:
        Updated headers dictionary with trace context
    """
    # Create a copy of headers to avoid modifying the original
    headers_copy = headers.copy()
    
    # Inject trace context
    TraceContextTextMapPropagator().inject(headers_copy)
    
    # Add correlation ID if provided
    if correlation_id:
        headers_copy[CORRELATION_ID_HEADER] = correlation_id
    
    return headers_copy


def extract_trace_context(headers: Dict[str, str]) -> Dict[str, Any]:
    """
    Extract trace context from headers.
    
    Args:
        headers: Dictionary of headers
        
    Returns:
        Trace context dictionary
    """
    context = TraceContextTextMapPropagator().extract(headers)
    return context


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
                # Convert value to string if it's not a basic type
                if not isinstance(value, (str, int, float, bool)):
                    value = str(value)
                current_span.set_attribute(key, value)


def trace_method(name: str, kind: str = "INTERNAL") -> Callable[[F], F]:
    """
    Decorator to trace a method with OpenTelemetry.
    
    Args:
        name: Name of the span
        kind: Kind of span (SERVER, CLIENT, INTERNAL, PRODUCER, CONSUMER)
        
    Returns:
        Decorated function
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            # Get span kind
            span_kind = getattr(SpanKind, kind, SpanKind.INTERNAL)
            
            # Get correlation ID from kwargs if available
            correlation_id = kwargs.get("correlation_id")
            
            # Start span
            tracer = get_tracer()
            with tracer.start_as_current_span(name, kind=span_kind) as span:
                # Add correlation ID attribute if available
                if correlation_id:
                    span.set_attribute("correlation_id", correlation_id)
                
                # Add function name attribute
                span.set_attribute("function.name", func.__name__)
                
                try:
                    # Execute the function
                    result = await func(*args, **kwargs)
                    
                    # Set span status to OK
                    span.set_status(Status(StatusCode.OK))
                    
                    return result
                except Exception as e:
                    # Set span status to ERROR with description
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    
                    # Record exception
                    span.record_exception(e)
                    
                    # Re-raise the exception
                    raise
        
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            # Get span kind
            span_kind = getattr(SpanKind, kind, SpanKind.INTERNAL)
            
            # Get correlation ID from kwargs if available
            correlation_id = kwargs.get("correlation_id")
            
            # Start span
            tracer = get_tracer()
            with tracer.start_as_current_span(name, kind=span_kind) as span:
                # Add correlation ID attribute if available
                if correlation_id:
                    span.set_attribute("correlation_id", correlation_id)
                
                # Add function name attribute
                span.set_attribute("function.name", func.__name__)
                
                try:
                    # Execute the function
                    result = func(*args, **kwargs)
                    
                    # Set span status to OK
                    span.set_status(Status(StatusCode.OK))
                    
                    return result
                except Exception as e:
                    # Set span status to ERROR with description
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    
                    # Record exception
                    span.record_exception(e)
                    
                    # Re-raise the exception
                    raise
        
        # Return appropriate wrapper based on whether the function is async or not
        if asyncio.iscoroutinefunction(func):
            return cast(F, async_wrapper)
        else:
            return cast(F, sync_wrapper)
    
    return decorator


def trace_redis_operation(operation_name: str) -> Callable[[F], F]:
    """
    Decorator to trace Redis operations with OpenTelemetry.
    
    Args:
        operation_name: Name of the Redis operation
        
    Returns:
        Decorated function
    """
    return trace_method(f"redis.{operation_name}", kind="CLIENT")


def trace_message_processing(channel_name: str) -> Callable[[F], F]:
    """
    Decorator to trace message processing with OpenTelemetry.
    
    Args:
        channel_name: Name of the channel
        
    Returns:
        Decorated function
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            tracer = get_tracer()
            with tracer.start_as_current_span(
                f"process_message.{channel_name}", kind=SpanKind.CONSUMER
            ) as span:
                # Add channel attribute
                span.set_attribute("messaging.channel", channel_name)
                span.set_attribute("messaging.system", "redis_pubsub")
                
                # Extract message from args or kwargs
                message = None
                if len(args) > 0:
                    message = args[0]
                elif "message" in kwargs:
                    message = kwargs["message"]
                
                # Add message attributes if available
                if message:
                    if hasattr(message, "id"):
                        span.set_attribute("messaging.message_id", str(message.id))
                    
                    # Try to extract correlation ID from message
                    correlation_id = None
                    if hasattr(message, "headers") and isinstance(message.headers, dict):
                        correlation_id = message.headers.get(CORRELATION_ID_HEADER)
                    elif hasattr(message, "correlation_id"):
                        correlation_id = message.correlation_id
                    
                    if correlation_id:
                        span.set_attribute("correlation_id", correlation_id)
                
                try:
                    # Execute the function
                    result = await func(*args, **kwargs)
                    
                    # Set span status to OK
                    span.set_status(Status(StatusCode.OK))
                    
                    return result
                except Exception as e:
                    # Set span status to ERROR with description
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    
                    # Record exception
                    span.record_exception(e)
                    
                    # Re-raise the exception
                    raise
        
        # Return async wrapper
        return cast(F, async_wrapper)
    
    return decorator


@contextmanager
def traced_span(name: str, kind: str = "INTERNAL", attributes: Optional[Dict[str, Any]] = None):
    """
    Context manager for creating a traced span.
    
    Args:
        name: Name of the span
        kind: Kind of span (SERVER, CLIENT, INTERNAL, PRODUCER, CONSUMER)
        attributes: Optional attributes to add to the span
    """
    # Get span kind
    span_kind = getattr(SpanKind, kind, SpanKind.INTERNAL)
    
    # Start span
    tracer = get_tracer()
    with tracer.start_as_current_span(name, kind=span_kind) as span:
        # Add attributes if provided
        if attributes:
            for key, value in attributes.items():
                if value is not None:
                    # Convert value to string if it's not a basic type
                    if not isinstance(value, (str, int, float, bool)):
                        value = str(value)
                    span.set_attribute(key, value)
        
        try:
            # Yield control back to the caller
            yield span
            
            # Set span status to OK if no exception was raised
            span.set_status(Status(StatusCode.OK))
        except Exception as e:
            # Set span status to ERROR with description
            span.set_status(Status(StatusCode.ERROR, str(e)))
            
            # Record exception
            span.record_exception(e)
            
            # Re-raise the exception
            raise


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
