"""
Vendor Performance KPI Definition
"""

VENDOR_PERFORMANCE = {
    "code": "VENDOR_PERFORMANCE",
    "name": "Vendor Performance",
    "display_name": "Vendor Performance",
    "description": "The overall performance of the company",
    "formula": "Qualitative and Quantitative Score based on Predefined Performance Criteria",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Delivery", "Product", "PurchaseOrder", "QualityMetric", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
