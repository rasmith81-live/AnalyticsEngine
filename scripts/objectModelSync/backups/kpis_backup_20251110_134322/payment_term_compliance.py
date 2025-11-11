"""
Payment Term Compliance KPI Definition
"""

PAYMENT_TERM_COMPLIANCE = {
    "code": "PAYMENT_TERM_COMPLIANCE",
    "name": "Payment Term Compliance",
    "display_name": "Payment Term Compliance",
    "description": "The rate at which payments to suppliers are made within the agreed-upon payment terms.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Payment", "PurchaseOrder", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
