# =============================================================================
# Multi-Agent Service Configuration Package
# =============================================================================
"""
Configuration modules for multi_agent_service.

Components:
- ClientFramework: Industry-agnostic client framework configuration
- FrameworkLoader: Loads client config from metadata service
"""

from .client_framework import (
    ClientConfiguration,
    ClientFramework,
    FrameworkLoader,
    FrameworkType,
    KPITemplate,
    ModuleDefinition,
    RelationshipDefinition,
)

__all__ = [
    "ClientConfiguration",
    "ClientFramework",
    "FrameworkLoader",
    "FrameworkType",
    "KPITemplate",
    "ModuleDefinition",
    "RelationshipDefinition",
]
