"""
Sales Cycle Length

The length of time it takes for a lead to become a customer.
"""

SALES_CYCLE_LENGTH = {
    "code": "SALES_CYCLE_LENGTH",
    "name": "Sales Cycle Length",
    "description": "The length of time it takes for a lead to become a customer.",
    "formula": "Average Time from First Contact to Deal Closure",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Cycle Length to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Deal", "Lead"], "last_validated": "2025-11-10T13:43:24.358904"},
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
                        25.1,
                        24.5,
                        24.9,
                        19.1,
                        21.7,
                        24.6,
                        22.5,
                        24.1,
                        19.9,
                        23.3,
                        25.3,
                        17.8
                ],
                "unit": "days"
        },
        "current": {
                "value": 17.8,
                "unit": "days",
                "change": -7.5,
                "change_percent": -29.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 22.73,
                "min": 17.8,
                "max": 25.3,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 3.1,
                        "percentage": 17.4
                },
                {
                        "category": "Category B",
                        "value": 5.1,
                        "percentage": 28.7
                },
                {
                        "category": "Category C",
                        "value": 2.59,
                        "percentage": 14.6
                },
                {
                        "category": "Category D",
                        "value": 2.04,
                        "percentage": 11.5
                },
                {
                        "category": "Other",
                        "value": 4.97,
                        "percentage": 27.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.358904",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Sales Cycle Length"
        }
    },
}
