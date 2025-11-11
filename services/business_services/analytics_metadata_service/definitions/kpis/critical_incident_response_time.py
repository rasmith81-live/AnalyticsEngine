"""
Critical Incident Response Time

The time taken to respond to and address critical incidents in the supply chain, affecting continuity and resilience.
"""

CRITICAL_INCIDENT_RESPONSE_TIME = {
    "code": "CRITICAL_INCIDENT_RESPONSE_TIME",
    "name": "Critical Incident Response Time",
    "description": "The time taken to respond to and address critical incidents in the supply chain, affecting continuity and resilience.",
    "formula": "Time of Incident Resolution - Time of Incident Identification",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Critical Incident Response Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.783127"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        12.3,
                        14.3,
                        12.3,
                        12.5,
                        18.9,
                        16.2,
                        12.7,
                        17.2,
                        17.9,
                        13.0,
                        12.3,
                        12.4
                ],
                "unit": "days"
        },
        "current": {
                "value": 12.4,
                "unit": "days",
                "change": 0.1,
                "change_percent": 0.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 14.33,
                "min": 12.3,
                "max": 18.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.78,
                        "percentage": 22.4
                },
                {
                        "category": "Segment B",
                        "value": 2.92,
                        "percentage": 23.5
                },
                {
                        "category": "Segment C",
                        "value": 1.43,
                        "percentage": 11.5
                },
                {
                        "category": "Segment D",
                        "value": 1.14,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 4.13,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.570595",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Critical Incident Response Time"
        }
    },
}
