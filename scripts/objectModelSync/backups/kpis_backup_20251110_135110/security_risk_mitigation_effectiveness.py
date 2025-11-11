"""
Security Risk Mitigation Effectiveness

The effectiveness of implemented measures to reduce supply chain security risks, measured by the reduction in identified risks over time.
"""

SECURITY_RISK_MITIGATION_EFFECTIVENESS = {
    "code": "SECURITY_RISK_MITIGATION_EFFECTIVENESS",
    "name": "Security Risk Mitigation Effectiveness",
    "description": "The effectiveness of implemented measures to reduce supply chain security risks, measured by the reduction in identified risks over time.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Risk Mitigation Effectiveness to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.560787"},
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
                        673.83,
                        620.62,
                        714.03,
                        712.19,
                        581.29,
                        603.51,
                        643.75,
                        648.1,
                        696.77,
                        717.97,
                        685.86,
                        695.66
                ],
                "unit": "units"
        },
        "current": {
                "value": 695.66,
                "unit": "units",
                "change": 9.8,
                "change_percent": 1.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 666.13,
                "min": 581.29,
                "max": 717.97,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 140.37,
                        "percentage": 20.2
                },
                {
                        "category": "Category B",
                        "value": 173.7,
                        "percentage": 25.0
                },
                {
                        "category": "Category C",
                        "value": 57.83,
                        "percentage": 8.3
                },
                {
                        "category": "Category D",
                        "value": 50.18,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 273.58,
                        "percentage": 39.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.735629",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Security Risk Mitigation Effectiveness"
        }
    },
}
