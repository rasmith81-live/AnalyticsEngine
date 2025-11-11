"""
Post-Training Support Satisfaction

The satisfaction of sales reps with the support they receive after completing training.
"""

POST_TRAINING_SUPPORT_SATISFACTION = {
    "code": "POST_TRAINING_SUPPORT_SATISFACTION",
    "name": "Post-Training Support Satisfaction",
    "description": "The satisfaction of sales reps with the support they receive after completing training.",
    "formula": "Average of Satisfaction Scores Collected from Post-Training Surveys",
    "calculation_formula": "Average of Satisfaction Scores Collected from Post-Training Surveys",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Post-Training Support Satisfaction to be added.",
    "trend_analysis": """



    * Increasing satisfaction with post-training support may indicate a positive impact on sales performance and confidence.
    * Decreasing satisfaction could signal a need for improved or more personalized support strategies.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas where sales reps feel they need more support after training?
    * How does the satisfaction level compare with the actual support provided, and are there any gaps?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular check-ins or follow-up sessions to address any post-training challenges or questions.
    * Provide access to additional resources or mentors for ongoing support and guidance.
    * Collect feedback from sales reps to continuously improve and tailor post-training support to their needs.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of satisfaction levels over time.
    * Comparison bar charts to analyze satisfaction levels across different support strategies or resources.
    
    
    
    """,
    "risk_warnings": """



    * Low satisfaction with post-training support can lead to decreased motivation and performance among sales reps.
    * Consistently low satisfaction may indicate a need for a complete overhaul of the support system.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with feedback and survey capabilities to gather and analyze post-training support satisfaction data.
    * Learning management systems to track and monitor the utilization of post-training resources and support materials.
    
    
    
    """,
    "integration_points": """



    * Integrate post-training support satisfaction data with sales performance metrics to understand the impact on results.
    * Link with HR systems to identify any correlations between post-training support and employee retention or turnover.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving post-training support satisfaction can lead to increased sales productivity and effectiveness.
    * Conversely, low satisfaction can result in higher turnover rates and a negative impact on the overall sales team morale.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Support Ticket", "Training Program"], "last_validated": "2025-11-10T13:49:33.251443"},
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
                        885.41,
                        943.88,
                        997.81,
                        1029.06,
                        1002.34,
                        884.08,
                        949.88,
                        1023.35,
                        919.45,
                        1013.7,
                        988.12,
                        1002.76
                ],
                "unit": "units"
        },
        "current": {
                "value": 1002.76,
                "unit": "units",
                "change": 14.64,
                "change_percent": 1.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 969.99,
                "min": 884.08,
                "max": 1029.06,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 278.25,
                        "percentage": 27.7
                },
                {
                        "category": "Segment B",
                        "value": 186.11,
                        "percentage": 18.6
                },
                {
                        "category": "Segment C",
                        "value": 85.34,
                        "percentage": 8.5
                },
                {
                        "category": "Segment D",
                        "value": 57.67,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 395.39,
                        "percentage": 39.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.591484",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Post-Training Support Satisfaction"
        }
    },
}
