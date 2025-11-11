"""
Strategic Partner Development Index

A measure of the effectiveness of developing strategic partnerships and alliances.
"""

STRATEGIC_PARTNER_DEVELOPMENT_INDEX = {
    "code": "STRATEGIC_PARTNER_DEVELOPMENT_INDEX",
    "name": "Strategic Partner Development Index",
    "description": "A measure of the effectiveness of developing strategic partnerships and alliances.",
    "formula": "(Sum of Partnership Scores Based on Defined Criteria) / (Total Number of Strategic Partnerships)",
    "calculation_formula": "(Sum of Partnership Scores Based on Defined Criteria) / (Total Number of Strategic Partnerships)",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Partner Development Index to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.825415"},
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
                        58.01,
                        54.14,
                        57.47,
                        43.7,
                        59.34,
                        50.34,
                        51.16,
                        56.02,
                        47.03,
                        44.57,
                        58.84,
                        48.55
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.55,
                "unit": "%",
                "change": -10.29,
                "change_percent": -17.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 52.43,
                "min": 43.7,
                "max": 59.34,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.0,
                        "percentage": 18.5
                },
                {
                        "category": "Category B",
                        "value": 10.63,
                        "percentage": 21.9
                },
                {
                        "category": "Category C",
                        "value": 6.21,
                        "percentage": 12.8
                },
                {
                        "category": "Category D",
                        "value": 6.39,
                        "percentage": 13.2
                },
                {
                        "category": "Other",
                        "value": 16.32,
                        "percentage": 33.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.825415",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Partner Development Index"
        }
    },
}
