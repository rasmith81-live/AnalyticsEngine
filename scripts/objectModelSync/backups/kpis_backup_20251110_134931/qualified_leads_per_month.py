"""
Qualified Leads per Month

The number of leads that meet certain criteria set by the sales team, indicating a higher probability of converting into customers.
"""

QUALIFIED_LEADS_PER_MONTH = {
    "code": "QUALIFIED_LEADS_PER_MONTH",
    "name": "Qualified Leads per Month",
    "description": "The number of leads that meet certain criteria set by the sales team, indicating a higher probability of converting into customers.",
    "formula": "Total Number of Qualified Leads in a Month",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Qualified Leads per Month to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Lead"], "last_validated": "2025-11-10T13:43:24.024783"},
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
                        211,
                        181,
                        209,
                        205,
                        190,
                        190,
                        206,
                        193,
                        180,
                        199,
                        179,
                        161
                ],
                "unit": "count"
        },
        "current": {
                "value": 161,
                "unit": "count",
                "change": -18,
                "change_percent": -10.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 192.0,
                "min": 161,
                "max": 211,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 39.82,
                        "percentage": 24.7
                },
                {
                        "category": "Category B",
                        "value": 20.99,
                        "percentage": 13.0
                },
                {
                        "category": "Category C",
                        "value": 24.5,
                        "percentage": 15.2
                },
                {
                        "category": "Category D",
                        "value": 20.49,
                        "percentage": 12.7
                },
                {
                        "category": "Other",
                        "value": 55.2,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.024783",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Qualified Leads per Month"
        }
    },
}
