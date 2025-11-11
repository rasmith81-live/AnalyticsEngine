"""
Customer Order Cycle Time

The total time taken from receiving a customer order to delivering the product or service, reflecting the speed of the supply chain.
"""

CUSTOMER_ORDER_CYCLE_TIME = {
    "code": "CUSTOMER_ORDER_CYCLE_TIME",
    "name": "Customer Order Cycle Time",
    "description": "The total time taken from receiving a customer order to delivering the product or service, reflecting the speed of the supply chain.",
    "formula": "Time of Order Delivery - Time of Order Placement",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Order Cycle Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Customer", "Delivery", "Order", "Product"], "last_validated": "2025-11-10T13:49:32.858371"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        18.1,
                        20.1,
                        23.0,
                        20.6,
                        22.0,
                        22.8,
                        19.7,
                        21.7,
                        25.6,
                        21.8,
                        18.2,
                        23.3
                ],
                "unit": "days"
        },
        "current": {
                "value": 23.3,
                "unit": "days",
                "change": 5.1,
                "change_percent": 28.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 21.41,
                "min": 18.1,
                "max": 25.6,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 5.95,
                        "percentage": 25.5
                },
                {
                        "category": "Existing Customers",
                        "value": 5.93,
                        "percentage": 25.5
                },
                {
                        "category": "VIP Customers",
                        "value": 1.84,
                        "percentage": 7.9
                },
                {
                        "category": "At-Risk Customers",
                        "value": 1.69,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 7.89,
                        "percentage": 33.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.747796",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Customer Order Cycle Time"
        }
    },
}
