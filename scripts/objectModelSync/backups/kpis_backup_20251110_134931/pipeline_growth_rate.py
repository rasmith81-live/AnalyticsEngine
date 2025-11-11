"""
Pipeline Growth Rate

The rate at which the sales pipeline is growing, indicating the potential for future sales.
"""

PIPELINE_GROWTH_RATE = {
    "code": "PIPELINE_GROWTH_RATE",
    "name": "Pipeline Growth Rate",
    "description": "The rate at which the sales pipeline is growing, indicating the potential for future sales.",
    "formula": "((Number of Opportunities at End of Period - Number of Opportunities at Start of Period) / Number of Opportunities at Start of Period) * 100",
    "calculation_formula": "((Number of Opportunities at End of Period - Number of Opportunities at Start of Period) / Number of Opportunities at Start of Period) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Pipeline Growth Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.933488"},
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
                        73.63,
                        80.53,
                        73.06,
                        81.98,
                        71.85,
                        85.35,
                        76.08,
                        80.89,
                        70.61,
                        80.57,
                        78.33,
                        68.95
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.95,
                "unit": "%",
                "change": -9.38,
                "change_percent": -12.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 76.82,
                "min": 68.95,
                "max": 85.35,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.28,
                        "percentage": 20.7
                },
                {
                        "category": "Category B",
                        "value": 16.62,
                        "percentage": 24.1
                },
                {
                        "category": "Category C",
                        "value": 8.64,
                        "percentage": 12.5
                },
                {
                        "category": "Category D",
                        "value": 8.63,
                        "percentage": 12.5
                },
                {
                        "category": "Other",
                        "value": 20.78,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.933488",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Pipeline Growth Rate"
        }
    },
}
