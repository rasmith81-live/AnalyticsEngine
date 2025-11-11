"""
Picking Productivity

The rate at which items are picked and processed for orders.
"""

PICKING_PRODUCTIVITY = {
    "code": "PICKING_PRODUCTIVITY",
    "name": "Picking Productivity",
    "description": "The rate at which items are picked and processed for orders.",
    "formula": "Total Items Picked / Total Picking Hours",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Picking Productivity to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Product"], "last_validated": "2025-11-10T13:43:23.929822"},
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
                        276.1,
                        274.69,
                        221.25,
                        154.13,
                        142.93,
                        264.65,
                        190.63,
                        247.56,
                        246.73,
                        233.75,
                        264.9,
                        194.44
                ],
                "unit": "units"
        },
        "current": {
                "value": 194.44,
                "unit": "units",
                "change": -70.46,
                "change_percent": -26.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 225.98,
                "min": 142.93,
                "max": 276.1,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 39.68,
                        "percentage": 20.4
                },
                {
                        "category": "Category B",
                        "value": 50.79,
                        "percentage": 26.1
                },
                {
                        "category": "Category C",
                        "value": 23.14,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 10.19,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 70.64,
                        "percentage": 36.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.929822",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Picking Productivity"
        }
    },
}
