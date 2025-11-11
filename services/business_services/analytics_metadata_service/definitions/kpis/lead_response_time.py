"""
Lead Response Time

The time it takes for a sales representative to respond to a new lead.
"""

LEAD_RESPONSE_TIME = {
    "code": "LEAD_RESPONSE_TIME",
    "name": "Lead Response Time",
    "description": "The time it takes for a sales representative to respond to a new lead.",
    "formula": "Total Time Taken to Respond to Leads / Total Number of Leads",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Response Time to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.012193"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        473,
                        473,
                        502,
                        477,
                        470,
                        514,
                        498,
                        503,
                        489,
                        515,
                        493,
                        478
                ],
                "unit": "count"
        },
        "current": {
                "value": 478,
                "unit": "count",
                "change": -15,
                "change_percent": -3.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 490.42,
                "min": 470,
                "max": 515,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 140.41,
                        "percentage": 29.4
                },
                {
                        "category": "Segment B",
                        "value": 78.98,
                        "percentage": 16.5
                },
                {
                        "category": "Segment C",
                        "value": 86.04,
                        "percentage": 18.0
                },
                {
                        "category": "Segment D",
                        "value": 49.8,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 122.77,
                        "percentage": 25.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.122924",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Lead Response Time"
        }
    },
}
