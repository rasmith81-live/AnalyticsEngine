"""
Warehouse Energy Costs per Square Foot

The cost of energy consumption per square foot of warehouse space.
"""

WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT = {
    "code": "WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT",
    "name": "Warehouse Energy Costs per Square Foot",
    "description": "The cost of energy consumption per square foot of warehouse space.",
    "formula": "Total Energy Costs / Total Square Footage of Warehouse",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Warehouse Energy Costs per Square Foot to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:43:25.247139"},
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
                        8140.23,
                        20237.18,
                        10023.48,
                        22365.36,
                        13704.1,
                        9675.37,
                        8204.07,
                        11279.76,
                        14769.69,
                        14655.75,
                        22648.33,
                        15910.16
                ],
                "unit": "$"
        },
        "current": {
                "value": 15910.16,
                "unit": "$",
                "change": -6738.17,
                "change_percent": -29.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 14301.12,
                "min": 8140.23,
                "max": 22648.33,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 4539.46,
                        "percentage": 28.5
                },
                {
                        "category": "Category B",
                        "value": 2068.64,
                        "percentage": 13.0
                },
                {
                        "category": "Category C",
                        "value": 1647.52,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 2135.27,
                        "percentage": 13.4
                },
                {
                        "category": "Other",
                        "value": 5519.27,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.247139",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Warehouse Energy Costs per Square Foot"
        }
    },
}
