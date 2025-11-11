"""
Supplier Quality Index KPI Definition
"""

SUPPLIER_QUALITY_INDEX = {
    "code": "SUPPLIER_QUALITY_INDEX",
    "name": "Supplier Quality Index",
    "display_name": "Supplier Quality Index",
    "description": "A composite score reflecting the quality of products or services provided by suppliers.",
    "formula": "Sum of Weighted Quality Metrics / Total Number of Quality Metrics",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Product", "PurchaseOrder", "QualityMetric", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
