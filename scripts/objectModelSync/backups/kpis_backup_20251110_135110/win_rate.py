"""
Win Rate

The percentage of deals won out of the total number of opportunities.
"""

WIN_RATE = {
    "code": "WIN_RATE",
    "name": "Win Rate",
    "description": "The percentage of deals won out of the total number of opportunities.",
    "formula": "(Number of Opportunities Won by Partners / Total Number of Opportunities) * 100",
    "calculation_formula": "(Number of Opportunities Won by Partners / Total Number of Opportunities) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Win Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.816297"},
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
                        55.08,
                        50.86,
                        58.52,
                        58.81,
                        59.99,
                        54.8,
                        65.56,
                        61.49,
                        54.47,
                        48.26,
                        54.87,
                        52.19
                ],
                "unit": "%"
        },
        "current": {
                "value": 52.19,
                "unit": "%",
                "change": -2.68,
                "change_percent": -4.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 56.24,
                "min": 48.26,
                "max": 65.56,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.94,
                        "percentage": 32.5
                },
                {
                        "category": "Category B",
                        "value": 10.93,
                        "percentage": 20.9
                },
                {
                        "category": "Category C",
                        "value": 6.9,
                        "percentage": 13.2
                },
                {
                        "category": "Category D",
                        "value": 1.83,
                        "percentage": 3.5
                },
                {
                        "category": "Other",
                        "value": 15.59,
                        "percentage": 29.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.281581",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Win Rate"
        }
    },
}
