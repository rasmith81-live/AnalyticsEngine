"""
Waste Reduction in Supply Chain

The percentage reduction of waste generated throughout the supply chain, aligning with ISO 20400
"""

WASTE_REDUCTION_IN_SUPPLY_CHAIN = {
    "code": "WASTE_REDUCTION_IN_SUPPLY_CHAIN",
    "name": "Waste Reduction in Supply Chain",
    "description": "The percentage reduction of waste generated throughout the supply chain, aligning with ISO 20400",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Waste Reduction in Supply Chain to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": [], "last_validated": "2025-11-10T13:43:25.269024"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        314.71,
                        335.65,
                        279.69,
                        251.69,
                        311.44,
                        346.54,
                        334.54,
                        323.95,
                        290.07,
                        361.69,
                        355.57,
                        260.79
                ],
                "unit": "units"
        },
        "current": {
                "value": 260.79,
                "unit": "units",
                "change": -94.78,
                "change_percent": -26.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 313.86,
                "min": 251.69,
                "max": 361.69,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 52.99,
                        "percentage": 20.3
                },
                {
                        "category": "Category B",
                        "value": 45.3,
                        "percentage": 17.4
                },
                {
                        "category": "Category C",
                        "value": 48.84,
                        "percentage": 18.7
                },
                {
                        "category": "Category D",
                        "value": 27.14,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 86.52,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.269024",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Waste Reduction in Supply Chain"
        }
    },
}
