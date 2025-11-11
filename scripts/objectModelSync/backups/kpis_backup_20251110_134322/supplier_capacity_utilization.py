"""
Supplier Capacity Utilization KPI Definition
"""

SUPPLIER_CAPACITY_UTILIZATION = {
    "code": "SUPPLIER_CAPACITY_UTILIZATION",
    "name": "Supplier Capacity Utilization",
    "display_name": "Supplier Capacity Utilization",
    "description": "The extent to which suppliers",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Lead", "Product", "PurchaseOrder", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
