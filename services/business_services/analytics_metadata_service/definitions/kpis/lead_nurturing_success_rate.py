"""
Lead Nurturing Success Rate

The percentage of leads that become opportunities as a result of lead nurturing efforts.
"""

LEAD_NURTURING_SUCCESS_RATE = {
    "code": "LEAD_NURTURING_SUCCESS_RATE",
    "name": "Lead Nurturing Success Rate",
    "description": "The percentage of leads that become opportunities as a result of lead nurturing efforts.",
    "formula": "(Number of Nurtured Leads Converted / Total Number of Nurtured Leads) * 100",
    "calculation_formula": "(Number of Nurtured Leads Converted / Total Number of Nurtured Leads) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Nurturing Success Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.005011"},
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
                        75.41,
                        63.73,
                        56.63,
                        63.43,
                        72.32,
                        70.19,
                        71.42,
                        59.27,
                        69.48,
                        64.33,
                        68.39,
                        63.95
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.95,
                "unit": "%",
                "change": -4.44,
                "change_percent": -6.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 66.55,
                "min": 56.63,
                "max": 75.41,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.32,
                        "percentage": 20.8
                },
                {
                        "category": "Segment B",
                        "value": 11.46,
                        "percentage": 17.9
                },
                {
                        "category": "Segment C",
                        "value": 8.87,
                        "percentage": 13.9
                },
                {
                        "category": "Segment D",
                        "value": 6.29,
                        "percentage": 9.8
                },
                {
                        "category": "Other",
                        "value": 24.01,
                        "percentage": 37.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.104007",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Lead Nurturing Success Rate"
        }
    },
}
