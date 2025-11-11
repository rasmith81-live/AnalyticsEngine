"""
Order Quantity Accuracy

The degree to which the quantity ordered matches the quantity needed, reducing overstock or stockouts.
"""

ORDER_QUANTITY_ACCURACY = {
    "code": "ORDER_QUANTITY_ACCURACY",
    "name": "Order Quantity Accuracy",
    "description": "The degree to which the quantity ordered matches the quantity needed, reducing overstock or stockouts.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Quantity Accuracy to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Inventory", "Order"], "last_validated": "2025-11-10T13:49:33.127848"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        328.88,
                        194.43,
                        192.28,
                        248.77,
                        202.79,
                        209.24,
                        311.42,
                        327.4,
                        315.77,
                        249.55,
                        262.33,
                        212.4
                ],
                "unit": "units"
        },
        "current": {
                "value": 212.4,
                "unit": "units",
                "change": -49.93,
                "change_percent": -19.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 254.61,
                "min": 192.28,
                "max": 328.88,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 47.33,
                        "percentage": 22.3
                },
                {
                        "category": "Category B",
                        "value": 39.14,
                        "percentage": 18.4
                },
                {
                        "category": "Category C",
                        "value": 21.68,
                        "percentage": 10.2
                },
                {
                        "category": "Category D",
                        "value": 14.95,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 89.3,
                        "percentage": 42.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.759747",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Quantity Accuracy"
        }
    },
}
