"""
Test script for backend service message handling.
Verifies that backend services correctly process messages from the API Gateway.
"""
import asyncio
import json
import uuid
from datetime import datetime
from typing import Dict, Any, Optional

import pytest
import redis.asyncio as redis
from pydantic import BaseModel, Field

# Mock Redis client for testing
class MockRedisClient:
    def __init__(self):
        self.channels = {}
        self.patterns = {}
        self.pubsub_channels = {}
    
    async def publish(self, channel: str, message: str) -> int:
        """Publish a message to a channel."""
        if channel not in self.channels:
            self.channels[channel] = []
        
        self.channels[channel].append(message)
        
        # Notify subscribers
        if channel in self.pubsub_channels:
            for callback in self.pubsub_channels[channel]:
                await callback(channel, message)
        
        # Check pattern subscribers
        for pattern, callbacks in self.patterns.items():
            if self._match_pattern(pattern, channel):
                for callback in callbacks:
                    await callback(channel, message)
        
        return len(self.channels.get(channel, []))
    
    async def subscribe(self, channel: str, callback):
        """Subscribe to a channel."""
        if channel not in self.pubsub_channels:
            self.pubsub_channels[channel] = []
        
        self.pubsub_channels[channel].append(callback)
    
    async def psubscribe(self, pattern: str, callback):
        """Subscribe to a pattern."""
        if pattern not in self.patterns:
            self.patterns[pattern] = []
        
        self.patterns[pattern].append(callback)
    
    def _match_pattern(self, pattern: str, channel: str) -> bool:
        """Check if channel matches pattern."""
        if pattern.endswith('*'):
            return channel.startswith(pattern[:-1])
        return pattern == channel


# Message models
class MessageMetadata(BaseModel):
    correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    user_id: Optional[str] = None
    response_channel: Optional[str] = None


class CommandMessage(BaseModel):
    command: str
    payload: Dict[str, Any]
    metadata: MessageMetadata = Field(default_factory=MessageMetadata)


class QueryMessage(BaseModel):
    query: str
    parameters: Dict[str, Any]
    metadata: MessageMetadata = Field(default_factory=MessageMetadata)


class ResponseMessage(BaseModel):
    data: Dict[str, Any]
    metadata: MessageMetadata = Field(default_factory=MessageMetadata)


# Test fixtures
@pytest.fixture
def mock_redis():
    """Create a mock Redis client."""
    return MockRedisClient()


@pytest.fixture
def command_handlers():
    """Create command handlers for testing."""
    handlers = {}
    
    async def register_handler(command_type, handler):
        handlers[command_type] = handler
    
    async def process_command(channel, message_str):
        try:
            message_dict = json.loads(message_str)
            command = message_dict.get("command")
            
            if command in handlers:
                await handlers[command](message_dict)
        except Exception as e:
            print(f"Error processing command: {e}")
    
    return {
        "register": register_handler,
        "process": process_command,
        "handlers": handlers
    }


@pytest.fixture
def query_handlers():
    """Create query handlers for testing."""
    handlers = {}
    
    async def register_handler(query_type, handler):
        handlers[query_type] = handler
    
    async def process_query(channel, message_str):
        try:
            message_dict = json.loads(message_str)
            query = message_dict.get("query")
            
            if query in handlers:
                response = await handlers[query](message_dict)
                
                # Send response to response channel
                if "metadata" in message_dict and "response_channel" in message_dict["metadata"]:
                    response_channel = message_dict["metadata"]["response_channel"]
                    response_message = ResponseMessage(
                        data=response,
                        metadata=MessageMetadata(
                            correlation_id=message_dict["metadata"]["correlation_id"]
                        )
                    )
                    await redis_client.publish(
                        response_channel,
                        response_message.model_dump_json()
                    )
        except Exception as e:
            print(f"Error processing query: {e}")
    
    return {
        "register": register_handler,
        "process": process_query,
        "handlers": handlers
    }


# Global Redis client for tests
redis_client = None


@pytest.mark.asyncio
async def test_command_handling(mock_redis, command_handlers):
    """Test handling commands from API Gateway."""
    global redis_client
    redis_client = mock_redis
    
    # Register command handlers
    async def handle_create_message(message):
        """Handle create_message command."""
        assert message["command"] == "create_message"
        assert "content" in message["payload"]
        assert "user_id" in message["payload"]
        assert "correlation_id" in message["metadata"]
        
        # Publish event notification
        event_message = {
            "event": "message_created",
            "data": {
                "id": str(uuid.uuid4()),
                "content": message["payload"]["content"],
                "user_id": message["payload"]["user_id"],
                "created_at": datetime.utcnow().isoformat()
            },
            "metadata": {
                "correlation_id": message["metadata"]["correlation_id"],
                "timestamp": datetime.utcnow().isoformat()
            }
        }
        
        await redis_client.publish(
            "events.business_service_a",
            json.dumps(event_message)
        )
        
        return True
    
    await command_handlers["register"]("create_message", handle_create_message)
    
    # Subscribe to command channel
    await mock_redis.subscribe("commands.business_service_a", command_handlers["process"])
    
    # Test command message
    command = CommandMessage(
        command="create_message",
        payload={
            "content": "Test message",
            "user_id": "test-user"
        }
    )
    
    # Publish command
    await mock_redis.publish(
        "commands.business_service_a",
        command.model_dump_json()
    )
    
    # Wait for processing
    await asyncio.sleep(0.1)
    
    # Verify event was published
    assert "events.business_service_a" in mock_redis.channels
    event_message = json.loads(mock_redis.channels["events.business_service_a"][0])
    assert event_message["event"] == "message_created"
    assert event_message["data"]["content"] == "Test message"
    assert event_message["data"]["user_id"] == "test-user"


@pytest.mark.asyncio
async def test_query_handling(mock_redis, query_handlers):
    """Test handling queries from API Gateway."""
    global redis_client
    redis_client = mock_redis
    
    # Register query handlers
    async def handle_get_message(message):
        """Handle get_message query."""
        assert message["query"] == "get_message"
        assert "message_id" in message["parameters"]
        assert "correlation_id" in message["metadata"]
        assert "response_channel" in message["metadata"]
        
        # Return mock data
        return {
            "id": message["parameters"]["message_id"],
            "content": "Test message content",
            "created_at": datetime.utcnow().isoformat(),
            "user_id": "test-user-id"
        }
    
    await query_handlers["register"]("get_message", handle_get_message)
    
    # Subscribe to query channel
    await mock_redis.subscribe("queries.business_service_a", query_handlers["process"])
    
    # Create a response handler
    response_received = asyncio.Event()
    response_data = None
    
    async def response_handler(channel, message_str):
        nonlocal response_data
        response_data = json.loads(message_str)
        response_received.set()
    
    # Subscribe to response channel
    response_channel = f"responses.{uuid.uuid4()}"
    await mock_redis.subscribe(response_channel, response_handler)
    
    # Test query message
    query = QueryMessage(
        query="get_message",
        parameters={
            "message_id": "test-message-id"
        },
        metadata=MessageMetadata(
            response_channel=response_channel
        )
    )
    
    # Publish query
    await mock_redis.publish(
        "queries.business_service_a",
        query.model_dump_json()
    )
    
    # Wait for response
    await asyncio.wait_for(response_received.wait(), timeout=1.0)
    
    # Verify response
    assert response_data is not None
    assert "data" in response_data
    assert response_data["data"]["id"] == "test-message-id"
    assert response_data["data"]["content"] == "Test message content"
    assert "metadata" in response_data
    assert "correlation_id" in response_data["metadata"]


@pytest.mark.asyncio
async def test_pattern_subscription(mock_redis):
    """Test pattern-based subscriptions."""
    # Create a pattern handler
    pattern_messages = []
    
    async def pattern_handler(channel, message_str):
        pattern_messages.append((channel, json.loads(message_str)))
    
    # Subscribe to pattern
    await mock_redis.psubscribe("responses.*", pattern_handler)
    
    # Publish messages to different channels
    await mock_redis.publish(
        "responses.123",
        json.dumps({"data": {"id": "123"}, "metadata": {}})
    )
    
    await mock_redis.publish(
        "responses.456",
        json.dumps({"data": {"id": "456"}, "metadata": {}})
    )
    
    await mock_redis.publish(
        "commands.service",
        json.dumps({"command": "test", "payload": {}, "metadata": {}})
    )
    
    # Wait for processing
    await asyncio.sleep(0.1)
    
    # Verify pattern handler received only matching messages
    assert len(pattern_messages) == 2
    assert pattern_messages[0][0] == "responses.123"
    assert pattern_messages[0][1]["data"]["id"] == "123"
    assert pattern_messages[1][0] == "responses.456"
    assert pattern_messages[1][1]["data"]["id"] == "456"


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
