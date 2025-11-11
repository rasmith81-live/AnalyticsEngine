"""
Qualified Leads per Month KPI Definition
"""

QUALIFIED_LEADS_PER_MONTH = {
    "code": "QUALIFIED_LEADS_PER_MONTH",
    "name": "Qualified Leads per Month",
    "display_name": "Qualified Leads per Month",
    "description": "The number of leads that meet certain criteria set by the sales team, indicating a higher probability of converting into customers.",
    "formula": "Total Number of Qualified Leads in a Month",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Lead"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
