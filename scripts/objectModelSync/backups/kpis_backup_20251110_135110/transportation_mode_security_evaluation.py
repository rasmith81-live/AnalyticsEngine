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
                        98.33,
                        89.08,
                        162.14,
                        52.78,
                        80.47,
                        149.82,
                        73.0,
                        54.69,
                        87.1,
                        112.21,
                        167.88,
                        154.82
                ],
                "unit": "units"
        },
        "current": {
                "value": 154.82,
                "unit": "units",
                "change": -13.06,
                "change_percent": -7.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 106.86,
                "min": 52.78,
                "max": 167.88,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 43.05,
                        "percentage": 27.8
                },
                {
                        "category": "Category B",
                        "value": 20.35,
                        "percentage": 13.1
                },
                {
                        "category": "Category C",
                        "value": 26.53,
                        "percentage": 17.1
                },
                {
                        "category": "Category D",
                        "value": 11.85,
                        "percentage": 7.7
                },
                {
                        "category": "Other",
                        "value": 53.04,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.148933",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Transportation Mode Security Evaluation"
        }
    },
}
