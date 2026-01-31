"""
Configuration for conversation_service agent integration with multi_agent_service.

Feature flags and settings for gradual rollout of blackboard-based coordination.
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from functools import lru_cache


class AgentIntegrationSettings(BaseSettings):
    """Settings for multi-agent service integration."""
    
    # Multi-agent service connection
    MULTI_AGENT_SERVICE_URL: str = os.getenv(
        "MULTI_AGENT_SERVICE_URL", 
        "http://multi_agent_service:8000"
    )
    MULTI_AGENT_SERVICE_TIMEOUT: float = float(os.getenv(
        "MULTI_AGENT_SERVICE_TIMEOUT", 
        "30.0"
    ))
    
    # Feature flags for gradual rollout
    MULTI_AGENT_SERVICE_ENABLED: bool = os.getenv(
        "MULTI_AGENT_SERVICE_ENABLED", 
        "false"
    ).lower() == "true"
    
    BLACKBOARD_ROLLOUT_PERCENT: int = int(os.getenv(
        "BLACKBOARD_ROLLOUT_PERCENT", 
        "0"
    ))
    
    CONTRACT_ENFORCEMENT_ENABLED: bool = os.getenv(
        "CONTRACT_ENFORCEMENT_ENABLED", 
        "false"
    ).lower() == "true"
    
    PEER_REVIEW_REQUIRED: bool = os.getenv(
        "PEER_REVIEW_REQUIRED", 
        "true"
    ).lower() == "true"
    
    # Circuit breaker settings
    CIRCUIT_BREAKER_FAILURE_THRESHOLD: int = int(os.getenv(
        "CIRCUIT_BREAKER_FAILURE_THRESHOLD", 
        "3"
    ))
    
    CIRCUIT_BREAKER_RECOVERY_TIMEOUT: int = int(os.getenv(
        "CIRCUIT_BREAKER_RECOVERY_TIMEOUT", 
        "60"
    ))
    
    # Degraded mode settings
    FALLBACK_TO_LOCAL_ENABLED: bool = os.getenv(
        "FALLBACK_TO_LOCAL_ENABLED", 
        "true"
    ).lower() == "true"
    
    ANNOUNCE_DEGRADED_MODE: bool = os.getenv(
        "ANNOUNCE_DEGRADED_MODE", 
        "true"
    ).lower() == "true"
    
    class Config:
        env_prefix = ""
        case_sensitive = True


@lru_cache()
def get_agent_settings() -> AgentIntegrationSettings:
    """Get cached agent integration settings."""
    return AgentIntegrationSettings()


def should_use_blackboard(session_id: str) -> bool:
    """
    Determine if a session should use blackboard-based coordination.
    
    Uses consistent hashing on session_id for predictable routing.
    This ensures the same session always gets the same behavior.
    
    Args:
        session_id: The session identifier
        
    Returns:
        True if blackboard should be used, False for legacy coordination
    """
    settings = get_agent_settings()
    
    if not settings.MULTI_AGENT_SERVICE_ENABLED:
        return False
    
    if settings.BLACKBOARD_ROLLOUT_PERCENT >= 100:
        return True
    
    if settings.BLACKBOARD_ROLLOUT_PERCENT <= 0:
        return False
    
    # Consistent hash for predictable routing
    session_hash = hash(session_id) % 100
    return session_hash < settings.BLACKBOARD_ROLLOUT_PERCENT


def should_enforce_contracts() -> bool:
    """Check if contract enforcement is enabled."""
    settings = get_agent_settings()
    return settings.CONTRACT_ENFORCEMENT_ENABLED


def should_require_peer_review() -> bool:
    """Check if peer review is required."""
    settings = get_agent_settings()
    return settings.PEER_REVIEW_REQUIRED


def get_multi_agent_service_url() -> str:
    """Get the multi-agent service URL."""
    settings = get_agent_settings()
    return settings.MULTI_AGENT_SERVICE_URL
