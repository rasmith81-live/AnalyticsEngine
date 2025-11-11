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
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.800818"},
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
                        59.78,
                        65.43,
                        64.65,
                        63.84,
                        65.88,
                        66.37,
                        67.65,
                        52.8,
                        64.79,
                        61.59,
                        53.95,
                        62.55
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.55,
                "unit": "%",
                "change": 8.6,
                "change_percent": 15.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 62.44,
                "min": 52.8,
                "max": 67.65,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 17.38,
                        "percentage": 27.8
                },
                {
                        "category": "Existing Customers",
                        "value": 9.35,
                        "percentage": 14.9
                },
                {
                        "category": "VIP Customers",
                        "value": 8.16,
                        "percentage": 13.0
                },
                {
                        "category": "At-Risk Customers",
                        "value": 6.73,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 20.93,
                        "percentage": 33.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.595270",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Advocacy"
        }
    },
}
