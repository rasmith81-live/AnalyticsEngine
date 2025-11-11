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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Order", "Product"], "last_validated": "2025-11-10T13:43:23.737347"},
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
                        57.65,
                        51.71,
                        66.35,
                        59.65,
                        66.53,
                        69.32,
                        62.18,
                        60.39,
                        54.46,
                        60.05,
                        68.72,
                        64.95
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.95,
                "unit": "%",
                "change": -3.77,
                "change_percent": -5.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 61.83,
                "min": 51.71,
                "max": 69.32,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.03,
                        "percentage": 33.9
                },
                {
                        "category": "Category B",
                        "value": 11.81,
                        "percentage": 18.2
                },
                {
                        "category": "Category C",
                        "value": 5.53,
                        "percentage": 8.5
                },
                {
                        "category": "Category D",
                        "value": 4.03,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 21.55,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.737347",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Order Accuracy Rate"
        }
    },
}
