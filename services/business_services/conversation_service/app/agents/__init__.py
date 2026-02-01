# =============================================================================
# Conversation Service Agents Module
# Post-Migration: All agent runtime components now live in multi_agent_service
# =============================================================================
"""
Multi-Agent Framework Client for Conversation Service

This module provides access to the multi-agent architecture via the
multi_agent_service backend using Redis Streams for event-driven communication.

Communication Pattern:
- Commands → Redis Streams (reliable, persistent, consumer groups)
- Responses → Redis Pub/Sub (real-time, low latency)
- State → Redis Hash (session caching)

Local components:
- RedisAgentClient: Redis Streams/Pub/Sub client for multi_agent_service
- MultiAgentServiceClient: HTTP client (fallback/external API access)
- CircuitBreaker: Resilience for service calls
- Config: Feature flags and configuration

Remote components (via multi_agent_service):
- All 27 specialized agents
- Strategy Coordinator
- Agent Orchestrator
- Blackboard operations
- Contract enforcement
"""

from .config import (
    should_use_blackboard,
    get_agent_settings,
    should_enforce_contracts,
    get_multi_agent_service_url,
)
from .circuit_breaker import CircuitBreaker
from .multi_agent_client import MultiAgentServiceClient
from .redis_agent_client import RedisAgentClient, get_redis_agent_client

__all__ = [
    # Redis-based client (primary)
    "RedisAgentClient",
    "get_redis_agent_client",
    
    # HTTP client (fallback/external)
    "MultiAgentServiceClient",
    
    # Resilience
    "CircuitBreaker",
    
    # Configuration
    "should_use_blackboard",
    "get_agent_settings",
    "should_enforce_contracts",
    "get_multi_agent_service_url",
]
