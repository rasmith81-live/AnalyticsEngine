"""
Sustainable Packaging Index

A measure of the percentage of packaging materials that are recyclable or biodegradable, reflecting environmentally friendly practices.
"""

SUSTAINABLE_PACKAGING_INDEX = {
    "code": "SUSTAINABLE_PACKAGING_INDEX",
    "name": "Sustainable Packaging Index",
    "description": "A measure of the percentage of packaging materials that are recyclable or biodegradable, reflecting environmentally friendly practices.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sustainable Packaging Index to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.693147"},
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
                        93.6,
                        81.6,
                        82.5,
                        84.8,
                        92.4,
                        87.8,
                        85.8,
                        81.1,
                        81.5,
                        93.4,
                        86.2,
                        82.1
                ],
                "unit": "score"
        },
        "current": {
                "value": 82.1,
                "unit": "score",
                "change": -4.1,
                "change_percent": -4.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 86.07,
                "min": 81.1,
                "max": 93.6,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 25.87,
                        "percentage": 31.5
                },
                {
                        "category": "Category B",
                        "value": 13.1,
                        "percentage": 16.0
                },
                {
                        "category": "Category C",
                        "value": 14.72,
                        "percentage": 17.9
                },
                {
                        "category": "Category D",
                        "value": 4.93,
                        "percentage": 6.0
                },
                {
                        "category": "Other",
                        "value": 23.48,
                        "percentage": 28.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.967727",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sustainable Packaging Index"
        }
    },
}
