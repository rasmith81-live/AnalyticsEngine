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
                        71.84,
                        75.86,
                        62.27,
                        66.61,
                        75.11,
                        70.08,
                        63.12,
                        62.96,
                        72.2,
                        62.93,
                        65.97,
                        62.96
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.96,
                "unit": "%",
                "change": -3.01,
                "change_percent": -4.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.66,
                "min": 62.27,
                "max": 75.86,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 18.89,
                        "percentage": 30.0
                },
                {
                        "category": "Existing Customers",
                        "value": 13.71,
                        "percentage": 21.8
                },
                {
                        "category": "VIP Customers",
                        "value": 9.2,
                        "percentage": 14.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.96,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 15.2,
                        "percentage": 24.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.706330",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Knowledge Retention Rate"
        }
    },
}
