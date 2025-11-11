"""
Product Knowledge Test Scores

Average scores on product knowledge tests taken by sales reps after training.
"""

PRODUCT_KNOWLEDGE_TEST_SCORES = {
    "code": "PRODUCT_KNOWLEDGE_TEST_SCORES",
    "name": "Product Knowledge Test Scores",
    "description": "Average scores on product knowledge tests taken by sales reps after training.",
    "formula": "Average of Product Knowledge Test Scores",
    "calculation_formula": "Average of Product Knowledge Test Scores",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Knowledge Test Scores to be added.",
    "trend_analysis": """

    * Increasing average scores may indicate improved training effectiveness or better product understanding among sales reps.
    * Decreasing scores could signal a need for updated training materials or a lack of product knowledge retention.
    
    """,
    "diagnostic_questions": """

    * Are there specific product areas where sales reps consistently score lower on the knowledge tests?
    * How do the average scores compare with the performance of top-performing sales reps?
    
    """,
    "actionable_tips": """

    * Regularly update training materials to reflect new product features or changes.
    * Implement regular refresher training sessions to reinforce product knowledge and ensure retention.
    * Encourage a culture of continuous learning and knowledge sharing among sales reps.
    
    """,
    "visualization_suggestions": """

    * Line charts showing average scores over time to identify trends in knowledge retention.
    * Comparison bar charts to visualize differences in scores across different product categories or sales teams.
    
    """,
    "risk_warnings": """

    * Low average scores may lead to decreased sales performance and missed opportunities.
    * Inaccurate product knowledge can result in customer dissatisfaction and lost sales.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) to track and manage training materials and assessments.
    * Knowledge management platforms to facilitate easy access to product information for sales reps.
    
    """,
    "integration_points": """

    * Integrate product knowledge test results with individual performance evaluations to identify areas for improvement.
    * Link training and assessment data with customer feedback to understand the impact of product knowledge on customer satisfaction.
    
    """,
    "change_impact_analysis": """

    * Improving product knowledge can lead to increased customer confidence and higher sales conversion rates.
    * Conversely, a decline in average scores may result in decreased customer trust and satisfaction, impacting sales performance.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Knowledge Base", "Partner Training", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.967956"},
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
                        89.1,
                        89.8,
                        86.5,
                        90.0,
                        92.4,
                        90.4,
                        87.1,
                        89.0,
                        80.6,
                        87.1,
                        91.9,
                        91.7
                ],
                "unit": "score"
        },
        "current": {
                "value": 91.7,
                "unit": "score",
                "change": -0.2,
                "change_percent": -0.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 88.8,
                "min": 80.6,
                "max": 92.4,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 25.14,
                        "percentage": 27.4
                },
                {
                        "category": "Category B",
                        "value": 10.4,
                        "percentage": 11.3
                },
                {
                        "category": "Category C",
                        "value": 18.68,
                        "percentage": 20.4
                },
                {
                        "category": "Category D",
                        "value": 7.87,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 29.61,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.967956",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Product Knowledge Test Scores"
        }
    },
}
