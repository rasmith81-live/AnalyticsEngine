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
                        69.6,
                        75.98,
                        64.43,
                        63.95,
                        74.12,
                        69.53,
                        68.39,
                        73.53,
                        63.1,
                        65.18,
                        62.11,
                        74.41
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.41,
                "unit": "%",
                "change": 12.3,
                "change_percent": 19.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.69,
                "min": 62.11,
                "max": 75.98,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 13.25,
                        "percentage": 17.8
                },
                {
                        "category": "Channel Sales",
                        "value": 19.99,
                        "percentage": 26.9
                },
                {
                        "category": "Online Sales",
                        "value": 10.43,
                        "percentage": 14.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 6.17,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 24.57,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.025510",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Meeting Conversion Ratio"
        }
    },
}
