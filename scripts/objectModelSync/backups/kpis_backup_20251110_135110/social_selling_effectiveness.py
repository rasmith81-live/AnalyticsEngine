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
                        325.35,
                        320.38,
                        276.28,
                        368.34,
                        352.57,
                        239.91,
                        245.07,
                        252.36,
                        241.01,
                        223.24,
                        232.7,
                        224.89
                ],
                "unit": "units"
        },
        "current": {
                "value": 224.89,
                "unit": "units",
                "change": -7.81,
                "change_percent": -3.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 275.18,
                "min": 223.24,
                "max": 368.34,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 48.9,
                        "percentage": 21.7
                },
                {
                        "category": "Category B",
                        "value": 27.98,
                        "percentage": 12.4
                },
                {
                        "category": "Category C",
                        "value": 42.5,
                        "percentage": 18.9
                },
                {
                        "category": "Category D",
                        "value": 12.53,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 92.98,
                        "percentage": 41.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.778127",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Social Selling Effectiveness"
        }
    },
}
