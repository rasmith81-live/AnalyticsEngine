"""
Telemetry Event Consumers for Database Service

This module implements event consumers to process telemetry data ingestion events
from the observability service and other services in the event-driven architecture.
"""

import logging
import json
import asyncio
from typing import Dict, Any, Optional
from datetime import datetime

from .database_manager import DatabaseManager
from .messaging_client import MessagingClient
from .telemetry import trace_method, add_span_attributes

logger = logging.getLogger(__name__)


class TelemetryEventConsumer:
    """Consumer for processing telemetry ingestion events."""
    
    def __init__(self, database_manager: DatabaseManager, messaging_client: MessagingClient):
        self.database_manager = database_manager
        self.messaging_client = messaging_client
        self.running = False
        self.consumer_tasks = []
    
    async def start(self):
        """Start all telemetry event consumers."""
        if self.running:
            return

        self.running = True
        logger.info("Starting telemetry event consumers...")

        # Subscribe to all necessary topics
        try:
            await self._consume_dependency_events()
            await self._consume_event_events()
            await self._consume_metric_events()
            await self._consume_health_events()
            await self._consume_trace_events()
            await self._consume_query_requests()
            await self._consume_data_requests()
            await self._consume_command_requests()
            logger.info("Successfully subscribed to all telemetry topics.")
        except Exception as e:
            logger.error(f"Failed to start telemetry consumers: {e}", exc_info=True)
            self.running = False
            raise
    
    async def stop(self):
        """Stop all telemetry event consumers."""
        if not self.running:
            return

        self.running = False
        logger.info("Stopping telemetry event consumers...")

        # Disconnect the messaging client, which will handle stopping listeners
        await self.messaging_client.disconnect()
        logger.info("Stopped all telemetry event consumers")
    
    @trace_method(name="telemetry_consumer.consume_dependency_events")
    async def _consume_dependency_events(self):
        """Subscribe to dependency telemetry ingestion events."""
        await self.messaging_client.subscribe(
            topic="telemetry.dependency.ingested",
            callback=self._handle_dependency_ingestion
        )
    
    @trace_method(name="telemetry_consumer.consume_event_events")
    async def _consume_event_events(self):
        """Subscribe to event telemetry ingestion events."""
        await self.messaging_client.subscribe(
            topic="telemetry.event.ingested",
            callback=self._handle_event_ingestion
        )
    
    @trace_method(name="telemetry_consumer.consume_metric_events")
    async def _consume_metric_events(self):
        """Subscribe to metric telemetry ingestion events."""
        await self.messaging_client.subscribe(
            topic="telemetry.metric.ingested",
            callback=self._handle_metric_ingestion
        )
    
    @trace_method(name="telemetry_consumer.consume_health_events")
    async def _consume_health_events(self):
        """Subscribe to health telemetry ingestion events."""
        await self.messaging_client.subscribe(
            topic="telemetry.health.ingested",
            callback=self._handle_health_ingestion
        )
    
    @trace_method(name="telemetry_consumer.consume_trace_events")
    async def _consume_trace_events(self):
        """Subscribe to trace telemetry ingestion events."""
        await self.messaging_client.subscribe(
            topic="telemetry.trace.ingested",
            callback=self._handle_trace_ingestion
        )
    
    @trace_method(name="telemetry_consumer.consume_query_requests")
    async def _consume_query_requests(self):
        """Subscribe to query request events."""
        await self.messaging_client.subscribe(
            topic="query.*.request",
            callback=self._handle_query_request
        )
    
    @trace_method(name="telemetry_consumer.consume_data_requests")
    async def _consume_data_requests(self):
        """Subscribe to data request events from services."""
        await self.messaging_client.subscribe(
            topic="data.request.*",
            callback=self._handle_data_request
        )
    
    @trace_method(name="telemetry_consumer.consume_command_requests")
    async def _consume_command_requests(self):
        """Subscribe to command execution events from services."""
        await self.messaging_client.subscribe(
            topic="command.*.execute",
            callback=self._handle_command_request
        )
    
    # Event Handlers
    
    @trace_method(name="telemetry_consumer.handle_dependency_ingestion")
    async def _handle_dependency_ingestion(self, event_data: Dict[str, Any]):
        """Handle dependency telemetry ingestion event."""
        try:
            dependency_data = event_data.get("dependency", {})
            correlation_id = event_data.get("correlation_id")
            
            add_span_attributes({
                "event_type": "telemetry.dependency.ingested",
                "dependency.service": dependency_data.get("service"),
                "dependency.name": dependency_data.get("name"),
                "correlation_id": correlation_id
            })
            
            # Store dependency data in TimescaleDB
            await self.database_manager.store_dependency_data(dependency_data)
            
            logger.info(f"Processed dependency ingestion for {dependency_data.get('service')}/{dependency_data.get('name')}")
            
        except Exception as e:
            logger.error(f"Failed to handle dependency ingestion: {e}")
            raise
    
    @trace_method(name="telemetry_consumer.handle_event_ingestion")
    async def _handle_event_ingestion(self, event_data: Dict[str, Any]):
        """Handle event telemetry ingestion event."""
        try:
            event_payload = event_data.get("event", {})
            correlation_id = event_data.get("correlation_id")
            
            add_span_attributes({
                "event_type": "telemetry.event.ingested",
                "event.service": event_payload.get("service"),
                "event.name": event_payload.get("name"),
                "correlation_id": correlation_id
            })
            
            # Store event data in TimescaleDB
            await self.database_manager.store_event_data(event_payload)
            
            logger.info(f"Processed event ingestion for {event_payload.get('service')}/{event_payload.get('name')}")
            
        except Exception as e:
            logger.error(f"Failed to handle event ingestion: {e}")
            raise
    
    @trace_method(name="telemetry_consumer.handle_metric_ingestion")
    async def _handle_metric_ingestion(self, event_data: Dict[str, Any]):
        """Handle metric telemetry ingestion event."""
        try:
            metric_data = event_data.get("metric", {})
            correlation_id = event_data.get("correlation_id")
            
            add_span_attributes({
                "event_type": "telemetry.metric.ingested",
                "metric.service": metric_data.get("service_name"),
                "metric.name": metric_data.get("name"),
                "correlation_id": correlation_id
            })
            
            # Store metric data in TimescaleDB
            await self.database_manager.store_metric_data(metric_data)
            
            logger.info(f"Processed metric ingestion for {metric_data.get('service_name')}/{metric_data.get('name')}")
            
        except Exception as e:
            logger.error(f"Failed to handle metric ingestion: {e}")
            raise
    
    @trace_method(name="telemetry_consumer.handle_health_ingestion")
    async def _handle_health_ingestion(self, event_data: Dict[str, Any]):
        """Handle health telemetry ingestion event."""
        try:
            health_data = event_data.get("health", {})
            correlation_id = event_data.get("correlation_id")
            
            add_span_attributes({
                "event_type": "telemetry.health.ingested",
                "health.service": health_data.get("service"),
                "health.status": health_data.get("status"),
                "correlation_id": correlation_id
            })
            
            # Store health data in TimescaleDB
            await self.database_manager.store_health_data(health_data)
            
            logger.info(f"Processed health ingestion for {health_data.get('service')}")
            
        except Exception as e:
            logger.error(f"Failed to handle health ingestion: {e}")
            raise
    
    @trace_method(name="telemetry_consumer.handle_trace_ingestion")
    async def _handle_trace_ingestion(self, event_data: Dict[str, Any]):
        """Handle trace telemetry ingestion event."""
        try:
            trace_data = event_data.get("trace", {})
            correlation_id = event_data.get("correlation_id")
            
            add_span_attributes({
                "event_type": "telemetry.trace.ingested",
                "trace.service": trace_data.get("service"),
                "trace.operation": trace_data.get("operation_name"),
                "correlation_id": correlation_id
            })
            
            # Store trace data in TimescaleDB
            await self.database_manager.store_trace_data(trace_data)
            
            logger.info(f"Processed trace ingestion for {trace_data.get('service')}/{trace_data.get('operation_name')}")
            
        except Exception as e:
            logger.error(f"Failed to handle trace ingestion: {e}")
            raise
    
    @trace_method(name="telemetry_consumer.handle_query_request")
    async def _handle_query_request(self, event_data: Dict[str, Any]):
        """Handle query request events from observability service."""
        try:
            query_type = event_data.get("query_type")
            correlation_id = event_data.get("correlation_id")
            
            add_span_attributes({
                "event_type": "query.request",
                "query.type": query_type,
                "correlation_id": correlation_id
            })
            
            # Process query and publish response
            result = await self._process_query_request(event_data)
            
            # Publish query response event
            await self.messaging_client.publish_event(
                event_type=f"query.{query_type}.response",
                event_data={
                    "result": result,
                    "correlation_id": correlation_id,
                    "status": "success"
                },
                correlation_id=correlation_id
            )
            
            logger.info(f"Processed query request: {query_type}")
            
        except Exception as e:
            logger.error(f"Failed to handle query request: {e}")
            # Publish error response
            await self.messaging_client.publish_event(
                event_type=f"query.error.response",
                event_data={
                    "error": str(e),
                    "correlation_id": event_data.get("correlation_id"),
                    "status": "error"
                },
                correlation_id=event_data.get("correlation_id")
            )
    
    @trace_method(name="telemetry_consumer.handle_data_request")
    async def _handle_data_request(self, event_data: Dict[str, Any]):
        """Handle data request events from business services."""
        try:
            service = event_data.get("service")
            operation = event_data.get("operation")
            parameters = event_data.get("parameters", {})
            
            add_span_attributes({
                "event_type": "data.request",
                "service": service,
                "operation": operation
            })
            
            # Process data request based on service and operation
            result = await self._process_data_request(service, operation, parameters)
            
            # Publish data response event
            await self.messaging_client.publish_event(
                event_type=f"data.response.{service}",
                event_data={
                    "result": result,
                    "service": service,
                    "operation": operation,
                    "status": "success"
                }
            )
            
            logger.info(f"Processed data request from {service}: {operation}")
            
        except Exception as e:
            logger.error(f"Failed to handle data request: {e}")
            raise
    
    @trace_method(name="telemetry_consumer.handle_command_request")
    async def _handle_command_request(self, event_data: Dict[str, Any]):
        """Handle command execution events from business services."""
        try:
            service = event_data.get("service")
            command = event_data.get("command", {})
            
            add_span_attributes({
                "event_type": "command.execute",
                "service": service,
                "command.action": command.get("action")
            })
            
            # Process command execution
            result = await self._process_command_execution(service, command)
            
            # Publish command response event
            await self.messaging_client.publish_event(
                event_type=f"command.response.{service}",
                event_data={
                    "result": result,
                    "service": service,
                    "command": command,
                    "status": "success"
                }
            )
            
            logger.info(f"Processed command from {service}: {command.get('action')}")
            
        except Exception as e:
            logger.error(f"Failed to handle command request: {e}")
            raise
    
    async def _process_query_request(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process query request and return results."""
        query_type = event_data.get("query_type")
        
        if query_type == "get_dependency":
            service = event_data.get("service")
            name = event_data.get("name")
            parameters = event_data.get("parameters", {})
            
            return await self.database_manager.query_dependency_data(
                {"service": service, "name": name},
                limit=parameters.get("limit", 1),
                order_by=parameters.get("order_by", "timestamp"),
                order_direction=parameters.get("order_direction", "desc")
            )
        
        elif query_type == "query_dependencies":
            query = event_data.get("query", {})
            parameters = event_data.get("parameters", {})
            
            return await self.database_manager.query_dependency_data(
                query,
                limit=parameters.get("limit", 100),
                offset=parameters.get("offset", 0),
                order_by=parameters.get("order_by", "timestamp"),
                order_direction=parameters.get("order_direction", "desc")
            )
        
        else:
            raise ValueError(f"Unknown query type: {query_type}")
    
    async def _process_data_request(self, service: str, operation: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Process data request from business services."""
        if operation == "get_data":
            limit = parameters.get("limit", 100)
            offset = parameters.get("offset", 0)
            
            # Return mock data for now - implement actual data retrieval logic
            return {
                "data": [],
                "total": 0,
                "limit": limit,
                "offset": offset,
                "service": service
            }
        
        else:
            raise ValueError(f"Unknown operation: {operation}")
    
    async def _process_command_execution(self, service: str, command: Dict[str, Any]) -> Dict[str, Any]:
        """Process command execution from business services."""
        action = command.get("action")
        
        # Process command based on action
        # Implement actual command processing logic here
        
        return {
            "command_id": command.get("command_id"),
            "action": action,
            "service": service,
            "executed_at": datetime.utcnow().isoformat(),
            "result": "Command processed successfully"
        }
