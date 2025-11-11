"""
Return Rate due to Packing Errors

The percentage of products returned due to errors in packing, serving as an indicator of the quality and accuracy of packing processes.
"""

RETURN_RATE_DUE_TO_PACKING_ERRORS = {
    "code": "RETURN_RATE_DUE_TO_PACKING_ERRORS",
    "name": "Return Rate due to Packing Errors",
    "description": "The percentage of products returned due to errors in packing, serving as an indicator of the quality and accuracy of packing processes.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Return Rate due to Packing Errors to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Product", "QualityMetric", "Return"], "last_validated": "2025-11-10T13:49:33.353040"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        65.95,
                        74.39,
                        60.52,
                        69.71,
                        68.11,
                        63.73,
                        58.13,
                        73.47,
                        58.06,
                        71.02,
                        65.7,
                        71.93
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.93,
                "unit": "%",
                "change": 6.23,
                "change_percent": 9.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 66.73,
                "min": 58.06,
                "max": 74.39,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 22.33,
                        "percentage": 31.0
                },
                {
                        "category": "Segment B",
                        "value": 9.66,
                        "percentage": 13.4
                },
                {
                        "category": "Segment C",
                        "value": 9.75,
                        "percentage": 13.6
                },
                {
                        "category": "Segment D",
                        "value": 5.15,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 25.04,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.825105",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Return Rate due to Packing Errors"
        }
    },
}
