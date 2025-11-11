"""
Sales Confidence Increase

A metric that tracks the increase in sales reps' confidence after training and coaching interventions.
"""

SALES_CONFIDENCE_INCREASE = {
    "code": "SALES_CONFIDENCE_INCREASE",
    "name": "Sales Confidence Increase",
    "description": "A metric that tracks the increase in sales reps' confidence after training and coaching interventions.",
    "formula": "(Average Confidence Level Post-Training - Average Confidence Level Pre-Training) / Average Confidence Level Pre-Training * 100",
    "calculation_formula": "(Average Confidence Level Post-Training - Average Confidence Level Pre-Training) / Average Confidence Level Pre-Training * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Confidence Increase to be added.",
    "trend_analysis": """



    * An increasing sales confidence may indicate the effectiveness of training and coaching interventions.
    * A decreasing confidence level could signal a need for reevaluation of training methods or individual coaching approaches.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas or topics where sales reps consistently show lower confidence levels?
    * How do the confidence levels of top-performing sales reps compare to those who are struggling?
    
    
    
    """,
    "actionable_tips": """



    * Provide personalized coaching and training to address individual sales reps' areas of low confidence.
    * Implement regular feedback sessions to reinforce positive behaviors and build confidence.
    * Create a supportive and collaborative team environment to boost overall confidence levels.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts tracking the average confidence levels over time for the entire sales team or specific individuals.
    * Radar charts comparing confidence levels across different sales competencies or skills.
    
    
    
    """,
    "risk_warnings": """



    * Low confidence levels can lead to decreased motivation and performance among sales reps.
    * Consistently low confidence across the team may indicate systemic issues in training or coaching methods.
    
    
    
    """,
    "tracking_tools": """



    * Utilize sales performance management software to track and analyze individual sales reps' confidence levels.
    * Implement video coaching platforms to provide personalized feedback and support for sales reps.
    
    
    
    """,
    "integration_points": """



    * Integrate sales confidence data with performance management systems to identify correlations between confidence levels and sales results.
    * Link confidence tracking with customer relationship management (CRM) systems to understand the impact on customer interactions and outcomes.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing sales confidence can lead to higher motivation, improved customer interactions, and ultimately, increased sales performance.
    * However, overly confident sales reps may need additional monitoring to ensure they maintain professionalism and accuracy in their interactions.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"], "last_validated": "2025-11-10T13:49:33.391729"},
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
                        58.22,
                        57.76,
                        54.43,
                        55.68,
                        47.23,
                        48.85,
                        47.09,
                        56.52,
                        63.36,
                        50.65,
                        65.22,
                        46.78
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.78,
                "unit": "%",
                "change": -18.44,
                "change_percent": -28.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 54.32,
                "min": 46.78,
                "max": 65.22,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 7.96,
                        "percentage": 17.0
                },
                {
                        "category": "Channel Sales",
                        "value": 8.26,
                        "percentage": 17.7
                },
                {
                        "category": "Online Sales",
                        "value": 9.88,
                        "percentage": 21.1
                },
                {
                        "category": "Enterprise Sales",
                        "value": 2.9,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 17.78,
                        "percentage": 38.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.907610",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Confidence Increase"
        }
    },
}
