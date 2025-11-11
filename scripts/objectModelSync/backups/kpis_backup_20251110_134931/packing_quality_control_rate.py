"""
Packing Quality Control Rate

The percentage of packed items that pass quality control checks, ensuring product integrity and customer satisfaction.
"""

PACKING_QUALITY_CONTROL_RATE = {
    "code": "PACKING_QUALITY_CONTROL_RATE",
    "name": "Packing Quality Control Rate",
    "description": "The percentage of packed items that pass quality control checks, ensuring product integrity and customer satisfaction.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Quality Control Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer", "Order", "Product", "QualityMetric"], "last_validated": "2025-11-10T13:43:23.833064"},
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
                        42.25,
                        38.68,
                        40.95,
                        46.66,
                        39.33,
                        50.0,
                        50.69,
                        49.25,
                        38.23,
                        44.23,
                        42.67,
                        48.05
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.05,
                "unit": "%",
                "change": 5.38,
                "change_percent": 12.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 44.25,
                "min": 38.23,
                "max": 50.69,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.19,
                        "percentage": 31.6
                },
                {
                        "category": "Category B",
                        "value": 10.49,
                        "percentage": 21.8
                },
                {
                        "category": "Category C",
                        "value": 4.3,
                        "percentage": 8.9
                },
                {
                        "category": "Category D",
                        "value": 5.32,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 12.75,
                        "percentage": 26.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.833064",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Quality Control Rate"
        }
    },
}
