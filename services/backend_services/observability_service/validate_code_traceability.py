import asyncio
import sys
import os
import time
from unittest.mock import MagicMock, AsyncMock

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.alerting_manager import AlertingManager
from app.code_traceability import tracer
from app.api.analysis import get_unused_files

async def validate_code_traceability():
    print("Starting Code Traceability Validation...")
    
    # 1. Verify AlertingManager is instrumented
    print("\n1. Verifying Instrumentation...")
    
    # Initialize AlertingManager (which is instrumented)
    manager = AlertingManager()
    
    # Use the method that is decorated
    metrics_data = {"cpu_usage": 50.0}
    await manager.evaluate_metrics(metrics_data)
    
    # Check if usage was recorded
    alerting_manager_path = os.path.abspath(os.path.join(service_dir, "app", "alerting_manager.py"))
    
    if alerting_manager_path in tracer.file_usage:
        print(f"   ✅ File usage recorded: {alerting_manager_path}")
        print(f"      Timestamp: {tracer.file_usage[alerting_manager_path]}")
    else:
        print(f"   ❌ File usage NOT recorded: {alerting_manager_path}")
        print(f"      Recorded files: {list(tracer.file_usage.keys())}")

    method_key = "AlertingManager.evaluate_metrics"
    # Note: Our tracer implementation stores full_name as "AlertingManager.evaluate_metrics" 
    # but let's check what's actually in method_usage[file_path]
    
    methods_used = tracer.method_usage.get(alerting_manager_path, set())
    if method_key in methods_used:
        print(f"   ✅ Method usage recorded: {method_key}")
    else:
        print(f"   ❌ Method usage NOT recorded: {method_key}")
        print(f"      Recorded methods: {methods_used}")

    # 2. Verify Unused Files Analysis
    print("\n2. Verifying Unused Files Analysis...")
    
    # We just used alerting_manager.py, so it should be "used".
    # app/models.py was imported but maybe not "executed" via a traced function? 
    # Actually, we didn't instrument models.py methods, only imported the file.
    # The tracer only tracks function calls via decorator.
    
    # Let's verify that alerting_manager.py is NOT in the unused list for a short period
    response = await get_unused_files(period_seconds=60, root_dir=os.path.join(service_dir, "app"))
    
    print(f"   Total scanned files: {response.total_files}")
    print(f"   Unused files count: {response.unused_files_count}")
    
    # AlertingManager should NOT be in unused files because we just used it
    if alerting_manager_path not in response.unused_files:
        print(f"   ✅ alerting_manager.py correctly identified as USED")
    else:
        print(f"   ❌ alerting_manager.py incorrectly identified as UNUSED")

    # Let's verify that some other file IS in unused list (e.g., something we didn't touch)
    # Since we only instrumented alerting_manager.py, most other files should be unused 
    # UNLESS they were used by imports? No, tracer only tracks decorated methods.
    
    # e.g., app/api/events.py
    events_path = os.path.abspath(os.path.join(service_dir, "app", "api", "events.py"))
    if events_path in response.unused_files:
        print(f"   ✅ app/api/events.py correctly identified as UNUSED (not instrumented/called)")
    else:
        # It might not be in the list if scanning logic failed or file not found
        if os.path.exists(events_path):
             print(f"   ❌ app/api/events.py MISSING from unused list (should be unused)")
        else:
             print(f"   ⚠️ app/api/events.py does not exist, skipping check")

    print("\nValidation Complete!")

if __name__ == "__main__":
    asyncio.run(validate_code_traceability())
