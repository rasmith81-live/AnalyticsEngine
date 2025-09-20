"""
Command Event Consumers for Database Service

This module implements event consumers to process commands from other services.
"""

import logging
import asyncio
from typing import Dict, Any

from .database_manager import DatabaseManager
from .messaging_client import MessagingClient
from .telemetry import trace_method, add_span_attributes

logger = logging.getLogger(__name__)


class CommandConsumer:
    """Consumer for processing command events."""

    def __init__(self, database_manager: DatabaseManager, messaging_client: MessagingClient):
        self.database_manager = database_manager
        self.messaging_client = messaging_client
        self.running = False
        self.consumer_tasks = []

    async def start(self):
        """Start all command event consumers."""
        if self.running:
            return

        self.running = True
        logger.info("Starting command consumers...")

        try:
            await self._consume_create_item_commands()
            # Add other command consumers here
            logger.info("Successfully subscribed to all command topics.")
        except Exception as e:
            logger.error(f"Failed to start command consumers: {e}", exc_info=True)
            self.running = False
            raise

    async def stop(self):
        """Stop all command event consumers."""
        if not self.running:
            return

        self.running = False
        logger.info("Stopping command consumers...")

        # Disconnect the messaging client, which will handle stopping listeners
        await self.messaging_client.disconnect()
        logger.info("Stopped all command consumers")

    @trace_method(name="command_consumer.consume_create_item_commands")
    async def _consume_create_item_commands(self):
        """Subscribe to CreateItemCommand events."""
        await self.messaging_client.subscribe(
            topic="commands.CreateItemCommand",
            callback=self._handle_create_item_command
        )

    @trace_method(name="command_consumer.handle_create_item_command")
    async def _handle_create_item_command(self, event_data: Dict[str, Any]):
        """Handle CreateItemCommand event."""
        try:
            command_payload = event_data.get("command", {})
            item_data = command_payload.get("data", {})
            correlation_id = event_data.get("correlation_id")

            add_span_attributes({
                "event_type": "commands.CreateItemCommand",
                "item.name": item_data.get("name"),
                "correlation_id": correlation_id
            })

            # Store item data in the database
            created_item = await self.database_manager.create_item(item_data)

            logger.info(f"Processed CreateItemCommand for item: {created_item['name']}")

            # Publish ItemCreated event
            await self.messaging_client.publish_event(
                event_type="ItemCreated",
                event_data={
                    "item": created_item,
                    "correlation_id": correlation_id
                },
                correlation_id=correlation_id
            )

        except Exception as e:
            logger.error(f"Failed to handle CreateItemCommand: {e}")
            # Optionally, publish an error event
            raise
