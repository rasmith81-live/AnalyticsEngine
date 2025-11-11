"""
Interactive Training Engagement

The level of interaction and participation of sales reps in training sessions that require active engagement.
"""

INTERACTIVE_TRAINING_ENGAGEMENT = {
    "code": "INTERACTIVE_TRAINING_ENGAGEMENT",
    "name": "Interactive Training Engagement",
    "description": "The level of interaction and participation of sales reps in training sessions that require active engagement.",
    "formula": "Number of Interactive Activities Completed / Total Number of Interactive Activities Offered",
    "calculation_formula": "Number of Interactive Activities Completed / Total Number of Interactive Activities Offered",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Interactive Training Engagement to be added.",
    "trend_analysis": """


    * Increasing interactive training engagement may indicate a more motivated and engaged sales team.
    * Decreasing engagement could signal a need for more dynamic and interactive training methods.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific training topics or sessions that consistently receive higher engagement?
    * How does the level of engagement in training sessions correlate with sales performance?
    
    
    """,
    "actionable_tips": """


    * Implement gamification elements in training to increase engagement and participation.
    * Encourage open discussions and role-playing exercises to make training sessions more interactive.
    * Use real-life scenarios and case studies to make training content more relatable and engaging.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of engagement levels over time.
    * Comparison bar charts to visualize engagement levels across different training topics or sessions.
    
    
    """,
    "risk_warnings": """


    * Low engagement in training may lead to a lack of knowledge retention and application in real sales scenarios.
    * Consistently low engagement could indicate a disconnect between the training content and the needs of the sales team.
    
    
    """,
    "tracking_tools": """


    * Utilize learning management systems (LMS) to track and analyze engagement metrics in training sessions.
    * Use survey and feedback tools to gather insights from sales reps about the effectiveness of training sessions.
    
    
    """,
    "integration_points": """


    * Integrate engagement data with sales performance metrics to understand the impact of training on actual results.
    * Link engagement data with individual performance evaluations to identify correlations between engagement and sales success.
    
    
    """,
    "change_impact_analysis": """


    * Increasing engagement in training may lead to improved sales performance and customer satisfaction.
    * However, changes in training methods to boost engagement may require additional resources and time investment.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"], "last_validated": "2025-11-10T13:49:32.976514"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
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
                        96,
                        109,
                        132,
                        114,
                        126,
                        98,
                        125,
                        114,
                        118,
                        134,
                        134,
                        101
                ],
                "unit": "count"
        },
        "current": {
                "value": 101,
                "unit": "count",
                "change": -33,
                "change_percent": -24.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 116.75,
                "min": 96,
                "max": 134,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.55,
                        "percentage": 16.4
                },
                {
                        "category": "Category B",
                        "value": 14.7,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 13.48,
                        "percentage": 13.3
                },
                {
                        "category": "Category D",
                        "value": 13.99,
                        "percentage": 13.9
                },
                {
                        "category": "Other",
                        "value": 42.28,
                        "percentage": 41.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.527621",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Interactive Training Engagement"
        }
    },
}
