"""
Lost Sales Due to Stockouts

The estimated sales lost due to items being out of stock.
"""

LOST_SALES_DUE_TO_STOCKOUTS = {
    "code": "LOST_SALES_DUE_TO_STOCKOUTS",
    "name": "Lost Sales Due to Stockouts",
    "description": "The estimated sales lost due to items being out of stock.",
    "formula": "Estimated Sales Value of Stockout Items",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lost Sales Due to Stockouts to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Product"], "last_validated": "2025-11-10T13:49:33.035246"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        474.54,
                        461.65,
                        471.32,
                        504.79,
                        504.87,
                        551.89,
                        561.64,
                        527.54,
                        536.62,
                        492.49,
                        475.94,
                        491.48
                ],
                "unit": "units"
        },
        "current": {
                "value": 491.48,
                "unit": "units",
                "change": 15.54,
                "change_percent": 3.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 504.56,
                "min": 461.65,
                "max": 561.64,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 78.38,
                        "percentage": 15.9
                },
                {
                        "category": "Channel Sales",
                        "value": 63.5,
                        "percentage": 12.9
                },
                {
                        "category": "Online Sales",
                        "value": 54.83,
                        "percentage": 11.2
                },
                {
                        "category": "Enterprise Sales",
                        "value": 72.55,
                        "percentage": 14.8
                },
                {
                        "category": "Other",
                        "value": 222.22,
                        "percentage": 45.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.175570",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Lost Sales Due to Stockouts"
        }
    },
}
