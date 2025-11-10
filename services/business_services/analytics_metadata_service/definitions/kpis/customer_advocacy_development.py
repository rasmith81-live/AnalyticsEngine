"""
Customer Advocacy Development KPI

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
    "kpi_definition": "The process and effectiveness of turning key account customers into advocates for the company.",
    "expected_business_insights": "Highlights the effectiveness of customer service and the brand’s ability to create promoters, which can lead to organic growth.",
    "measurement_approach": "Assesses the increase in the number of customer advocates over time.",
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
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Sales Process Workflow"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
