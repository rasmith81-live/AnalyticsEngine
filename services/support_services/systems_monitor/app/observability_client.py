"""
Observability Client for Systems Monitor.

This client sends structured metric data to the Observability Service
for centralized monitoring, alerting, and analysis.
"""

import aiohttp
import logging
from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class MetricData(BaseModel):
    """Model matching Observability Service's MetricData."""
    name: str
    value: float
    service_name: str
    aggregation: str = "gauge"
    labels: Dict[str, str] = {}
    timestamp: Optional[datetime] = None


class ObservabilityClient:
    """Client for sending metrics to Observability Service."""
    
    def __init__(self, base_url: str, service_name: str = "systems_monitor"):
        """
        Initialize Observability Client.
        
        Args:
            base_url: Base URL of Observability Service
            service_name: Name of this service
        """
        self.base_url = base_url.rstrip('/')
        self.service_name = service_name
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create aiohttp session."""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session
    
    async def send_metric(self, metric: MetricData) -> bool:
        """
        Send a single metric to Observability Service.
        
        Args:
            metric: Metric data to send
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            session = await self._get_session()
            
            async with session.post(
                f"{self.base_url}/api/v1/metrics/ingest",
                json=metric.model_dump(mode='json'),
                headers={"Content-Type": "application/json"},
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status in (200, 201, 202):
                    logger.debug(f"Successfully sent metric: {metric.name}")
                    return True
                else:
                    response_text = await response.text()
                    logger.warning(
                        f"Failed to send metric {metric.name}: "
                        f"{response.status} - {response_text}"
                    )
                    return False
                    
        except Exception as e:
            logger.error(f"Error sending metric {metric.name}: {str(e)}")
            return False
    
    async def send_metrics_batch(self, metrics: List[MetricData]) -> int:
        """
        Send multiple metrics to Observability Service.
        
        Args:
            metrics: List of metrics to send
            
        Returns:
            int: Number of successfully sent metrics
        """
        success_count = 0
        
        for metric in metrics:
            if await self.send_metric(metric):
                success_count += 1
        
        return success_count
    
    async def close(self):
        """Close the client session."""
        if self.session and not self.session.closed:
            await self.session.close()
