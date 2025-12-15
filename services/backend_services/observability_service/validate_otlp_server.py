import asyncio
import sys
import os
import logging
from unittest.mock import MagicMock, AsyncMock

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

# Mock grpc and protobufs since we might not have them installed or want to run a full server
sys.modules["grpc"] = MagicMock()
sys.modules["grpc.aio"] = MagicMock()

# Create mock classes for protobuf objects
class MockSpan:
    def __init__(self, trace_id, span_id, parent_span_id, name):
        self.trace_id = trace_id
        self.span_id = span_id
        self.parent_span_id = parent_span_id
        self.name = name

class MockScopeSpans:
    def __init__(self, spans):
        self.spans = spans

class MockResourceSpans:
    def __init__(self, scope_spans):
        self.scope_spans = scope_spans

class MockExportTraceServiceRequest:
    def __init__(self, resource_spans):
        self.resource_spans = resource_spans

class MockExportMetricsServiceRequest:
    def __init__(self, resource_metrics):
        self.resource_metrics = resource_metrics

# Mock the protobuf modules
trace_service_pb2_grpc = MagicMock()
trace_service_pb2_grpc.TraceServiceServicer = object
sys.modules["opentelemetry.proto.collector.trace.v1"] = MagicMock()
sys.modules["opentelemetry.proto.collector.trace.v1"].trace_service_pb2_grpc = trace_service_pb2_grpc
sys.modules["opentelemetry.proto.collector.trace.v1"].trace_service_pb2 = MagicMock()

metrics_service_pb2_grpc = MagicMock()
metrics_service_pb2_grpc.MetricsServiceServicer = object
sys.modules["opentelemetry.proto.collector.metrics.v1"] = MagicMock()
sys.modules["opentelemetry.proto.collector.metrics.v1"].metrics_service_pb2_grpc = metrics_service_pb2_grpc
sys.modules["opentelemetry.proto.collector.metrics.v1"].metrics_service_pb2 = MagicMock()

# Import the server implementation
from app.otlp_grpc_server import TraceService, MetricsService

async def validate_otlp_server():
    print("Starting OTLP Server Validation...")
    
    # 1. Validate TraceService Logic
    print("\n1. Validating TraceService Export Logic...")
    
    # Mock handler
    mock_handler = AsyncMock()
    trace_service = TraceService(trace_handler=mock_handler)
    
    # Create mock request data
    # Use bytes for IDs as protobufs usually use bytes
    trace_id = b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10'
    span_id = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    parent_id = b'\x08\x07\x06\x05\x04\x03\x02\x01'
    
    span = MockSpan(trace_id, span_id, parent_id, "test-span")
    scope_spans = MockScopeSpans([span])
    resource_spans = MockResourceSpans([scope_spans])
    request = MockExportTraceServiceRequest([resource_spans])
    context = MagicMock()
    
    # Call Export
    await trace_service.Export(request, context)
    
    # Verify handler call
    mock_handler.assert_awaited()
    call_args = mock_handler.call_args[0][0]
    
    print(f"   Handler called with: {call_args}")
    
    if call_args["trace_id"] == trace_id.hex():
        print("   ✅ Trace ID mapped correctly")
    else:
        print(f"   ❌ Trace ID mismatch: {call_args['trace_id']}")
        
    if call_args["span_id"] == span_id.hex():
        print("   ✅ Span ID mapped correctly")
    else:
        print(f"   ❌ Span ID mismatch: {call_args['span_id']}")
        
    if call_args["name"] == "test-span":
        print("   ✅ Span name mapped correctly")
    else:
        print(f"   ❌ Span name mismatch: {call_args['name']}")

    # 2. Validate MetricsService Logic
    print("\n2. Validating MetricsService Export Logic...")
    metrics_service = MetricsService()
    
    # Create mock metrics request
    metrics_request = MockExportMetricsServiceRequest([]) # Empty list for now as implementation is stub
    
    # Call Export
    response = await metrics_service.Export(metrics_request, context)
    print("   ✅ MetricsService.Export executed without error")

    print("\nValidation Complete!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(validate_otlp_server())
