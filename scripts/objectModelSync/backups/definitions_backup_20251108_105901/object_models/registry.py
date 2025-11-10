"""
ObjectModel Registry

Automatically discovers and registers all object model definitions.
"""

from analytics_models import ObjectModel
from ..base_registry import BaseRegistry


class ObjectModelRegistry(BaseRegistry):
    """Registry for all object models."""
    
    def __init__(self):
        super().__init__(
            entity_class=ObjectModel,
            module_path='definitions.object_models'
        )


# Create singleton instance
object_models = ObjectModelRegistry()


# Convenience functions
def get_object_model(code: str) -> ObjectModel:
    """Get object model by code."""
    return object_models.get(code)


def get_all_object_models() -> list[ObjectModel]:
    """Get all object models."""
    return object_models.get_all()


def list_object_model_codes() -> list[str]:
    """List all object model codes."""
    return object_models.list_codes()
