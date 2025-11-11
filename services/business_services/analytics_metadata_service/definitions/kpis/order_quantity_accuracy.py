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
                        618.09,
                        511.86,
                        607.85,
                        655.32,
                        588.01,
                        589.92,
                        540.61,
                        631.28,
                        535.49,
                        542.03,
                        561.4,
                        563.23
                ],
                "unit": "units"
        },
        "current": {
                "value": 563.23,
                "unit": "units",
                "change": 1.83,
                "change_percent": 0.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 578.76,
                "min": 511.86,
                "max": 655.32,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 194.25,
                        "percentage": 34.5
                },
                {
                        "category": "Segment B",
                        "value": 72.71,
                        "percentage": 12.9
                },
                {
                        "category": "Segment C",
                        "value": 69.75,
                        "percentage": 12.4
                },
                {
                        "category": "Segment D",
                        "value": 39.46,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 187.06,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.333829",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Quantity Accuracy"
        }
    },
}
