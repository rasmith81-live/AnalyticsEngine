# =============================================================================
# Agent Versioning Model
# Phase 18: Microsoft Best Practices Integration
# Reference: https://developer.microsoft.com/blog/designing-multi-agent-intelligence
# =============================================================================
"""
Agent versioning state machine for lifecycle management.

Prevents breaking changes from impacting production by enforcing
formal version states and transitions.
"""

from enum import Enum
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class AgentVersionState(str, Enum):
    """Agent lifecycle states for versioning."""
    DRAFT = "draft"              # In development
    TESTING = "testing"          # Under validation
    PUBLISHED = "published"      # Production ready
    DEPRECATED = "deprecated"    # Scheduled for removal
    ARCHIVED = "archived"        # No longer available


class AgentVersionTransition:
    """Valid state transitions for agent versions."""
    
    VALID_TRANSITIONS: Set[Tuple[str, str]] = {
        ("draft", "testing"),
        ("testing", "published"),
        ("testing", "draft"),        # Failed testing
        ("published", "deprecated"),
        ("deprecated", "archived"),
        ("deprecated", "published"),  # Rollback from deprecation
    }
    
    @classmethod
    def is_valid(cls, from_state: str, to_state: str) -> bool:
        """Check if a transition is valid."""
        return (from_state, to_state) in cls.VALID_TRANSITIONS
    
    @classmethod
    def get_allowed_transitions(cls, current_state: str) -> List[str]:
        """Get list of states that can be transitioned to from current state."""
        return [
            to_state 
            for from_state, to_state in cls.VALID_TRANSITIONS 
            if from_state == current_state
        ]


@dataclass
class AgentVersion:
    """Represents a specific version of an agent."""
    agent_role: str
    version: str
    state: AgentVersionState = AgentVersionState.DRAFT
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    published_at: Optional[datetime] = None
    deprecated_at: Optional[datetime] = None
    changelog: str = ""
    metadata: Dict = field(default_factory=dict)
    
    def transition_to(self, new_state: AgentVersionState) -> bool:
        """
        Attempt to transition to a new state.
        
        Returns True if successful, raises ValueError if invalid.
        """
        current = self.state.value
        target = new_state.value
        
        if not AgentVersionTransition.is_valid(current, target):
            allowed = AgentVersionTransition.get_allowed_transitions(current)
            raise ValueError(
                f"Invalid transition: {current} → {target}. "
                f"Allowed transitions: {allowed}"
            )
        
        # Record timestamps for specific transitions
        if new_state == AgentVersionState.PUBLISHED:
            self.published_at = datetime.utcnow()
        elif new_state == AgentVersionState.DEPRECATED:
            self.deprecated_at = datetime.utcnow()
        
        self.state = new_state
        self.updated_at = datetime.utcnow()
        
        logger.info(f"Agent {self.agent_role} v{self.version}: {current} → {target}")
        return True
    
    def can_transition_to(self, new_state: AgentVersionState) -> bool:
        """Check if a transition is allowed without performing it."""
        return AgentVersionTransition.is_valid(self.state.value, new_state.value)
    
    def is_active(self) -> bool:
        """Check if this version is active (published)."""
        return self.state == AgentVersionState.PUBLISHED
    
    def is_available(self) -> bool:
        """Check if this version is available for use."""
        return self.state in (
            AgentVersionState.PUBLISHED,
            AgentVersionState.DEPRECATED  # Still usable during deprecation
        )
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "agent_role": self.agent_role,
            "version": self.version,
            "state": self.state.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "published_at": self.published_at.isoformat() if self.published_at else None,
            "deprecated_at": self.deprecated_at.isoformat() if self.deprecated_at else None,
            "changelog": self.changelog,
            "metadata": self.metadata,
        }


@dataclass
class AgentRegistry:
    """
    Registry for managing agent versions.
    
    Supports multiple versions per agent with lifecycle management.
    """
    agents: Dict[str, Dict[str, AgentVersion]] = field(default_factory=dict)
    
    def register_version(
        self,
        agent_role: str,
        version: str,
        changelog: str = "",
        metadata: Dict = None
    ) -> AgentVersion:
        """Register a new version of an agent."""
        if agent_role not in self.agents:
            self.agents[agent_role] = {}
        
        if version in self.agents[agent_role]:
            raise ValueError(f"Version {version} already exists for {agent_role}")
        
        agent_version = AgentVersion(
            agent_role=agent_role,
            version=version,
            changelog=changelog,
            metadata=metadata or {}
        )
        
        self.agents[agent_role][version] = agent_version
        logger.info(f"Registered agent {agent_role} version {version}")
        
        return agent_version
    
    def get_version(self, agent_role: str, version: str) -> Optional[AgentVersion]:
        """Get a specific version of an agent."""
        return self.agents.get(agent_role, {}).get(version)
    
    def get_published_version(self, agent_role: str) -> Optional[AgentVersion]:
        """Get the currently published version of an agent."""
        for version in self.agents.get(agent_role, {}).values():
            if version.state == AgentVersionState.PUBLISHED:
                return version
        return None
    
    def get_all_versions(self, agent_role: str) -> List[AgentVersion]:
        """Get all versions of an agent."""
        return list(self.agents.get(agent_role, {}).values())
    
    def get_available_versions(self, agent_role: str) -> List[AgentVersion]:
        """Get all available (usable) versions of an agent."""
        return [
            v for v in self.agents.get(agent_role, {}).values()
            if v.is_available()
        ]
    
    def promote_to_testing(self, agent_role: str, version: str) -> bool:
        """Promote a draft version to testing."""
        v = self.get_version(agent_role, version)
        if v:
            return v.transition_to(AgentVersionState.TESTING)
        return False
    
    def publish_version(self, agent_role: str, version: str) -> bool:
        """Publish a tested version."""
        v = self.get_version(agent_role, version)
        if v:
            # Deprecate current published version
            current = self.get_published_version(agent_role)
            if current and current.version != version:
                current.transition_to(AgentVersionState.DEPRECATED)
            return v.transition_to(AgentVersionState.PUBLISHED)
        return False
    
    def deprecate_version(self, agent_role: str, version: str) -> bool:
        """Deprecate a published version."""
        v = self.get_version(agent_role, version)
        if v:
            return v.transition_to(AgentVersionState.DEPRECATED)
        return False
    
    def archive_version(self, agent_role: str, version: str) -> bool:
        """Archive a deprecated version."""
        v = self.get_version(agent_role, version)
        if v:
            return v.transition_to(AgentVersionState.ARCHIVED)
        return False
    
    def to_dict(self) -> Dict:
        """Convert registry to dictionary."""
        return {
            agent_role: {
                version: v.to_dict() 
                for version, v in versions.items()
            }
            for agent_role, versions in self.agents.items()
        }


# Global registry instance
_agent_registry: Optional[AgentRegistry] = None


def get_agent_registry() -> AgentRegistry:
    """Get the global agent registry instance."""
    global _agent_registry
    if _agent_registry is None:
        _agent_registry = AgentRegistry()
    return _agent_registry
