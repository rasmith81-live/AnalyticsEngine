"""
Post-Training Assessment Score

The average scores of sales reps on assessments administered after training completion.
"""

POST_TRAINING_ASSESSMENT_SCORE = {
    "code": "POST_TRAINING_ASSESSMENT_SCORE",
    "name": "Post-Training Assessment Score",
    "description": "The average scores of sales reps on assessments administered after training completion.",
    "formula": "Sum of Assessment Scores / Number of Assessments Administered",
    "calculation_formula": "Sum of Assessment Scores / Number of Assessments Administered",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Post-Training Assessment Score to be added.",
    "trend_analysis": """


    * Increasing post-training assessment scores may indicate the effectiveness of the training program and improved knowledge retention among sales reps.
    * Decreasing scores could signal a need for reevaluation of the training content, delivery methods, or individual coaching needs.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific areas or topics where sales reps consistently score lower on post-training assessments?
    * How do the post-training assessment scores correlate with actual sales performance and quota attainment?
    
    
    """,
    "actionable_tips": """


    * Provide ongoing coaching and reinforcement of training materials to ensure long-term retention and application of knowledge.
    * Customize training programs to address specific knowledge gaps identified through post-training assessments.
    * Implement mentorship programs or peer-to-peer learning initiatives to support continuous learning and skill development.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of average assessment scores over time to visualize improvements or declines.
    * Comparison bar charts to highlight the performance of different sales teams or individuals in post-training assessments.
    
    
    """,
    "risk_warnings": """


    * Consistently low post-training assessment scores may indicate a need for more comprehensive training programs or individual coaching interventions.
    * High variability in scores across different sales teams or regions could signal inconsistent training delivery or support.
    
    
    """,
    "tracking_tools": """


    * Learning management systems (LMS) to track and analyze post-training assessment scores across the sales organization.
    * Assessment and survey tools to gather feedback from sales reps on the effectiveness of training programs and areas for improvement.
    
    
    """,
    "integration_points": """


    * Integrate post-training assessment data with sales performance metrics to identify correlations between training effectiveness and actual results.
    * Link assessment scores with individual development plans and performance reviews to drive continuous improvement and skill enhancement.
    
    
    """,
    "change_impact_analysis": """


    * Improving post-training assessment scores can lead to increased sales productivity, higher customer satisfaction, and improved revenue generation.
    * On the other hand, declining scores may result in missed sales opportunities, decreased confidence among sales reps, and potential turnover.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.249841"},
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
                        303,
                        344,
                        311,
                        307,
                        324,
                        336,
                        328,
                        310,
                        338,
                        314,
                        321,
                        326
                ],
                "unit": "count"
        },
        "current": {
                "value": 326,
                "unit": "count",
                "change": 5,
                "change_percent": 1.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 321.83,
                "min": 303,
                "max": 344,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 80.16,
                        "percentage": 24.6
                },
                {
                        "category": "Category B",
                        "value": 43.15,
                        "percentage": 13.2
                },
                {
                        "category": "Category C",
                        "value": 39.62,
                        "percentage": 12.2
                },
                {
                        "category": "Category D",
                        "value": 30.65,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 132.42,
                        "percentage": 40.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.943438",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Post-Training Assessment Score"
        }
    },
}
