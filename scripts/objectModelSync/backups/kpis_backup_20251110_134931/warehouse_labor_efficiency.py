"""
Warehouse Labor Efficiency

The overall efficiency of warehouse staff based on output over input.
"""

WAREHOUSE_LABOR_EFFICIENCY = {
    "code": "WAREHOUSE_LABOR_EFFICIENCY",
    "name": "Warehouse Labor Efficiency",
    "description": "The overall efficiency of warehouse staff based on output over input.",
    "formula": "Total Number of Orders Fulfilled / Total Labor Hours",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Warehouse Labor Efficiency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Employee", "Order", "Warehouse"], "last_validated": "2025-11-10T13:43:25.252123"},
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
                        471,
                        509,
                        480,
                        502,
                        501,
                        513,
                        493,
                        473,
                        495,
                        475,
                        482,
                        475
                ],
                "unit": "count"
        },
        "current": {
                "value": 475,
                "unit": "count",
                "change": -7,
                "change_percent": -1.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 489.08,
                "min": 471,
                "max": 513,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 93.81,
                        "percentage": 19.7
                },
                {
                        "category": "Category B",
                        "value": 85.7,
                        "percentage": 18.0
                },
                {
                        "category": "Category C",
                        "value": 68.76,
                        "percentage": 14.5
                },
                {
                        "category": "Category D",
                        "value": 39.34,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 187.39,
                        "percentage": 39.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.252123",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Warehouse Labor Efficiency"
        }
    },
}
