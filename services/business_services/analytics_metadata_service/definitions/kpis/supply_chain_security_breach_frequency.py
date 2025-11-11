"""
Supply Chain Security Breach Frequency

The number of times the security of the supply chain is breached within a given period, indicating the effectiveness of security measures in place.
"""

SUPPLY_CHAIN_SECURITY_BREACH_FREQUENCY = {
    "code": "SUPPLY_CHAIN_SECURITY_BREACH_FREQUENCY",
    "name": "Supply Chain Security Breach Frequency",
    "description": "The number of times the security of the supply chain is breached within a given period, indicating the effectiveness of security measures in place.",
    "formula": "Total Number of Supply Chain Security Breaches / Time Period",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Security Breach Frequency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.673565"},
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
                        408,
                        435,
                        401,
                        411,
                        398,
                        421,
                        422,
                        410,
                        407,
                        413,
                        410,
                        435
                ],
                "unit": "count"
        },
        "current": {
                "value": 435,
                "unit": "count",
                "change": 25,
                "change_percent": 6.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 414.25,
                "min": 398,
                "max": 435,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 94.6,
                        "percentage": 21.7
                },
                {
                        "category": "Segment B",
                        "value": 101.81,
                        "percentage": 23.4
                },
                {
                        "category": "Segment C",
                        "value": 63.94,
                        "percentage": 14.7
                },
                {
                        "category": "Segment D",
                        "value": 25.62,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 149.03,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.651049",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Supply Chain Security Breach Frequency"
        }
    },
}
