"""
Inbound Orders Processed per Hour

The number of inbound orders processed per hour.
"""

INBOUND_ORDERS_PROCESSED_PER_HOUR = {
    "code": "INBOUND_ORDERS_PROCESSED_PER_HOUR",
    "name": "Inbound Orders Processed per Hour",
    "description": "The number of inbound orders processed per hour.",
    "formula": "Total Inbound Orders Processed / Total Hours Worked",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inbound Orders Processed per Hour to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:43:23.513992"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        306.55,
                        289.84,
                        367.04,
                        334.63,
                        344.73,
                        296.47,
                        390.64,
                        297.94,
                        305.97,
                        319.33,
                        327.98,
                        339.04
                ],
                "unit": "units"
        },
        "current": {
                "value": 339.04,
                "unit": "units",
                "change": 11.06,
                "change_percent": 3.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 326.68,
                "min": 289.84,
                "max": 390.64,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 58.25,
                        "percentage": 17.2
                },
                {
                        "category": "Category B",
                        "value": 71.34,
                        "percentage": 21.0
                },
                {
                        "category": "Category C",
                        "value": 57.41,
                        "percentage": 16.9
                },
                {
                        "category": "Category D",
                        "value": 20.12,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 131.92,
                        "percentage": 38.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.513992",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Inbound Orders Processed per Hour"
        }
    },
}
