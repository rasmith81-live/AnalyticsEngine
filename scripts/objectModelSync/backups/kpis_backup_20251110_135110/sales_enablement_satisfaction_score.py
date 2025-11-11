"""
Sales Enablement Satisfaction Score

Sales team members' satisfaction with the support and resources provided by the Sales Enablement Team.
"""

SALES_ENABLEMENT_SATISFACTION_SCORE = {
    "code": "SALES_ENABLEMENT_SATISFACTION_SCORE",
    "name": "Sales Enablement Satisfaction Score",
    "description": "Sales team members' satisfaction with the support and resources provided by the Sales Enablement Team.",
    "formula": "Average Satisfaction Score on Sales Enablement Surveys",
    "calculation_formula": "Average Satisfaction Score on Sales Enablement Surveys",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Enablement Satisfaction Score to be added.",
    "trend_analysis": """


    * Increasing satisfaction scores may indicate improved sales team performance and effectiveness of enablement resources.
    * Decreasing scores could signal a lack of alignment between enablement efforts and sales team needs or changing market dynamics.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific resources or tools that sales team members find most valuable?
    * How does the satisfaction score correlate with sales performance metrics such as win rates or deal sizes?
    
    
    """,
    "actionable_tips": """


    * Regularly gather feedback from sales team members to understand their evolving needs and challenges.
    * Customize enablement resources and training programs to address specific pain points or skill gaps identified by the sales team.
    * Provide ongoing coaching and support to ensure sales team members can effectively leverage enablement resources in their day-to-day activities.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of satisfaction scores over time.
    * Comparison bar charts to visualize satisfaction scores across different sales teams or regions.
    
    
    """,
    "risk_warnings": """


    * Low satisfaction scores may lead to decreased motivation and engagement among the sales team.
    * Consistently low scores could indicate a need for significant changes in enablement strategies to avoid negative impacts on overall sales performance.
    
    
    """,
    "tracking_tools": """


    * CRM systems with built-in feedback and survey capabilities to collect and analyze satisfaction scores from sales team members.
    * Training and content management platforms to ensure easy access to relevant resources and materials for the sales team.
    
    
    """,
    "integration_points": """


    * Integrate satisfaction score data with performance management systems to identify correlations between enablement satisfaction and sales results.
    * Link satisfaction scores with learning management systems to tailor training and development programs based on feedback from the sales team.
    
    
    """,
    "change_impact_analysis": """


    * Improving satisfaction scores can lead to increased sales productivity and effectiveness, positively impacting revenue and customer relationships.
    * Conversely, declining satisfaction scores may result in missed sales opportunities and reduced customer satisfaction, affecting overall business performance.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.422405"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        88.9,
                        76.8,
                        87.8,
                        87.1,
                        88.0,
                        82.3,
                        85.8,
                        84.1,
                        86.6,
                        84.7,
                        87.8,
                        88.1
                ],
                "unit": "score"
        },
        "current": {
                "value": 88.1,
                "unit": "score",
                "change": 0.3,
                "change_percent": 0.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 85.67,
                "min": 76.8,
                "max": 88.9,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.72,
                        "percentage": 15.6
                },
                {
                        "category": "Category B",
                        "value": 20.38,
                        "percentage": 23.1
                },
                {
                        "category": "Category C",
                        "value": 18.18,
                        "percentage": 20.6
                },
                {
                        "category": "Category D",
                        "value": 5.75,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 30.07,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.391782",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Enablement Satisfaction Score"
        }
    },
}
