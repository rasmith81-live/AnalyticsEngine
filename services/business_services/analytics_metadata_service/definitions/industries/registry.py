"""
Industry Registry

Automatically discovers and registers all industry definitions.
"""

from analytics_models import Industry
from ..base_registry import BaseRegistry


class IndustryRegistry(BaseRegistry):
    """Registry for all industries."""
    
    def __init__(self):
        super().__init__(
            entity_class=Industry,
            module_path='definitions.industries'
        )


# Create singleton instance
industries = IndustryRegistry()


# Convenience functions
def get_industry(code: str) -> Industry:
    """Get industry by code."""
    return industries.get(code)


def get_all_industries() -> list[Industry]:
    """Get all industries."""
    return industries.get_all()


def list_industry_codes() -> list[str]:
    """List all industry codes."""
    return industries.list_codes()
