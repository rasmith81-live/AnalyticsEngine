"""
Sales Onboarding Feedback Score

The average feedback score from new sales reps about the onboarding and training process.
"""

SALES_ONBOARDING_FEEDBACK_SCORE = {
    "code": "SALES_ONBOARDING_FEEDBACK_SCORE",
    "name": "Sales Onboarding Feedback Score",
    "description": "The average feedback score from new sales reps about the onboarding and training process.",
    "formula": "Average of Feedback Scores Collected from New Sales Reps",
    "calculation_formula": "Average of Feedback Scores Collected from New Sales Reps",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Onboarding Feedback Score to be added.",
    "trend_analysis": """



    * Increasing feedback scores may indicate a more effective onboarding process and better training materials.
    * Decreasing scores could signal issues with the onboarding program or a lack of support for new sales reps.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific aspects of the onboarding process that new sales reps consistently rate poorly?
    * How does the feedback score compare with industry benchmarks or with feedback from more tenured sales reps?
    
    
    
    """,
    "actionable_tips": """



    * Regularly update onboarding materials to reflect changes in products, processes, or market conditions.
    * Provide mentors or coaches for new sales reps to offer ongoing support and guidance beyond initial training.
    * Collect feedback from new sales reps at multiple points during the onboarding process to identify and address issues in real-time.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average feedback score over time to track improvements or declines.
    * Pie charts comparing feedback scores for different training modules or aspects of the onboarding process.
    
    
    
    """,
    "risk_warnings": """



    * Low feedback scores may lead to higher turnover among new sales reps and increased recruitment costs.
    * Consistently poor feedback could indicate a need for a complete overhaul of the onboarding program.
    
    
    
    """,
    "tracking_tools": """



    * Feedback collection and analysis tools like SurveyMonkey or Qualtrics to gather and interpret new sales rep feedback.
    * Learning management systems (LMS) to deliver and track onboarding materials and assessments.
    
    
    
    """,
    "integration_points": """



    * Integrate feedback scores with performance management systems to identify correlations between onboarding experience and subsequent sales performance.
    * Link feedback data with HR systems to track the impact of onboarding on employee retention and satisfaction.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the onboarding feedback score can lead to higher sales productivity and better customer interactions.
    * Conversely, a poor onboarding experience may result in lost sales opportunities and damage to the company's reputation.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Feedback", "Customer Onboarding", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.444111"},
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
                        84.0,
                        80.9,
                        90.4,
                        84.4,
                        87.4,
                        82.0,
                        90.8,
                        86.1,
                        81.9,
                        86.0,
                        86.7,
                        85.9
                ],
                "unit": "score"
        },
        "current": {
                "value": 85.9,
                "unit": "score",
                "change": -0.8,
                "change_percent": -0.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 85.54,
                "min": 80.9,
                "max": 90.8,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 28.88,
                        "percentage": 33.6
                },
                {
                        "category": "Channel Sales",
                        "value": 14.02,
                        "percentage": 16.3
                },
                {
                        "category": "Online Sales",
                        "value": 12.84,
                        "percentage": 14.9
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.93,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 25.23,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.045526",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Onboarding Feedback Score"
        }
    },
}
