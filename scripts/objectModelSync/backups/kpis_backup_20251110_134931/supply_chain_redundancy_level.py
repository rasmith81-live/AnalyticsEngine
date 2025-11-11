"""
Supply Chain Redundancy Level

The level of redundancy built into the supply chain to ensure continuity in the event of a disruption or security breach.
"""

SUPPLY_CHAIN_REDUNDANCY_LEVEL = {
    "code": "SUPPLY_CHAIN_REDUNDANCY_LEVEL",
    "name": "Supply Chain Redundancy Level",
    "description": "The level of redundancy built into the supply chain to ensure continuity in the event of a disruption or security breach.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Redundancy Level to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.913490"},
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
                        439.49,
                        526.16,
                        503.14,
                        504.64,
                        447.95,
                        439.67,
                        436.04,
                        531.13,
                        500.73,
                        390.35,
                        394.77,
                        414.86
                ],
                "unit": "units"
        },
        "current": {
                "value": 414.86,
                "unit": "units",
                "change": 20.09,
                "change_percent": 5.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 460.74,
                "min": 390.35,
                "max": 531.13,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 93.4,
                        "percentage": 22.5
                },
                {
                        "category": "Category B",
                        "value": 60.37,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 54.71,
                        "percentage": 13.2
                },
                {
                        "category": "Category D",
                        "value": 40.11,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 166.27,
                        "percentage": 40.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.913490",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Redundancy Level"
        }
    },
}
