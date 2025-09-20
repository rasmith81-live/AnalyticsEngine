import asyncio
import uuid
from datetime import datetime
from typing import Any, Callable, Awaitable

from ..core.logging import get_logger
from ..core.pubsub import pubsub_service

logger = get_logger(__name__)

class MessagingClient:
    def __init__(self, timeout: int = 10):
        self.pubsub_service = pubsub_service
        self.timeout = timeout

    async def publish(self, channel: str, message: Any):
        await self.pubsub_service.publish(channel, message)

    async def subscribe(self, channel: str, handler: Callable[[str, Any], Awaitable[None]]):
        await self.pubsub_service.subscribe(channel, handler)

    async def unsubscribe(self, channel: str, handler: Callable[[str, Any], Awaitable[None]]):
        await self.pubsub_service.unsubscribe(channel, handler)

    async def send_command(self, channel: str, command: str, payload: Any, correlation_id: str = None) -> str:
        correlation_id = correlation_id or str(uuid.uuid4())
        command_message = {
            "command": command,
            "payload": payload,
            "metadata": {
                "correlation_id": correlation_id,
                "timestamp": datetime.utcnow().isoformat(),
                "source": "api_gateway",
            },
        }
        await self.publish(channel, command_message)
        logger.info(f"Published command '{command}' to {channel} with correlation ID {correlation_id}")
        return correlation_id

    async def send_query(self, channel: str, query: str, params: Any, correlation_id: str = None) -> Any:
        correlation_id = correlation_id or str(uuid.uuid4())
        response_channel = f"responses.{correlation_id}"
        response_future = asyncio.Future()

        async def response_handler(ch: str, message: Any):
            if not response_future.done():
                response_future.set_result(message)

        await self.subscribe(response_channel, response_handler)

        query_message = {
            "query": query,
            "parameters": params,
            "metadata": {
                "correlation_id": correlation_id,
                "timestamp": datetime.utcnow().isoformat(),
                "source": "api_gateway",
                "response_channel": response_channel,
            },
        }

        try:
            await self.publish(channel, query_message)
            logger.info(f"Published query '{query}' to {channel} with correlation ID {correlation_id}")
            response = await asyncio.wait_for(response_future, timeout=self.timeout)
            return response
        finally:
            await self.unsubscribe(response_channel, response_handler)

    async def record_metric(self, name: str, value: float, labels: dict):
        """
        Publishes a metric to the messaging service.
        """
        payload = {
            "name": name,
            "value": value,
            "labels": labels,
        }
        await self.send_command(
            channel="metrics.events",
            command="record_metric",
            payload=payload
        )
        logger.debug(f"Recorded metric '{name}' with value {value} and labels {labels}")
