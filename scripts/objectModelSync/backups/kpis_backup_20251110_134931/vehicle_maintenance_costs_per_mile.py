"""
Vehicle Maintenance Costs per Mile

The cost incurred for maintaining a vehicle per mile driven.
"""

VEHICLE_MAINTENANCE_COSTS_PER_MILE = {
    "code": "VEHICLE_MAINTENANCE_COSTS_PER_MILE",
    "name": "Vehicle Maintenance Costs per Mile",
    "description": "The cost incurred for maintaining a vehicle per mile driven.",
    "formula": "Total Vehicle Maintenance Costs / Total Miles Driven",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Vehicle Maintenance Costs per Mile to be added.",
    "trend_analysis": "Trend analysis to be defined.",
    "diagnostic_questions": """
* What factors are influencing this metric?
* Are there any anomalies in the data?
    """,
    "actionable_tips": """
* Monitor this KPI regularly
* Set appropriate targets and thresholds
    """,
    "visualization_suggestions": """
* Line chart for time series analysis
* Bar chart for comparisons
    """,
    "risk_warnings": "* Monitor for significant deviations from expected values",
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": "* Integrate with related business metrics",
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:43:25.208557"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        104660.58,
                        104024.29,
                        101681.52,
                        102668.96,
                        100647.93,
                        97249.37,
                        94935.03,
                        104316.82,
                        102657.37,
                        99375.25,
                        96414.66,
                        105427.35
                ],
                "unit": "$"
        },
        "current": {
                "value": 105427.35,
                "unit": "$",
                "change": 9012.69,
                "change_percent": 9.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 101171.59,
                "min": 94935.03,
                "max": 105427.35,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16610.93,
                        "percentage": 15.8
                },
                {
                        "category": "Category B",
                        "value": 29299.92,
                        "percentage": 27.8
                },
                {
                        "category": "Category C",
                        "value": 9539.81,
                        "percentage": 9.0
                },
                {
                        "category": "Category D",
                        "value": 6865.2,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 43111.49,
                        "percentage": 40.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.208557",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Vehicle Maintenance Costs per Mile"
        }
    },
}
