"""
Inventory Turnover Rate

How many times inventory is sold and replaced within a given period. It helps determine if inventory levels are too high or too low, and if adjustments are needed to optimize inventory management.
"""

INVENTORY_TURNOVER_RATE = {
    "code": "INVENTORY_TURNOVER_RATE",
    "name": "Inventory Turnover Rate",
    "description": "How many times inventory is sold and replaced within a given period. It helps determine if inventory levels are too high or too low, and if adjustments are needed to optimize inventory management.",
    "formula": "Cost of Goods Sold / Average Inventory Value",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Turnover Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:32.982972"},
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
                        72.51,
                        77.54,
                        63.08,
                        78.53,
                        66.61,
                        63.93,
                        70.41,
                        72.17,
                        73.19,
                        78.77,
                        74.14,
                        79.31
                ],
                "unit": "%"
        },
        "current": {
                "value": 79.31,
                "unit": "%",
                "change": 5.17,
                "change_percent": 7.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 72.52,
                "min": 63.08,
                "max": 79.31,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 26.64,
                        "percentage": 33.6
                },
                {
                        "category": "Category B",
                        "value": 16.27,
                        "percentage": 20.5
                },
                {
                        "category": "Category C",
                        "value": 10.49,
                        "percentage": 13.2
                },
                {
                        "category": "Category D",
                        "value": 3.01,
                        "percentage": 3.8
                },
                {
                        "category": "Other",
                        "value": 22.9,
                        "percentage": 28.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.554862",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Turnover Rate"
        }
    },
}
