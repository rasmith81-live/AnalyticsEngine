"""
Cross-docking Efficiency

The effectiveness of moving incoming goods directly to outbound shipping with no storage time.
"""

CROSS_DOCKING_EFFICIENCY = {
    "code": "CROSS_DOCKING_EFFICIENCY",
    "name": "Cross-docking Efficiency",
    "description": "The effectiveness of moving incoming goods directly to outbound shipping with no storage time.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cross-docking Efficiency to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:43:23.194839"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        286.48,
                        280.25,
                        414.08,
                        278.46,
                        284.99,
                        348.55,
                        385.38,
                        411.15,
                        361.35,
                        302.42,
                        359.6,
                        402.5
                ],
                "unit": "units"
        },
        "current": {
                "value": 402.5,
                "unit": "units",
                "change": 42.9,
                "change_percent": 11.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 342.93,
                "min": 278.46,
                "max": 414.08,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 80.43,
                        "percentage": 20.0
                },
                {
                        "category": "Category B",
                        "value": 90.1,
                        "percentage": 22.4
                },
                {
                        "category": "Category C",
                        "value": 60.28,
                        "percentage": 15.0
                },
                {
                        "category": "Category D",
                        "value": 34.98,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 136.71,
                        "percentage": 34.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.194839",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Cross-docking Efficiency"
        }
    },
}
