"""
Carrier Compliance Rate

The percentage of deliveries that comply with the carrier’s requirements and standards.
"""

CARRIER_COMPLIANCE_RATE = {
    "code": "CARRIER_COMPLIANCE_RATE",
    "name": "Carrier Compliance Rate",
    "description": "The percentage of deliveries that comply with the carrier\u2019s requirements and standards.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Carrier Compliance Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:32.674414"},
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
                        73.61,
                        66.71,
                        62.14,
                        70.99,
                        60.46,
                        74.18,
                        63.9,
                        66.68,
                        62.83,
                        67.95,
                        67.55,
                        71.8
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.8,
                "unit": "%",
                "change": 4.25,
                "change_percent": 6.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.4,
                "min": 60.46,
                "max": 74.18,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18.95,
                        "percentage": 26.4
                },
                {
                        "category": "Segment B",
                        "value": 10.13,
                        "percentage": 14.1
                },
                {
                        "category": "Segment C",
                        "value": 13.31,
                        "percentage": 18.5
                },
                {
                        "category": "Segment D",
                        "value": 4.9,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 24.51,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.420845",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Carrier Compliance Rate"
        }
    },
}
