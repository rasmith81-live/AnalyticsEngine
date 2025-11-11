"""
New Business Opportunities Identified

The number of new business opportunities identified by the team, indicating the potential for revenue growth.
"""

NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED = {
    "code": "NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED",
    "name": "New Business Opportunities Identified",
    "description": "The number of new business opportunities identified by the team, indicating the potential for revenue growth.",
    "formula": "Total Number of New Opportunities Identified",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for New Business Opportunities Identified to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.681002"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        282,
                        285,
                        266,
                        241,
                        256,
                        248,
                        282,
                        275,
                        265,
                        244,
                        285,
                        263
                ],
                "unit": "count"
        },
        "current": {
                "value": 263,
                "unit": "count",
                "change": -22,
                "change_percent": -7.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 266.0,
                "min": 241,
                "max": 285,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 60.83,
                        "percentage": 23.1
                },
                {
                        "category": "Category B",
                        "value": 49.61,
                        "percentage": 18.9
                },
                {
                        "category": "Category C",
                        "value": 39.81,
                        "percentage": 15.1
                },
                {
                        "category": "Category D",
                        "value": 29.46,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 83.29,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.681002",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "New Business Opportunities Identified"
        }
    },
}
