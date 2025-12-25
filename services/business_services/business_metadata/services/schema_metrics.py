"""
Schema Metrics Service

Tracks and reports metrics for schema extraction and migration operations.
Integrates with Observability Service for monitoring.
"""

from typing import Dict, Any, Optional
from datetime import datetime
import time
import logging

logger = logging.getLogger(__name__)


class SchemaMetrics:
    """
    Tracks metrics for schema extraction and migration operations.
    
    Metrics tracked:
    - schema.extraction.count - Number of schema extractions
    - schema.extraction.duration_ms - Time to extract schema
    - schema.extraction.success_rate - Percentage of successful extractions
    - schema.extraction.errors - Count of extraction errors
    - schema.bulk_extraction.count - Number of bulk extractions
    - schema.bulk_extraction.entities_processed - Total entities in bulk operations
    """
    
    def __init__(self, observability_client=None):
        """
        Initialize SchemaMetrics.
        
        Args:
            observability_client: ObservabilityClient for sending metrics (optional)
        """
        self.observability_client = observability_client
        self._metrics = {
            "extraction_count": 0,
            "extraction_success": 0,
            "extraction_failure": 0,
            "bulk_extraction_count": 0,
            "total_entities_processed": 0,
            "total_duration_ms": 0
        }
    
    async def record_extraction_start(self, entity_code: str) -> str:
        """
        Record the start of a schema extraction.
        
        Args:
            entity_code: Entity being extracted
            
        Returns:
            Operation ID for tracking
        """
        operation_id = f"extract_{entity_code}_{int(time.time() * 1000)}"
        
        logger.debug(f"Schema extraction started: {entity_code} (op_id: {operation_id})")
        
        return operation_id
    
    async def record_extraction_complete(
        self,
        operation_id: str,
        entity_code: str,
        duration_ms: float,
        success: bool,
        error: Optional[str] = None
    ):
        """
        Record the completion of a schema extraction.
        
        Args:
            operation_id: Operation ID from start
            entity_code: Entity that was extracted
            duration_ms: Time taken in milliseconds
            success: Whether extraction succeeded
            error: Error message if failed
        """
        # Update local metrics
        self._metrics["extraction_count"] += 1
        self._metrics["total_duration_ms"] += duration_ms
        
        if success:
            self._metrics["extraction_success"] += 1
        else:
            self._metrics["extraction_failure"] += 1
        
        # Calculate success rate
        success_rate = (
            self._metrics["extraction_success"] / self._metrics["extraction_count"] * 100
            if self._metrics["extraction_count"] > 0 else 0
        )
        
        # Send to Observability Service if available
        if self.observability_client:
            try:
                await self.observability_client.record_metric(
                    name="schema.extraction.duration_ms",
                    value=duration_ms,
                    labels={
                        "entity_code": entity_code,
                        "success": str(success).lower()
                    }
                )
                
                await self.observability_client.record_metric(
                    name="schema.extraction.success_rate",
                    value=success_rate,
                    labels={"entity_code": entity_code}
                )
                
                if not success and error:
                    await self.observability_client.log_event(
                        level="error",
                        message=f"Schema extraction failed for {entity_code}",
                        context={
                            "entity_code": entity_code,
                            "error": error,
                            "duration_ms": duration_ms
                        }
                    )
            except Exception as e:
                logger.warning(f"Failed to send metrics to Observability Service: {e}")
        
        logger.info(
            f"Schema extraction {'succeeded' if success else 'failed'}: {entity_code} "
            f"(duration: {duration_ms:.2f}ms, success_rate: {success_rate:.1f}%)"
        )
    
    async def record_bulk_extraction_start(self, entity_count: int) -> str:
        """
        Record the start of a bulk schema extraction.
        
        Args:
            entity_count: Number of entities to extract
            
        Returns:
            Operation ID for tracking
        """
        operation_id = f"bulk_extract_{int(time.time() * 1000)}"
        
        logger.info(f"Bulk schema extraction started: {entity_count} entities (op_id: {operation_id})")
        
        return operation_id
    
    async def record_bulk_extraction_complete(
        self,
        operation_id: str,
        entity_count: int,
        successful: int,
        failed: int,
        duration_ms: float
    ):
        """
        Record the completion of a bulk schema extraction.
        
        Args:
            operation_id: Operation ID from start
            entity_count: Total entities processed
            successful: Number of successful extractions
            failed: Number of failed extractions
            duration_ms: Total time taken in milliseconds
        """
        # Update local metrics
        self._metrics["bulk_extraction_count"] += 1
        self._metrics["total_entities_processed"] += entity_count
        
        # Calculate metrics
        success_rate = (successful / entity_count * 100) if entity_count > 0 else 0
        avg_duration_per_entity = duration_ms / entity_count if entity_count > 0 else 0
        
        # Send to Observability Service if available
        if self.observability_client:
            try:
                await self.observability_client.record_metric(
                    name="schema.bulk_extraction.entities_processed",
                    value=entity_count,
                    labels={"operation_id": operation_id}
                )
                
                await self.observability_client.record_metric(
                    name="schema.bulk_extraction.success_rate",
                    value=success_rate,
                    labels={"operation_id": operation_id}
                )
                
                await self.observability_client.record_metric(
                    name="schema.bulk_extraction.duration_ms",
                    value=duration_ms,
                    labels={"operation_id": operation_id}
                )
                
                await self.observability_client.record_metric(
                    name="schema.bulk_extraction.avg_duration_per_entity_ms",
                    value=avg_duration_per_entity,
                    labels={"operation_id": operation_id}
                )
            except Exception as e:
                logger.warning(f"Failed to send bulk metrics to Observability Service: {e}")
        
        logger.info(
            f"Bulk schema extraction complete: {successful}/{entity_count} successful "
            f"(duration: {duration_ms:.2f}ms, avg: {avg_duration_per_entity:.2f}ms/entity)"
        )
    
    async def record_api_call(
        self,
        endpoint: str,
        method: str,
        duration_ms: float,
        status_code: int
    ):
        """
        Record an API call metric.
        
        Args:
            endpoint: API endpoint called
            method: HTTP method
            duration_ms: Request duration
            status_code: HTTP status code
        """
        if self.observability_client:
            try:
                await self.observability_client.record_metric(
                    name="schema.api.request.duration_ms",
                    value=duration_ms,
                    labels={
                        "endpoint": endpoint,
                        "method": method,
                        "status_code": str(status_code)
                    }
                )
                
                # Track success/failure
                success = 200 <= status_code < 300
                await self.observability_client.record_metric(
                    name="schema.api.request.count",
                    value=1,
                    labels={
                        "endpoint": endpoint,
                        "method": method,
                        "success": str(success).lower()
                    }
                )
            except Exception as e:
                logger.warning(f"Failed to send API metrics to Observability Service: {e}")
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """
        Get summary of all tracked metrics.
        
        Returns:
            Dictionary with metric summaries
        """
        avg_duration = (
            self._metrics["total_duration_ms"] / self._metrics["extraction_count"]
            if self._metrics["extraction_count"] > 0 else 0
        )
        
        success_rate = (
            self._metrics["extraction_success"] / self._metrics["extraction_count"] * 100
            if self._metrics["extraction_count"] > 0 else 0
        )
        
        return {
            "total_extractions": self._metrics["extraction_count"],
            "successful_extractions": self._metrics["extraction_success"],
            "failed_extractions": self._metrics["extraction_failure"],
            "success_rate_percent": round(success_rate, 2),
            "average_duration_ms": round(avg_duration, 2),
            "bulk_extractions": self._metrics["bulk_extraction_count"],
            "total_entities_processed": self._metrics["total_entities_processed"],
            "total_duration_ms": round(self._metrics["total_duration_ms"], 2)
        }
    
    async def report_health(self) -> Dict[str, Any]:
        """
        Report health status based on metrics.
        
        Returns:
            Health status dictionary
        """
        summary = self.get_metrics_summary()
        
        # Determine health status
        success_rate = summary["success_rate_percent"]
        
        if success_rate >= 95:
            status = "healthy"
        elif success_rate >= 80:
            status = "degraded"
        else:
            status = "unhealthy"
        
        health = {
            "status": status,
            "metrics": summary,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # Send to Observability Service if available
        if self.observability_client:
            try:
                await self.observability_client.report_health(
                    status=status,
                    details=summary
                )
            except Exception as e:
                logger.warning(f"Failed to send health status to Observability Service: {e}")
        
        return health
