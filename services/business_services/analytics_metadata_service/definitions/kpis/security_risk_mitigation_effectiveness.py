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
                        342.67,
                        383.42,
                        482.29,
                        479.09,
                        379.89,
                        451.48,
                        434.28,
                        431.94,
                        391.55,
                        482.45,
                        417.55,
                        370.39
                ],
                "unit": "units"
        },
        "current": {
                "value": 370.39,
                "unit": "units",
                "change": -47.16,
                "change_percent": -11.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 420.58,
                "min": 342.67,
                "max": 482.45,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 117.62,
                        "percentage": 31.8
                },
                {
                        "category": "Segment B",
                        "value": 52.69,
                        "percentage": 14.2
                },
                {
                        "category": "Segment C",
                        "value": 53.49,
                        "percentage": 14.4
                },
                {
                        "category": "Segment D",
                        "value": 15.28,
                        "percentage": 4.1
                },
                {
                        "category": "Other",
                        "value": 131.31,
                        "percentage": 35.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.349778",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Security Risk Mitigation Effectiveness"
        }
    },
}
