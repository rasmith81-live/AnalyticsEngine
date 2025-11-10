"""
Module Registry

Automatically discovers and registers all module definitions.
"""

from analytics_models import Module
from ..base_registry import BaseRegistry


class ModuleRegistry(BaseRegistry):
    """Registry for all modules."""
    
    def __init__(self):
        super().__init__(
            entity_class=Module,
            module_path='definitions.modules'
        )


# Create singleton instance
modules = ModuleRegistry()


# Convenience functions
def get_module(code: str) -> Module:
    """Get module by code."""
    return modules.get(code)


def get_all_modules() -> list[Module]:
    """Get all modules."""
    return modules.get_all()


def list_module_codes() -> list[str]:
    """List all module codes."""
    return modules.list_codes()
