"""
Category Management Effectiveness

The performance of procurement in managing different categories of goods and services.
"""

CATEGORY_MANAGEMENT_EFFECTIVENESS = {
    "code": "CATEGORY_MANAGEMENT_EFFECTIVENESS",
    "name": "Category Management Effectiveness",
    "description": "The performance of procurement in managing different categories of goods and services.",
    "formula": "Sum of Performance Metrics within a Category / Total Number of Metrics for Category",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Category Management Effectiveness to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.678159"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        324,
                        350,
                        338,
                        323,
                        320,
                        341,
                        322,
                        336,
                        352,
                        329,
                        344,
                        357
                ],
                "unit": "count"
        },
        "current": {
                "value": 357,
                "unit": "count",
                "change": 13,
                "change_percent": 3.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 336.33,
                "min": 320,
                "max": 357,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 123.72,
                        "percentage": 34.7
                },
                {
                        "category": "Category B",
                        "value": 35.39,
                        "percentage": 9.9
                },
                {
                        "category": "Category C",
                        "value": 51.16,
                        "percentage": 14.3
                },
                {
                        "category": "Category D",
                        "value": 27.7,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 119.03,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.079693",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Category Management Effectiveness"
        }
    },
}
