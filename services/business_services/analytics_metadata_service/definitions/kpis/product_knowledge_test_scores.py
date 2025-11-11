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
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Knowledge Base", "Partner Training", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.264482"},
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
                        68.8,
                        71.5,
                        70.0,
                        67.7,
                        71.1,
                        74.8,
                        71.8,
                        67.1,
                        76.2,
                        68.9,
                        69.4,
                        73.2
                ],
                "unit": "score"
        },
        "current": {
                "value": 73.2,
                "unit": "score",
                "change": 3.8,
                "change_percent": 5.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 70.88,
                "min": 67.1,
                "max": 76.2,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 22.55,
                        "percentage": 30.8
                },
                {
                        "category": "Product Line B",
                        "value": 16.68,
                        "percentage": 22.8
                },
                {
                        "category": "Product Line C",
                        "value": 6.64,
                        "percentage": 9.1
                },
                {
                        "category": "Services",
                        "value": 3.17,
                        "percentage": 4.3
                },
                {
                        "category": "Other",
                        "value": 24.16,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.627714",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Product Knowledge Test Scores"
        }
    },
}
