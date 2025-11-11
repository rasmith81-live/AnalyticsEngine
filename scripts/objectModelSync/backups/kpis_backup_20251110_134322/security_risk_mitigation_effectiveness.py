"""
Security Risk Mitigation Effectiveness KPI Definition
"""

SECURITY_RISK_MITIGATION_EFFECTIVENESS = {
    "code": "SECURITY_RISK_MITIGATION_EFFECTIVENESS",
    "name": "Security Risk Mitigation Effectiveness",
    "display_name": "Security Risk Mitigation Effectiveness",
    "description": "The effectiveness of implemented measures to reduce supply chain security risks, measured by the reduction in identified risks over time.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
