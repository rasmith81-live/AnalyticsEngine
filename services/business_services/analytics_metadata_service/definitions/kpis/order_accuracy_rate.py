"""
Order Accuracy Rate

The percentage of orders that are accurately fulfilled without errors, such as wrong items, wrong quantities, or damaged products. It helps assess the effectiveness of inventory management and order processing, and identify areas for improvement in the supply chain process.
"""

ORDER_ACCURACY_RATE = {
    "code": "ORDER_ACCURACY_RATE",
    "name": "Order Accuracy Rate",
    "description": "The percentage of orders that are accurately fulfilled without errors, such as wrong items, wrong quantities, or damaged products. It helps assess the effectiveness of inventory management and order processing, and identify areas for improvement in the supply chain process.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Accuracy Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Order", "Product"], "last_validated": "2025-11-10T13:49:33.112579"},
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
                        37.96,
                        48.64,
                        55.56,
                        50.52,
                        52.13,
                        44.96,
                        54.95,
                        51.32,
                        50.1,
                        44.82,
                        44.2,
                        57.02
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.02,
                "unit": "%",
                "change": 12.82,
                "change_percent": 29.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 49.35,
                "min": 37.96,
                "max": 57.02,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.5,
                        "percentage": 28.9
                },
                {
                        "category": "Segment B",
                        "value": 13.74,
                        "percentage": 24.1
                },
                {
                        "category": "Segment C",
                        "value": 6.27,
                        "percentage": 11.0
                },
                {
                        "category": "Segment D",
                        "value": 5.18,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 15.33,
                        "percentage": 26.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.302089",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Order Accuracy Rate"
        }
    },
}
