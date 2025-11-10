"""
ValueChain Registry

Automatically discovers and registers all value chain definitions.
"""

from analytics_models import ValueChain
from ..base_registry import BaseRegistry


class ValueChainRegistry(BaseRegistry):
    """Registry for all value chains."""
    
    def __init__(self):
        super().__init__(
            entity_class=ValueChain,
            module_path='definitions.value_chains'
        )


# Create singleton instance
value_chains = ValueChainRegistry()


# Convenience functions
def get_value_chain(code: str) -> ValueChain:
    """Get value chain by code."""
    return value_chains.get(code)


def get_all_value_chains() -> list[ValueChain]:
    """Get all value chains."""
    return value_chains.get_all()


def list_value_chain_codes() -> list[str]:
    """List all value chain codes."""
    return value_chains.list_codes()
