"""
Packaging Sustainability Score

A composite score measuring various sustainability factors such as recyclability, biodegradability, and carbon footprint of packaging materials.
"""

PACKAGING_SUSTAINABILITY_SCORE = {
    "code": "PACKAGING_SUSTAINABILITY_SCORE",
    "name": "Packaging Sustainability Score",
    "description": "A composite score measuring various sustainability factors such as recyclability, biodegradability, and carbon footprint of packaging materials.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Sustainability Score to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.794825"},
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
                        91.3,
                        93.7,
                        85.4,
                        88.7,
                        96.1,
                        92.8,
                        89.5,
                        87.7,
                        96.6,
                        84.2,
                        92.8,
                        90.7
                ],
                "unit": "score"
        },
        "current": {
                "value": 90.7,
                "unit": "score",
                "change": -2.1,
                "change_percent": -2.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 90.79,
                "min": 84.2,
                "max": 96.6,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.0,
                        "percentage": 24.3
                },
                {
                        "category": "Category B",
                        "value": 12.76,
                        "percentage": 14.1
                },
                {
                        "category": "Category C",
                        "value": 12.07,
                        "percentage": 13.3
                },
                {
                        "category": "Category D",
                        "value": 4.54,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 39.33,
                        "percentage": 43.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.794825",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Packaging Sustainability Score"
        }
    },
}
