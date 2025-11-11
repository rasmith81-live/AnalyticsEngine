"""
Return Rate due to Packing Errors KPI Definition
"""

RETURN_RATE_DUE_TO_PACKING_ERRORS = {
    "code": "RETURN_RATE_DUE_TO_PACKING_ERRORS",
    "name": "Return Rate due to Packing Errors",
    "display_name": "Return Rate due to Packing Errors",
    "description": "The percentage of products returned due to errors in packing, serving as an indicator of the quality and accuracy of packing processes.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Product", "QualityMetric", "Return"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
