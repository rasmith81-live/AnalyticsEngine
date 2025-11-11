"""
Driver Retention Rate

The rate at which a company retains its drivers over a period.
"""

DRIVER_RETENTION_RATE = {
    "code": "DRIVER_RETENTION_RATE",
    "name": "Driver Retention Rate",
    "description": "The rate at which a company retains its drivers over a period.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Driver Retention Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.935239"},
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
                        66.55,
                        69.6,
                        66.5,
                        66.65,
                        59.98,
                        75.72,
                        70.0,
                        62.96,
                        75.25,
                        76.13,
                        71.14,
                        74.19
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.19,
                "unit": "%",
                "change": 3.05,
                "change_percent": 4.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 69.56,
                "min": 59.98,
                "max": 76.13,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.94,
                        "percentage": 32.3
                },
                {
                        "category": "Category B",
                        "value": 10.94,
                        "percentage": 14.7
                },
                {
                        "category": "Category C",
                        "value": 7.42,
                        "percentage": 10.0
                },
                {
                        "category": "Category D",
                        "value": 9.25,
                        "percentage": 12.5
                },
                {
                        "category": "Other",
                        "value": 22.64,
                        "percentage": 30.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.451427",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Driver Retention Rate"
        }
    },
}
