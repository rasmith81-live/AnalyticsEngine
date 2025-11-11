"""
Dock-to-stock Cycle Time

The time taken to move goods from the receiving dock to the storage area.
"""

DOCK_TO_STOCK_CYCLE_TIME = {
    "code": "DOCK_TO_STOCK_CYCLE_TIME",
    "name": "Dock-to-stock Cycle Time",
    "description": "The time taken to move goods from the receiving dock to the storage area.",
    "formula": "Average Time from Goods Receipt to Warehouse Stocking",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Dock-to-stock Cycle Time to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Warehouse"], "last_validated": "2025-11-10T13:43:23.446775"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        4.6,
                        4.4,
                        5.5,
                        6.5,
                        4.4,
                        10.0,
                        6.8,
                        10.1,
                        8.0,
                        10.2,
                        5.9,
                        6.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 6.0,
                "unit": "days",
                "change": 0.1,
                "change_percent": 1.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 6.87,
                "min": 4.4,
                "max": 10.2,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 1.59,
                        "percentage": 26.5
                },
                {
                        "category": "Category B",
                        "value": 1.21,
                        "percentage": 20.2
                },
                {
                        "category": "Category C",
                        "value": 0.53,
                        "percentage": 8.8
                },
                {
                        "category": "Category D",
                        "value": 0.32,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 2.35,
                        "percentage": 39.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.446775",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Dock-to-stock Cycle Time"
        }
    },
}
