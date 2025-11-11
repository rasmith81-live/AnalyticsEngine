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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.609984"},
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
                        55.88,
                        54.97,
                        48.74,
                        63.13,
                        63.11,
                        55.51,
                        52.42,
                        59.66,
                        47.01,
                        64.61,
                        56.22,
                        46.03
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.03,
                "unit": "%",
                "change": -10.19,
                "change_percent": -18.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 55.61,
                "min": 46.03,
                "max": 64.61,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.5,
                        "percentage": 25.0
                },
                {
                        "category": "Segment B",
                        "value": 10.65,
                        "percentage": 23.1
                },
                {
                        "category": "Segment C",
                        "value": 3.88,
                        "percentage": 8.4
                },
                {
                        "category": "Segment D",
                        "value": 4.6,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 15.4,
                        "percentage": 33.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.480179",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Partner Development Index"
        }
    },
}
