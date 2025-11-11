"""
Social Responsibility Index in Procurement

The index measuring the consideration of social responsibility in procurement decisions, aligning with ISO 20400.
"""

SOCIAL_RESPONSIBILITY_INDEX_IN_PROCUREMENT = {
    "code": "SOCIAL_RESPONSIBILITY_INDEX_IN_PROCUREMENT",
    "name": "Social Responsibility Index in Procurement",
    "description": "The index measuring the consideration of social responsibility in procurement decisions, aligning with ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Social Responsibility Index in Procurement to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.576930"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        74.9,
                        82.8,
                        82.0,
                        72.4,
                        81.3,
                        77.0,
                        71.5,
                        79.5,
                        80.8,
                        73.1,
                        81.7,
                        75.5
                ],
                "unit": "score"
        },
        "current": {
                "value": 75.5,
                "unit": "score",
                "change": -6.2,
                "change_percent": -7.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 77.71,
                "min": 71.5,
                "max": 82.8,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 24.15,
                        "percentage": 32.0
                },
                {
                        "category": "Segment B",
                        "value": 15.14,
                        "percentage": 20.1
                },
                {
                        "category": "Segment C",
                        "value": 10.42,
                        "percentage": 13.8
                },
                {
                        "category": "Segment D",
                        "value": 5.39,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 20.4,
                        "percentage": 27.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.391128",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Social Responsibility Index in Procurement"
        }
    },
}
