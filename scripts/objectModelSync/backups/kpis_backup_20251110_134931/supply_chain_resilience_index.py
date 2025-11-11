"""
Supply Chain Resilience Index

A measure of the supply chain
"""

SUPPLY_CHAIN_RESILIENCE_INDEX = {
    "code": "SUPPLY_CHAIN_RESILIENCE_INDEX",
    "name": "Supply Chain Resilience Index",
    "description": "A measure of the supply chain",
    "formula": "Supply Chain Resilience Score",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Resilience Index to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.916623"},
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
                        93.3,
                        92.5,
                        92.3,
                        90.5,
                        87.1,
                        84.7,
                        85.4,
                        94.2,
                        81.4,
                        89.0,
                        82.5,
                        87.5
                ],
                "unit": "score"
        },
        "current": {
                "value": 87.5,
                "unit": "score",
                "change": 5.0,
                "change_percent": 6.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 88.37,
                "min": 81.4,
                "max": 94.2,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 29.11,
                        "percentage": 33.3
                },
                {
                        "category": "Category B",
                        "value": 15.53,
                        "percentage": 17.7
                },
                {
                        "category": "Category C",
                        "value": 10.96,
                        "percentage": 12.5
                },
                {
                        "category": "Category D",
                        "value": 3.42,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 28.48,
                        "percentage": 32.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.916623",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Resilience Index"
        }
    },
}
