"""
Freight Bill Accuracy KPI Definition
"""

FREIGHT_BILL_ACCURACY = {
    "code": "FREIGHT_BILL_ACCURACY",
    "name": "Freight Bill Accuracy",
    "display_name": "Freight Bill Accuracy",
    "description": "The accuracy of freight costs and billing, reducing discrepancies and overcharges in transportation expenses.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
