"""
Query Response Handler for Observability Service

This module handles asynchronous query responses from the database service
to complete the event-driven architecture pattern.
"""

import logging
import asyncio
import json
from typing import Dict, Any, Optional, Callable
from datetime import datetime, timedelta

from .messaging_client import MessagingClient
from .config import get_settings
from .telemetry import trace_method, add_span_attributes

logger = logging.getLogger(__name__)


class QueryResponseHandler:
    """Handler for processing query responses from database service."""
    
    def __init__(self, messaging_client: MessagingClient):
        self.messaging_client = messaging_client
        self.running = False
        self.consumer_tasks = []
        self.pending_queries = {}  # Store pending query callbacks
        self.query_timeout = 30  # seconds
    
    async def start(self):
        """Start query response consumers."""
        if self.running:
            return
            
        self.running = True
        logger.info("Starting query response handlers...")
        
        # Start consumers for different response types
        consumers = [
            self._consume_dependency_responses(),
            self._consume_event_responses(),
            self._consume_metric_responses(),
            self._consume_health_responses(),
            self._consume_trace_responses(),
            self._consume_error_responses(),
            self._cleanup_expired_queries()
        ]
        
        self.consumer_tasks = [asyncio.create_task(consumer) for consumer in consumers]
        logger.info(f"Started {len(self.consumer_tasks)} query response handlers")
    
    async def stop(self):
        """Stop query response consumers."""
        if not self.running:
            return
            
        self.running = False
        logger.info("Stopping query response handlers...")
        
        # Cancel all consumer tasks
        for task in self.consumer_tasks:
            task.cancel()
        
        # Wait for tasks to complete
        await asyncio.gather(*self.consumer_tasks, return_exceptions=True)
        self.consumer_tasks.clear()
        
        # Clear pending queries
        self.pending_queries.clear()
        logger.info("Stopped all query response handlers")
    
    async def register_query_callback(self, correlation_id: str, callback: Callable[[Dict[str, Any]], None], timeout: int = None):
        """Register a callback for a query response."""
        timeout = timeout or self.query_timeout
        expiry_time = datetime.utcnow() + timedelta(seconds=timeout)
        
        self.pending_queries[correlation_id] = {
            "callback": callback,
            "expiry_time": expiry_time,
            "registered_at": datetime.utcnow()
        }
        
        logger.debug(f"Registered query callback for correlation_id: {correlation_id}")
    
    @trace_method(name="query_response_handler.consume_dependency_responses")
    async def _consume_dependency_responses(self):
        """Consume dependency query responses."""
        while self.running:
            try:
                await self.messaging_client.consume_events(
                    event_type="query.dependency.response",
                    handler=self._handle_dependency_response,
                    consumer_group="observability_service_dependency_response"
                )
            except Exception as e:
                logger.error(f"Error in dependency response consumer: {e}")
                if self.running:
                    await asyncio.sleep(5)
    
    @trace_method(name="query_response_handler.consume_event_responses")
    async def _consume_event_responses(self):
        """Consume event query responses."""
        while self.running:
            try:
                await self.messaging_client.consume_events(
                    event_type="query.event.response",
                    handler=self._handle_event_response,
                    consumer_group="observability_service_event_response"
                )
            except Exception as e:
                logger.error(f"Error in event response consumer: {e}")
                if self.running:
                    await asyncio.sleep(5)
    
    @trace_method(name="query_response_handler.consume_metric_responses")
    async def _consume_metric_responses(self):
        """Consume metric query responses."""
        while self.running:
            try:
                await self.messaging_client.consume_events(
                    event_type="query.metric.response",
                    handler=self._handle_metric_response,
                    consumer_group="observability_service_metric_response"
                )
            except Exception as e:
                logger.error(f"Error in metric response consumer: {e}")
                if self.running:
                    await asyncio.sleep(5)
    
    @trace_method(name="query_response_handler.consume_health_responses")
    async def _consume_health_responses(self):
        """Consume health query responses."""
        while self.running:
            try:
                await self.messaging_client.consume_events(
                    event_type="query.health.response",
                    handler=self._handle_health_response,
                    consumer_group="observability_service_health_response"
                )
            except Exception as e:
                logger.error(f"Error in health response consumer: {e}")
                if self.running:
                    await asyncio.sleep(5)
    
    @trace_method(name="query_response_handler.consume_trace_responses")
    async def _consume_trace_responses(self):
        """Consume trace query responses."""
        while self.running:
            try:
                await self.messaging_client.consume_events(
                    event_type="query.trace.response",
                    handler=self._handle_trace_response,
                    consumer_group="observability_service_trace_response"
                )
            except Exception as e:
                logger.error(f"Error in trace response consumer: {e}")
                if self.running:
                    await asyncio.sleep(5)
    
    @trace_method(name="query_response_handler.consume_error_responses")
    async def _consume_error_responses(self):
        """Consume error responses from database service."""
        while self.running:
            try:
                await self.messaging_client.consume_events(
                    event_type="query.error.response",
                    handler=self._handle_error_response,
                    consumer_group="observability_service_error_response"
                )
            except Exception as e:
                logger.error(f"Error in error response consumer: {e}")
                if self.running:
                    await asyncio.sleep(5)
    
    async def _cleanup_expired_queries(self):
        """Clean up expired query callbacks."""
        while self.running:
            try:
                current_time = datetime.utcnow()
                expired_queries = []
                
                for correlation_id, query_info in self.pending_queries.items():
                    if current_time > query_info["expiry_time"]:
                        expired_queries.append(correlation_id)
                
                for correlation_id in expired_queries:
                    query_info = self.pending_queries.pop(correlation_id, None)
                    if query_info:
                        logger.warning(f"Query timeout for correlation_id: {correlation_id}")
                        # Call callback with timeout error
                        try:
                            query_info["callback"]({
                                "error": "Query timeout",
                                "correlation_id": correlation_id,
                                "status": "timeout"
                            })
                        except Exception as e:
                            logger.error(f"Error calling timeout callback: {e}")
                
                # Sleep for 10 seconds before next cleanup
                await asyncio.sleep(10)
                
            except Exception as e:
                logger.error(f"Error in query cleanup: {e}")
                await asyncio.sleep(10)
    
    # Response Handlers
    
    @trace_method(name="query_response_handler.handle_dependency_response")
    async def _handle_dependency_response(self, event_data: Dict[str, Any]):
        """Handle dependency query response."""
        try:
            correlation_id = event_data.get("correlation_id")
            result = event_data.get("result")
            status = event_data.get("status", "success")
            
            add_span_attributes({
                "event_type": "query.dependency.response",
                "correlation_id": correlation_id,
                "status": status
            })
            
            # Find and execute callback
            query_info = self.pending_queries.pop(correlation_id, None)
            if query_info:
                try:
                    query_info["callback"]({
                        "result": result,
                        "status": status,
                        "correlation_id": correlation_id
                    })
                    logger.debug(f"Processed dependency query response for {correlation_id}")
                except Exception as e:
                    logger.error(f"Error executing dependency response callback: {e}")
            else:
                logger.warning(f"No callback found for dependency response: {correlation_id}")
                
        except Exception as e:
            logger.error(f"Failed to handle dependency response: {e}")
    
    @trace_method(name="query_response_handler.handle_event_response")
    async def _handle_event_response(self, event_data: Dict[str, Any]):
        """Handle event query response."""
        try:
            correlation_id = event_data.get("correlation_id")
            result = event_data.get("result")
            status = event_data.get("status", "success")
            
            add_span_attributes({
                "event_type": "query.event.response",
                "correlation_id": correlation_id,
                "status": status
            })
            
            # Find and execute callback
            query_info = self.pending_queries.pop(correlation_id, None)
            if query_info:
                try:
                    query_info["callback"]({
                        "result": result,
                        "status": status,
                        "correlation_id": correlation_id
                    })
                    logger.debug(f"Processed event query response for {correlation_id}")
                except Exception as e:
                    logger.error(f"Error executing event response callback: {e}")
            else:
                logger.warning(f"No callback found for event response: {correlation_id}")
                
        except Exception as e:
            logger.error(f"Failed to handle event response: {e}")
    
    @trace_method(name="query_response_handler.handle_metric_response")
    async def _handle_metric_response(self, event_data: Dict[str, Any]):
        """Handle metric query response."""
        try:
            correlation_id = event_data.get("correlation_id")
            result = event_data.get("result")
            status = event_data.get("status", "success")
            
            add_span_attributes({
                "event_type": "query.metric.response",
                "correlation_id": correlation_id,
                "status": status
            })
            
            # Find and execute callback
            query_info = self.pending_queries.pop(correlation_id, None)
            if query_info:
                try:
                    query_info["callback"]({
                        "result": result,
                        "status": status,
                        "correlation_id": correlation_id
                    })
                    logger.debug(f"Processed metric query response for {correlation_id}")
                except Exception as e:
                    logger.error(f"Error executing metric response callback: {e}")
            else:
                logger.warning(f"No callback found for metric response: {correlation_id}")
                
        except Exception as e:
            logger.error(f"Failed to handle metric response: {e}")
    
    @trace_method(name="query_response_handler.handle_health_response")
    async def _handle_health_response(self, event_data: Dict[str, Any]):
        """Handle health query response."""
        try:
            correlation_id = event_data.get("correlation_id")
            result = event_data.get("result")
            status = event_data.get("status", "success")
            
            add_span_attributes({
                "event_type": "query.health.response",
                "correlation_id": correlation_id,
                "status": status
            })
            
            # Find and execute callback
            query_info = self.pending_queries.pop(correlation_id, None)
            if query_info:
                try:
                    query_info["callback"]({
                        "result": result,
                        "status": status,
                        "correlation_id": correlation_id
                    })
                    logger.debug(f"Processed health query response for {correlation_id}")
                except Exception as e:
                    logger.error(f"Error executing health response callback: {e}")
            else:
                logger.warning(f"No callback found for health response: {correlation_id}")
                
        except Exception as e:
            logger.error(f"Failed to handle health response: {e}")
    
    @trace_method(name="query_response_handler.handle_trace_response")
    async def _handle_trace_response(self, event_data: Dict[str, Any]):
        """Handle trace query response."""
        try:
            correlation_id = event_data.get("correlation_id")
            result = event_data.get("result")
            status = event_data.get("status", "success")
            
            add_span_attributes({
                "event_type": "query.trace.response",
                "correlation_id": correlation_id,
                "status": status
            })
            
            # Find and execute callback
            query_info = self.pending_queries.pop(correlation_id, None)
            if query_info:
                try:
                    query_info["callback"]({
                        "result": result,
                        "status": status,
                        "correlation_id": correlation_id
                    })
                    logger.debug(f"Processed trace query response for {correlation_id}")
                except Exception as e:
                    logger.error(f"Error executing trace response callback: {e}")
            else:
                logger.warning(f"No callback found for trace response: {correlation_id}")
                
        except Exception as e:
            logger.error(f"Failed to handle trace response: {e}")
    
    @trace_method(name="query_response_handler.handle_error_response")
    async def _handle_error_response(self, event_data: Dict[str, Any]):
        """Handle error response from database service."""
        try:
            correlation_id = event_data.get("correlation_id")
            error = event_data.get("error")
            status = event_data.get("status", "error")
            
            add_span_attributes({
                "event_type": "query.error.response",
                "correlation_id": correlation_id,
                "error": error,
                "status": status
            })
            
            # Find and execute callback
            query_info = self.pending_queries.pop(correlation_id, None)
            if query_info:
                try:
                    query_info["callback"]({
                        "error": error,
                        "status": status,
                        "correlation_id": correlation_id
                    })
                    logger.debug(f"Processed error response for {correlation_id}")
                except Exception as e:
                    logger.error(f"Error executing error response callback: {e}")
            else:
                logger.warning(f"No callback found for error response: {correlation_id}")
                
        except Exception as e:
            logger.error(f"Failed to handle error response: {e}")


# Global query response handler instance
query_response_handler: Optional[QueryResponseHandler] = None


async def get_query_response_handler() -> QueryResponseHandler:
    """Get the global query response handler instance."""
    global query_response_handler
    
    if query_response_handler is None:
        messaging_client = MessagingClient(
            base_url=get_settings().messaging_service_url,
            service_name=get_settings().service_name
        )
        query_response_handler = QueryResponseHandler(messaging_client)
        await query_response_handler.start()
    
    return query_response_handler
