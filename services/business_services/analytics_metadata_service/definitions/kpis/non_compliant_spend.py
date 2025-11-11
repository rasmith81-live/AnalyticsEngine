"""
Non-Compliant Spend

The amount of spending that does not comply with procurement policies or contracts.
"""

NON_COMPLIANT_SPEND = {
    "code": "NON_COMPLIANT_SPEND",
    "name": "Non-Compliant Spend",
    "description": "The amount of spending that does not comply with procurement policies or contracts.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Non-Compliant Spend to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Contract", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.080094"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        197.51,
                        83.85,
                        76.57,
                        206.59,
                        199.5,
                        82.96,
                        189.3,
                        87.57,
                        213.12,
                        218.3,
                        198.38,
                        110.57
                ],
                "unit": "units"
        },
        "current": {
                "value": 110.57,
                "unit": "units",
                "change": -87.81,
                "change_percent": -44.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 155.35,
                "min": 76.57,
                "max": 218.3,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 31.84,
                        "percentage": 28.8
                },
                {
                        "category": "Segment B",
                        "value": 23.72,
                        "percentage": 21.5
                },
                {
                        "category": "Segment C",
                        "value": 11.19,
                        "percentage": 10.1
                },
                {
                        "category": "Segment D",
                        "value": 9.22,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 34.6,
                        "percentage": 31.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.248046",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Non-Compliant Spend"
        }
    },
}
