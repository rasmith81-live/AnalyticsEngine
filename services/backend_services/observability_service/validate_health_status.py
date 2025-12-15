import asyncio
import sys
import os
import time
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

# Import metrics to access the counters directly for verification
from app.metrics import TELEMETRY_INGESTION_COUNTER, HEALTH_CHECK_COUNT

# Import endpoint handlers
from app.api.health import ingest_health_data
from app.models import HealthData

async def validate_health_status():
    print("Starting Health & Status Tracking Validation...")
    
    # 1. Ingest Health Data
    print("\n1. Ingesting Health Data...")
    health_data = HealthData(
        service="test-service",
        status="healthy",
        timestamp=datetime.utcnow(),
        details={"db": "up", "cache": "up"},
        latency_ms=10.5
    )
    
    # Get initial counter values
    initial_ingestion_count = TELEMETRY_INGESTION_COUNTER.labels(type="health")._value.get()
    initial_health_count = HEALTH_CHECK_COUNT.labels(service="test-service", status="healthy")._value.get()
    
    print(f"   Initial Ingestion Count: {initial_ingestion_count}")
    print(f"   Initial Health Count: {initial_health_count}")
    
    # Call endpoint
    response = await ingest_health_data(health_data=health_data, messaging_client=mock_messaging_client)
    print(f"   Response: {response}")
    
    # 2. Verify Messaging
    print("\n2. Verifying Event Publication...")
    mock_messaging_client.publish_event.assert_awaited()
    call_args = mock_messaging_client.publish_event.call_args.kwargs
    if call_args['event_type'] == "telemetry.health.ingested" and \
       call_args['event_data']['health']['service'] == "test-service":
        print("   ✅ Health event published correctly")
    else:
        print(f"   ❌ Health event mismatch: {call_args}")

    # 3. Verify Prometheus Metrics Update
    print("\n3. Verifying Prometheus Metrics Update...")
    
    # Get new counter values
    final_ingestion_count = TELEMETRY_INGESTION_COUNTER.labels(type="health")._value.get()
    final_health_count = HEALTH_CHECK_COUNT.labels(service="test-service", status="healthy")._value.get()
    
    print(f"   Final Ingestion Count: {final_ingestion_count}")
    print(f"   Final Health Count: {final_health_count}")
    
    if final_ingestion_count == initial_ingestion_count + 1:
        print("   ✅ Telemetry Ingestion Counter incremented")
    else:
        print("   ❌ Telemetry Ingestion Counter did not increment correctly")
        
    if final_health_count == initial_health_count + 1:
        print("   ✅ Health Check Counter incremented")
    else:
        print("   ❌ Health Check Counter did not increment correctly")

    print("\nValidation Complete!")

if __name__ == "__main__":
    asyncio.run(validate_health_status())
