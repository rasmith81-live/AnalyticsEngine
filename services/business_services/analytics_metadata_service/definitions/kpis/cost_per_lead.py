"""
Cost per Lead

The average cost incurred to generate one lead, which helps to evaluate the efficiency of marketing campaigns.
"""

COST_PER_LEAD = {
    "code": "COST_PER_LEAD",
    "name": "Cost per Lead",
    "description": "The average cost incurred to generate one lead, which helps to evaluate the efficiency of marketing campaigns.",
    "formula": "Total Cost of Lead Generation / Total Number of Leads",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Lead to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead"], "last_validated": "2025-11-10T13:49:32.727350"},
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
                        432,
                        411,
                        414,
                        422,
                        427,
                        429,
                        429,
                        428,
                        412,
                        428,
                        421,
                        403
                ],
                "unit": "count"
        },
        "current": {
                "value": 403,
                "unit": "count",
                "change": -18,
                "change_percent": -4.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 421.33,
                "min": 403,
                "max": 432,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 91.31,
                        "percentage": 22.7
                },
                {
                        "category": "Segment B",
                        "value": 105.67,
                        "percentage": 26.2
                },
                {
                        "category": "Segment C",
                        "value": 43.5,
                        "percentage": 10.8
                },
                {
                        "category": "Segment D",
                        "value": 32.54,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 129.98,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.534914",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Lead"
        }
    },
}
