"""
Packaging Efficiency Rate

The percentage of packaging operations completed within a set time frame, indicating the effectiveness of packing processes in fulfilling orders swiftly.
"""

PACKAGING_EFFICIENCY_RATE = {
    "code": "PACKAGING_EFFICIENCY_RATE",
    "name": "Packaging Efficiency Rate",
    "description": "The percentage of packaging operations completed within a set time frame, indicating the effectiveness of packing processes in fulfilling orders swiftly.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Efficiency Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:43:23.787946"},
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
                        73.9,
                        65.58,
                        68.51,
                        71.26,
                        74.64,
                        72.25,
                        58.91,
                        72.84,
                        73.34,
                        59.36,
                        56.56,
                        59.51
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.51,
                "unit": "%",
                "change": 2.95,
                "change_percent": 5.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.22,
                "min": 56.56,
                "max": 74.64,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.43,
                        "percentage": 27.6
                },
                {
                        "category": "Category B",
                        "value": 10.77,
                        "percentage": 18.1
                },
                {
                        "category": "Category C",
                        "value": 8.34,
                        "percentage": 14.0
                },
                {
                        "category": "Category D",
                        "value": 4.42,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 19.55,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.787946",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packaging Efficiency Rate"
        }
    },
}
