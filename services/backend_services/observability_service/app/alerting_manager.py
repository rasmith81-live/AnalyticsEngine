import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from pydantic import BaseModel
from .code_traceability import trace_execution

logger = logging.getLogger(__name__)

class AlertRule(BaseModel):
    id: str
    name: str
    metric_name: str
    condition: str  # e.g., ">", "<", "=="
    threshold: float
    channels: List[str]  # e.g., ["slack", "email"]
    enabled: bool = True

class AlertingManager:
    """
    Manages alert rules and notifications for the Observability Service.
    """
    
    def __init__(self, notification_endpoints: Dict[str, str] = None):
        self.rules: Dict[str, AlertRule] = {}
        self.notification_endpoints = notification_endpoints or {}
        
        # Business metric alert rules
        self.add_rule(AlertRule(
            id="retention_drop",
            name="Retention Rate Drop",
            metric_name="retention_rate",
            condition="<",
            threshold=0.85,
            channels=["slack"]
        ))
        
        # System-level alert rules for Systems Monitor
        self.add_rule(AlertRule(
            id="high_cpu_usage",
            name="High CPU Usage",
            metric_name="system_cpu_usage",
            condition=">",
            threshold=80.0,
            channels=["slack"],
            enabled=True
        ))
        
        self.add_rule(AlertRule(
            id="high_memory_usage",
            name="High Memory Usage",
            metric_name="system_memory_usage",
            condition=">",
            threshold=85.0,
            channels=["slack"],
            enabled=True
        ))
        
        self.add_rule(AlertRule(
            id="high_disk_usage",
            name="High Disk Usage",
            metric_name="system_disk_usage",
            condition=">",
            threshold=90.0,
            channels=["slack"],
            enabled=True
        ))
        
        self.add_rule(AlertRule(
            id="service_unhealthy",
            name="Service Unhealthy",
            metric_name="service_health",
            condition="<",
            threshold=1.0,
            channels=["slack"],
            enabled=True
        ))
        
        self.add_rule(AlertRule(
            id="service_not_ready",
            name="Service Not Ready",
            metric_name="service_ready",
            condition="<",
            threshold=1.0,
            channels=["slack"],
            enabled=True
        ))

    def add_rule(self, rule: AlertRule):
        self.rules[rule.id] = rule

    @trace_execution
    async def evaluate_metrics(self, metrics_data: Dict[str, float]):
        """
        Evaluates incoming metrics against active alert rules.
        """
        for rule_id, rule in self.rules.items():
            if not rule.enabled:
                continue
            
            if rule.metric_name in metrics_data:
                value = metrics_data[rule.metric_name]
                if self._check_condition(value, rule.condition, rule.threshold):
                    await self._trigger_alert(rule, value)

    def _check_condition(self, value: float, condition: str, threshold: float) -> bool:
        if condition == ">": return value > threshold
        if condition == "<": return value < threshold
        if condition == "==": return value == threshold
        if condition == ">=": return value >= threshold
        if condition == "<=": return value <= threshold
        return False

    async def _trigger_alert(self, rule: AlertRule, current_value: float):
        message = f"ALERT: {rule.name} triggered! Current value: {current_value} (Threshold: {rule.threshold})"
        logger.warning(message)
        
        for channel in rule.channels:
            await self._send_notification(channel, message)

    async def _send_notification(self, channel: str, message: str):
        endpoint = self.notification_endpoints.get(channel)
        if not endpoint:
            logger.info(f"Mock Notification to {channel}: {message}")
            return

        # In real impl, use aiohttp to post to Slack/Email webhook
        logger.info(f"Sending {channel} notification to {endpoint}: {message}")
