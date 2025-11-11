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
                        65.04,
                        52.6,
                        48.15,
                        56.51,
                        49.43,
                        51.59,
                        50.48,
                        57.07,
                        57.13,
                        48.79,
                        60.58,
                        63.67
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.67,
                "unit": "%",
                "change": 3.09,
                "change_percent": 5.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 55.09,
                "min": 48.15,
                "max": 65.04,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.15,
                        "percentage": 34.8
                },
                {
                        "category": "Category B",
                        "value": 9.64,
                        "percentage": 15.1
                },
                {
                        "category": "Category C",
                        "value": 7.12,
                        "percentage": 11.2
                },
                {
                        "category": "Category D",
                        "value": 7.41,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 17.35,
                        "percentage": 27.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.569938",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Knowledge Base Utilization Rate"
        }
    },
}
