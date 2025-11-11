"""
Opportunity-to-Close Rate

The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team
"""

OPPORTUNITY_TO_CLOSE_RATE = {
    "code": "OPPORTUNITY_TO_CLOSE_RATE",
    "name": "Opportunity-to-Close Rate",
    "description": "The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team",
    "formula": "(Number of Opportunities Closed as Wins / Total Number of Opportunities) * 100",
    "calculation_formula": "(Number of Opportunities Closed as Wins / Total Number of Opportunities) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Opportunity-to-Close Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Opportunity", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.109445"},
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
                        74.37,
                        76.08,
                        57.19,
                        72.13,
                        56.96,
                        76.69,
                        75.51,
                        65.05,
                        68.38,
                        57.28,
                        72.52,
                        62.64
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.64,
                "unit": "%",
                "change": -9.88,
                "change_percent": -13.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.9,
                "min": 56.96,
                "max": 76.69,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 9.64,
                        "percentage": 15.4
                },
                {
                        "category": "Segment B",
                        "value": 9.41,
                        "percentage": 15.0
                },
                {
                        "category": "Segment C",
                        "value": 14.62,
                        "percentage": 23.3
                },
                {
                        "category": "Segment D",
                        "value": 5.3,
                        "percentage": 8.5
                },
                {
                        "category": "Other",
                        "value": 23.67,
                        "percentage": 37.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.296755",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Opportunity-to-Close Rate"
        }
    },
}
