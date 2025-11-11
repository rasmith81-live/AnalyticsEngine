"""
Supplier Quality Rating KPI Definition
"""

SUPPLIER_QUALITY_RATING = {
    "code": "SUPPLIER_QUALITY_RATING",
    "name": "Supplier Quality Rating",
    "display_name": "Supplier Quality Rating",
    "description": "The average score of suppliers",
    "formula": "Sum of Supplier Quality Scores / Number of Suppliers",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["QualityMetric", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
