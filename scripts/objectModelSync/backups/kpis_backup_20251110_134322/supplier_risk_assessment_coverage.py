"""
Supplier Risk Assessment Coverage KPI Definition
"""

SUPPLIER_RISK_ASSESSMENT_COVERAGE = {
    "code": "SUPPLIER_RISK_ASSESSMENT_COVERAGE",
    "name": "Supplier Risk Assessment Coverage",
    "display_name": "Supplier Risk Assessment Coverage",
    "description": "The extent to which the supply base has been assessed for risks related to social, environmental, and economic factors as per ISO 20400.",
    "formula": "",
    "unit": "count",
    "category": "Iso 20400",
    "metadata_": {
        "modules": ["ISO_20400"],
        "required_objects": ["Supplier"]
    },
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
}
