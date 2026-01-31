# =============================================================================
# Event Schemas for Service Communication
# Standardized command/response formats for Redis Streams
# =============================================================================
"""
Pydantic schemas for event-driven service communication.

All internal service-to-service communication uses these schemas
for consistent message format and validation.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
import json
import uuid


class CommandType(Enum):
    """Standard command types for service operations."""
    # Entity operations
    CREATE_ENTITY = "create_entity"
    UPDATE_ENTITY = "update_entity"
    DELETE_ENTITY = "delete_entity"
    GET_ENTITY = "get_entity"
    LIST_ENTITIES = "list_entities"
    
    # KPI operations
    CREATE_KPI = "create_kpi"
    UPDATE_KPI = "update_kpi"
    DELETE_KPI = "delete_kpi"
    GET_KPI = "get_kpi"
    LIST_KPIS = "list_kpis"
    CALCULATE_KPI = "calculate_kpi"
    CALCULATE_BATCH = "calculate_batch"
    
    # Module operations
    CREATE_MODULE = "create_module"
    UPDATE_MODULE = "update_module"
    GET_MODULE = "get_module"
    LIST_MODULES = "list_modules"
    
    # Value chain operations
    CREATE_VALUE_CHAIN = "create_value_chain"
    UPDATE_VALUE_CHAIN = "update_value_chain"
    GET_VALUE_CHAIN = "get_value_chain"
    LIST_VALUE_CHAINS = "list_value_chains"
    
    # Connector operations
    FETCH_DATA = "fetch_data"
    TEST_CONNECTION = "test_connection"
    LIST_SOURCES = "list_sources"
    
    # Database operations
    EXECUTE_QUERY = "execute_query"
    EXECUTE_WRITE = "execute_write"
    
    # Ingestion operations
    PROCESS_DOCUMENT = "process_document"
    EXTRACT_ENTITIES = "extract_entities"
    ENRICH_METADATA = "enrich_metadata"
    
    # Agent operations (from Phase 20)
    CREATE_SESSION = "create_session"
    SEND_MESSAGE = "send_message"
    RUN_ANALYSIS = "run_analysis"
    FINALIZE_SESSION = "finalize_session"
    
    # Generic
    HEALTH_CHECK = "health_check"
    CUSTOM = "custom"


class ResponseType(Enum):
    """Standard response types for service operations."""
    # Success responses
    ENTITY_CREATED = "entity_created"
    ENTITY_UPDATED = "entity_updated"
    ENTITY_DELETED = "entity_deleted"
    ENTITY_DATA = "entity_data"
    ENTITY_LIST = "entity_list"
    
    KPI_CREATED = "kpi_created"
    KPI_UPDATED = "kpi_updated"
    KPI_DATA = "kpi_data"
    KPI_LIST = "kpi_list"
    KPI_RESULT = "kpi_result"
    BATCH_RESULT = "batch_result"
    
    MODULE_CREATED = "module_created"
    MODULE_DATA = "module_data"
    MODULE_LIST = "module_list"
    
    VALUE_CHAIN_CREATED = "value_chain_created"
    VALUE_CHAIN_DATA = "value_chain_data"
    VALUE_CHAIN_LIST = "value_chain_list"
    
    DATA_FETCHED = "data_fetched"
    CONNECTION_OK = "connection_ok"
    SOURCES_LIST = "sources_list"
    
    QUERY_RESULT = "query_result"
    WRITE_COMPLETE = "write_complete"
    
    DOCUMENT_PROCESSED = "document_processed"
    ENTITIES_EXTRACTED = "entities_extracted"
    METADATA_ENRICHED = "metadata_enriched"
    
    # Agent responses
    SESSION_CREATED = "session_created"
    MESSAGE_RESPONSE = "message_response"
    ANALYSIS_RESULT = "analysis_result"
    SESSION_FINALIZED = "session_finalized"
    
    # Streaming
    STREAM_CHUNK = "stream_chunk"
    STREAM_COMPLETE = "stream_complete"
    
    # Status
    HEALTH_OK = "health_ok"
    ERROR = "error"
    ACK = "ack"


@dataclass
class StreamConfig:
    """Configuration for a service stream."""
    stream_name: str
    consumer_group: str
    max_len: int = 10000
    
    @classmethod
    def for_service(cls, service_name: str, operation: str = "commands") -> "StreamConfig":
        """Create stream config for a service."""
        prefix = service_name.replace("_service", "").replace("business_", "")
        return cls(
            stream_name=f"{prefix}:{operation}",
            consumer_group=f"{prefix}_consumers"
        )


@dataclass
class ServiceCommand:
    """
    Command message sent between services via Redis Streams.
    
    Attributes:
        command_id: Unique identifier for correlation
        command_type: Type of operation requested
        source_service: Service sending the command
        target_service: Service that should process command
        session_id: Optional session for tracing
        payload: Command-specific data
        reply_channel: Pub/Sub channel for response
        timestamp: When command was created
        ttl_seconds: Time-to-live for response waiting
    """
    command_id: str
    command_type: CommandType
    source_service: str
    target_service: str
    payload: Dict[str, Any]
    reply_channel: str
    session_id: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    ttl_seconds: int = 30
    
    @classmethod
    def create(
        cls,
        command_type: CommandType,
        source_service: str,
        target_service: str,
        payload: Dict[str, Any],
        session_id: Optional[str] = None,
        ttl_seconds: int = 30
    ) -> "ServiceCommand":
        """Factory method to create a new command."""
        command_id = str(uuid.uuid4())
        return cls(
            command_id=command_id,
            command_type=command_type,
            source_service=source_service,
            target_service=target_service,
            payload=payload,
            reply_channel=f"responses:{command_id}",
            session_id=session_id,
            ttl_seconds=ttl_seconds
        )
    
    def to_stream_dict(self) -> Dict[str, str]:
        """Convert to Redis stream entry (all values must be strings)."""
        return {
            "command_id": self.command_id,
            "command_type": self.command_type.value,
            "source_service": self.source_service,
            "target_service": self.target_service,
            "session_id": self.session_id or "",
            "payload": json.dumps(self.payload),
            "reply_channel": self.reply_channel,
            "timestamp": self.timestamp,
            "ttl_seconds": str(self.ttl_seconds)
        }
    
    @classmethod
    def from_stream_dict(cls, data: Dict[str, str]) -> "ServiceCommand":
        """Create from Redis stream entry."""
        return cls(
            command_id=data["command_id"],
            command_type=CommandType(data["command_type"]),
            source_service=data["source_service"],
            target_service=data["target_service"],
            session_id=data.get("session_id") or None,
            payload=json.loads(data.get("payload", "{}")),
            reply_channel=data["reply_channel"],
            timestamp=data.get("timestamp", ""),
            ttl_seconds=int(data.get("ttl_seconds", "30"))
        )


@dataclass
class ServiceResponse:
    """
    Response message sent back via Redis Pub/Sub.
    
    Attributes:
        command_id: Correlates to original command
        response_type: Type of response
        source_service: Service sending response
        payload: Response data
        success: Whether operation succeeded
        error: Error message if failed
        timestamp: When response was created
    """
    command_id: str
    response_type: ResponseType
    source_service: str
    payload: Dict[str, Any]
    success: bool = True
    error: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    @classmethod
    def success_response(
        cls,
        command: ServiceCommand,
        response_type: ResponseType,
        payload: Dict[str, Any],
        source_service: str
    ) -> "ServiceResponse":
        """Create a success response for a command."""
        return cls(
            command_id=command.command_id,
            response_type=response_type,
            source_service=source_service,
            payload=payload,
            success=True
        )
    
    @classmethod
    def error_response(
        cls,
        command: ServiceCommand,
        error: str,
        source_service: str
    ) -> "ServiceResponse":
        """Create an error response for a command."""
        return cls(
            command_id=command.command_id,
            response_type=ResponseType.ERROR,
            source_service=source_service,
            payload={},
            success=False,
            error=error
        )
    
    def to_json(self) -> str:
        """Serialize for pub/sub."""
        return json.dumps({
            "command_id": self.command_id,
            "response_type": self.response_type.value,
            "source_service": self.source_service,
            "payload": self.payload,
            "success": self.success,
            "error": self.error,
            "timestamp": self.timestamp
        })
    
    @classmethod
    def from_json(cls, data: str) -> "ServiceResponse":
        """Deserialize from pub/sub."""
        d = json.loads(data)
        return cls(
            command_id=d["command_id"],
            response_type=ResponseType(d["response_type"]),
            source_service=d["source_service"],
            payload=d.get("payload", {}),
            success=d.get("success", True),
            error=d.get("error"),
            timestamp=d.get("timestamp", "")
        )


# Stream naming utilities
def get_stream_name(service: str, operation: str = "commands") -> str:
    """Get standardized stream name for a service."""
    prefix = service.replace("_service", "").replace("business_", "")
    return f"{prefix}:{operation}"


def get_consumer_group(service: str) -> str:
    """Get standardized consumer group name for a service."""
    prefix = service.replace("_service", "").replace("business_", "")
    return f"{prefix}_consumers"


def get_response_channel(command_id: str) -> str:
    """Get response channel for a command."""
    return f"responses:{command_id}"
