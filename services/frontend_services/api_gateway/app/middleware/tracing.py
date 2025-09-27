"""
Tracing middleware for the API Gateway service.
Implements distributed tracing using OpenTelemetry.
"""
from typing import Callable

from fastapi import FastAPI, Request, Response
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.sampling import Decision, ParentBased, Sampler, SamplingResult, TraceIdRatioBased
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter, SpanExportResult
from opentelemetry.trace import Status, StatusCode
import grpc
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

def setup_tracing(app: FastAPI, export_interval_ms: int = 15000, trace_sample_rate: float = 0.1) -> None:
    """
    Set up OpenTelemetry tracing for the application.
    
    Args:
        app: FastAPI application
    """
    # Create a resource with service information
    resource = Resource.create({
        "service.name": settings.SERVICE_NAME,
        "service.namespace": "supply_chain_analytics",
        "service.version": "1.0.0",
    })
    
    # Defer sampling decision to a custom exporter that filters based on error status.
    sampler = ParentBased(root=ErrorSampler(fallback_sampler=TraceIdRatioBased(trace_sample_rate)))

    # Create a tracer provider
    tracer_provider = TracerProvider(resource=resource, sampler=sampler)
    
    # Set up the OTLP exporter if an endpoint is configured
    if settings.OTLP_ENDPOINT:
        base_exporter = None
        try:
            # Attempt to create secure credentials from the certificate file
            with open('/certs/server.crt', 'rb') as f:
                cert_bytes = f.read()
            credentials = grpc.ssl_channel_credentials(root_certificates=cert_bytes)
            base_exporter = OTLPSpanExporter(
                endpoint=settings.OTLP_ENDPOINT,
                credentials=credentials
            )
            logger.info(f"OTLP exporter configured with secure endpoint: {settings.OTLP_ENDPOINT}")
        except (FileNotFoundError, ImportError):
            logger.warning("TLS certificate not found or grpc not installed. Falling back to insecure OTLP exporter.")
            base_exporter = OTLPSpanExporter(endpoint=settings.OTLP_ENDPOINT, insecure=True)

        otlp_exporter = ErrorFilteringExporter(base_exporter)
        span_processor = BatchSpanProcessor(
            otlp_exporter, schedule_delay_millis=export_interval_ms
        )
        tracer_provider.add_span_processor(span_processor)
    else:
        logger.warning("No OTLP endpoint provided. Traces will not be exported.")
    
    # Set the tracer provider
    trace.set_tracer_provider(tracer_provider)
    
    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)
    
    logger.info("OpenTelemetry tracing initialized")

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


class TracingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that adds tracing information to requests.
    Propagates trace context to downstream services.
    """
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request with tracing.
        
        Args:
            request: FastAPI request
            call_next: Next middleware or endpoint handler
            
        Returns:
            Response from downstream
        """
        # Get current span
        current_span = trace.get_current_span()
        
        # Extract correlation ID from headers or generate a new one
        correlation_id = request.headers.get("X-Correlation-ID")
        if correlation_id:
            # Set correlation ID as a span attribute
            current_span.set_attribute("correlation_id", correlation_id)
        
        # Extract service from path
        try:
            _, service, *_ = request.url.path.strip("/").split("/")
            current_span.set_attribute("target_service", service)
        except ValueError:
            pass
        
        # Add request attributes to span
        current_span.set_attribute("http.method", request.method)
        current_span.set_attribute("http.url", str(request.url))
        current_span.set_attribute("http.client_ip", request.client.host)
        
        # Process the request
        response = await call_next(request)
        
        # Add response attributes to span
        current_span.set_attribute("http.status_code", response.status_code)
        
        return response
