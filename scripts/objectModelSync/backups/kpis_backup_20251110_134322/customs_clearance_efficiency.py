"""
Customs Clearance Efficiency KPI Definition
"""

CUSTOMS_CLEARANCE_EFFICIENCY = {
    "code": "CUSTOMS_CLEARANCE_EFFICIENCY",
    "name": "Customs Clearance Efficiency",
    "display_name": "Customs Clearance Efficiency",
    "description": "The average time it takes for goods to clear customs, reflecting the effectiveness of security procedures in international trade.",
    "formula": "Sum of Customs Clearance Times / Total Number of Shipments",
    "unit": "count",
    "category": "Iso 28000",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Shipment"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
