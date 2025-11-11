"""
Order Picking Accuracy Rate

The percentage of orders picked without errors.
"""

ORDER_PICKING_ACCURACY_RATE = {
    "code": "ORDER_PICKING_ACCURACY_RATE",
    "name": "Order Picking Accuracy Rate",
    "description": "The percentage of orders picked without errors.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Picking Accuracy Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.125481"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        70.51,
                        68.69,
                        74.2,
                        81.3,
                        67.49,
                        72.88,
                        66.98,
                        68.78,
                        72.9,
                        68.97,
                        69.2,
                        84.76
                ],
                "unit": "%"
        },
        "current": {
                "value": 84.76,
                "unit": "%",
                "change": 15.56,
                "change_percent": 22.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 72.22,
                "min": 66.98,
                "max": 84.76,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 29.25,
                        "percentage": 34.5
                },
                {
                        "category": "Segment B",
                        "value": 10.76,
                        "percentage": 12.7
                },
                {
                        "category": "Segment C",
                        "value": 14.29,
                        "percentage": 16.9
                },
                {
                        "category": "Segment D",
                        "value": 7.61,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 22.85,
                        "percentage": 27.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.325368",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Order Picking Accuracy Rate"
        }
    },
}
