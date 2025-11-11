"""
Business Continuity Plan Effectiveness

The effectiveness of the business continuity plan as it relates to supply chain operations, which is essential for maintaining operations during and after security incidents.
"""

BUSINESS_CONTINUITY_PLAN_EFFECTIVENESS = {
    "code": "BUSINESS_CONTINUITY_PLAN_EFFECTIVENESS",
    "name": "Business Continuity Plan Effectiveness",
    "description": "The effectiveness of the business continuity plan as it relates to supply chain operations, which is essential for maintaining operations during and after security incidents.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Business Continuity Plan Effectiveness to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.061189"},
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
                        205.42,
                        116.65,
                        198.92,
                        165.98,
                        198.09,
                        108.56,
                        102.11,
                        164.2,
                        150.06,
                        227.38,
                        103.59,
                        128.14
                ],
                "unit": "units"
        },
        "current": {
                "value": 128.14,
                "unit": "units",
                "change": 24.55,
                "change_percent": 23.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 155.76,
                "min": 102.11,
                "max": 227.38,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.1,
                        "percentage": 17.2
                },
                {
                        "category": "Category B",
                        "value": 24.74,
                        "percentage": 19.3
                },
                {
                        "category": "Category C",
                        "value": 21.22,
                        "percentage": 16.6
                },
                {
                        "category": "Category D",
                        "value": 6.45,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 53.63,
                        "percentage": 41.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.061189",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Business Continuity Plan Effectiveness"
        }
    },
}
