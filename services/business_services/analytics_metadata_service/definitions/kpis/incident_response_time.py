"""
Incident Response Time

The average time it takes for the organization to respond to a supply chain security incident, reflecting the efficiency and preparedness of the response team.
"""

INCIDENT_RESPONSE_TIME = {
    "code": "INCIDENT_RESPONSE_TIME",
    "name": "Incident Response Time",
    "description": "The average time it takes for the organization to respond to a supply chain security incident, reflecting the efficiency and preparedness of the response team.",
    "formula": "Sum of Response Times for All Incidents / Number of Incidents",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Incident Response Time to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.972134"},
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
                        70,
                        50,
                        78,
                        66,
                        82,
                        77,
                        66,
                        50,
                        71,
                        95,
                        70,
                        68
                ],
                "unit": "count"
        },
        "current": {
                "value": 68,
                "unit": "count",
                "change": -2,
                "change_percent": -2.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 70.25,
                "min": 50,
                "max": 95,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.1,
                        "percentage": 22.2
                },
                {
                        "category": "Segment B",
                        "value": 16.77,
                        "percentage": 24.7
                },
                {
                        "category": "Segment C",
                        "value": 8.2,
                        "percentage": 12.1
                },
                {
                        "category": "Segment D",
                        "value": 4.68,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 23.25,
                        "percentage": 34.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.028014",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Incident Response Time"
        }
    },
}
