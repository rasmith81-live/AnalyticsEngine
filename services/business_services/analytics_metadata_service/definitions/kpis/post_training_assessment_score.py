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
                        522,
                        495,
                        509,
                        507,
                        477,
                        522,
                        478,
                        519,
                        489,
                        504,
                        502,
                        517
                ],
                "unit": "count"
        },
        "current": {
                "value": 517,
                "unit": "count",
                "change": 15,
                "change_percent": 3.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 503.42,
                "min": 477,
                "max": 522,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 130.6,
                        "percentage": 25.3
                },
                {
                        "category": "Segment B",
                        "value": 133.14,
                        "percentage": 25.8
                },
                {
                        "category": "Segment C",
                        "value": 77.39,
                        "percentage": 15.0
                },
                {
                        "category": "Segment D",
                        "value": 18.54,
                        "percentage": 3.6
                },
                {
                        "category": "Other",
                        "value": 157.33,
                        "percentage": 30.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.587863",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Post-Training Assessment Score"
        }
    },
}
