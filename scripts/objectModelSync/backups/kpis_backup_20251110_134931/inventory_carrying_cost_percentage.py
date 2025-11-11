"""
Inventory Carrying Cost Percentage

The percentage of total inventory value that represents the cost of holding inventory, including storage, insurance, and obsolescence.
"""

INVENTORY_CARRYING_COST_PERCENTAGE = {
    "code": "INVENTORY_CARRYING_COST_PERCENTAGE",
    "name": "Inventory Carrying Cost Percentage",
    "description": "The percentage of total inventory value that represents the cost of holding inventory, including storage, insurance, and obsolescence.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Carrying Cost Percentage to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:43:23.542899"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        67.89,
                        78.74,
                        82.39,
                        82.1,
                        71.22,
                        75.27,
                        72.24,
                        73.41,
                        72.85,
                        76.43,
                        67.48,
                        77.49
                ],
                "unit": "%"
        },
        "current": {
                "value": 77.49,
                "unit": "%",
                "change": 10.01,
                "change_percent": 14.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.79,
                "min": 67.48,
                "max": 82.39,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.24,
                        "percentage": 30.0
                },
                {
                        "category": "Category B",
                        "value": 12.75,
                        "percentage": 16.5
                },
                {
                        "category": "Category C",
                        "value": 9.2,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 5.28,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 27.02,
                        "percentage": 34.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.542899",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Carrying Cost Percentage"
        }
    },
}
