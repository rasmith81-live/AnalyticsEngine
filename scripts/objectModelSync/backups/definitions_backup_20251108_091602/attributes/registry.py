"""
Attribute Registry with Dynamic ObjectModel Linking
"""

from analytics_models import ObjectAttribute
from ..base_registry import BaseRegistry


class AttributeRegistry(BaseRegistry):
    """Registry for all object attributes with dynamic linking."""
    
    def __init__(self):
        super().__init__(
            entity_class=ObjectAttribute,
            module_path='definitions.attributes'
        )
    
    def link_to_object_models(self):
        """
        Dynamically link attributes to their object models.
        
        Each attribute declares its object_model_code, and we link it.
        """
        from ..object_models.registry import get_object_model
        
        for attribute in self.get_all():
            # Get object model code from attribute
            om_code = getattr(attribute, 'object_model_code', None)
            if not om_code:
                # Try metadata as fallback
                om_code = attribute.metadata_.get('object_model') if attribute.metadata_ else None
            
            if om_code:
                object_model = get_object_model(om_code)
                if object_model:
                    # Add attribute to object model if not already there
                    if attribute not in object_model.attributes:
                        object_model.attributes.append(attribute)


# Create singleton instance
attributes = AttributeRegistry()


# Convenience functions
def get_attribute(code: str) -> ObjectAttribute:
    """Get attribute by code."""
    return attributes.get(code)


def get_all_attributes() -> list[ObjectAttribute]:
    """Get all attributes."""
    return attributes.get_all()


def list_attribute_codes() -> list[str]:
    """List all attribute codes."""
    return attributes.list_codes()
