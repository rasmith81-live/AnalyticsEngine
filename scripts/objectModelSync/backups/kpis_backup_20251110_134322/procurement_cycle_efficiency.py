"""
Procurement Cycle Efficiency KPI Definition
"""

PROCUREMENT_CYCLE_EFFICIENCY = {
    "code": "PROCUREMENT_CYCLE_EFFICIENCY",
    "name": "Procurement Cycle Efficiency",
    "display_name": "Procurement Cycle Efficiency",
    "description": "The efficiency of the procurement process from requisition to payment.",
    "formula": "Total Time for All Procurement Cycles / Number of Procurement Cycles",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Payment"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
