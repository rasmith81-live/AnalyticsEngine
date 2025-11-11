"""
Vendor Risk Management Efficiency KPI Definition
"""

VENDOR_RISK_MANAGEMENT_EFFICIENCY = {
    "code": "VENDOR_RISK_MANAGEMENT_EFFICIENCY",
    "name": "Vendor Risk Management Efficiency",
    "display_name": "Vendor Risk Management Efficiency",
    "description": "The efficiency of the vendor risk management process, indicating the ability to identify and mitigate risks posed by third-party vendors.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["PurchaseOrder", "Supplier"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
