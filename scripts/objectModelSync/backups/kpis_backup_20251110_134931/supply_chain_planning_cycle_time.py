"""
Supply Chain Planning Cycle Time

The time required to create a supply chain plan, with shorter cycles allowing for more agility and responsiveness to changes.
"""

SUPPLY_CHAIN_PLANNING_CYCLE_TIME = {
    "code": "SUPPLY_CHAIN_PLANNING_CYCLE_TIME",
    "name": "Supply Chain Planning Cycle Time",
    "description": "The time required to create a supply chain plan, with shorter cycles allowing for more agility and responsiveness to changes.",
    "formula": "Total Planning Cycle Time",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Planning Cycle Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:24.910349"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        24.9,
                        24.6,
                        24.9,
                        26.9,
                        30.1,
                        31.6,
                        32.6,
                        28.9,
                        29.2,
                        27.6,
                        29.5,
                        24.7
                ],
                "unit": "days"
        },
        "current": {
                "value": 24.7,
                "unit": "days",
                "change": -4.8,
                "change_percent": -16.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 27.96,
                "min": 24.6,
                "max": 32.6,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.31,
                        "percentage": 29.6
                },
                {
                        "category": "Category B",
                        "value": 4.98,
                        "percentage": 20.2
                },
                {
                        "category": "Category C",
                        "value": 3.67,
                        "percentage": 14.9
                },
                {
                        "category": "Category D",
                        "value": 2.06,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 6.68,
                        "percentage": 27.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.910349",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supply Chain Planning Cycle Time"
        }
    },
}
