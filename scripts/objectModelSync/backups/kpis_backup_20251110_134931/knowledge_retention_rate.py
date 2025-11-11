"""
Knowledge Retention Rate

The percentage of training information and skills retained by sales reps over time.
"""

KNOWLEDGE_RETENTION_RATE = {
    "code": "KNOWLEDGE_RETENTION_RATE",
    "name": "Knowledge Retention Rate",
    "description": "The percentage of training information and skills retained by sales reps over time.",
    "formula": "(Number of Correct Responses in Follow-up Assessments / Total Number of Assessment Questions) * 100",
    "calculation_formula": "(Number of Correct Responses in Follow-up Assessments / Total Number of Assessment Questions) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Knowledge Retention Rate to be added.",
    "trend_analysis": """

    * Knowledge retention rate may initially increase after training but gradually decline over time without reinforcement.
    * Positive trends may indicate effective coaching and ongoing support, while negative trends could signal a need for refresher training or improved coaching techniques.
    
    """,
    "diagnostic_questions": """

    * Are there specific training modules or skills that sales reps struggle to retain?
    * How do our knowledge retention rates compare with industry benchmarks or best practices?
    
    """,
    "actionable_tips": """

    * Implement spaced repetition techniques to reinforce training material at regular intervals.
    * Encourage peer-to-peer knowledge sharing and mentoring to solidify learning through teaching.
    * Provide ongoing coaching and support to help sales reps apply and retain new knowledge and skills.
    
    """,
    "visualization_suggestions": """

    * Line charts showing knowledge retention rates over time for different training modules.
    * Comparison bar charts to visualize retention rates across different sales teams or regions.
    
    """,
    "risk_warnings": """

    * Low knowledge retention rates can lead to decreased sales performance and missed opportunities.
    * Inconsistent retention may indicate a need for improved training content or delivery methods.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) with built-in assessment and tracking features to monitor knowledge retention.
    * Interactive e-learning platforms that offer quizzes, simulations, and interactive exercises to reinforce learning.
    
    """,
    "integration_points": """

    * Integrate knowledge retention data with performance management systems to correlate retention with sales results.
    * Link retention rates with individual coaching and development plans to tailor support based on specific needs.
    
    """,
    "change_impact_analysis": """

    * Improving knowledge retention can lead to more effective sales conversations and higher customer satisfaction.
    * However, investing in retention strategies may require allocating resources and time away from other sales activities.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Customer", "Deal", "Knowledge Base", "Lead", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.572626"},
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
                        46.98,
                        56.37,
                        59.67,
                        42.93,
                        46.54,
                        47.29,
                        47.77,
                        50.58,
                        46.93,
                        50.32,
                        51.25,
                        59.82
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.82,
                "unit": "%",
                "change": 8.57,
                "change_percent": 16.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 50.54,
                "min": 42.93,
                "max": 59.82,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.85,
                        "percentage": 23.2
                },
                {
                        "category": "Category B",
                        "value": 9.71,
                        "percentage": 16.2
                },
                {
                        "category": "Category C",
                        "value": 7.1,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 4.79,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 24.37,
                        "percentage": 40.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.572626",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Knowledge Retention Rate"
        }
    },
}
