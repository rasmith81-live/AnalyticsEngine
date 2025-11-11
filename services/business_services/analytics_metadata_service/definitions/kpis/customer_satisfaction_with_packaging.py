"""
Customer Satisfaction with Packaging

The level of customer satisfaction with the quality and condition of packaging upon delivery, impacting customer loyalty.
"""

CUSTOMER_SATISFACTION_WITH_PACKAGING = {
    "code": "CUSTOMER_SATISFACTION_WITH_PACKAGING",
    "name": "Customer Satisfaction with Packaging",
    "description": "The level of customer satisfaction with the quality and condition of packaging upon delivery, impacting customer loyalty.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Satisfaction with Packaging to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer", "Delivery", "PurchaseOrder", "QualityMetric"], "last_validated": "2025-11-10T13:49:32.879144"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        592.57,
                        589.83,
                        564.13,
                        641.99,
                        674.79,
                        700.63,
                        623.68,
                        633.68,
                        662.39,
                        682.66,
                        690.49,
                        560.58
                ],
                "unit": "units"
        },
        "current": {
                "value": 560.58,
                "unit": "units",
                "change": -129.91,
                "change_percent": -18.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 634.79,
                "min": 560.58,
                "max": 700.63,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 161.31,
                        "percentage": 28.8
                },
                {
                        "category": "Existing Customers",
                        "value": 104.4,
                        "percentage": 18.6
                },
                {
                        "category": "VIP Customers",
                        "value": 51.25,
                        "percentage": 9.1
                },
                {
                        "category": "At-Risk Customers",
                        "value": 66.76,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 176.86,
                        "percentage": 31.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.801317",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Satisfaction with Packaging"
        }
    },
}
