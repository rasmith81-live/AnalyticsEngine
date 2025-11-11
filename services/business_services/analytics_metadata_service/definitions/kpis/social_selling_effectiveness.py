"""
Social Selling Effectiveness

A measure of how effectively the sales team uses social media channels to engage with prospects, build relationships, and close deals.
"""

SOCIAL_SELLING_EFFECTIVENESS = {
    "code": "SOCIAL_SELLING_EFFECTIVENESS",
    "name": "Social Selling Effectiveness",
    "description": "A measure of how effectively the sales team uses social media channels to engage with prospects, build relationships, and close deals.",
    "formula": "(Number of Leads or Sales Attributed to Social Media Efforts / Total Number of Leads or Sales) * 100",
    "calculation_formula": "(Number of Leads or Sales Attributed to Social Media Efforts / Total Number of Leads or Sales) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Social Selling Effectiveness to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal", "Lead"], "last_validated": "2025-11-10T13:49:33.580494"},
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
                        60.42,
                        65.73,
                        49.39,
                        57.46,
                        54.69,
                        67.52,
                        53.6,
                        54.23,
                        58.05,
                        51.24,
                        54.09,
                        56.67
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.67,
                "unit": "%",
                "change": 2.58,
                "change_percent": 4.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 56.92,
                "min": 49.39,
                "max": 67.52,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 8.66,
                        "percentage": 15.3
                },
                {
                        "category": "Channel Sales",
                        "value": 15.55,
                        "percentage": 27.4
                },
                {
                        "category": "Online Sales",
                        "value": 11.12,
                        "percentage": 19.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 2.31,
                        "percentage": 4.1
                },
                {
                        "category": "Other",
                        "value": 19.03,
                        "percentage": 33.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.396681",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Social Selling Effectiveness"
        }
    },
}
