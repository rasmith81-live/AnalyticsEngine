"""
Invoice Error Rate KPI Definition
"""

INVOICE_ERROR_RATE = {
    "code": "INVOICE_ERROR_RATE",
    "name": "Invoice Error Rate",
    "display_name": "Invoice Error Rate",
    "description": "The percentage of invoices that contain errors, requiring additional time and resources to resolve.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Invoice"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
