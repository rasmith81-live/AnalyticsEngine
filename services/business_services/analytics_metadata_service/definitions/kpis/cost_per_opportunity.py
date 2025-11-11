"""
Cost per Opportunity

The average cost incurred to turn a lead into a sales opportunity.
"""

COST_PER_OPPORTUNITY = {
    "code": "COST_PER_OPPORTUNITY",
    "name": "Cost per Opportunity",
    "description": "The average cost incurred to turn a lead into a sales opportunity.",
    "formula": "Total Cost of Sales and Marketing / Total Number of Opportunities",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Opportunity to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "Opportunity", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.728409"},
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
                        447,
                        414,
                        451,
                        451,
                        420,
                        433,
                        444,
                        416,
                        431,
                        437,
                        422,
                        443
                ],
                "unit": "count"
        },
        "current": {
                "value": 443,
                "unit": "count",
                "change": 21,
                "change_percent": 5.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 434.08,
                "min": 414,
                "max": 451,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 115.36,
                        "percentage": 26.0
                },
                {
                        "category": "Channel Sales",
                        "value": 113.74,
                        "percentage": 25.7
                },
                {
                        "category": "Online Sales",
                        "value": 60.24,
                        "percentage": 13.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 25.79,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 127.87,
                        "percentage": 28.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.537181",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Opportunity"
        }
    },
}
