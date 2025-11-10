"""
Product Usage Frequency KPI

The frequency at which customers use a product or service.
"""

PRODUCT_USAGE_FREQUENCY = {
    "code": "PRODUCT_USAGE_FREQUENCY",
    "name": "Product Usage Frequency",
    "description": "The frequency at which customers use a product or service.",
    "formula": "Total Number of Product Uses / Total Number of Users",
    "calculation_formula": "Total Number of Product Uses / Total Number of Users",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The frequency at which customers use a product or service.",
    "expected_business_insights": "Highlights product engagement and can inform decisions on product improvements and customer communication.",
    "measurement_approach": "Tracks how often customers use a product within a certain time frame.",
    "trend_analysis": """
    * Increasing product usage frequency may indicate higher customer satisfaction and engagement with the product or service.
    * Decreasing usage frequency could signal a decline in customer interest or the emergence of competing products in the market.
    """,
    "diagnostic_questions": """
    * Are there specific features or aspects of the product that are driving higher or lower usage frequency?
    * How does the product usage frequency compare with industry benchmarks or with customer feedback and satisfaction metrics?
    """,
    "actionable_tips": """
    * Regularly gather customer feedback to understand their usage patterns and identify areas for improvement.
    * Offer incentives or promotions to encourage increased usage frequency, such as loyalty programs or exclusive content.
    * Continuously innovate and update the product to maintain customer interest and usage frequency.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend in product usage frequency over time.
    * Stacked bar charts comparing usage frequency across different customer segments or product versions.
    """,
    "risk_warnings": """
    * Low product usage frequency may lead to customer churn and decreased revenue.
    * High usage frequency without corresponding customer satisfaction may indicate potential burnout or dissatisfaction in the long run.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track and analyze customer usage patterns.
    * Analytics tools to monitor and analyze customer behavior and engagement with the product or service.
    """,
    "integration_points": """
    * Integrate product usage frequency data with customer support systems to identify and address usage-related issues proactively.
    * Link usage frequency with marketing automation platforms to tailor targeted campaigns and communications based on usage patterns.
    """,
    "change_impact_analysis": """
    * Increasing product usage frequency can lead to higher customer lifetime value and overall revenue growth.
    * However, pushing for higher usage frequency without considering customer satisfaction may lead to negative brand perception and reduced customer loyalty.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
