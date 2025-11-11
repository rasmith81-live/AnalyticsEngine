"""
Training Participation Rate

The percentage of eligible sales reps who actively participate in training programs.
"""

TRAINING_PARTICIPATION_RATE = {
    "code": "TRAINING_PARTICIPATION_RATE",
    "name": "Training Participation Rate",
    "description": "The percentage of eligible sales reps who actively participate in training programs.",
    "formula": "(Number of Employees Who Completed Training / Total Number of Employees Eligible for Training) * 100",
    "calculation_formula": "(Number of Employees Who Completed Training / Total Number of Employees Eligible for Training) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Participation Rate to be added.",
    "trend_analysis": """

    * Training participation rate may show an initial increase as new training programs are introduced, followed by a gradual decline as the novelty wears off.
    * An upward trend could indicate a positive shift in the company culture towards continuous learning and development, while a downward trend may signal disengagement or lack of perceived value in the training programs.
    
    """,
    "diagnostic_questions": """

    * What are the common reasons for sales reps to opt out of training programs?
    * How does the participation rate vary across different sales teams or regions, and what factors contribute to these differences?
    
    """,
    "actionable_tips": """

    * Offer incentives or rewards for active participation in training programs to boost engagement.
    * Customize training content to be more relevant and tailored to the specific needs and challenges faced by the sales reps.
    * Implement a mentorship or coaching program to provide ongoing support and reinforcement of the training content.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the participation rate over time, with different lines representing different sales teams or regions for comparison.
    * Pie charts to illustrate the distribution of participation across different training programs or modules.
    
    """,
    "risk_warnings": """

    * A consistently low participation rate may indicate a disconnect between the training content and the actual needs of the sales reps, leading to wasted resources and ineffective training.
    * High participation rates without corresponding improvements in sales performance may suggest that the training content is not impactful or that the application of the learning is lacking.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) to track and analyze participation rates, completion rates, and feedback from sales reps regarding the training programs.
    * Survey and feedback tools to gather insights from sales reps about their training preferences and needs.
    
    """,
    "integration_points": """

    * Integrate training participation data with sales performance metrics to identify correlations between training engagement and sales results.
    * Link participation rates with individual performance evaluations to assess the impact of training on individual sales rep effectiveness.
    
    """,
    "change_impact_analysis": """

    * Improving the training participation rate can lead to a more knowledgeable and skilled sales force, potentially resulting in increased sales and customer satisfaction.
    * However, a high participation rate without tangible improvements in sales performance may indicate a need to reassess the quality and relevance of the training content.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:25.132269"},
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
                        86.88,
                        79.92,
                        84.45,
                        69.28,
                        86.92,
                        81.37,
                        79.85,
                        87.84,
                        78.73,
                        73.47,
                        88.06,
                        81.04
                ],
                "unit": "%"
        },
        "current": {
                "value": 81.04,
                "unit": "%",
                "change": -7.02,
                "change_percent": -8.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 81.48,
                "min": 69.28,
                "max": 88.06,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.08,
                        "percentage": 22.3
                },
                {
                        "category": "Category B",
                        "value": 15.37,
                        "percentage": 19.0
                },
                {
                        "category": "Category C",
                        "value": 7.64,
                        "percentage": 9.4
                },
                {
                        "category": "Category D",
                        "value": 6.13,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 33.82,
                        "percentage": 41.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.132269",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Training Participation Rate"
        }
    },
}
