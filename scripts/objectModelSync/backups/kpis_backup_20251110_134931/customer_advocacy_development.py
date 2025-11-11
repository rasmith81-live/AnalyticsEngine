"""
Customer Advocacy Development

The process and effectiveness of turning key account customers into advocates for the company.
"""

CUSTOMER_ADVOCACY_DEVELOPMENT = {
    "code": "CUSTOMER_ADVOCACY_DEVELOPMENT",
    "name": "Customer Advocacy Development",
    "description": "The process and effectiveness of turning key account customers into advocates for the company.",
    "formula": "(Number of Advocates at End of Period - Number of Advocates at Start of Period) / Number of Advocates at Start of Period * 100",
    "calculation_formula": "(Number of Advocates at End of Period - Number of Advocates at Start of Period) / Number of Advocates at Start of Period * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Advocacy Development to be added.",
    "trend_analysis": """

    * An increasing number of key account customers becoming advocates may indicate a positive shift in customer satisfaction and loyalty.
    * A decreasing trend in customer advocacy development could signal dissatisfaction with the company's products or services.
    
    """,
    "diagnostic_questions": """

    * What specific actions or initiatives have been taken to turn key account customers into advocates?
    * Are there any common reasons or feedback from key account customers who have not become advocates?
    
    """,
    "actionable_tips": """

    * Implement a formal customer advocacy program to recognize and reward key account customers who promote the company.
    * Provide exceptional customer service and personalized experiences to encourage advocacy.
    * Regularly communicate with key account customers to understand their needs and address any concerns.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the growth or decline in the number of key account customers who have become advocates over time.
    * Pie charts illustrating the distribution of key account customers based on their advocacy level (advocate, neutral, detractor).
    
    """,
    "risk_warnings": """

    * Low levels of customer advocacy may result in reduced referrals and recommendations, impacting new customer acquisition.
    * Key account customers who are not advocates may share negative experiences, leading to potential reputation damage.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and manage interactions with key account customers.
    * Advocacy marketing platforms to facilitate the creation and management of customer advocacy programs.
    
    """,
    "integration_points": """

    * Integrate customer advocacy data with sales and marketing systems to identify opportunities for targeted advocacy campaigns.
    * Link customer advocacy metrics with customer feedback and satisfaction scores to gain a comprehensive view of customer sentiment.
    
    """,
    "change_impact_analysis": """

    * Increased customer advocacy can lead to higher customer retention and lifetime value.
    * On the other hand, a decline in customer advocacy may result in decreased revenue and market share.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Sales Process Workflow"], "last_validated": "2025-11-10T13:43:23.210909"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        269,
                        271,
                        283,
                        287,
                        262,
                        298,
                        256,
                        295,
                        260,
                        280,
                        291,
                        259
                ],
                "unit": "count"
        },
        "current": {
                "value": 259,
                "unit": "count",
                "change": -32,
                "change_percent": -11.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 275.92,
                "min": 256,
                "max": 298,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 63.31,
                        "percentage": 24.4
                },
                {
                        "category": "Category B",
                        "value": 57.25,
                        "percentage": 22.1
                },
                {
                        "category": "Category C",
                        "value": 44.18,
                        "percentage": 17.1
                },
                {
                        "category": "Category D",
                        "value": 14.76,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 79.5,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.210909",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Advocacy Development"
        }
    },
}
