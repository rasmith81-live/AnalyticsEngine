"""
Risk Assessment Coverage Ratio

The proportion of the supply chain that has undergone risk assessments, showing the extent of proactive security risk management.
"""

RISK_ASSESSMENT_COVERAGE_RATIO = {
    "code": "RISK_ASSESSMENT_COVERAGE_RATIO",
    "name": "Risk Assessment Coverage Ratio",
    "description": "The proportion of the supply chain that has undergone risk assessments, showing the extent of proactive security risk management.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Risk Assessment Coverage Ratio to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.368360"},
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
                        70.2,
                        73.29,
                        65.83,
                        83.28,
                        72.0,
                        75.66,
                        76.97,
                        72.25,
                        72.15,
                        73.69,
                        71.05,
                        70.38
                ],
                "unit": "%"
        },
        "current": {
                "value": 70.38,
                "unit": "%",
                "change": -0.67,
                "change_percent": -0.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.06,
                "min": 65.83,
                "max": 83.28,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12.29,
                        "percentage": 17.5
                },
                {
                        "category": "Segment B",
                        "value": 17.79,
                        "percentage": 25.3
                },
                {
                        "category": "Segment C",
                        "value": 11.31,
                        "percentage": 16.1
                },
                {
                        "category": "Segment D",
                        "value": 3.67,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 25.32,
                        "percentage": 36.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.854835",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Risk Assessment Coverage Ratio"
        }
    },
}
