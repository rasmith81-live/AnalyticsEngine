"""
Knowledge Base Utilization Rate

The usage rate of a self-service knowledge base by customers for problem-solving.
"""

KNOWLEDGE_BASE_UTILIZATION_RATE = {
    "code": "KNOWLEDGE_BASE_UTILIZATION_RATE",
    "name": "Knowledge Base Utilization Rate",
    "description": "The usage rate of a self-service knowledge base by customers for problem-solving.",
    "formula": "Number of Customer Interactions with Knowledge Base / Total Number of Customer Support Interactions",
    "calculation_formula": "Number of Customer Interactions with Knowledge Base / Total Number of Customer Support Interactions",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Knowledge Base Utilization Rate to be added.",
    "trend_analysis": """



    * An increasing knowledge base utilization rate may indicate a growing customer preference for self-service support and a positive shift towards more efficient problem-solving.
    * A decreasing rate could signal that the knowledge base content is outdated or not meeting customer needs, leading to negative performance shifts in customer satisfaction and support efficiency.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific topics or articles within the knowledge base that are frequently accessed by customers?
    * How does the knowledge base utilization rate correlate with customer support ticket volume or resolution times?
    
    
    
    """,
    "actionable_tips": """



    * Regularly update and expand the knowledge base content to address common customer issues and questions.
    * Promote the knowledge base as a primary resource for problem-solving through targeted customer communications and support channels.
    * Collect and analyze feedback from customers regarding the knowledge base usability and content relevance to make continuous improvements.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of knowledge base utilization rate over time.
    * Pie charts illustrating the distribution of knowledge base utilization across different categories or topics.
    
    
    
    """,
    "risk_warnings": """



    * A low knowledge base utilization rate may indicate a lack of customer awareness or trust in the self-service support option, leading to increased support costs and customer dissatisfaction.
    * High utilization without corresponding resolution rates could indicate that the knowledge base content is not effectively addressing customer issues, risking customer frustration and churn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems with integrated knowledge base functionality to track customer interactions and knowledge base usage.
    * Analytics tools like Google Analytics or Mixpanel to monitor and analyze knowledge base traffic and user behavior.
    
    
    
    """,
    "integration_points": """



    * Integrate knowledge base utilization data with customer satisfaction surveys and feedback collection systems to understand the impact on overall customer experience.
    * Link knowledge base usage metrics with employee performance evaluations to incentivize and reward effective knowledge base utilization in customer support interactions.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the knowledge base utilization rate can lead to reduced support costs and increased customer satisfaction, positively impacting overall customer success metrics.
    * Conversely, a declining utilization rate may lead to higher support costs and decreased customer satisfaction, affecting customer retention and loyalty.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Knowledge Base", "Product", "Product Usage", "Service Level Agreement", "Support Ticket"], "last_validated": "2025-11-10T13:49:32.994109"},
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
                        76.42,
                        75.14,
                        63.06,
                        70.23,
                        70.02,
                        78.75,
                        78.9,
                        78.46,
                        78.3,
                        75.9,
                        66.25,
                        71.03
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.03,
                "unit": "%",
                "change": 4.78,
                "change_percent": 7.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.54,
                "min": 63.06,
                "max": 78.9,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 14.87,
                        "percentage": 20.9
                },
                {
                        "category": "Existing Customers",
                        "value": 12.89,
                        "percentage": 18.1
                },
                {
                        "category": "VIP Customers",
                        "value": 10.68,
                        "percentage": 15.0
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.79,
                        "percentage": 6.7
                },
                {
                        "category": "Other",
                        "value": 27.8,
                        "percentage": 39.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.087416",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Knowledge Base Utilization Rate"
        }
    },
}
