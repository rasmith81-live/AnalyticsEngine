"""
Average Warehouse Capacity

The average amount of inventory a warehouse can hold over a certain period.
"""

WAREHOUSE_CAPACITY = {
    "code": "WAREHOUSE_CAPACITY",
    "name": "Average Warehouse Capacity",
    "description": "The average amount of inventory a warehouse can hold over a certain period.",
    "formula": "Total Available Warehouse Space for Inventory / Total Warehouse Capacity",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Warehouse Capacity to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Warehouse"], "last_validated": "2025-11-10T13:49:33.795452"},
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
                        174.58,
                        256.07,
                        274.97,
                        226.48,
                        226.83,
                        274.42,
                        190.45,
                        160.96,
                        262.13,
                        153.05,
                        135.47,
                        249.97
                ],
                "unit": "units"
        },
        "current": {
                "value": 249.97,
                "unit": "units",
                "change": 114.5,
                "change_percent": 84.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 215.45,
                "min": 135.47,
                "max": 274.97,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 76.59,
                        "percentage": 30.6
                },
                {
                        "category": "Category B",
                        "value": 55.32,
                        "percentage": 22.1
                },
                {
                        "category": "Category C",
                        "value": 24.54,
                        "percentage": 9.8
                },
                {
                        "category": "Category D",
                        "value": 11.37,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 82.15,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.240048",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Average Warehouse Capacity"
        }
    },
}
