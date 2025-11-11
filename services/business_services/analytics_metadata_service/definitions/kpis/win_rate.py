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
                        77.79,
                        64.98,
                        72.74,
                        73.48,
                        78.27,
                        63.84,
                        72.02,
                        69.08,
                        78.93,
                        71.99,
                        70.19,
                        73.62
                ],
                "unit": "%"
        },
        "current": {
                "value": 73.62,
                "unit": "%",
                "change": 3.43,
                "change_percent": 4.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 72.24,
                "min": 63.84,
                "max": 78.93,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.66,
                        "percentage": 21.3
                },
                {
                        "category": "Segment B",
                        "value": 19.21,
                        "percentage": 26.1
                },
                {
                        "category": "Segment C",
                        "value": 9.11,
                        "percentage": 12.4
                },
                {
                        "category": "Segment D",
                        "value": 6.87,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 22.77,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:14.000992",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Win Rate"
        }
    },
}
