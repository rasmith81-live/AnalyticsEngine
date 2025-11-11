"""
Counterfeit Product Rate

The rate at which counterfeit products are identified within the supply chain, indicating the effectiveness of security measures to protect product authenticity.
"""

COUNTERFEIT_PRODUCT_RATE = {
    "code": "COUNTERFEIT_PRODUCT_RATE",
    "name": "Counterfeit Product Rate",
    "description": "The rate at which counterfeit products are identified within the supply chain, indicating the effectiveness of security measures to protect product authenticity.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Counterfeit Product Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:43:23.187418"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        81.13,
                        71.07,
                        72.13,
                        87.79,
                        79.19,
                        85.12,
                        87.19,
                        76.85,
                        88.12,
                        81.78,
                        72.86,
                        86.2
                ],
                "unit": "%"
        },
        "current": {
                "value": 86.2,
                "unit": "%",
                "change": 13.34,
                "change_percent": 18.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 80.79,
                "min": 71.07,
                "max": 88.12,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 24.69,
                        "percentage": 28.6
                },
                {
                        "category": "Category B",
                        "value": 14.62,
                        "percentage": 17.0
                },
                {
                        "category": "Category C",
                        "value": 7.58,
                        "percentage": 8.8
                },
                {
                        "category": "Category D",
                        "value": 5.97,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 33.34,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.187418",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Counterfeit Product Rate"
        }
    },
}
