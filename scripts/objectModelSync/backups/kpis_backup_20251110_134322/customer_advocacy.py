"""
Customer Advocacy KPI

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
    "kpi_definition": "The level at which customers are willing to positively promote the company to others.",
    "expected_business_insights": "Reveals the level of customer loyalty and satisfaction, and the potential for organic growth.",
    "measurement_approach": "Measures the percentage of customers who actively promote the company through referrals or positive reviews.",
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
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Service Level Agreement"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
