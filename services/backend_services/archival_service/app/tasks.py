"""
Scheduled tasks for the Archival Service.

This module provides scheduled tasks for health checks, maintenance operations,
and automatic archival management.
"""

import asyncio
import logging
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from .config import settings
from .management import get_archival_manager, ArchivalStats
from .models import ArchivalStatus
from .telemetry import trace_method, add_span_attributes, traced_span

# Configure logging
logger = logging.getLogger(__name__)


class ScheduledTaskManager:
    """Manager for scheduled archival service tasks."""
    
    def __init__(self):
        """Initialize the scheduled task manager."""
        self.tasks = {}
        self.running = False
        self._lock = asyncio.Lock()
        self._last_health_check = None
        self._health_check_interval = 300  # 5 minutes
        self._last_maintenance = None
        self._maintenance_interval = 3600  # 1 hour
        self._last_auto_archival = None
        self._auto_archival_interval = 86400  # 24 hours
        self._health_status = {"status": "unknown"}
    
    @trace_method(name="ScheduledTaskManager.start", kind="INTERNAL")
    async def start(self):
        """Start the scheduled tasks."""
        # Add span attributes for task management
        add_span_attributes({
            "task_management.operation": "start_tasks",
            "task_management.auto_archival_enabled": str(settings.auto_archival_enabled)
        })
        
        async with self._lock:
            if self.running:
                return
            
            self.running = True
            
            # Start the health check task
            self.tasks["health_check"] = asyncio.create_task(
                self._run_periodic_health_check()
            )
            
            # Start the maintenance task
            self.tasks["maintenance"] = asyncio.create_task(
                self._run_periodic_maintenance()
            )
            
            # Start the auto archival task if enabled
            if settings.auto_archival_enabled:
                self.tasks["auto_archival"] = asyncio.create_task(
                    self._run_auto_archival()
                )
            
            logger.info("Scheduled tasks started")
    
    @trace_method(name="ScheduledTaskManager.stop", kind="INTERNAL")
    async def stop(self):
        """Stop the scheduled tasks."""
        # Add span attributes for task management
        add_span_attributes({
            "task_management.operation": "stop_tasks",
            "task_management.active_tasks": str(len(self.tasks))
        })
        
        async with self._lock:
            if not self.running:
                return
            
            self.running = False
            
            # Cancel all tasks
            for name, task in self.tasks.items():
                if not task.done():
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass
            
            self.tasks = {}
            logger.info("Scheduled tasks stopped")
    
    @trace_method(name="ScheduledTaskManager.get_health_status", kind="INTERNAL")
    async def get_health_status(self) -> Dict:
        """Get the current health status.
        
        Returns:
            Dict: The current health status.
        """
        # Add span attributes for health status
        add_span_attributes({
            "task_management.operation": "get_health_status",
            "health_status": self._health_status.get("status", "unknown")
        })
        
        async with self._lock:
            return self._health_status.copy()
    
    @trace_method(name="ScheduledTaskManager._run_periodic_health_check", kind="INTERNAL")
    async def _run_periodic_health_check(self):
        """Run periodic health checks."""
        while self.running:
            try:
                now = datetime.utcnow()
                
                # Check if it's time to run a health check
                if (self._last_health_check is None or 
                    (now - self._last_health_check).total_seconds() >= self._health_check_interval):
                    
                    logger.debug("Running scheduled health check")
                    # Create a span for this specific health check run
                    async with traced_span(
                        name="scheduled_health_check",
                        kind="INTERNAL",
                        attributes={
                            "task_management.operation": "scheduled_health_check",
                            "task_management.interval_seconds": self._health_check_interval,
                            "task_management.last_run": self._last_health_check.isoformat() if self._last_health_check else "never"
                        }
                    ):
                        await self._perform_health_check()
                        self._last_health_check = now
                
                # Sleep for a short time before checking again
                await asyncio.sleep(60)  # Check every minute
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in health check task: {e}", exc_info=True)
                await asyncio.sleep(60)  # Wait before retrying
    
    @trace_method(name="ScheduledTaskManager._run_periodic_maintenance", kind="INTERNAL")
    async def _run_periodic_maintenance(self):
        """Run periodic maintenance operations."""
        while self.running:
            try:
                now = datetime.utcnow()
                
                # Check if it's time to run maintenance
                if (self._last_maintenance is None or 
                    (now - self._last_maintenance).total_seconds() >= self._maintenance_interval):
                    
                    logger.debug("Running scheduled maintenance")
                    # Create a span for this specific maintenance run
                    async with traced_span(
                        name="scheduled_maintenance",
                        kind="INTERNAL",
                        attributes={
                            "task_management.operation": "scheduled_maintenance",
                            "task_management.interval_seconds": self._maintenance_interval,
                            "task_management.last_run": self._last_maintenance.isoformat() if self._last_maintenance else "never"
                        }
                    ):
                        await self._perform_maintenance()
                        self._last_maintenance = now
                
                # Sleep for a short time before checking again
                await asyncio.sleep(300)  # Check every 5 minutes
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in maintenance task: {e}", exc_info=True)
                await asyncio.sleep(300)  # Wait before retrying
    
    @trace_method(name="ScheduledTaskManager._run_auto_archival", kind="INTERNAL")
    async def _run_auto_archival(self):
        """Run automatic archival operations."""
        while self.running:
            try:
                now = datetime.utcnow()
                
                # Check if it's time to run auto archival
                if (self._last_auto_archival is None or 
                    (now - self._last_auto_archival).total_seconds() >= self._auto_archival_interval):
                    
                    logger.debug("Running scheduled auto archival")
                    # Create a span for this specific auto archival run
                    async with traced_span(
                        name="scheduled_auto_archival",
                        kind="INTERNAL",
                        attributes={
                            "task_management.operation": "scheduled_auto_archival",
                            "task_management.interval_seconds": self._auto_archival_interval,
                            "task_management.last_run": self._last_auto_archival.isoformat() if self._last_auto_archival else "never"
                        }
                    ):
                        await self._perform_auto_archival()
                        self._last_auto_archival = now
                
                # Sleep for a longer time before checking again
                await asyncio.sleep(3600)  # Check every hour
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in auto archival task: {e}", exc_info=True)
                await asyncio.sleep(3600)  # Wait before retrying
    
    @trace_method(name="ScheduledTaskManager._perform_health_check", kind="INTERNAL")
    async def _perform_health_check(self):
        """Perform a health check of the archival system."""
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for health check
        add_span_attributes({
            "task_management.operation": "health_check",
            "task_management.operation_id": operation_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        try:
            # Get the archival manager
            manager = get_archival_manager()
            
            # Check services health
            services_health = await manager.get_health_status()
            
            # Check if any service is unhealthy
            status = "healthy"
            issues = []
            
            # Check if services_health is a dictionary with expected structure
            overall_status = services_health.get("status", "unknown")
            status = overall_status

            # Check database service health
            db_service_health = services_health.get("database_service", {})
            if db_service_health.get("status") != "healthy":
                issues.append(f"Database service is {db_service_health.get('status')}: {db_service_health.get('details')}")

            # Check archival service health
            archival_service_health = services_health.get("archival_service", {})
            if archival_service_health.get("status") != "healthy":
                issues.append(f"Archival service is {archival_service_health.get('status')}: {archival_service_health.get('details')}")
            
            # Get archival stats
            try:
                stats = await manager.calculate_archival_stats()
                
                # Check for potential issues
                if stats.pending_chunks > 1000:  # Arbitrary threshold
                    issues.append(f"Large backlog: {stats.pending_chunks} chunks pending archival")
                    if status == "healthy":
                        status = "warning"
                
                if stats.failed_chunks > 0:
                    failure_rate = stats.failed_chunks / (stats.archived_chunks + stats.failed_chunks) if (stats.archived_chunks + stats.failed_chunks) > 0 else 0
                    if failure_rate > 0.1:  # More than 10% failure rate
                        issues.append(f"High failure rate: {failure_rate:.2%}")
                        if status == "healthy":
                            status = "warning"
                    
                    if failure_rate > 0.3:  # More than 30% failure rate
                        status = "critical"
                
                if stats.oldest_chunk_age_days and stats.oldest_chunk_age_days > 30:  # Older than 30 days
                    issues.append(f"Old chunks: oldest chunk is {stats.oldest_chunk_age_days} days old")
                    if status == "healthy":
                        status = "warning"
            
            except Exception as e:
                logger.warning(f"Error getting archival stats: {e}")
                issues.append(f"Error getting archival stats: {str(e)}")
                if status == "healthy":
                    status = "warning"
            
            # Update health status
            self._health_status = {
                "status": status,
                "issues": issues,
                "last_check": datetime.utcnow().isoformat(),
                "services": services_health
            }
            
            # Log health status
            if status != "healthy":
                logger.warning(f"Health check status: {status}, issues: {issues}")
            else:
                logger.debug("Health check status: healthy")
            
        except Exception as e:
            logger.error(f"Error performing health check: {e}", exc_info=True)
            self._health_status = {
                "status": "critical",
                "issues": [f"Error performing health check: {str(e)}"],
                "last_check": datetime.utcnow().isoformat()
            }
    
    @trace_method(name="ScheduledTaskManager._perform_maintenance", kind="INTERNAL")
    async def _perform_maintenance(self):
        """Perform maintenance operations."""
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for maintenance operation
        add_span_attributes({
            "task_management.operation": "maintenance",
            "task_management.operation_id": operation_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        try:
            # Get the archival manager
            manager = get_archival_manager()
            
            # Get archival stats
            stats = await manager.calculate_archival_stats()
            
            # Log maintenance information
            logger.info(f"Maintenance: Total chunks: {stats.total_chunks}, "
                       f"Archived: {stats.archived_chunks}, "
                       f"Pending: {stats.pending_chunks}, "
                       f"Failed: {stats.failed_chunks}")
            
            # Check for failed chunks and log them
            if stats.failed_chunks > 0:
                logger.warning(f"Maintenance: {stats.failed_chunks} failed chunks detected")
            
            # Additional maintenance tasks could be added here
            # For example, cleaning up old events, retrying failed archival operations, etc.
            
        except Exception as e:
            logger.error(f"Error performing maintenance: {e}", exc_info=True)
    
    @trace_method(name="ScheduledTaskManager._perform_auto_archival", kind="INTERNAL")
    async def _perform_auto_archival(self):
        """Perform automatic archival operations."""
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for auto archival operation
        add_span_attributes({
            "task_management.operation": "auto_archival",
            "task_management.operation_id": operation_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        try:
            # Get the archival manager
            manager = get_archival_manager()
            
            # Get retention status
            retention = await manager.get_retention_status()
            
            # Check if there are tables that need archival
            for table in retention.tables:
                if table.chunks_to_archive > 0:
                    logger.info(f"Auto archival: Triggering archival for table {table.table_name} "
                               f"({table.chunks_to_archive} chunks)")
                    
                    # Trigger archival for the table
                    try:
                        response = await manager.trigger_archival(table.table_name)
                        logger.info(f"Auto archival: Triggered archival for {table.table_name}, "
                                   f"response: {response}")
                    except Exception as e:
                        logger.error(f"Error triggering archival for {table.table_name}: {e}")
            
        except Exception as e:
            logger.error(f"Error performing auto archival: {e}", exc_info=True)


# Singleton instance
_task_manager = None


@trace_method(name="get_task_manager", kind="INTERNAL")
def get_task_manager() -> ScheduledTaskManager:
    """Get the singleton instance of the scheduled task manager.
    
    Returns:
        ScheduledTaskManager: The scheduled task manager instance.
    """
    global _task_manager
    if _task_manager is None:
        _task_manager = ScheduledTaskManager()
        # Add span attributes for task manager creation
        add_span_attributes({"task_management.operation": "create_task_manager"})
    else:
        # Add span attributes for task manager retrieval
        add_span_attributes({"task_management.operation": "get_task_manager"})
    return _task_manager


@trace_method(name="start_scheduled_tasks", kind="INTERNAL")
async def start_scheduled_tasks():
    """Start the scheduled tasks."""
    # Add span attributes for starting scheduled tasks
    add_span_attributes({"task_management.operation": "start_scheduled_tasks"})
    manager = get_task_manager()
    await manager.start()


@trace_method(name="stop_scheduled_tasks", kind="INTERNAL")
async def stop_scheduled_tasks():
    """Stop the scheduled tasks."""
    # Add span attributes for stopping scheduled tasks
    add_span_attributes({"task_management.operation": "stop_scheduled_tasks"})
    global _task_manager
    if _task_manager:
        await _task_manager.stop()
        _task_manager = None
