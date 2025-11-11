"""
Training Effectiveness

The percentage of sales reps who rate the training and coaching as effective. A higher rating indicates effective training and coaching.
"""

TRAINING_EFFECTIVENESS = {
    "code": "TRAINING_EFFECTIVENESS",
    "name": "Training Effectiveness",
    "description": "The percentage of sales reps who rate the training and coaching as effective. A higher rating indicates effective training and coaching.",
    "formula": "Composite Score from Effectiveness Surveys and Performance Improvements",
    "calculation_formula": "Composite Score from Effectiveness Surveys and Performance Improvements",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Effectiveness to be added.",
    "trend_analysis": """

    * An increasing percentage of sales reps rating the training and coaching as effective may indicate a positive shift in performance and skill development.
    * A decreasing percentage could signal a decline in the quality of training and coaching, leading to potential negative impacts on sales performance.
    
    """,
    "diagnostic_questions": """

    * Are there specific areas of the training and coaching program that receive consistently lower ratings?
    * How do the ratings for training and coaching correlate with actual sales performance and targets?
    
    """,
    "actionable_tips": """

    * Regularly solicit feedback from sales reps to identify areas for improvement in the training and coaching program.
    * Provide additional resources and support for sales reps who may require extra assistance in implementing the training and coaching content.
    * Implement a mentorship program to pair experienced sales reps with those who may benefit from additional guidance and support.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of the percentage of sales reps rating the training and coaching as effective over time.
    * Comparative bar charts displaying the effectiveness ratings across different sales teams or regions.
    
    """,
    "risk_warnings": """

    * A consistently low percentage of sales reps rating the training and coaching as effective may lead to decreased motivation and performance.
    * Failure to address issues with training and coaching effectiveness could result in increased turnover and recruitment costs.
    
    """,
    "tracking_tools": """

    * Utilize survey and feedback tools to gather and analyze ratings and comments from sales reps regarding the training and coaching program.
    * Implement learning management systems (LMS) to track the completion and effectiveness of training modules and coaching sessions.
    
    """,
    "integration_points": """

    * Integrate training and coaching effectiveness data with sales performance metrics to identify correlations and areas for improvement.
    * Link feedback from sales reps regarding training and coaching to performance management and development plans.
    
    """,
    "change_impact_analysis": """

    * Improving the effectiveness of training and coaching can lead to increased sales productivity and revenue generation.
    * Conversely, a decline in training and coaching effectiveness may result in missed sales opportunities and reduced customer satisfaction.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer Feedback", "Enablement Feedback", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:25.106833"},
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
                        296.63,
                        259.61,
                        345.4,
                        305.38,
                        267.24,
                        340.6,
                        392.21,
                        257.92,
                        375.5,
                        324.69,
                        271.99,
                        371.29
                ],
                "unit": "units"
        },
        "current": {
                "value": 371.29,
                "unit": "units",
                "change": 99.3,
                "change_percent": 36.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 317.37,
                "min": 257.92,
                "max": 392.21,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 69.59,
                        "percentage": 18.7
                },
                {
                        "category": "Category B",
                        "value": 58.14,
                        "percentage": 15.7
                },
                {
                        "category": "Category C",
                        "value": 39.4,
                        "percentage": 10.6
                },
                {
                        "category": "Category D",
                        "value": 24.43,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 179.73,
                        "percentage": 48.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.106833",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Training Effectiveness"
        }
    },
}
