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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "Opportunity", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.169969"},
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
                        135,
                        149,
                        122,
                        140,
                        116,
                        138,
                        157,
                        134,
                        145,
                        116,
                        160,
                        142
                ],
                "unit": "count"
        },
        "current": {
                "value": 142,
                "unit": "count",
                "change": -18,
                "change_percent": -11.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 137.83,
                "min": 116,
                "max": 160,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 45.55,
                        "percentage": 32.1
                },
                {
                        "category": "Category B",
                        "value": 17.56,
                        "percentage": 12.4
                },
                {
                        "category": "Category C",
                        "value": 14.27,
                        "percentage": 10.0
                },
                {
                        "category": "Category D",
                        "value": 17.4,
                        "percentage": 12.3
                },
                {
                        "category": "Other",
                        "value": 47.22,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.169969",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Opportunity"
        }
    },
}
