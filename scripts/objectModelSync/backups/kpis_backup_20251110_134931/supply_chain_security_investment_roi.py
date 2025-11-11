"""
Supply Chain Security Investment ROI

The return on investment for security measures implemented within the supply chain, demonstrating the financial impact of security investments.
"""

SUPPLY_CHAIN_SECURITY_INVESTMENT_ROI = {
    "code": "SUPPLY_CHAIN_SECURITY_INVESTMENT_ROI",
    "name": "Supply Chain Security Investment ROI",
    "description": "The return on investment for security measures implemented within the supply chain, demonstrating the financial impact of security investments.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Security Investment ROI to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Return"], "last_validated": "2025-11-10T13:43:24.937046"},
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
                        269.69,
                        258.56,
                        349.69,
                        329.05,
                        331.52,
                        263.35,
                        384.04,
                        305.22,
                        278.91,
                        372.24,
                        323.96,
                        372.24
                ],
                "unit": "units"
        },
        "current": {
                "value": 372.24,
                "unit": "units",
                "change": 48.28,
                "change_percent": 14.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 319.87,
                "min": 258.56,
                "max": 384.04,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 64.28,
                        "percentage": 17.3
                },
                {
                        "category": "Category B",
                        "value": 106.2,
                        "percentage": 28.5
                },
                {
                        "category": "Category C",
                        "value": 41.13,
                        "percentage": 11.0
                },
                {
                        "category": "Category D",
                        "value": 19.25,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 141.38,
                        "percentage": 38.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.937046",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Security Investment ROI"
        }
    },
}
