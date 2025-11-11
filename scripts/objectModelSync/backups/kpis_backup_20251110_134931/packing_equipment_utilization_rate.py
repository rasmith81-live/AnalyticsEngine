"""
Packing Equipment Utilization Rate

The percentage of time that packing equipment is actively used compared to available operational time, indicating equipment efficiency.
"""

PACKING_EQUIPMENT_UTILIZATION_RATE = {
    "code": "PACKING_EQUIPMENT_UTILIZATION_RATE",
    "name": "Packing Equipment Utilization Rate",
    "description": "The percentage of time that packing equipment is actively used compared to available operational time, indicating equipment efficiency.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Equipment Utilization Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.808377"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        61.35,
                        56.16,
                        63.99,
                        63.01,
                        59.32,
                        53.57,
                        65.68,
                        53.07,
                        71.36,
                        64.93,
                        67.12,
                        69.27
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.27,
                "unit": "%",
                "change": 2.15,
                "change_percent": 3.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 62.4,
                "min": 53.07,
                "max": 71.36,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.14,
                        "percentage": 21.9
                },
                {
                        "category": "Category B",
                        "value": 16.76,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 8.08,
                        "percentage": 11.7
                },
                {
                        "category": "Category D",
                        "value": 5.49,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 23.8,
                        "percentage": 34.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.808377",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Equipment Utilization Rate"
        }
    },
}
