"""
Inventory Carrying Cost

The total cost of holding inventory including storage, insurance, and taxes.
"""

INVENTORY_CARRYING_COST = {
    "code": "INVENTORY_CARRYING_COST",
    "name": "Inventory Carrying Cost",
    "description": "The total cost of holding inventory including storage, insurance, and taxes.",
    "formula": "Sum of All Inventory-Related Costs / Total Value of Inventory",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Carrying Cost to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:43:23.540233"},
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
                        61353.43,
                        69049.79,
                        74166.02,
                        75293.72,
                        60651.44,
                        63958.92,
                        62573.13,
                        63112.53,
                        68919.25,
                        66226.91,
                        64145.88,
                        73875.72
                ],
                "unit": "$"
        },
        "current": {
                "value": 73875.72,
                "unit": "$",
                "change": 9729.84,
                "change_percent": 15.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 66943.9,
                "min": 60651.44,
                "max": 75293.72,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 25086.01,
                        "percentage": 34.0
                },
                {
                        "category": "Category B",
                        "value": 12176.18,
                        "percentage": 16.5
                },
                {
                        "category": "Category C",
                        "value": 6926.06,
                        "percentage": 9.4
                },
                {
                        "category": "Category D",
                        "value": 7486.04,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 22201.43,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.540233",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Inventory Carrying Cost"
        }
    },
}
