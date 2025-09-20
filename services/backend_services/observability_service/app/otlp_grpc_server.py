"""
OTLP gRPC Server for Observability Service

This module implements a gRPC server to receive OTLP traces and metrics.
"""

import asyncio
import logging
from concurrent import futures

import grpc
from opentelemetry.proto.collector.trace.v1 import trace_service_pb2_grpc, trace_service_pb2
from opentelemetry.proto.collector.metrics.v1 import metrics_service_pb2_grpc, metrics_service_pb2
from typing import Callable, Awaitable, Dict, Any

logger = logging.getLogger(__name__)

class TraceService(trace_service_pb2_grpc.TraceServiceServicer):
    def __init__(self, trace_handler: Callable[[Dict[str, Any]], Awaitable[None]]):
        self.trace_handler = trace_handler

    async def Export(self, request, context):
        logger.info(f"Received {len(request.resource_spans)} trace resource spans.")
        for resource_span in request.resource_spans:
            for scope_span in resource_span.scope_spans:
                for span in scope_span.spans:
                    trace_data = {
                        "trace_id": span.trace_id.hex(),
                        "span_id": span.span_id.hex(),
                        "parent_span_id": span.parent_span_id.hex() if span.parent_span_id else None,
                        "name": span.name,
                        # This is a simplification; real mapping is more complex
                    }
                    await self.trace_handler(trace_data)
        return trace_service_pb2.ExportTraceServiceResponse()

class MetricsService(metrics_service_pb2_grpc.MetricsServiceServicer):
    async def Export(self, request, context):
        logger.info(f"Received {len(request.resource_metrics)} metric resource metrics.")
        # Processing logic for metrics would go here
        return metrics_service_pb2.ExportMetricsServiceResponse()

async def serve_otlp_grpc(trace_handler: Callable[[Dict[str, Any]], Awaitable[None]]):
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    trace_service_pb2_grpc.add_TraceServiceServicer_to_server(TraceService(trace_handler), server)
    metrics_service_pb2_grpc.add_MetricsServiceServicer_to_server(MetricsService(), server)
    
    try:
        with open('/certs/server.key', 'rb') as f:
            private_key = f.read()
        with open('/certs/server.crt', 'rb') as f:
            certificate_chain = f.read()
        
        server_credentials = grpc.ssl_server_credentials(
            private_key_certificate_chain_pairs=[(private_key, certificate_chain)]
        )
        
        server.add_secure_port('[::]:4317', server_credentials)
        logger.info("Starting OTLP gRPC server with TLS on port 4317")
        await server.start()
        return server
        
    except FileNotFoundError:
        logger.error("TLS certificate or key not found. OTLP gRPC server cannot start.")
        raise

async def shutdown_otlp_grpc(server: grpc.aio.Server):
    logger.info("Shutting down OTLP gRPC server")
    await server.stop(0)
