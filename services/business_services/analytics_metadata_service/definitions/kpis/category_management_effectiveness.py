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
                        213,
                        202,
                        221,
                        202,
                        230,
                        212,
                        216,
                        231,
                        227,
                        231,
                        235,
                        242
                ],
                "unit": "count"
        },
        "current": {
                "value": 242,
                "unit": "count",
                "change": 7,
                "change_percent": 3.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 221.83,
                "min": 202,
                "max": 242,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 78.41,
                        "percentage": 32.4
                },
                {
                        "category": "Segment B",
                        "value": 27.0,
                        "percentage": 11.2
                },
                {
                        "category": "Segment C",
                        "value": 23.7,
                        "percentage": 9.8
                },
                {
                        "category": "Segment D",
                        "value": 22.83,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 90.06,
                        "percentage": 37.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.430135",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Category Management Effectiveness"
        }
    },
}
