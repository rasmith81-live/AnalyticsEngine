"""
Stockout Frequency

The frequency with which inventory items are out of stock.
"""

STOCKOUT_FREQUENCY = {
    "code": "STOCKOUT_FREQUENCY",
    "name": "Stockout Frequency",
    "description": "The frequency with which inventory items are out of stock.",
    "formula": "Total Number of Stockouts / Total Number of Inventory Checks",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stockout Frequency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Product"], "last_validated": "2025-11-10T13:43:24.797713"},
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
                        135,
                        157,
                        141,
                        137,
                        172,
                        159,
                        171,
                        167,
                        147,
                        180,
                        139,
                        175
                ],
                "unit": "count"
        },
        "current": {
                "value": 175,
                "unit": "count",
                "change": 36,
                "change_percent": 25.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 156.67,
                "min": 135,
                "max": 180,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 50.2,
                        "percentage": 28.7
                },
                {
                        "category": "Category B",
                        "value": 40.31,
                        "percentage": 23.0
                },
                {
                        "category": "Category C",
                        "value": 16.59,
                        "percentage": 9.5
                },
                {
                        "category": "Category D",
                        "value": 19.25,
                        "percentage": 11.0
                },
                {
                        "category": "Other",
                        "value": 48.65,
                        "percentage": 27.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.797713",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Stockout Frequency"
        }
    },
}
