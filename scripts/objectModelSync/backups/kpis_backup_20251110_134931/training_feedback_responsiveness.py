"""
Training Feedback Responsiveness

The speed and quality of how sales training providers respond to and act on trainee feedback.
"""

TRAINING_FEEDBACK_RESPONSIVENESS = {
    "code": "TRAINING_FEEDBACK_RESPONSIVENESS",
    "name": "Training Feedback Responsiveness",
    "description": "The speed and quality of how sales training providers respond to and act on trainee feedback.",
    "formula": "Time Taken to Implement Changes Post-Feedback",
    "calculation_formula": "Time Taken to Implement Changes Post-Feedback",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Feedback Responsiveness to be added.",
    "trend_analysis": """

    * Increased responsiveness to training feedback may indicate a positive shift in the quality of sales training being provided.
    * Decreasing responsiveness could signal a decline in the effectiveness of the sales training program or a lack of attention to trainee feedback.
    
    """,
    "diagnostic_questions": """

    * Are there specific areas of the sales training program where feedback responsiveness is consistently low?
    * How do trainees perceive the impact of their feedback on the training content and delivery?
    
    """,
    "actionable_tips": """

    * Implement regular feedback collection mechanisms to ensure timely and comprehensive responses to trainee input.
    * Train sales managers and trainers on how to effectively analyze and act on feedback to continuously improve the training program.
    * Encourage open communication channels between trainees and training providers to address feedback in real-time.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of responsiveness over time.
    * Comparison bar charts to highlight differences in responsiveness across different training modules or providers.
    
    """,
    "risk_warnings": """

    * Poor responsiveness to feedback can lead to disengagement and reduced effectiveness of the sales training program.
    * Consistently low responsiveness may indicate a systemic issue in the training provider's ability to adapt and improve.
    
    """,
    "tracking_tools": """

    * Feedback management software to streamline the collection, analysis, and response to trainee feedback.
    * Training evaluation platforms that provide insights into the impact of feedback on training outcomes.
    
    """,
    "integration_points": """

    * Integrate feedback responsiveness data with sales performance metrics to understand the correlation between training improvements and sales results.
    * Link feedback responsiveness with employee development systems to identify training needs and opportunities for individual improvement.
    
    """,
    "change_impact_analysis": """

    * Improving feedback responsiveness can lead to a more engaged and skilled sales team, positively impacting overall sales performance.
    * On the other hand, a decline in responsiveness may result in decreased employee satisfaction and retention.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Feedback", "Deal", "Enablement Feedback", "Lead", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:25.110461"},
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
                        707.01,
                        748.57,
                        701.73,
                        764.86,
                        743.29,
                        695.97,
                        726.72,
                        737.82,
                        764.18,
                        802.86,
                        700.68,
                        740.52
                ],
                "unit": "units"
        },
        "current": {
                "value": 740.52,
                "unit": "units",
                "change": 39.84,
                "change_percent": 5.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 736.18,
                "min": 695.97,
                "max": 802.86,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 177.21,
                        "percentage": 23.9
                },
                {
                        "category": "Category B",
                        "value": 175.48,
                        "percentage": 23.7
                },
                {
                        "category": "Category C",
                        "value": 102.69,
                        "percentage": 13.9
                },
                {
                        "category": "Category D",
                        "value": 83.02,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 202.12,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.110461",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Training Feedback Responsiveness"
        }
    },
}
