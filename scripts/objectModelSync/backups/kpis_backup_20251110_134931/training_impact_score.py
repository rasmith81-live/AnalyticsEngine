"""
Training Impact Score

The impact of training on sales performance, typically measured by improvements in sales metrics post-training.
"""

TRAINING_IMPACT_SCORE = {
    "code": "TRAINING_IMPACT_SCORE",
    "name": "Training Impact Score",
    "description": "The impact of training on sales performance, typically measured by improvements in sales metrics post-training.",
    "formula": "(Post-Training Sales Performance - Pre-Training Sales Performance) / Cost of Training",
    "calculation_formula": "(Post-Training Sales Performance - Pre-Training Sales Performance) / Cost of Training",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Impact Score to be added.",
    "trend_analysis": """

    * Improvements in sales metrics post-training may indicate the effectiveness of the training program and the willingness of sales teams to apply new knowledge.
    * Declines in sales metrics post-training could suggest that the training content was not relevant or that the implementation of new strategies was ineffective.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales metrics that show a clear improvement or decline after training sessions?
    * How do the improvements in sales metrics post-training compare to the initial goals set for the training program?
    
    """,
    "actionable_tips": """

    * Regularly assess the relevance and effectiveness of training content to ensure it aligns with the evolving needs of the sales team.
    * Provide ongoing coaching and support to reinforce the application of new knowledge and skills gained from training.
    * Encourage feedback from sales teams to identify areas for improvement in the training program.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of sales metrics before and after each training session.
    * Comparison bar charts displaying the performance of different sales teams or individuals pre and post-training.
    
    """,
    "risk_warnings": """

    * If improvements in sales metrics are not observed post-training, it may indicate a need for a more tailored or effective training approach.
    * Overreliance on training as a solution for poor sales performance without addressing other underlying issues can lead to wasted resources.
    
    """,
    "tracking_tools": """

    * CRM systems with training module integration to track the application of new skills and knowledge in real sales scenarios.
    * Sales performance analytics tools to measure the direct impact of training on specific sales metrics.
    
    """,
    "integration_points": """

    * Integrate training impact data with performance management systems to align individual and team goals with the outcomes of training.
    * Link training impact with customer feedback systems to understand the correlation between improved sales performance and customer satisfaction.
    
    """,
    "change_impact_analysis": """

    * Improving sales performance through training can lead to increased revenue and customer satisfaction, but may also require additional investment in ongoing training and support.
    * Failure to see improvements in sales metrics post-training can impact overall team morale and confidence in the effectiveness of training programs.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Enablement Feedback", "Enablement Platform", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:25.124356"},
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
                        68.0,
                        65.7,
                        65.8,
                        57.8,
                        68.2,
                        62.0,
                        58.3,
                        66.3,
                        64.3,
                        65.0,
                        67.5,
                        59.0
                ],
                "unit": "score"
        },
        "current": {
                "value": 59.0,
                "unit": "score",
                "change": -8.5,
                "change_percent": -12.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.99,
                "min": 57.8,
                "max": 68.2,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.01,
                        "percentage": 17.0
                },
                {
                        "category": "Category B",
                        "value": 16.19,
                        "percentage": 27.4
                },
                {
                        "category": "Category C",
                        "value": 7.02,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 6.68,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 19.1,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.124356",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Training Impact Score"
        }
    },
}
