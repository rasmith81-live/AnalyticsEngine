"""
Equipment Utilization Rate

The percentage of time warehouse equipment is used compared to its availability.
"""

EQUIPMENT_UTILIZATION_RATE = {
    "code": "EQUIPMENT_UTILIZATION_RATE",
    "name": "Equipment Utilization Rate",
    "description": "The percentage of time warehouse equipment is used compared to its availability.",
    "formula": "Total Operating Time of Equipment / Total Available Time",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Equipment Utilization Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:43:23.474966"},
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
                        83.36,
                        85.35,
                        83.31,
                        76.98,
                        70.33,
                        75.35,
                        70.33,
                        86.3,
                        76.71,
                        70.8,
                        77.65,
                        73.64
                ],
                "unit": "%"
        },
        "current": {
                "value": 73.64,
                "unit": "%",
                "change": -4.01,
                "change_percent": -5.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 77.51,
                "min": 70.33,
                "max": 86.3,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.54,
                        "percentage": 26.5
                },
                {
                        "category": "Category B",
                        "value": 18.8,
                        "percentage": 25.5
                },
                {
                        "category": "Category C",
                        "value": 10.29,
                        "percentage": 14.0
                },
                {
                        "category": "Category D",
                        "value": 3.29,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 21.72,
                        "percentage": 29.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.474966",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Equipment Utilization Rate"
        }
    },
}
