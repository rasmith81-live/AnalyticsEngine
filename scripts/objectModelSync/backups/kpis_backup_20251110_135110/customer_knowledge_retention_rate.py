"""
Customer Knowledge Retention Rate

The rate at which customers retain the knowledge or training provided by the company over time.
"""

CUSTOMER_KNOWLEDGE_RETENTION_RATE = {
    "code": "CUSTOMER_KNOWLEDGE_RETENTION_RATE",
    "name": "Customer Knowledge Retention Rate",
    "description": "The rate at which customers retain the knowledge or training provided by the company over time.",
    "formula": "(Number of Correct Responses in Follow-Up Assessments / Total Number of Responses) * 100",
    "calculation_formula": "(Number of Correct Responses in Follow-Up Assessments / Total Number of Responses) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Knowledge Retention Rate to be added.",
    "trend_analysis": """


    * An increasing customer knowledge retention rate may indicate improved training programs or better customer engagement.
    * A decreasing rate could signal changes in the customer base, shifts in product complexity, or ineffective training methods.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific areas of training where customers consistently struggle to retain knowledge?
    * How does our customer knowledge retention rate compare with industry benchmarks or with different customer segments?
    
    
    """,
    "actionable_tips": """


    * Implement interactive and engaging training methods to improve knowledge retention.
    * Regularly assess and update training materials to ensure relevance and effectiveness.
    * Provide ongoing support and resources for customers to reinforce and apply their knowledge.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer knowledge retention rate over time.
    * Comparison charts to analyze retention rates across different training modules or customer segments.
    
    
    """,
    "risk_warnings": """


    * Low customer knowledge retention can lead to increased support costs and customer dissatisfaction.
    * Inconsistent knowledge retention may indicate a need for better alignment between training and customer needs.
    
    
    """,
    "tracking_tools": """


    * Learning management systems (LMS) to track and analyze customer engagement with training materials.
    * Customer relationship management (CRM) software to monitor customer feedback and support interactions related to training.
    
    
    """,
    "integration_points": """


    * Integrate customer knowledge retention data with product development to improve user experience and product usability.
    * Link retention rate with customer feedback systems to identify areas for improvement in training and support.
    
    
    """,
    "change_impact_analysis": """


    * Improving customer knowledge retention can lead to higher customer satisfaction and loyalty.
    * Conversely, a decline in retention rate may impact overall customer experience and brand perception.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Knowledge Base", "Lead", "Opportunity", "Partner Training", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.842433"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
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
                        47.49,
                        39.43,
                        36.12,
                        39.79,
                        42.99,
                        49.77,
                        36.19,
                        49.89,
                        33.64,
                        41.37,
                        37.22,
                        50.28
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.28,
                "unit": "%",
                "change": 13.06,
                "change_percent": 35.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 42.01,
                "min": 33.64,
                "max": 50.28,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.84,
                        "percentage": 23.5
                },
                {
                        "category": "Category B",
                        "value": 9.13,
                        "percentage": 18.2
                },
                {
                        "category": "Category C",
                        "value": 7.7,
                        "percentage": 15.3
                },
                {
                        "category": "Category D",
                        "value": 4.42,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 17.19,
                        "percentage": 34.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.291354",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Knowledge Retention Rate"
        }
    },
}
