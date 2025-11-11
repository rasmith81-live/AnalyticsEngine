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
                        74.68,
                        76.34,
                        61.64,
                        58.77,
                        69.18,
                        69.04,
                        66.66,
                        76.66,
                        58.3,
                        71.49,
                        68.46,
                        61.87
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.87,
                "unit": "%",
                "change": -6.59,
                "change_percent": -9.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.76,
                "min": 58.3,
                "max": 76.66,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 21.15,
                        "percentage": 34.2
                },
                {
                        "category": "Existing Customers",
                        "value": 12.56,
                        "percentage": 20.3
                },
                {
                        "category": "VIP Customers",
                        "value": 8.21,
                        "percentage": 13.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.47,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 16.48,
                        "percentage": 26.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.609604",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Claim Rate"
        }
    },
}
