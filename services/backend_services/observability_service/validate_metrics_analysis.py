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
# We need to make sure we use the same registry/counters as the app
from app.metrics import TELEMETRY_INGESTION_COUNTER, METRIC_COUNT

# Import endpoint handlers
from app.api.metrics import ingest_metric
from app.models import MetricData

async def validate_metrics_analysis():
    print("Starting Metrics & Analysis Validation...")
    
    # 1. Ingest a metric
    print("\n1. Ingesting Metric...")
    metric_data = MetricData(
        name="test_metric_counter",
        value=1.0,
        timestamp=datetime.utcnow(),
        service_name="test-service",
        aggregation="counter",
        labels={"env": "test"}
    )
    
    # Get initial counter values
    initial_ingestion_count = TELEMETRY_INGESTION_COUNTER.labels(type="metric")._value.get()
    initial_processing_count = METRIC_COUNT.labels(service="test-service", type="counter")._value.get()
    
    print(f"   Initial Ingestion Count: {initial_ingestion_count}")
    print(f"   Initial Processing Count: {initial_processing_count}")
    
    # Call endpoint
    response = await ingest_metric(metric=metric_data, messaging_client=mock_messaging_client)
    print(f"   Response: {response}")
    
    # 2. Verify Messaging
    print("\n2. Verifying Event Publication...")
    mock_messaging_client.publish_event.assert_awaited()
    call_args = mock_messaging_client.publish_event.call_args.kwargs
    if call_args['event_type'] == "telemetry.metric.ingested" and \
       call_args['event_data']['metric']['name'] == "test_metric_counter":
        print("   ✅ Metric event published correctly")
    else:
        print(f"   ❌ Metric event mismatch: {call_args}")

    # 3. Verify Prometheus Metrics Update
    print("\n3. Verifying Prometheus Metrics Update...")
    
    # Get new counter values
    final_ingestion_count = TELEMETRY_INGESTION_COUNTER.labels(type="metric")._value.get()
    final_processing_count = METRIC_COUNT.labels(service="test-service", type="counter")._value.get()
    
    print(f"   Final Ingestion Count: {final_ingestion_count}")
    print(f"   Final Processing Count: {final_processing_count}")
    
    if final_ingestion_count == initial_ingestion_count + 1:
        print("   ✅ Telemetry Ingestion Counter incremented")
    else:
        print("   ❌ Telemetry Ingestion Counter did not increment correctly")
        
    if final_processing_count == initial_processing_count + 1:
        print("   ✅ Metric Processing Counter incremented")
    else:
        print("   ❌ Metric Processing Counter did not increment correctly")

    print("\nValidation Complete!")

if __name__ == "__main__":
    asyncio.run(validate_metrics_analysis())
