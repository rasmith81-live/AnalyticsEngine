"""
Customer Advocacy

The level at which customers are willing to positively promote the company to others.
"""

CUSTOMER_ADVOCACY = {
    "code": "CUSTOMER_ADVOCACY",
    "name": "Customer Advocacy",
    "description": "The level at which customers are willing to positively promote the company to others.",
    "formula": "(Number of Advocating Customers / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Advocating Customers / Total Number of Customers) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Advocacy to be added.",
    "trend_analysis": """

    * An increasing customer advocacy level may indicate a positive shift in customer satisfaction and brand loyalty.
    * A decreasing advocacy level could signal dissatisfaction with products or services, leading to potential customer churn.
    
    """,
    "diagnostic_questions": """

    * What specific actions or experiences have led customers to advocate for the company?
    * Are there any common complaints or issues that could be impacting customer advocacy?
    
    """,
    "actionable_tips": """

    * Focus on delivering exceptional customer service to create positive advocacy experiences.
    * Implement loyalty programs or referral incentives to encourage customers to advocate for the company.
    * Regularly solicit feedback from customers to identify areas for improvement and address any issues impacting advocacy.
    
    """,
    "visualization_suggestions": """

    * Net Promoter Score (NPS) charts to track the overall level of customer advocacy over time.
    * Word cloud visualizations to highlight the most commonly used positive words or phrases by customers when advocating for the company.
    
    """,
    "risk_warnings": """

    * Low customer advocacy can lead to negative word-of-mouth and a decline in new customer acquisition.
    * Unaddressed customer complaints or issues may further erode advocacy and damage the company's reputation.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) systems to track customer interactions and feedback.
    * Social listening tools to monitor online conversations and sentiment about the company.
    
    """,
    "integration_points": """

    * Integrate customer advocacy data with sales and marketing systems to better understand the impact on customer acquisition and retention.
    * Link advocacy metrics with product development and quality assurance processes to address any recurring issues.
    
    """,
    "change_impact_analysis": """

    * Increasing customer advocacy can lead to higher customer lifetime value and improved brand reputation.
    * Conversely, a decline in advocacy may result in increased marketing costs to acquire new customers and mitigate negative sentiment.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.208396"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION"],
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
                        167,
                        167,
                        197,
                        170,
                        161,
                        158,
                        158,
                        191,
                        176,
                        184,
                        151,
                        165
                ],
                "unit": "count"
        },
        "current": {
                "value": 165,
                "unit": "count",
                "change": 14,
                "change_percent": 9.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 170.42,
                "min": 151,
                "max": 197,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 35.4,
                        "percentage": 21.5
                },
                {
                        "category": "Category B",
                        "value": 37.21,
                        "percentage": 22.6
                },
                {
                        "category": "Category C",
                        "value": 29.16,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 9.32,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 53.91,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.208396",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Advocacy"
        }
    },
}
