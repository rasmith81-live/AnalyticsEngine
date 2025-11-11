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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead"], "last_validated": "2025-11-10T13:43:23.167696"},
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
                        245,
                        227,
                        210,
                        212,
                        227,
                        239,
                        209,
                        245,
                        209,
                        244,
                        236,
                        213
                ],
                "unit": "count"
        },
        "current": {
                "value": 213,
                "unit": "count",
                "change": -23,
                "change_percent": -9.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 226.33,
                "min": 209,
                "max": 245,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 39.1,
                        "percentage": 18.4
                },
                {
                        "category": "Category B",
                        "value": 43.18,
                        "percentage": 20.3
                },
                {
                        "category": "Category C",
                        "value": 44.23,
                        "percentage": 20.8
                },
                {
                        "category": "Category D",
                        "value": 25.86,
                        "percentage": 12.1
                },
                {
                        "category": "Other",
                        "value": 60.63,
                        "percentage": 28.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.167696",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Lead"
        }
    },
}
