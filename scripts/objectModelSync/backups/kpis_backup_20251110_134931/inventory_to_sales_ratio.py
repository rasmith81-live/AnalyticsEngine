"""
Inventory to Sales Ratio

The ratio of inventory on hand to the number of sales orders fulfilled.
"""

INVENTORY_TO_SALES_RATIO = {
    "code": "INVENTORY_TO_SALES_RATIO",
    "name": "Inventory to Sales Ratio",
    "description": "The ratio of inventory on hand to the number of sales orders fulfilled.",
    "formula": "Average Inventory Value / Total Sales",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory to Sales Ratio to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Order"], "last_validated": "2025-11-10T13:43:23.551065"},
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
                        72.1,
                        79.93,
                        89.23,
                        74.56,
                        75.32,
                        71.79,
                        87.93,
                        70.83,
                        80.32,
                        72.28,
                        87.92,
                        81.8
                ],
                "unit": "%"
        },
        "current": {
                "value": 81.8,
                "unit": "%",
                "change": -6.12,
                "change_percent": -7.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 78.67,
                "min": 70.83,
                "max": 89.23,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 28.6,
                        "percentage": 35.0
                },
                {
                        "category": "Category B",
                        "value": 13.28,
                        "percentage": 16.2
                },
                {
                        "category": "Category C",
                        "value": 11.38,
                        "percentage": 13.9
                },
                {
                        "category": "Category D",
                        "value": 4.13,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 24.41,
                        "percentage": 29.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.551065",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory to Sales Ratio"
        }
    },
}
