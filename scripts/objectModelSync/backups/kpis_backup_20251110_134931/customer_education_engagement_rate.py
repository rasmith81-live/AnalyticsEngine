"""
Customer Education Engagement Rate

The engagement level of customers with educational content or training provided by the company.
"""

CUSTOMER_EDUCATION_ENGAGEMENT_RATE = {
    "code": "CUSTOMER_EDUCATION_ENGAGEMENT_RATE",
    "name": "Customer Education Engagement Rate",
    "description": "The engagement level of customers with educational content or training provided by the company.",
    "formula": "(Number of Customers Engaging with Education Content / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Engaging with Education Content / Total Number of Customers) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Education Engagement Rate to be added.",
    "trend_analysis": """

    * An increasing customer education engagement rate may indicate a growing interest in learning more about the products or services offered.
    * A decreasing rate could signal a lack of interest in educational content or a need to improve the quality and relevance of the materials provided.
    
    """,
    "diagnostic_questions": """

    * Are there specific topics or types of educational content that customers engage with more than others?
    * How does the customer education engagement rate correlate with customer satisfaction or retention?
    
    """,
    "actionable_tips": """

    * Regularly update and refresh educational content to keep it relevant and engaging for customers.
    * Personalize educational materials to cater to different customer segments and their specific needs.
    * Collect feedback from customers on the educational content to understand what resonates with them and what needs improvement.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of customer education engagement rate over time.
    * Comparison charts to visualize the engagement rates for different types of educational content or training.
    
    """,
    "risk_warnings": """

    * A consistently low customer education engagement rate may indicate a disconnect between the content provided and customer needs, leading to decreased customer satisfaction and retention.
    * High engagement with irrelevant or low-quality educational content can also have a negative impact on customer perception of the brand.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) systems with built-in educational content tracking and analysis capabilities.
    * Learning management systems (LMS) for delivering and managing educational content in a structured and organized manner.
    
    """,
    "integration_points": """

    * Integrate customer education engagement data with customer feedback and satisfaction metrics to gain a comprehensive understanding of the impact of educational content on customer relationships.
    * Link engagement data with sales performance metrics to assess the influence of customer education on sales outcomes.
    
    """,
    "change_impact_analysis": """

    * Improving the customer education engagement rate can lead to better-informed customers, potentially resulting in higher sales and customer retention.
    * Conversely, a decline in the engagement rate may indicate a need to reevaluate the effectiveness of the educational content and its impact on overall business performance.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Partner Training", "Prospect Engagement", "Sales Content", "Sales Training Program", "Service Level Agreement", "Training Program"], "replaces": ["CUSTOMER_EDUCATION_COMPLETION_RATE"], "last_validated": "2025-11-10T13:43:23.234831"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_RETENTION",
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
                        65.62,
                        83.63,
                        77.35,
                        65.87,
                        67.8,
                        73.81,
                        64.21,
                        76.15,
                        81.81,
                        65.43,
                        73.01,
                        72.64
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.64,
                "unit": "%",
                "change": -0.37,
                "change_percent": -0.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 72.28,
                "min": 64.21,
                "max": 83.63,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.0,
                        "percentage": 17.9
                },
                {
                        "category": "Category B",
                        "value": 11.75,
                        "percentage": 16.2
                },
                {
                        "category": "Category C",
                        "value": 7.19,
                        "percentage": 9.9
                },
                {
                        "category": "Category D",
                        "value": 5.31,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 35.39,
                        "percentage": 48.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.234831",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Education Engagement Rate"
        }
    },
}
