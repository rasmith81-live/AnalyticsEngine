"""
Sales Force Engagement Level

The degree to which a sales representative actively engages in sales activities and goals.
"""

SALES_FORCE_ENGAGEMENT_LEVEL = {
    "code": "SALES_FORCE_ENGAGEMENT_LEVEL",
    "name": "Sales Force Engagement Level",
    "description": "The degree to which a sales representative actively engages in sales activities and goals.",
    "formula": "No Standard Formula - This KPI is typically assessed through a combination of activity metrics and qualitative analysis.",
    "calculation_formula": "No Standard Formula - This KPI is typically assessed through a combination of activity metrics and qualitative analysis.",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Force Engagement Level to be added.",
    "trend_analysis": """



    * An increasing sales force engagement level may indicate a more motivated and productive sales team.
    * A decreasing engagement level could signal dissatisfaction, burnout, or lack of alignment with sales goals.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales activities or targets that sales representatives struggle to engage with?
    * How does the current engagement level compare with historical data or industry benchmarks?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular feedback sessions and coaching to keep sales representatives motivated and aligned with goals.
    * Provide clear and achievable sales targets to maintain engagement and focus.
    * Utilize sales performance management software to track and analyze individual engagement levels.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of engagement levels over time for each sales representative.
    * Pie charts to compare the distribution of engagement levels across different sales territories or product lines.
    
    
    
    """,
    "risk_warnings": """



    * Low engagement levels can lead to decreased sales performance and missed opportunities.
    * High engagement levels without corresponding results may indicate misaligned goals or ineffective sales strategies.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with built-in engagement tracking and reporting capabilities.
    * Sales enablement platforms to provide sales representatives with the necessary tools and resources for effective engagement.
    
    
    
    """,
    "integration_points": """



    * Integrate engagement level data with performance reviews and incentive programs to align recognition and rewards with actual engagement.
    * Link engagement data with customer relationship management systems to understand the impact of engagement on customer interactions and satisfaction.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving sales force engagement can lead to increased sales productivity and revenue generation.
    * However, a focus solely on engagement without corresponding results may lead to inefficiencies and wasted resources.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Competitive Analysis", "Customer", "Goal", "Lead", "Outbound Call", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.426815"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_STRATEGY"],
    "module_code": "OUTSIDE_SALES",
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
                        250.22,
                        201.6,
                        208.14,
                        317.08,
                        292.34,
                        321.16,
                        315.85,
                        267.18,
                        194.79,
                        290.21,
                        270.91,
                        287.36
                ],
                "unit": "units"
        },
        "current": {
                "value": 287.36,
                "unit": "units",
                "change": 16.45,
                "change_percent": 6.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 268.07,
                "min": 194.79,
                "max": 321.16,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 73.85,
                        "percentage": 25.7
                },
                {
                        "category": "Channel Sales",
                        "value": 46.14,
                        "percentage": 16.1
                },
                {
                        "category": "Online Sales",
                        "value": 50.67,
                        "percentage": 17.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 30.05,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 86.65,
                        "percentage": 30.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.000027",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Force Engagement Level"
        }
    },
}
