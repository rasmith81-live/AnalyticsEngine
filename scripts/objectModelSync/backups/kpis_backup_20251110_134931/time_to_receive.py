"""
Time to Receive

The time it takes to accept, process, and store incoming goods.
"""

TIME_TO_RECEIVE = {
    "code": "TIME_TO_RECEIVE",
    "name": "Time to Receive",
    "description": "The time it takes to accept, process, and store incoming goods.",
    "formula": "Total Time Taken for Receiving / Total Number of Deliveries",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Receive to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:25.048613"},
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
                        443,
                        426,
                        439,
                        425,
                        431,
                        418,
                        453,
                        418,
                        464,
                        449,
                        418,
                        463
                ],
                "unit": "count"
        },
        "current": {
                "value": 463,
                "unit": "count",
                "change": 45,
                "change_percent": 10.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 437.25,
                "min": 418,
                "max": 464,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 151.88,
                        "percentage": 32.8
                },
                {
                        "category": "Category B",
                        "value": 60.22,
                        "percentage": 13.0
                },
                {
                        "category": "Category C",
                        "value": 52.84,
                        "percentage": 11.4
                },
                {
                        "category": "Category D",
                        "value": 48.02,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 150.04,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.048613",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Receive"
        }
    },
}
