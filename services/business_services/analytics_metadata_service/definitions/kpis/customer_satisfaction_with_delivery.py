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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Customer", "Delivery", "Order"], "last_validated": "2025-11-10T13:49:32.878104"},
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
                        697.2,
                        691.32,
                        615.74,
                        600.37,
                        693.89,
                        629.1,
                        677.78,
                        620.61,
                        675.94,
                        639.7,
                        636.72,
                        615.69
                ],
                "unit": "units"
        },
        "current": {
                "value": 615.69,
                "unit": "units",
                "change": -21.03,
                "change_percent": -3.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 649.5,
                "min": 600.37,
                "max": 697.2,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 102.83,
                        "percentage": 16.7
                },
                {
                        "category": "Existing Customers",
                        "value": 129.28,
                        "percentage": 21.0
                },
                {
                        "category": "VIP Customers",
                        "value": 100.16,
                        "percentage": 16.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 44.78,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 238.64,
                        "percentage": 38.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.797781",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Satisfaction with Delivery"
        }
    },
}
