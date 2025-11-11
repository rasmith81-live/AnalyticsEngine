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
                        343.39,
                        455.25,
                        462.03,
                        407.94,
                        393.94,
                        404.05,
                        392.74,
                        385.06,
                        478.8,
                        480.53,
                        473.4,
                        439.16
                ],
                "unit": "units"
        },
        "current": {
                "value": 439.16,
                "unit": "units",
                "change": -34.24,
                "change_percent": -7.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 426.36,
                "min": 343.39,
                "max": 480.53,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 150.82,
                        "percentage": 34.3
                },
                {
                        "category": "Segment B",
                        "value": 83.39,
                        "percentage": 19.0
                },
                {
                        "category": "Segment C",
                        "value": 36.18,
                        "percentage": 8.2
                },
                {
                        "category": "Segment D",
                        "value": 41.14,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 127.63,
                        "percentage": 29.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.964094",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Average Warehouse Capacity"
        }
    },
}
