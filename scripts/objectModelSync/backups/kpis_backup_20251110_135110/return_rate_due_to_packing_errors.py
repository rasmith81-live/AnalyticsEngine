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
                        71.29,
                        77.53,
                        72.27,
                        62.69,
                        69.47,
                        60.77,
                        60.76,
                        64.88,
                        61.44,
                        76.42,
                        76.01,
                        61.3
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.3,
                "unit": "%",
                "change": -14.71,
                "change_percent": -19.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.9,
                "min": 60.76,
                "max": 77.53,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.23,
                        "percentage": 21.6
                },
                {
                        "category": "Category B",
                        "value": 11.42,
                        "percentage": 18.6
                },
                {
                        "category": "Category C",
                        "value": 8.34,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 8.24,
                        "percentage": 13.4
                },
                {
                        "category": "Other",
                        "value": 20.07,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.100466",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Return Rate due to Packing Errors"
        }
    },
}
