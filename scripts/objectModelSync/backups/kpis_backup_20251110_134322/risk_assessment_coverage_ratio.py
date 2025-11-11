"""
Risk Assessment Coverage Ratio KPI Definition
"""

RISK_ASSESSMENT_COVERAGE_RATIO = {
    "code": "RISK_ASSESSMENT_COVERAGE_RATIO",
    "name": "Risk Assessment Coverage Ratio",
    "display_name": "Risk Assessment Coverage Ratio",
    "description": "The proportion of the supply chain that has undergone risk assessments, showing the extent of proactive security risk management.",
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
