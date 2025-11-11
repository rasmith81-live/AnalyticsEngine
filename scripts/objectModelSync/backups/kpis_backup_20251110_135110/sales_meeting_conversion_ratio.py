"""
Sales Meeting Conversion Ratio

The proportion of sales meetings or presentations that result in a sale or movement to the next stage of the buying process.
"""

SALES_MEETING_CONVERSION_RATIO = {
    "code": "SALES_MEETING_CONVERSION_RATIO",
    "name": "Sales Meeting Conversion Ratio",
    "description": "The proportion of sales meetings or presentations that result in a sale or movement to the next stage of the buying process.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Meeting Conversion Ratio to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.438088"},
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
                        79.58,
                        68.07,
                        82.36,
                        81.05,
                        79.56,
                        83.75,
                        70.01,
                        86.84,
                        79.58,
                        85.23,
                        75.23,
                        80.26
                ],
                "unit": "%"
        },
        "current": {
                "value": 80.26,
                "unit": "%",
                "change": 5.03,
                "change_percent": 6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 79.29,
                "min": 68.07,
                "max": 86.84,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 27.1,
                        "percentage": 33.8
                },
                {
                        "category": "Category B",
                        "value": 15.03,
                        "percentage": 18.7
                },
                {
                        "category": "Category C",
                        "value": 10.86,
                        "percentage": 13.5
                },
                {
                        "category": "Category D",
                        "value": 6.36,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 20.91,
                        "percentage": 26.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.425299",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Meeting Conversion Ratio"
        }
    },
}
