"""
Deal Size

The average value of closed deals.
"""

DEAL_SIZE = {
    "code": "DEAL_SIZE",
    "name": "Deal Size",
    "description": "The average value of closed deals.",
    "formula": "Total Revenue from Closed Deals / Number of Closed Deals",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Size to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal"], "last_validated": "2025-11-10T13:49:32.911021"},
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
                        430,
                        438,
                        436,
                        440,
                        450,
                        427,
                        462,
                        433,
                        465,
                        430,
                        442,
                        474
                ],
                "unit": "count"
        },
        "current": {
                "value": 474,
                "unit": "count",
                "change": 32,
                "change_percent": 7.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 443.92,
                "min": 427,
                "max": 474,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 119.17,
                        "percentage": 25.1
                },
                {
                        "category": "Segment B",
                        "value": 82.18,
                        "percentage": 17.3
                },
                {
                        "category": "Segment C",
                        "value": 65.76,
                        "percentage": 13.9
                },
                {
                        "category": "Segment D",
                        "value": 45.36,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 161.53,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.883579",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Deal Size"
        }
    },
}
