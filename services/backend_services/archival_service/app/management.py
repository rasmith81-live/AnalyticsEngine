"""
Archival Management Module for the Archival Service.

This module provides self-management capabilities for the archival service,
including retention status monitoring, archival metrics, and management operations.
"""

import asyncio
import json
import logging
import os
import time
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple, Union

import httpx
from pydantic import BaseModel, Field, ConfigDict

from .models import ArchivalStatus
from .telemetry import trace_method, add_span_attributes, traced_span
from .api.monitoring_endpoints import get_monitor
from .state import archival_events

# Configure logging
logger = logging.getLogger(__name__)


class ArchivalStats(BaseModel):
    """Statistics about the archival process."""
    model_config = ConfigDict(populate_by_name=True)
    
    total_chunks: int = 0
    archived_chunks: int = 0
    pending_chunks: int = 0
    failed_chunks: int = 0
    oldest_chunk_age_days: Optional[int] = None
    newest_chunk_age_days: Optional[int] = None
    estimated_size_mb: Optional[float] = None


class TableRetentionStatus(BaseModel):
    """Retention status for a specific table."""
    model_config = ConfigDict(populate_by_name=True)
    
    table_name: str
    schema_name: str = "public"
    total_chunks: int
    chunks_to_archive: int
    oldest_chunk_time: Optional[str] = None
    newest_chunk_time: Optional[str] = None
    archival_status: Dict[str, int] = Field(default_factory=dict)


class RetentionStatus(BaseModel):
    """Overall retention status for all tables."""
    model_config = ConfigDict(populate_by_name=True)
    
    tables: List[TableRetentionStatus] = Field(default_factory=list)
    total_chunks: int = 0
    total_chunks_to_archive: int = 0


class ArchivalManager:
    """Utility class for managing TimescaleDB archival within the archival service."""
    
    def __init__(
        self,
        database_service_url: str = "http://localhost:8000",
        archival_service_url: str = "http://localhost:8080",
        timeout: int = 30
    ):
        """Initialize the archival manager.
        
        Args:
            database_service_url: URL of the Database Service.
            archival_service_url: URL of the Archival Service.
            timeout: Timeout for HTTP requests in seconds.
        """
        self.database_service_url = database_service_url
        self.archival_service_url = archival_service_url
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=timeout)
        self.monitor = get_monitor()
        self._lock = asyncio.Lock()
        self._last_stats_update = None
        self._cached_stats = None
        self._stats_cache_ttl = 60  # Cache stats for 60 seconds
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()
    
    @trace_method(name="ArchivalManager.get_retention_status", kind="CLIENT")
    async def get_retention_status(self) -> RetentionStatus:
        """Get the current retention status for all hypertables.
        
        Returns:
            RetentionStatus: The current retention status.
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for the request
        add_span_attributes({
            "archival.operation": "get_retention_status",
            "archival.operation_id": operation_id,
            "http.url": f"{self.database_service_url}/database/retention/status",
            "http.method": "GET",
            "service.name": "database_service"
        })
        
        url = f"{self.database_service_url}/database/retention/status"
        response = await self.client.get(url)
        response.raise_for_status()
        
        # Add span attributes for the response
        result = response.json()
        add_span_attributes({
            "archival.tables_count": len(result.get("tables", [])),
            "archival.total_chunks": result.get("total_chunks", 0),
            "archival.total_chunks_to_archive": result.get("total_chunks_to_archive", 0)
        })
        
        return RetentionStatus.model_validate(result)
    
    @trace_method(name="ArchivalManager.get_archival_metrics", kind="CLIENT")
    async def get_archival_metrics(self) -> Dict:
        """Get archival metrics from the Archival Service.
        
        Returns:
            Dict: Archival metrics.
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for the request
        add_span_attributes({
            "archival.operation": "get_archival_metrics",
            "archival.operation_id": operation_id,
            "service.name": "archival_service"
        })
        
        result = await self.monitor.get_metrics()
        add_span_attributes({
            "archival.metrics.total_archived_chunks": result.get("total_archived_chunks", 0),
            "archival.metrics.total_failed_chunks": result.get("total_failed_chunks", 0),
            "archival.metrics.avg_chunk_size_bytes": result.get("avg_chunk_size_bytes", 0)
        })
        
        return result
    
    @trace_method(name="ArchivalManager.trigger_archival", kind="CLIENT")
    async def trigger_archival(self, table_name: str) -> Dict:
        """Manually trigger archival for a specific table.
        
        Args:
            table_name: Name of the table to archive.
            
        Returns:
            Dict: Response from the API.
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for the request
        add_span_attributes({
            "archival.operation": "trigger_archival",
            "archival.operation_id": operation_id,
            "archival.table_name": table_name,
            "http.url": f"{self.database_service_url}/database/retention/trigger-archival",
            "http.method": "POST",
            "service.name": "database_service"
        })
        
        url = f"{self.database_service_url}/database/retention/trigger-archival"
        params = {"table_name": table_name}
        response = await self.client.post(url, params=params)
        response.raise_for_status()
        
        # Add span attributes for the response
        result = response.json()
        add_span_attributes({
            "archival.trigger_result": "success" if result.get("status") == "success" else "failure",
            "archival.job_id": result.get("job_id", "unknown")
        })
        
        return result
    
    @trace_method(name="ArchivalManager.get_database_health", kind="CLIENT")
    async def get_database_health(self) -> Dict:
        """Get health status from the Database Service.
        
        Returns:
            Dict: Health status of the Database Service.
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for the request
        add_span_attributes({
            "archival.operation": "get_database_health",
            "archival.operation_id": operation_id,
            "http.url": f"{self.database_service_url}/health",
            "http.method": "GET",
            "service.name": "database_service"
        })
        
        try:
            url = f"{self.database_service_url}/health"
            response = await self.client.get(url, timeout=5.0)  # Short timeout for health checks
            
            if response.status_code == 200:
                data = response.json()
                # Add span attributes for successful health check
                add_span_attributes({
                    "health.status": "healthy",
                    "health.database_status": data.get("database", {}).get("status", "unknown")
                })
                return {
                    "status": "healthy",
                    "details": data
                }
            else:
                # Add span attributes for unsuccessful health check
                add_span_attributes({
                    "health.status": "unhealthy",
                    "health.status_code": response.status_code,
                    "health.reason": "Non-200 response"
                })
                return {
                    "status": "unhealthy",
                    "details": {
                        "status_code": response.status_code,
                        "reason": "Non-200 response"
                    }
                }
                
        except Exception as e:
            logger.warning(f"Error checking database service health: {e}")
            # Add span attributes for health check error
            add_span_attributes({
                "health.status": "unhealthy",
                "health.error": str(e),
                "health.error_type": type(e).__name__
            })
            return {
                "status": "unhealthy",
                "details": {
                    "error": str(e),
                    "type": type(e).__name__
                }
            }
    
    @trace_method(name="ArchivalManager.get_health_status", kind="CLIENT")
    async def get_health_status(self) -> Dict:
        """Get health status of both the Database Service and Archival Service.
        
        Returns:
            Dict: Health status of both services.
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for the operation
        add_span_attributes({
            "archival.operation": "get_health_status",
            "archival.operation_id": operation_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Get database service health
        db_health = await self.get_database_health()
        
        # Check archival service health (this service)
        archival_health = {
            "status": "healthy",
            "details": {}
        }
        
        # Get active events to check if the archival service is functioning
        try:
            events = await self.get_active_events()
            archival_health["details"]["active_events"] = len(events)
            # Add span attributes for active events
            add_span_attributes({
                "archival.active_events": len(events)
            })
        except Exception as e:
            logger.warning(f"Error getting active events: {e}")
            archival_health = {
                "status": "warning",
                "details": {
                    "error": str(e),
                    "type": type(e).__name__
                }
            }
            # Add span attributes for error
            add_span_attributes({
                "archival.health.error": str(e),
                "archival.health.error_type": type(e).__name__
            })
        
        # Determine overall status
        overall_status = "healthy"
        if db_health["status"] != "healthy" or archival_health["status"] != "healthy":
            overall_status = "unhealthy"
        elif archival_health["status"] == "warning":
            overall_status = "warning"
        
        # Add span attributes for overall health status
        add_span_attributes({
            "health.overall_status": overall_status,
            "health.database_status": db_health["status"],
            "health.archival_status": archival_health["status"]
        })
        
        return {
            "status": overall_status,
            "database_service": db_health,
            "archival_service": archival_health,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    @trace_method(name="ArchivalManager.get_active_events", kind="CLIENT")
    async def get_active_events(self) -> List[Dict]:
        """Get active archival events from the local cache maintained by Redis subscription.
        
        The archival service tracks active events via Redis subscription to 'archival.events' topic
        and maintains them in the `state.py` archival_events dictionary.
        
        Returns:
            List[Dict]: List of active archival events.
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for the request
        add_span_attributes({
            "archival.operation": "get_active_events",
            "archival.operation_id": operation_id,
            "service.name": "archival_service"
        })

        try:
            # Directly access the in-memory dictionary
            active_events_list = [
                {
                    "event_id": event_id,
                    "table_name": data["event"].table_name,
                    "status": data["status"],
                    "started_at": data["started_at"],
                }
                for event_id, data in archival_events.items()
                if data["status"] in ["received", "processing"]
            ]

            # Add span attributes for the response
            add_span_attributes({
                "archival.active_events_count": len(active_events_list)
            })

            return active_events_list
        except Exception as e:
            logger.error(f"Error getting active events directly: {e}")
            # Add span attributes for error
            add_span_attributes({
                "archival.error": str(e),
                "archival.error_type": type(e).__name__
            })
            return []
            
    async def retrieve_archived_data(
        self,
        table_name: str,
        start_time: str,
        end_time: str,
        limit: int = 100,  # Reduced default limit to minimize compute costs
        offset: int = 0,
        columns: Optional[List[str]] = None,
        optimize_cost: bool = True
    ) -> Dict[str, Any]:
        """Retrieve archived data for a specific table within a time frame.
        
        Args:
            table_name: Name of the table to retrieve data from
            start_time: Start time in ISO format (YYYY-MM-DDTHH:MM:SS)
            end_time: End time in ISO format (YYYY-MM-DDTHH:MM:SS)
            limit: Maximum number of records to return (default reduced to minimize compute costs)
            offset: Offset for pagination
            columns: Optional list of columns to include (reduces data transfer)
            optimize_cost: If True, optimizes for compute cost over performance
            
        Returns:
            Dict: Retrieved data with metadata
            
        Raises:
            ValueError: If parameters are invalid
        """
        try:
            # Validate time format
            try:
                start_dt = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                end_dt = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
            except ValueError:
                raise ValueError("Invalid time format. Expected ISO format (YYYY-MM-DDTHH:MM:SS)")
                
            if end_dt < start_dt:
                raise ValueError("End time must be after start time")
            
            # Enforce reasonable time range to prevent excessive compute costs if optimize_cost is True
            time_range = end_dt - start_dt
            if optimize_cost:
                max_days = 31  # Maximum 31 days range to control costs
                if time_range.days > max_days:
                    raise ValueError(f"Time range too large. Maximum allowed is {max_days} days to control compute costs")
            elif time_range.days > 366:  # Still enforce a reasonable limit even in performance mode
                raise ValueError(f"Time range too large. Maximum allowed is 366 days")
                
            # Import lakehouse client to avoid circular imports
            from app.clients import lakehouse_client, messaging_client as redis_client
            from app.core.config import settings
            
            # Use Redis cache to minimize repeated expensive operations if optimize_cost is True
            cache_key = f"archived_data:{table_name}:{start_time}:{end_time}:{limit}:{offset}"
            cached_metadata = None
            if optimize_cost:
                cached_metadata = await redis_client.get(cache_key + ":metadata")
            
            if cached_metadata:
                # We have metadata cached, check if we need full data
                metadata = json.loads(cached_metadata)
                # If requesting just metadata or zero records, return cached metadata
                if limit == 0:
                    return {
                        "table_name": table_name,
                        "start_time": start_time,
                        "end_time": end_time,
                        "total_files_found": metadata["total_files_found"],
                        "files_read": 0,
                        "record_count": 0,
                        "data": [],
                        "metadata": {
                            "limit": limit,
                            "offset": offset,
                            "has_more": metadata["has_more"]
                        }
                    }
            
            # Construct path pattern for efficient directory traversal
            # This avoids listing all directories when we can narrow down by date components
            base_path = f"timescaledb_archive/{table_name}"
            
            # Generate only the needed year/month/day paths based on date range
            # This is much more efficient than listing all paths
            date_paths = []
            current_date = start_dt.date()
            end_date = end_dt.date()
            
            while current_date <= end_date:
                year, month, day = current_date.year, current_date.month, current_date.day
                date_paths.append(f"{base_path}/{year}/{month:02d}/{day:02d}")
                current_date += timedelta(days=1)
            
            # Check which paths actually exist to avoid unnecessary operations
            matching_files = []
            for path in date_paths:
                try:
                    # Only check if directory exists first before listing files
                    if await lakehouse_client.path_exists(path):
                        chunk_files = await lakehouse_client.list_files(path)
                        matching_files.extend([f"{path}/{chunk}" for chunk in chunk_files])
                except Exception as e:
                    logger.debug(f"Path {path} does not exist or cannot be accessed: {e}")
                    continue
            
            # Cache the metadata for future requests if optimize_cost is True
            metadata = {
                "total_files_found": len(matching_files),
                "has_more": len(matching_files) > (offset + limit)
            }
            if optimize_cost:
                await redis_client.set(
                    cache_key + ":metadata", 
                    json.dumps(metadata),
                    ex=settings.CACHE_TTL_SECONDS  # Use configured TTL
                )
            
            # If only metadata is requested, return early
            if limit == 0:
                return {
                    "table_name": table_name,
                    "start_time": start_time,
                    "end_time": end_time,
                    "total_files_found": len(matching_files),
                    "files_read": 0,
                    "record_count": 0,
                    "data": [],
                    "metadata": {
                        "limit": limit,
                        "offset": offset,
                        "has_more": len(matching_files) > (offset + limit)
                    }
                }
            
            # Apply pagination - only process the files we actually need
            paginated_files = matching_files[offset:offset+limit] if matching_files else []
            
            # Read data from files - use lazy loading to minimize memory usage
            all_data = []
            records_needed = limit
            
            for file_path in paginated_files:
                if records_needed <= 0:
                    break
                    
                # Check if we have this file's data cached (only if optimize_cost is True)
                file_cache_key = f"archived_file:{file_path}"
                cached_data = None
                if optimize_cost:
                    cached_data = await redis_client.get(file_cache_key)
                
                if cached_data:
                    # Use cached data
                    file_records = json.loads(cached_data)
                    all_data.extend(file_records[:records_needed])
                    records_needed -= len(file_records[:records_needed])
                else:
                    # Read from storage - only if needed
                    try:
                        # Remove file extension for reading
                        clean_path = file_path.rsplit('.', 1)[0] if '.' in file_path else file_path
                        
                        # Use column filtering if available to reduce data transfer
                        df = await lakehouse_client.read_data(
                            clean_path,
                            columns=columns  # Pass column filtering to reduce data transfer
                        )
                        
                        if df is not None:
                            # Convert DataFrame to records
                            file_records = df.to_dict(orient='records')
                            
                            # Cache the file data for future requests if optimize_cost is True
                            if optimize_cost:
                                await redis_client.set(
                                    file_cache_key,
                                    json.dumps(file_records),
                                    ex=settings.CACHE_TTL_SECONDS
                                )
                            
                            # Add to result set
                            all_data.extend(file_records[:records_needed])
                            records_needed -= len(file_records[:records_needed])
                    except Exception as e:
                        logger.warning(f"Error reading file {clean_path}: {e}")
                        continue
            
            return {
                "table_name": table_name,
                "start_time": start_time,
                "end_time": end_time,
                "total_files_found": len(matching_files),
                "files_read": len(paginated_files),
                "record_count": len(all_data),
                "data": all_data,
                "metadata": {
                    "limit": limit,
                    "offset": offset,
                    "has_more": len(matching_files) > (offset + limit)
                }
            }
            
        except ValueError as e:
            # Re-raise validation errors
            raise
        except Exception as e:
            logger.error(f"Error retrieving archived data: {e}", exc_info=True)
            raise ValueError(f"Error retrieving archived data: {str(e)}")
            
    
    @trace_method(name="ArchivalManager.calculate_archival_stats", kind="INTERNAL")
    async def calculate_archival_stats(self) -> ArchivalStats:
        """Calculate statistics about the archival process.
        
        Returns:
            ArchivalStats: Statistics about the archival process.
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        
        # Add span attributes for the operation
        add_span_attributes({
            "archival.operation": "calculate_archival_stats",
            "archival.operation_id": operation_id,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        async with self._lock:
            # Check if we have a recent cached result
            now = datetime.utcnow()
            if (self._last_stats_update and 
                self._cached_stats and 
                (now - self._last_stats_update).total_seconds() < self._stats_cache_ttl):
                # Add span attributes for cache hit
                add_span_attributes({
                    "archival.stats.cache_hit": True,
                    "archival.stats.cache_age_seconds": (now - self._last_stats_update).total_seconds()
                })
                return self._cached_stats
            
            stats = ArchivalStats()
            
            try:
                # Get retention status
                retention = await self.get_retention_status()
                
                # Calculate total chunks and pending chunks
                stats.total_chunks = retention.total_chunks
                stats.pending_chunks = retention.total_chunks_to_archive
                
                # Get archival metrics
                try:
                    metrics = await self.get_archival_metrics()
                    stats.archived_chunks = metrics.get("total_archived_chunks", 0)
                    stats.failed_chunks = metrics.get("total_failed_chunks", 0)
                except Exception as e:
                    logger.warning(f"Error getting archival metrics: {e}")
                
                # Calculate chunk ages
                oldest_time = None
                newest_time = None
                
                for table in retention.tables:
                    if table.oldest_chunk_time:
                        table_oldest = datetime.fromisoformat(table.oldest_chunk_time.replace('Z', '+00:00'))
                        if oldest_time is None or table_oldest < oldest_time:
                            oldest_time = table_oldest
                    
                    if table.newest_chunk_time:
                        table_newest = datetime.fromisoformat(table.newest_chunk_time.replace('Z', '+00:00'))
                        if newest_time is None or table_newest > newest_time:
                            newest_time = table_newest
                
                if oldest_time:
                    stats.oldest_chunk_age_days = (now - oldest_time).days
                
                if newest_time:
                    stats.newest_chunk_age_days = (now - newest_time).days
                
                # Estimate size (very rough estimate)
                # Assuming average chunk size from metrics if available
                try:
                    avg_chunk_size = metrics.get("avg_chunk_size_bytes", 0)
                    if avg_chunk_size > 0:
                        stats.estimated_size_mb = (stats.pending_chunks * avg_chunk_size) / (1024 * 1024)
                except Exception:
                    pass
                
                # Cache the result
                self._cached_stats = stats
                self._last_stats_update = now
                
                return stats
            
            except Exception as e:
                logger.error(f"Error calculating archival stats: {e}")
                return stats


# Singleton instance
_manager_instance = None


@trace_method(name="get_archival_manager", kind="INTERNAL")
def get_archival_manager(
    database_service_url: str = "http://localhost:8000",
    archival_service_url: str = "http://localhost:8080"
) -> ArchivalManager:
    """Get the singleton instance of the archival manager.
    
    Args:
        database_service_url: URL of the Database Service.
        archival_service_url: URL of the Archival Service.
        
    Returns:
        ArchivalManager: The archival manager instance.
    """
    # Add span attributes for the operation
    add_span_attributes({
        "archival.operation": "get_archival_manager",
        "archival.database_service_url": database_service_url,
        "archival.archival_service_url": archival_service_url
    })
    
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = ArchivalManager(
            database_service_url=database_service_url,
            archival_service_url=archival_service_url
        )
        # Add span attributes for manager creation
        add_span_attributes({"archival.manager_created": True})
    else:
        # Add span attributes for manager retrieval
        add_span_attributes({"archival.manager_created": False})
    
    return _manager_instance


@trace_method(name="close_archival_manager", kind="INTERNAL")
async def close_archival_manager():
    """Close the archival manager instance."""
    # Add span attributes for the operation
    add_span_attributes({"archival.operation": "close_archival_manager"})
    
    global _manager_instance
    if _manager_instance:
        await _manager_instance.close()
        _manager_instance = None
        # Add span attributes for manager closure
        add_span_attributes({"archival.manager_closed": True})
    else:
        # Add span attributes when no manager exists
        add_span_attributes({"archival.manager_closed": False})
