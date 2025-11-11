"""
Lead Response Time

The time it takes for a sales representative to respond to a new lead.
"""

LEAD_RESPONSE_TIME = {
    "code": "LEAD_RESPONSE_TIME",
    "name": "Lead Response Time",
    "description": "The time it takes for a sales representative to respond to a new lead.",
    "formula": "Total Time Taken to Respond to Leads / Total Number of Leads",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Response Time to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.592628"},
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
                        478,
                        513,
                        479,
                        524,
                        523,
                        515,
                        494,
                        481,
                        496,
                        495,
                        503,
                        507
                ],
                "unit": "count"
        },
        "current": {
                "value": 507,
                "unit": "count",
                "change": 4,
                "change_percent": 0.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 500.67,
                "min": 478,
                "max": 524,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 174.98,
                        "percentage": 34.5
                },
                {
                        "category": "Category B",
                        "value": 105.39,
                        "percentage": 20.8
                },
                {
                        "category": "Category C",
                        "value": 75.95,
                        "percentage": 15.0
                },
                {
                        "category": "Category D",
                        "value": 33.49,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 117.19,
                        "percentage": 23.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.592628",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Lead Response Time"
        }
    },
}
