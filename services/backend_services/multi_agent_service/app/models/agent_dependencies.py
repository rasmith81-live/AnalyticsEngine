# =============================================================================
# Agent Dependencies Model
# Phase 18: Microsoft Best Practices Integration
# Reference: https://developer.microsoft.com/blog/designing-multi-agent-intelligence
# =============================================================================
"""
Dependency and impact tracking for agents.

Tracks dependencies on external resources (knowledge bases, services)
to detect breaking changes before they impact production.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Any
import hashlib
import logging

logger = logging.getLogger(__name__)


@dataclass
class DependencyChange:
    """Represents a detected change in a dependency."""
    dependency_name: str
    dependency_type: str  # knowledge_base, external_service, upstream_agent
    previous_hash: Optional[str]
    current_hash: str
    detected_at: datetime
    severity: str = "warning"  # info, warning, critical
    description: str = ""
    
    def to_dict(self) -> Dict:
        return {
            "dependency_name": self.dependency_name,
            "dependency_type": self.dependency_type,
            "previous_hash": self.previous_hash,
            "current_hash": self.current_hash,
            "detected_at": self.detected_at.isoformat(),
            "severity": self.severity,
            "description": self.description,
        }


@dataclass
class AgentDependencies:
    """
    Track agent dependencies for impact analysis.
    
    Detects changes in dependencies that might affect agent behavior.
    """
    agent_role: str
    knowledge_bases: List[str] = field(default_factory=list)
    external_services: List[str] = field(default_factory=list)
    upstream_agents: List[str] = field(default_factory=list)
    downstream_agents: List[str] = field(default_factory=list)
    tools: List[str] = field(default_factory=list)
    last_verified: Optional[datetime] = None
    version_hashes: Dict[str, str] = field(default_factory=dict)
    
    def compute_hash(self, content: Any) -> str:
        """Compute a hash for content to detect changes."""
        if isinstance(content, str):
            data = content.encode()
        elif isinstance(content, bytes):
            data = content
        else:
            data = str(content).encode()
        return hashlib.sha256(data).hexdigest()[:16]
    
    def update_hash(self, resource_name: str, content: Any) -> Optional[DependencyChange]:
        """
        Update the hash for a resource and detect changes.
        
        Returns a DependencyChange if a change was detected, None otherwise.
        """
        new_hash = self.compute_hash(content)
        previous_hash = self.version_hashes.get(resource_name)
        
        if previous_hash is not None and previous_hash != new_hash:
            # Change detected
            dep_type = self._get_dependency_type(resource_name)
            change = DependencyChange(
                dependency_name=resource_name,
                dependency_type=dep_type,
                previous_hash=previous_hash,
                current_hash=new_hash,
                detected_at=datetime.utcnow(),
                severity=self._determine_severity(dep_type),
                description=f"Content changed for {resource_name}"
            )
            
            logger.warning(
                f"Dependency change detected for {self.agent_role}: "
                f"{resource_name} ({dep_type})"
            )
            
            self.version_hashes[resource_name] = new_hash
            return change
        
        # Update hash (no change or first time)
        self.version_hashes[resource_name] = new_hash
        return None
    
    def _get_dependency_type(self, resource_name: str) -> str:
        """Determine the type of a dependency."""
        if resource_name in self.knowledge_bases:
            return "knowledge_base"
        elif resource_name in self.external_services:
            return "external_service"
        elif resource_name in self.upstream_agents:
            return "upstream_agent"
        elif resource_name in self.tools:
            return "tool"
        return "unknown"
    
    def _determine_severity(self, dep_type: str) -> str:
        """Determine severity based on dependency type."""
        severity_map = {
            "knowledge_base": "warning",
            "external_service": "critical",
            "upstream_agent": "warning",
            "tool": "warning",
            "unknown": "info"
        }
        return severity_map.get(dep_type, "info")
    
    def check_all_dependencies(
        self,
        current_states: Dict[str, Any]
    ) -> List[DependencyChange]:
        """
        Check all dependencies for changes.
        
        Args:
            current_states: Dict mapping resource names to their current content/state
            
        Returns:
            List of detected changes
        """
        changes = []
        
        for resource_name, content in current_states.items():
            change = self.update_hash(resource_name, content)
            if change:
                changes.append(change)
        
        self.last_verified = datetime.utcnow()
        return changes
    
    def add_dependency(
        self,
        name: str,
        dep_type: str,
        initial_content: Any = None
    ):
        """Add a dependency to track."""
        if dep_type == "knowledge_base":
            if name not in self.knowledge_bases:
                self.knowledge_bases.append(name)
        elif dep_type == "external_service":
            if name not in self.external_services:
                self.external_services.append(name)
        elif dep_type == "upstream_agent":
            if name not in self.upstream_agents:
                self.upstream_agents.append(name)
        elif dep_type == "tool":
            if name not in self.tools:
                self.tools.append(name)
        
        if initial_content is not None:
            self.version_hashes[name] = self.compute_hash(initial_content)
    
    def remove_dependency(self, name: str):
        """Remove a dependency from tracking."""
        for dep_list in [
            self.knowledge_bases,
            self.external_services,
            self.upstream_agents,
            self.tools
        ]:
            if name in dep_list:
                dep_list.remove(name)
        
        self.version_hashes.pop(name, None)
    
    def get_impact_report(self) -> Dict:
        """Get an impact report for this agent's dependencies."""
        return {
            "agent_role": self.agent_role,
            "last_verified": self.last_verified.isoformat() if self.last_verified else None,
            "dependency_counts": {
                "knowledge_bases": len(self.knowledge_bases),
                "external_services": len(self.external_services),
                "upstream_agents": len(self.upstream_agents),
                "downstream_agents": len(self.downstream_agents),
                "tools": len(self.tools),
            },
            "tracked_resources": list(self.version_hashes.keys()),
        }
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "agent_role": self.agent_role,
            "knowledge_bases": self.knowledge_bases,
            "external_services": self.external_services,
            "upstream_agents": self.upstream_agents,
            "downstream_agents": self.downstream_agents,
            "tools": self.tools,
            "last_verified": self.last_verified.isoformat() if self.last_verified else None,
            "version_hashes": self.version_hashes,
        }


class DependencyRegistry:
    """Registry for managing agent dependencies."""
    
    def __init__(self):
        self._dependencies: Dict[str, AgentDependencies] = {}
    
    def register(self, agent_role: str) -> AgentDependencies:
        """Register or get dependencies for an agent."""
        if agent_role not in self._dependencies:
            self._dependencies[agent_role] = AgentDependencies(agent_role=agent_role)
        return self._dependencies[agent_role]
    
    def get(self, agent_role: str) -> Optional[AgentDependencies]:
        """Get dependencies for an agent."""
        return self._dependencies.get(agent_role)
    
    def check_all(
        self,
        current_states: Dict[str, Dict[str, Any]]
    ) -> Dict[str, List[DependencyChange]]:
        """
        Check all agents for dependency changes.
        
        Args:
            current_states: Dict mapping agent_role to resource states
            
        Returns:
            Dict mapping agent_role to list of changes
        """
        all_changes = {}
        
        for agent_role, deps in self._dependencies.items():
            states = current_states.get(agent_role, {})
            changes = deps.check_all_dependencies(states)
            if changes:
                all_changes[agent_role] = changes
        
        return all_changes
    
    def get_downstream_impact(
        self,
        changed_agent: str
    ) -> List[str]:
        """Get list of agents that depend on a changed agent."""
        impacted = []
        
        for agent_role, deps in self._dependencies.items():
            if changed_agent in deps.upstream_agents:
                impacted.append(agent_role)
        
        return impacted
    
    def to_dict(self) -> Dict:
        """Convert registry to dictionary."""
        return {
            agent_role: deps.to_dict()
            for agent_role, deps in self._dependencies.items()
        }


# Global registry instance
_dependency_registry: Optional[DependencyRegistry] = None


def get_dependency_registry() -> DependencyRegistry:
    """Get the global dependency registry instance."""
    global _dependency_registry
    if _dependency_registry is None:
        _dependency_registry = DependencyRegistry()
    return _dependency_registry
