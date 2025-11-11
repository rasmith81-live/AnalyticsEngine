"""
Inventory Accuracy

How well the inventory records match the physical inventory. The KPI is calculated as the number of items in inventory that match the records divided by the total number of items in inventory.
"""

INVENTORY_ACCURACY = {
    "code": "INVENTORY_ACCURACY",
    "name": "Inventory Accuracy",
    "description": "How well the inventory records match the physical inventory. The KPI is calculated as the number of items in inventory that match the records divided by the total number of items in inventory.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Accuracy to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Product"], "last_validated": "2025-11-10T13:43:23.536546"},
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
                        785.8,
                        708.36,
                        741.77,
                        690.84,
                        797.34,
                        777.15,
                        795.75,
                        740.55,
                        722.87,
                        766.22,
                        788.6,
                        735.59
                ],
                "unit": "units"
        },
        "current": {
                "value": 735.59,
                "unit": "units",
                "change": -53.01,
                "change_percent": -6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 754.24,
                "min": 690.84,
                "max": 797.34,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 201.36,
                        "percentage": 27.4
                },
                {
                        "category": "Category B",
                        "value": 144.0,
                        "percentage": 19.6
                },
                {
                        "category": "Category C",
                        "value": 89.48,
                        "percentage": 12.2
                },
                {
                        "category": "Category D",
                        "value": 89.41,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 211.34,
                        "percentage": 28.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.536546",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Inventory Accuracy"
        }
    },
}
