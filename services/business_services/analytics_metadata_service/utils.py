"""
Utility functions for Analytics Models

Helper functions for working with the analytics hierarchy.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime


def calculate_kpi_status(
    current_value: Optional[float],
    target_value: Optional[float],
    threshold_warning: Optional[float],
    threshold_critical: Optional[float]
) -> str:
    """
    Calculate KPI status based on current value and thresholds.
    
    Args:
        current_value: Current KPI value
        target_value: Target KPI value
        threshold_warning: Warning threshold
        threshold_critical: Critical threshold
        
    Returns:
        Status string: 'normal', 'warning', 'critical', or 'unknown'
    """
    if current_value is None:
        return "unknown"
    
    if threshold_critical is not None and current_value <= threshold_critical:
        return "critical"
    
    if threshold_warning is not None and current_value <= threshold_warning:
        return "warning"
    
    return "normal"


def calculate_kpi_variance(
    current_value: Optional[float],
    target_value: Optional[float]
) -> Dict[str, Optional[float]]:
    """
    Calculate variance between current and target KPI values.
    
    Args:
        current_value: Current KPI value
        target_value: Target KPI value
        
    Returns:
        Dictionary with 'variance' and 'variance_percentage' keys
    """
    if current_value is None or target_value is None or target_value == 0:
        return {
            "variance": None,
            "variance_percentage": None
        }
    
    variance = current_value - target_value
    variance_percentage = (variance / target_value) * 100
    
    return {
        "variance": variance,
        "variance_percentage": variance_percentage
    }


def validate_hierarchy_path(
    industry_id: Optional[int] = None,
    module_id: Optional[int] = None,
    object_model_id: Optional[int] = None
) -> bool:
    """
    Validate that hierarchy path IDs are provided in correct order.
    
    Args:
        industry_id: Industry ID
        module_id: Module ID
        object_model_id: ObjectModel ID
        
    Returns:
        True if valid hierarchy path, False otherwise
    """
    # If module_id is provided, industry_id must be provided
    if module_id is not None and industry_id is None:
        return False
    
    # If object_model_id is provided, module_id must be provided
    if object_model_id is not None and module_id is None:
        return False
    
    return True


def build_hierarchy_dict(
    industry: Any,
    include_modules: bool = True,
    include_object_models: bool = True,
    include_objects: bool = True,
    include_kpis: bool = True
) -> Dict[str, Any]:
    """
    Build a complete hierarchy dictionary from an Industry object.
    
    Args:
        industry: Industry database object
        include_modules: Include modules in hierarchy
        include_object_models: Include object models in hierarchy
        include_objects: Include objects in hierarchy
        include_kpis: Include KPIs in hierarchy
        
    Returns:
        Dictionary representation of the hierarchy
    """
    result = {
        "id": industry.id,
        "name": industry.name,
        "code": industry.code,
        "description": industry.description,
        "is_active": industry.is_active,
        "created_at": industry.created_at.isoformat() if industry.created_at else None,
        "updated_at": industry.updated_at.isoformat() if industry.updated_at else None,
    }
    
    if include_modules and hasattr(industry, 'modules'):
        result["modules"] = []
        for module in industry.modules:
            module_dict = {
                "id": module.id,
                "name": module.name,
                "code": module.code,
                "description": module.description,
                "is_active": module.is_active,
                "display_order": module.display_order,
            }
            
            if include_object_models and hasattr(module, 'object_models'):
                module_dict["object_models"] = []
                for obj_model in module.object_models:
                    obj_model_dict = {
                        "id": obj_model.id,
                        "name": obj_model.name,
                        "code": obj_model.code,
                        "description": obj_model.description,
                        "is_active": obj_model.is_active,
                        "display_order": obj_model.display_order,
                    }
                    
                    if include_objects and hasattr(obj_model, 'objects'):
                        obj_model_dict["objects"] = [
                            {
                                "id": obj.id,
                                "name": obj.name,
                                "code": obj.code,
                                "data_values": obj.data_values,
                            }
                            for obj in obj_model.objects
                        ]
                    
                    if include_kpis and hasattr(obj_model, 'kpis'):
                        obj_model_dict["kpis"] = [
                            {
                                "id": kpi.id,
                                "name": kpi.name,
                                "code": kpi.code,
                                "current_value": kpi.current_value,
                                "target_value": kpi.target_value,
                                "unit_of_measure": kpi.unit_of_measure,
                                "category": kpi.category,
                                "status": calculate_kpi_status(
                                    kpi.current_value,
                                    kpi.target_value,
                                    kpi.threshold_warning,
                                    kpi.threshold_critical
                                ),
                            }
                            for kpi in obj_model.kpis
                        ]
                    
                    module_dict["object_models"].append(obj_model_dict)
            
            result["modules"].append(module_dict)
    
    return result


def generate_unique_code(prefix: str, existing_codes: List[str]) -> str:
    """
    Generate a unique code with the given prefix.
    
    Args:
        prefix: Code prefix
        existing_codes: List of existing codes to check against
        
    Returns:
        Unique code string
    """
    counter = 1
    while True:
        code = f"{prefix}_{counter:03d}"
        if code not in existing_codes:
            return code
        counter += 1


def validate_schema_definition(schema_def: Dict[str, Any]) -> tuple[bool, Optional[str]]:
    """
    Validate an object model schema definition.
    
    Args:
        schema_def: Schema definition dictionary
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(schema_def, dict):
        return False, "Schema definition must be a dictionary"
    
    if "fields" not in schema_def:
        return False, "Schema definition must contain 'fields' key"
    
    if not isinstance(schema_def["fields"], list):
        return False, "'fields' must be a list"
    
    if len(schema_def["fields"]) == 0:
        return False, "'fields' list cannot be empty"
    
    return True, None


def merge_metadata(
    existing_metadata: Optional[Dict[str, Any]],
    new_metadata: Optional[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Merge new metadata with existing metadata.
    
    Args:
        existing_metadata: Existing metadata dictionary
        new_metadata: New metadata to merge
        
    Returns:
        Merged metadata dictionary
    """
    result = existing_metadata.copy() if existing_metadata else {}
    
    if new_metadata:
        result.update(new_metadata)
    
    return result


def filter_active_items(items: List[Any]) -> List[Any]:
    """
    Filter a list to only include active items.
    
    Args:
        items: List of items with is_active attribute
        
    Returns:
        Filtered list of active items
    """
    return [item for item in items if getattr(item, 'is_active', True)]


def sort_by_display_order(items: List[Any]) -> List[Any]:
    """
    Sort items by their display_order attribute.
    
    Args:
        items: List of items with display_order attribute
        
    Returns:
        Sorted list
    """
    return sorted(items, key=lambda x: getattr(x, 'display_order', 0))


def get_kpi_summary(kpis: List[Any]) -> Dict[str, Any]:
    """
    Generate a summary of KPIs including counts by status.
    
    Args:
        kpis: List of KPI objects
        
    Returns:
        Summary dictionary with counts and statistics
    """
    total = len(kpis)
    active = len([k for k in kpis if k.is_active])
    
    status_counts = {
        "normal": 0,
        "warning": 0,
        "critical": 0,
        "unknown": 0
    }
    
    categories = {}
    
    for kpi in kpis:
        if kpi.is_active:
            status = calculate_kpi_status(
                kpi.current_value,
                kpi.target_value,
                kpi.threshold_warning,
                kpi.threshold_critical
            )
            status_counts[status] += 1
            
            if kpi.category:
                categories[kpi.category] = categories.get(kpi.category, 0) + 1
    
    return {
        "total": total,
        "active": active,
        "inactive": total - active,
        "status_counts": status_counts,
        "categories": categories
    }
