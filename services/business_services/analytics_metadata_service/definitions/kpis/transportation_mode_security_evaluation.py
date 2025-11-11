"""
Transportation Mode Security Evaluation

The evaluation of security measures specific to different modes of transportation within the supply chain.
"""

TRANSPORTATION_MODE_SECURITY_EVALUATION = {
    "code": "TRANSPORTATION_MODE_SECURITY_EVALUATION",
    "name": "Transportation Mode Security Evaluation",
    "description": "The evaluation of security measures specific to different modes of transportation within the supply chain.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Transportation Mode Security Evaluation to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.756601"},
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
                        490.14,
                        448.1,
                        494.3,
                        483.11,
                        473.75,
                        467.12,
                        481.87,
                        344.45,
                        352.65,
                        418.15,
                        430.71,
                        474.97
                ],
                "unit": "units"
        },
        "current": {
                "value": 474.97,
                "unit": "units",
                "change": 44.26,
                "change_percent": 10.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 446.61,
                "min": 344.45,
                "max": 494.3,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 102.47,
                        "percentage": 21.6
                },
                {
                        "category": "Segment B",
                        "value": 122.78,
                        "percentage": 25.9
                },
                {
                        "category": "Segment C",
                        "value": 39.19,
                        "percentage": 8.3
                },
                {
                        "category": "Segment D",
                        "value": 44.94,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 165.59,
                        "percentage": 34.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.886156",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Transportation Mode Security Evaluation"
        }
    },
}
