"""
Time to Pick

The time it takes to collect items for an order from the warehouse.
"""

TIME_TO_PICK = {
    "code": "TIME_TO_PICK",
    "name": "Time to Pick",
    "description": "The time it takes to collect items for an order from the warehouse.",
    "formula": "Total Time Taken for Picking / Total Number of Orders Picked",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Pick to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Product", "Warehouse"], "last_validated": "2025-11-10T13:43:25.040709"},
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
                        112,
                        118,
                        151,
                        150,
                        135,
                        142,
                        113,
                        140,
                        116,
                        118,
                        129,
                        113
                ],
                "unit": "count"
        },
        "current": {
                "value": 113,
                "unit": "count",
                "change": -16,
                "change_percent": -12.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 128.08,
                "min": 112,
                "max": 151,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 31.48,
                        "percentage": 27.9
                },
                {
                        "category": "Category B",
                        "value": 13.48,
                        "percentage": 11.9
                },
                {
                        "category": "Category C",
                        "value": 13.63,
                        "percentage": 12.1
                },
                {
                        "category": "Category D",
                        "value": 14.56,
                        "percentage": 12.9
                },
                {
                        "category": "Other",
                        "value": 39.85,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.040709",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Pick"
        }
    },
}
