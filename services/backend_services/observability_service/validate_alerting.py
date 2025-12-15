import asyncio
import sys
import os
from unittest.mock import MagicMock, AsyncMock

# Add the service directory to sys.path
service_dir = os.path.dirname(os.path.abspath(__file__))
if service_dir not in sys.path:
    sys.path.insert(0, service_dir)

from app.alerting_manager import AlertingManager, AlertRule

async def validate_alerting():
    print("Starting Alerting & Notification System Validation...")
    
    # 1. Initialize AlertingManager
    print("\n1. Initializing AlertingManager...")
    notification_endpoints = {"slack": "http://mock-slack-webhook"}
    manager = AlertingManager(notification_endpoints=notification_endpoints)
    
    # Mock _send_notification to verify calls
    manager._send_notification = AsyncMock()
    
    # 2. Define Alert Rules
    print("\n2. Defining Alert Rules...")
    # Rule 1: High CPU Usage
    cpu_rule = AlertRule(
        id="high_cpu",
        name="High CPU Usage",
        metric_name="cpu_usage_percent",
        condition=">",
        threshold=90.0,
        channels=["slack"]
    )
    manager.add_rule(cpu_rule)
    print(f"   Added rule: {cpu_rule.name} when {cpu_rule.metric_name} {cpu_rule.condition} {cpu_rule.threshold}")

    # Rule 2: Low Memory
    memory_rule = AlertRule(
        id="low_memory",
        name="Low Memory Available",
        metric_name="memory_free_mb",
        condition="<",
        threshold=500.0,
        channels=["slack"]
    )
    manager.add_rule(memory_rule)
    print(f"   Added rule: {memory_rule.name} when {memory_rule.metric_name} {memory_rule.condition} {memory_rule.threshold}")

    # 3. Evaluate Metrics (No Alert)
    print("\n3. Evaluating Metrics (Normal Conditions)...")
    metrics_normal = {
        "cpu_usage_percent": 45.5,
        "memory_free_mb": 2048.0
    }
    await manager.evaluate_metrics(metrics_normal)
    
    if manager._send_notification.call_count == 0:
        print("   ✅ No alerts triggered for normal metrics")
    else:
        print(f"   ❌ Alerts triggered incorrectly: {manager._send_notification.call_count}")

    # 4. Evaluate Metrics (Trigger Alert)
    print("\n4. Evaluating Metrics (Alert Conditions)...")
    metrics_alert = {
        "cpu_usage_percent": 95.5,  # Should trigger High CPU
        "memory_free_mb": 2048.0
    }
    await manager.evaluate_metrics(metrics_alert)
    
    if manager._send_notification.call_count == 1:
        print("   ✅ Alert triggered for High CPU")
        call_args = manager._send_notification.call_args
        print(f"      Notification sent to channel '{call_args[0][0]}' with message: '{call_args[0][1]}'")
    else:
        print(f"   ❌ Expected 1 alert, got {manager._send_notification.call_count}")

    # Reset mock
    manager._send_notification.reset_mock()

    # 5. Evaluate Metrics (Multiple Alerts)
    print("\n5. Evaluating Metrics (Multiple Alerts)...")
    metrics_multi_alert = {
        "cpu_usage_percent": 99.9,
        "memory_free_mb": 100.0   # Should trigger Low Memory
    }
    await manager.evaluate_metrics(metrics_multi_alert)
    
    if manager._send_notification.call_count == 2:
        print("   ✅ Alerts triggered for both High CPU and Low Memory")
    else:
        print(f"   ❌ Expected 2 alerts, got {manager._send_notification.call_count}")

    print("\nValidation Complete!")

if __name__ == "__main__":
    asyncio.run(validate_alerting())
