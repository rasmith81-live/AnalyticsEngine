"""
Supplier Collaboration Index KPI Definition
"""

SUPPLIER_COLLABORATION_INDEX = {
    "code": "SUPPLIER_COLLABORATION_INDEX",
    "name": "Supplier Collaboration Index",
    "display_name": "Supplier Collaboration Index",
    "description": "A measure of the quality and depth of collaborative efforts between the organization and its suppliers, impacting innovation and performance.",
    "formula": "Sum of collaboration scores / Number of Suppliers",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["QualityMetric", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
