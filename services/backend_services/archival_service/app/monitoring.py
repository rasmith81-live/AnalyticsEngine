"""
Monitoring module for the Archival Service.

This module provides metrics collection, performance tracking, and health monitoring
for the TimescaleDB archival process.
"""

import asyncio
import logging
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from .models import ArchivalStatus

# Configure logging
logger = logging.getLogger(__name__)

# Global monitor instance
_monitor_instance = None


def get_archival_monitor() -> 'ArchivalMonitor':
    """Get the singleton instance of the archival monitor.
    
    Returns:
        ArchivalMonitor: The archival monitor instance.
    """
    global _monitor_instance
    if _monitor_instance is None:
        _monitor_instance = ArchivalMonitor()
    return _monitor_instance


class ArchivalMetrics(BaseModel):
    """Metrics for the archival process."""
    
    # Counters
    total_events_received: int = 0
    total_archived_chunks: int = 0
    total_failed_chunks: int = 0
    
    # Time-based metrics
    chunks_archived_last_hour: int = 0
    chunks_failed_last_hour: int = 0
    
    # Performance metrics
    avg_processing_time_ms: float = 0
    max_processing_time_ms: float = 0
    
    # Size metrics
    total_archived_bytes: int = 0
    avg_chunk_size_bytes: int = 0
    
    # Recent events
    recent_events: List[Dict] = Field(default_factory=list)
    
    # Last update
    last_updated: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class ArchivalMonitor:
    """Monitor for the archival process."""
    
    def __init__(self, max_recent_events: int = 10):
        """Initialize the archival monitor.
        
        Args:
            max_recent_events: Maximum number of recent events to keep.
        """
        self.metrics = ArchivalMetrics()
        self.max_recent_events = max_recent_events
        self.processing_times: List[float] = []
        self.chunk_sizes: List[int] = []
        self.event_times: List[datetime] = []
        self.status_counts: Dict[ArchivalStatus, int] = {
            status: 0 for status in ArchivalStatus
        }
        self._lock = asyncio.Lock()
    
    async def record_event(
        self,
        event_id: str,
        chunk_id: str,
        table_name: str,
        status: ArchivalStatus,
        processing_time_ms: float,
        chunk_size_bytes: Optional[int] = None,
        error_message: Optional[str] = None
    ):
        """Record an archival event.
        
        Args:
            event_id: ID of the event.
            chunk_id: ID of the chunk.
            table_name: Name of the table.
            status: Status of the archival.
            processing_time_ms: Processing time in milliseconds.
            chunk_size_bytes: Size of the chunk in bytes.
            error_message: Error message if status is FAILED.
        """
        async with self._lock:
            # Update counters
            self.metrics.total_events_received += 1
            
            if status == ArchivalStatus.SUCCESS:
                self.metrics.total_archived_chunks += 1
                if chunk_size_bytes:
                    self.metrics.total_archived_bytes += chunk_size_bytes
                    self.chunk_sizes.append(chunk_size_bytes)
            elif status == ArchivalStatus.FAILED:
                self.metrics.total_failed_chunks += 1
            
            # Update status counts
            self.status_counts[status] += 1
            
            # Update performance metrics
            self.processing_times.append(processing_time_ms)
            if len(self.processing_times) > 100:
                self.processing_times.pop(0)
            
            self.metrics.avg_processing_time_ms = sum(self.processing_times) / len(self.processing_times)
            self.metrics.max_processing_time_ms = max(self.processing_times)
            
            # Update chunk size metrics
            if self.chunk_sizes:
                self.metrics.avg_chunk_size_bytes = sum(self.chunk_sizes) / len(self.chunk_sizes)
            
            # Record event time
            now = datetime.utcnow()
            self.event_times.append(now)
            
            # Clean up old event times
            one_hour_ago = now - timedelta(hours=1)
            self.event_times = [t for t in self.event_times if t > one_hour_ago]
            
            # Update time-based metrics
            self.metrics.chunks_archived_last_hour = sum(
                1 for t in self.event_times 
                if t > one_hour_ago and self.status_counts.get(ArchivalStatus.SUCCESS, 0) > 0
            )
            self.metrics.chunks_failed_last_hour = sum(
                1 for t in self.event_times 
                if t > one_hour_ago and self.status_counts.get(ArchivalStatus.FAILED, 0) > 0
            )
            
            # Update recent events
            event_data = {
                "event_id": event_id,
                "chunk_id": chunk_id,
                "table_name": table_name,
                "status": status.value,
                "processing_time_ms": processing_time_ms,
                "timestamp": now.isoformat()
            }
            
            if chunk_size_bytes:
                event_data["chunk_size_bytes"] = chunk_size_bytes
            
            if error_message:
                event_data["error_message"] = error_message
            
            self.metrics.recent_events.append(event_data)
            if len(self.metrics.recent_events) > self.max_recent_events:
                self.metrics.recent_events.pop(0)
            
            # Update last updated timestamp
            self.metrics.last_updated = now.isoformat()
    
    async def get_metrics(self) -> Dict:
        """Get the current metrics.
        
        Returns:
            Dict: The current metrics.
        """
        async with self._lock:
            return self.metrics.model_dump()
            
    async def get_recent_events(self, limit: int = 10) -> List[Dict]:
        """Get recent archival events.
        
        Args:
            limit: Maximum number of events to return
            
        Returns:
            List[Dict]: Recent archival events
        """
        async with self._lock:
            # Return the most recent events up to the limit
            return self.metrics.recent_events[-limit:] if self.metrics.recent_events else []
    
    async def get_health_status(self) -> Dict:
        """Get the health status of the archival process.
        
        Returns:
            Dict: Health status information.
        """
        async with self._lock:
            # Calculate health metrics
            now = datetime.utcnow()
            last_updated = datetime.fromisoformat(self.metrics.last_updated)
            time_since_last_event = (now - last_updated).total_seconds()
            
            # Check if there have been any events in the last hour
            events_last_hour = len([t for t in self.event_times if t > now - timedelta(hours=1)])
            
            # Calculate failure rate
            failure_rate = 0
            if self.metrics.total_events_received > 0:
                failure_rate = self.metrics.total_failed_chunks / self.metrics.total_events_received
            
            # Determine health status
            status = "healthy"
            issues = []
            
            if time_since_last_event > 3600 and events_last_hour > 0:
                status = "warning"
                issues.append("No events processed in the last hour")
            
            if failure_rate > 0.1:  # More than 10% failure rate
                status = "warning"
                issues.append(f"High failure rate: {failure_rate:.2%}")
            
            if failure_rate > 0.3:  # More than 30% failure rate
                status = "critical"
            
            if self.metrics.avg_processing_time_ms > 10000:  # More than 10 seconds
                issues.append("High average processing time")
            
            return {
                "status": status,
                "total_events": self.metrics.total_events_received,
                "success_rate": 1 - failure_rate,
                "avg_processing_time_ms": self.metrics.avg_processing_time_ms,
                "events_last_hour": events_last_hour,
                "time_since_last_event_seconds": time_since_last_event,
                "issues": issues,
                "last_updated": self.metrics.last_updated
            }


class PerformanceTracker:
    """Utility class for tracking performance of operations."""
    
    def __init__(self, operation_name: str):
        """Initialize the performance tracker.
        
        Args:
            operation_name: Name of the operation being tracked.
        """
        self.operation_name = operation_name
        self.start_time = None
        self.end_time = None
    
    async def __aenter__(self):
        """Start tracking performance."""
        self.start_time = time.time()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Stop tracking performance and log results."""
        self.end_time = time.time()
        duration_ms = (self.end_time - self.start_time) * 1000
        
        if exc_type:
            logger.warning(
                f"Operation '{self.operation_name}' failed after {duration_ms:.2f}ms: {exc_val}"
            )
        else:
            logger.debug(
                f"Operation '{self.operation_name}' completed in {duration_ms:.2f}ms"
            )
        
        return False  # Don't suppress exceptions
    
    @property
    def duration_ms(self) -> float:
        """Get the duration of the operation in milliseconds.
        
        Returns:
            float: Duration in milliseconds.
        """
        if self.start_time is None or self.end_time is None:
            return 0
        
        return (self.end_time - self.start_time) * 1000
