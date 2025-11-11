"""
Security Training Completion Rate

The percentage of employees who have completed mandatory security training, reflecting the organization
"""

SECURITY_TRAINING_COMPLETION_RATE = {
    "code": "SECURITY_TRAINING_COMPLETION_RATE",
    "name": "Security Training Completion Rate",
    "description": "The percentage of employees who have completed mandatory security training, reflecting the organization",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Training Completion Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Employee"], "last_validated": "2025-11-10T13:49:33.562875"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        72.15,
                        63.89,
                        64.77,
                        69.19,
                        66.78,
                        73.27,
                        62.22,
                        66.94,
                        62.96,
                        75.84,
                        75.99,
                        65.64
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.64,
                "unit": "%",
                "change": -10.35,
                "change_percent": -13.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 68.3,
                "min": 62.22,
                "max": 75.99,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 21.49,
                        "percentage": 32.7
                },
                {
                        "category": "Category B",
                        "value": 12.3,
                        "percentage": 18.7
                },
                {
                        "category": "Category C",
                        "value": 10.15,
                        "percentage": 15.5
                },
                {
                        "category": "Category D",
                        "value": 4.23,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 17.47,
                        "percentage": 26.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.739088",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Security Training Completion Rate"
        }
    },
}
