"""
Packaging Innovation Index

A measure of the adoption and implementation of innovative packaging solutions, highlighting competitiveness and adaptability.
"""

PACKAGING_INNOVATION_INDEX = {
    "code": "PACKAGING_INNOVATION_INDEX",
    "name": "Packaging Innovation Index",
    "description": "A measure of the adoption and implementation of innovative packaging solutions, highlighting competitiveness and adaptability.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Innovation Index to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.144731"},
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
                        79.8,
                        80.5,
                        76.8,
                        84.9,
                        81.8,
                        76.3,
                        72.8,
                        72.8,
                        77.6,
                        77.3,
                        80.2,
                        74.0
                ],
                "unit": "score"
        },
        "current": {
                "value": 74.0,
                "unit": "score",
                "change": -6.2,
                "change_percent": -7.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 77.9,
                "min": 72.8,
                "max": 84.9,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.93,
                        "percentage": 22.9
                },
                {
                        "category": "Category B",
                        "value": 12.94,
                        "percentage": 17.5
                },
                {
                        "category": "Category C",
                        "value": 6.91,
                        "percentage": 9.3
                },
                {
                        "category": "Category D",
                        "value": 5.48,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 31.74,
                        "percentage": 42.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.790641",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Packaging Innovation Index"
        }
    },
}
