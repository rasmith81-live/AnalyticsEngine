# =============================================================================
# Base Command Consumer for Redis Streams
# Reusable consumer for processing service commands
# =============================================================================
"""
Base consumer class for processing commands from Redis Streams.

Provides:
- Consumer group management
- Command dispatching
- Response publishing
- Error handling
"""

import asyncio
import json
import logging
import os
import uuid
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Optional

import redis.asyncio as redis

from .schemas import (
    ServiceCommand,
    ServiceResponse,
    CommandType,
    ResponseType,
    get_stream_name,
    get_consumer_group,
)

logger = logging.getLogger(__name__)


CommandHandler = Callable[[ServiceCommand], Any]


class BaseCommandConsumer(ABC):
    """
    Base consumer for processing commands from Redis Streams.
    
    Subclass and implement handlers for specific command types.
    
    Usage:
        class MetadataConsumer(BaseCommandConsumer):
            def __init__(self):
                super().__init__("business_metadata")
                
            async def _register_handlers(self):
                self.register_handler(CommandType.CREATE_ENTITY, self._handle_create_entity)
                
            async def _handle_create_entity(self, command: ServiceCommand) -> Dict[str, Any]:
                # Process and return result
                return {"id": "..."}
    """
    
    def __init__(
        self,
        service_name: str,
        redis_url: Optional[str] = None,
        consumer_name: Optional[str] = None
    ):
        """
        Initialize consumer.
        
        Args:
            service_name: Name of this service
            redis_url: Redis connection URL
            consumer_name: Unique consumer name (auto-generated if not provided)
        """
        self.service_name = service_name
        self.redis_url = redis_url or os.getenv("REDIS_URL", "redis://redis:6379/0")
        self.consumer_name = consumer_name or f"consumer_{uuid.uuid4().hex[:8]}"
        
        self._stream_name = get_stream_name(service_name)
        self._consumer_group = get_consumer_group(service_name)
        
        self._redis: Optional[redis.Redis] = None
        self._running = False
        self._handlers: Dict[CommandType, CommandHandler] = {}
    
    async def start(self) -> None:
        """Start the consumer."""
        self._redis = redis.Redis.from_url(
            self.redis_url,
            decode_responses=True,
            max_connections=10
        )
        
        await self._redis.ping()
        logger.info(f"{self.service_name} consumer connected to Redis")
        
        # Create consumer group if not exists
        try:
            await self._redis.xgroup_create(
                self._stream_name,
                self._consumer_group,
                id="0",
                mkstream=True
            )
            logger.info(f"Created consumer group: {self._consumer_group}")
        except redis.ResponseError as e:
            if "BUSYGROUP" not in str(e):
                raise
            logger.debug(f"Consumer group {self._consumer_group} already exists")
        
        # Register handlers
        await self._register_handlers()
        
        self._running = True
        logger.info(f"{self.service_name} consumer started: {self.consumer_name}")
    
    async def stop(self) -> None:
        """Stop the consumer."""
        self._running = False
        
        if self._redis:
            await self._redis.close()
            self._redis = None
        
        logger.info(f"{self.service_name} consumer stopped")
    
    @abstractmethod
    async def _register_handlers(self) -> None:
        """Register command handlers. Override in subclass."""
        pass
    
    def register_handler(
        self,
        command_type: CommandType,
        handler: CommandHandler
    ) -> None:
        """Register a handler for a command type."""
        self._handlers[command_type] = handler
        logger.debug(f"Registered handler for {command_type.value}")
    
    async def consume(self) -> None:
        """Main consume loop."""
        while self._running:
            try:
                messages = await self._redis.xreadgroup(
                    groupname=self._consumer_group,
                    consumername=self.consumer_name,
                    streams={self._stream_name: ">"},
                    count=10,
                    block=1000
                )
                
                for stream_name, stream_messages in messages:
                    for message_id, message_data in stream_messages:
                        await self._process_message(message_id, message_data)
            
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error consuming messages: {e}")
                await asyncio.sleep(1)
    
    async def _process_message(
        self,
        message_id: str,
        message_data: Dict[str, str]
    ) -> None:
        """Process a single command message."""
        command = None
        try:
            command = ServiceCommand.from_stream_dict(message_data)
            
            logger.debug(
                f"Processing {command.command_type.value} from {command.source_service}"
            )
            
            # Find handler
            handler = self._handlers.get(command.command_type)
            
            if handler is None:
                await self._send_error(command, f"Unknown command: {command.command_type.value}")
            else:
                # Execute handler
                result = await handler(command)
                
                # Send success response
                response_type = self._get_response_type(command.command_type)
                await self._send_response(command, response_type, result)
            
            # Acknowledge
            await self._redis.xack(
                self._stream_name,
                self._consumer_group,
                message_id
            )
            
        except Exception as e:
            logger.error(f"Error processing message {message_id}: {e}")
            if command:
                await self._send_error(command, str(e))
            # Still acknowledge to prevent infinite reprocessing
            await self._redis.xack(
                self._stream_name,
                self._consumer_group,
                message_id
            )
    
    async def _send_response(
        self,
        command: ServiceCommand,
        response_type: ResponseType,
        payload: Dict[str, Any]
    ) -> None:
        """Send success response via pub/sub."""
        response = ServiceResponse.success_response(
            command=command,
            response_type=response_type,
            payload=payload,
            source_service=self.service_name
        )
        
        await self._redis.publish(command.reply_channel, response.to_json())
    
    async def _send_error(self, command: ServiceCommand, error: str) -> None:
        """Send error response via pub/sub."""
        response = ServiceResponse.error_response(
            command=command,
            error=error,
            source_service=self.service_name
        )
        
        await self._redis.publish(command.reply_channel, response.to_json())
    
    def _get_response_type(self, command_type: CommandType) -> ResponseType:
        """Map command type to response type."""
        mapping = {
            # Entity
            CommandType.CREATE_ENTITY: ResponseType.ENTITY_CREATED,
            CommandType.UPDATE_ENTITY: ResponseType.ENTITY_UPDATED,
            CommandType.DELETE_ENTITY: ResponseType.ENTITY_DELETED,
            CommandType.GET_ENTITY: ResponseType.ENTITY_DATA,
            CommandType.LIST_ENTITIES: ResponseType.ENTITY_LIST,
            # KPI
            CommandType.CREATE_KPI: ResponseType.KPI_CREATED,
            CommandType.UPDATE_KPI: ResponseType.KPI_UPDATED,
            CommandType.GET_KPI: ResponseType.KPI_DATA,
            CommandType.LIST_KPIS: ResponseType.KPI_LIST,
            CommandType.CALCULATE_KPI: ResponseType.KPI_RESULT,
            CommandType.CALCULATE_BATCH: ResponseType.BATCH_RESULT,
            # Module
            CommandType.CREATE_MODULE: ResponseType.MODULE_CREATED,
            CommandType.GET_MODULE: ResponseType.MODULE_DATA,
            CommandType.LIST_MODULES: ResponseType.MODULE_LIST,
            # Value chain
            CommandType.CREATE_VALUE_CHAIN: ResponseType.VALUE_CHAIN_CREATED,
            CommandType.GET_VALUE_CHAIN: ResponseType.VALUE_CHAIN_DATA,
            CommandType.LIST_VALUE_CHAINS: ResponseType.VALUE_CHAIN_LIST,
            # Connector
            CommandType.FETCH_DATA: ResponseType.DATA_FETCHED,
            CommandType.TEST_CONNECTION: ResponseType.CONNECTION_OK,
            CommandType.LIST_SOURCES: ResponseType.SOURCES_LIST,
            # Database
            CommandType.EXECUTE_QUERY: ResponseType.QUERY_RESULT,
            CommandType.EXECUTE_WRITE: ResponseType.WRITE_COMPLETE,
            # Ingestion
            CommandType.PROCESS_DOCUMENT: ResponseType.DOCUMENT_PROCESSED,
            CommandType.EXTRACT_ENTITIES: ResponseType.ENTITIES_EXTRACTED,
            CommandType.ENRICH_METADATA: ResponseType.METADATA_ENRICHED,
            # Agent
            CommandType.CREATE_SESSION: ResponseType.SESSION_CREATED,
            CommandType.SEND_MESSAGE: ResponseType.MESSAGE_RESPONSE,
            CommandType.RUN_ANALYSIS: ResponseType.ANALYSIS_RESULT,
            CommandType.FINALIZE_SESSION: ResponseType.SESSION_FINALIZED,
            # Generic
            CommandType.HEALTH_CHECK: ResponseType.HEALTH_OK,
        }
        return mapping.get(command_type, ResponseType.ACK)
