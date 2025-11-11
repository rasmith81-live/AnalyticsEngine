"""
Customer Claim Rate

The frequency at which customers make claims for undelivered or damaged goods.
"""

CUSTOMER_CLAIM_RATE = {
    "code": "CUSTOMER_CLAIM_RATE",
    "name": "Customer Claim Rate",
    "description": "The frequency at which customers make claims for undelivered or damaged goods.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Claim Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:49:32.806559"},
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
                        52.14,
                        57.15,
                        52.75,
                        59.7,
                        54.12,
                        57.95,
                        47.02,
                        53.8,
                        44.95,
                        47.48,
                        56.39,
                        49.81
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.81,
                "unit": "%",
                "change": -6.58,
                "change_percent": -11.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 52.77,
                "min": 44.95,
                "max": 59.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.58,
                        "percentage": 17.2
                },
                {
                        "category": "Category B",
                        "value": 11.79,
                        "percentage": 23.7
                },
                {
                        "category": "Category C",
                        "value": 9.01,
                        "percentage": 18.1
                },
                {
                        "category": "Category D",
                        "value": 3.85,
                        "percentage": 7.7
                },
                {
                        "category": "Other",
                        "value": 16.58,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.213719",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Claim Rate"
        }
    },
}
