"""
Customer Satisfaction with Delivery

Customer satisfaction with the company
"""

CUSTOMER_SATISFACTION_WITH_DELIVERY = {
    "code": "CUSTOMER_SATISFACTION_WITH_DELIVERY",
    "name": "Customer Satisfaction with Delivery",
    "description": "Customer satisfaction with the company",
    "formula": "Average of Customer Delivery Satisfaction Scores",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Satisfaction with Delivery to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Customer", "Delivery", "Order"], "last_validated": "2025-11-10T13:43:23.353443"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        432.16,
                        453.44,
                        548.56,
                        444.09,
                        422.87,
                        465.77,
                        529.23,
                        470.89,
                        467.91,
                        425.74,
                        424.45,
                        488.26
                ],
                "unit": "units"
        },
        "current": {
                "value": 488.26,
                "unit": "units",
                "change": 63.81,
                "change_percent": 15.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 464.45,
                "min": 422.87,
                "max": 548.56,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 104.91,
                        "percentage": 21.5
                },
                {
                        "category": "Category B",
                        "value": 118.32,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 66.99,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 40.73,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 157.31,
                        "percentage": 32.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.353443",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Satisfaction with Delivery"
        }
    },
}
