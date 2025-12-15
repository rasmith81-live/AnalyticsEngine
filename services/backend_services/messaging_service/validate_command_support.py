import asyncio
import sys
import os
import uuid
from unittest.mock import MagicMock, AsyncMock

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

# Mock telemetry before importing app
sys.modules["app.telemetry"] = MagicMock()
sys.modules["app.telemetry"].trace_method = lambda name=None, kind=None: lambda func: func
sys.modules["app.telemetry"].traced_span = MagicMock()
sys.modules["app.telemetry"].traced_span.return_value.__enter__ = MagicMock()
sys.modules["app.telemetry"].traced_span.return_value.__exit__ = MagicMock()
sys.modules["app.telemetry"].extract_correlation_id_from_headers = lambda headers: headers.get("X-Correlation-ID")
sys.modules["app.telemetry"].instrument_fastapi = MagicMock()

# Mock metrics
sys.modules["app.metrics"] = MagicMock()
sys.modules["app.metrics"].track_redis_operation = lambda operation_name=None, operation=None: lambda func: func

from app.event_publisher import EventPublisher
from app.models import PublishCommandRequest, CommandReceipt

# Mock config
sys.modules["app.config"] = MagicMock()
sys.modules["app.config"].get_settings = MagicMock()
sys.modules["app.config"].get_settings.return_value.service_name = "test-service"
sys.modules["app.config"].get_settings.return_value.propagate_correlation_id = True
sys.modules["app.config"].get_settings.return_value.enable_distributed_tracing = False
sys.modules["app.config"].get_settings.return_value.enable_prometheus_metrics = False

# Import main after mocking dependencies
from app.main import publish_command

async def validate_command_support():
    print("Starting Command Support Validation...")
    
    # 1. Initialize Publisher Mock
    print("\n1. Initializing EventPublisher Mock...")
    publisher = MagicMock(spec=EventPublisher)
    publisher.publish_message = AsyncMock(return_value=str(uuid.uuid4()))
    
    # 2. Test publish_command
    print("\n2. Testing publish_command endpoint logic...")
    command_type = "CreateOrder"
    payload = {"order_id": "12345", "amount": 99.99}
    service_name = "order-service"
    correlation_id = str(uuid.uuid4())
    
    request = PublishCommandRequest(
        command_type=command_type,
        payload=payload,
        service_name=service_name,
        correlation_id=correlation_id,
        metadata={"source": "validation_script"}
    )
    
    # Mock Request object for dependency
    mock_request_obj = MagicMock()
    mock_request_obj.state.correlation_id = correlation_id
    
    try:
        receipt = await publish_command(
            request=request,
            publisher=publisher,
            request_obj=mock_request_obj
        )
        
        print(f"   Command Published: ID={receipt.command_id}, Success={receipt.success}")
        
        # Verify call to publisher
        publisher.publish_message.assert_awaited_once()
        call_kwargs = publisher.publish_message.call_args.kwargs
        
        expected_channel = f"commands.{command_type}"
        actual_channel = call_kwargs.get('channel')
        
        print(f"   Verified Channel: {actual_channel}")
        
        if actual_channel == expected_channel:
            print("   ✅ Channel name formatted correctly")
        else:
            print(f"   ❌ Channel name mismatch. Expected {expected_channel}, got {actual_channel}")
            
        if call_kwargs.get('correlation_id') == correlation_id:
             print("   ✅ Correlation ID propagated")
        else:
             print("   ❌ Correlation ID mismatch")
             
        if call_kwargs.get('payload') == payload:
            print("   ✅ Payload passed correctly")
        else:
            print("   ❌ Payload mismatch")

    except Exception as e:
        print(f"   ❌ Exception during command publish: {e}")
        import traceback
        traceback.print_exc()

    print("\nValidation Complete!")

if __name__ == "__main__":
    asyncio.run(validate_command_support())
