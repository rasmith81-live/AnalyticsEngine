# =============================================================================
# Models Package
# Phase 18: Microsoft Best Practices Integration
# =============================================================================
"""Models for multi-agent service governance and versioning."""

from .agent_version import (
    AgentVersionState,
    AgentVersionTransition,
    AgentVersion,
    AgentRegistry,
    get_agent_registry
)

from .agent_dependencies import (
    DependencyChange,
    AgentDependencies,
    DependencyRegistry,
    get_dependency_registry
)

__all__ = [
    # Version management
    "AgentVersionState",
    "AgentVersionTransition",
    "AgentVersion",
    "AgentRegistry",
    "get_agent_registry",
    # Dependency tracking
    "DependencyChange",
    "AgentDependencies",
    "DependencyRegistry",
    "get_dependency_registry",
]
