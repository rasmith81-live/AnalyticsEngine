"""
Material Utilization Rate

The percentage of packaging materials that are optimally used without excess waste, reflecting sustainable packaging practices.
"""

MATERIAL_UTILIZATION_RATE = {
    "code": "MATERIAL_UTILIZATION_RATE",
    "name": "Material Utilization Rate",
    "description": "The percentage of packaging materials that are optimally used without excess waste, reflecting sustainable packaging practices.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Material Utilization Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.648554"},
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
                        70.44,
                        82.92,
                        65.74,
                        69.24,
                        66.02,
                        83.89,
                        65.32,
                        68.49,
                        77.55,
                        83.62,
                        82.67,
                        71.58
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.58,
                "unit": "%",
                "change": -11.09,
                "change_percent": -13.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 73.96,
                "min": 65.32,
                "max": 83.89,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.89,
                        "percentage": 16.6
                },
                {
                        "category": "Category B",
                        "value": 10.77,
                        "percentage": 15.0
                },
                {
                        "category": "Category C",
                        "value": 8.31,
                        "percentage": 11.6
                },
                {
                        "category": "Category D",
                        "value": 4.85,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 35.76,
                        "percentage": 50.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.648554",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Material Utilization Rate"
        }
    },
}
