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
                        51.04,
                        48.18,
                        35.5,
                        49.61,
                        35.14,
                        45.15,
                        51.0,
                        34.51,
                        33.14,
                        43.62,
                        46.59,
                        37.26
                ],
                "unit": "%"
        },
        "current": {
                "value": 37.26,
                "unit": "%",
                "change": -9.33,
                "change_percent": -20.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 42.56,
                "min": 33.14,
                "max": 51.04,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.05,
                        "percentage": 18.9
                },
                {
                        "category": "Category B",
                        "value": 10.56,
                        "percentage": 28.3
                },
                {
                        "category": "Category C",
                        "value": 3.71,
                        "percentage": 10.0
                },
                {
                        "category": "Category D",
                        "value": 3.48,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 12.46,
                        "percentage": 33.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.131049",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Risk Assessment Coverage Ratio"
        }
    },
}
