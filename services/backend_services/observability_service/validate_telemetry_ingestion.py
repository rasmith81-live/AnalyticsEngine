import asyncio
import sys
import os
from datetime import datetime
from unittest.mock import MagicMock, AsyncMock

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

# Mock dependencies
sys.modules["app.dependencies"] = MagicMock()
mock_messaging_client = AsyncMock()
mock_messaging_client.publish_event.return_value = "msg-123"
sys.modules["app.dependencies"].get_messaging_client = lambda: mock_messaging_client
sys.modules["app.dependencies"].MessagingClient = MagicMock()

# Mock telemetry
sys.modules["app.telemetry"] = MagicMock()
sys.modules["app.telemetry"].trace_method = lambda name=None, kind=None: lambda func: func
sys.modules["app.telemetry"].add_span_attributes = MagicMock()
sys.modules["app.telemetry"].get_correlation_id = lambda: "test-correlation-id"

# Mock metrics
sys.modules["app.metrics"] = MagicMock()
sys.modules["app.metrics"].track_telemetry_ingestion = MagicMock()
sys.modules["app.metrics"].track_telemetry_processing = MagicMock()
sys.modules["app.metrics"].track_event_processing = MagicMock()

# Import endpoint handlers
from app.api.events import ingest_event
from app.api.traces import ingest_trace
from app.api.logs import ingest_log
from app.models import EventData, TraceData, LogData, EventSeverity, LogSeverity

async def validate_telemetry_ingestion():
    print("Starting Telemetry Ingestion Validation...")

    # 1. Validate Event Ingestion
    print("\n1. Validating Event Ingestion...")
    event_data = EventData(
        event_type="user.login",
        source_service="auth-service",
        event_data={"user_id": "u123", "method": "password"},
        severity=EventSeverity.INFO,
        timestamp=datetime.utcnow()
    )
    
    response = await ingest_event(event=event_data, messaging_client=mock_messaging_client)
    print(f"   Response: {response}")
    
    mock_messaging_client.publish_event.assert_awaited()
    call_args = mock_messaging_client.publish_event.call_args.kwargs
    if call_args['event_type'] == "telemetry.event.ingested" and \
       call_args['channel'] == "database" and \
       call_args['event_data']['event']['event_type'] == "user.login":
        print("   ✅ Event published to messaging service correctly")
    else:
        print(f"   ❌ Event publication mismatch: {call_args}")

    mock_messaging_client.publish_event.reset_mock()

    # 2. Validate Trace Ingestion
    print("\n2. Validating Trace Ingestion...")
    trace_data = TraceData(
        service="order-service",
        trace_id="trace-123",
        span_id="span-456",
        name="create_order",
        kind="SERVER",
        timestamp=datetime.utcnow(),
        duration_ms=150.5,
        status_code="OK"
    )
    
    response = await ingest_trace(trace=trace_data, messaging_client=mock_messaging_client)
    print(f"   Response: {response}")
    
    mock_messaging_client.publish_event.assert_awaited()
    call_args = mock_messaging_client.publish_event.call_args.kwargs
    if call_args['event_type'] == "telemetry.trace.ingested" and \
       call_args['channel'] == "database" and \
       call_args['event_data']['trace']['trace_id'] == "trace-123":
        print("   ✅ Trace published to messaging service correctly")
    else:
        print(f"   ❌ Trace publication mismatch: {call_args}")

    mock_messaging_client.publish_event.reset_mock()

    # 3. Validate Log Ingestion
    print("\n3. Validating Log Ingestion...")
    log_data = LogData(
        service="payment-service",
        message="Payment processed",
        severity=LogSeverity.INFO,
        timestamp=datetime.utcnow(),
        attributes={"amount": 100}
    )
    
    response = await ingest_log(log=log_data, messaging_client=mock_messaging_client)
    print(f"   Response: {response}")
    
    mock_messaging_client.publish_event.assert_awaited()
    call_args = mock_messaging_client.publish_event.call_args.kwargs
    if call_args['event_type'] == "telemetry.log.ingested" and \
       call_args['channel'] == "database" and \
       call_args['event_data']['log']['message'] == "Payment processed":
        print("   ✅ Log published to messaging service correctly")
    else:
        print(f"   ❌ Log publication mismatch: {call_args}")

    print("\nValidation Complete!")

if __name__ == "__main__":
    asyncio.run(validate_telemetry_ingestion())
