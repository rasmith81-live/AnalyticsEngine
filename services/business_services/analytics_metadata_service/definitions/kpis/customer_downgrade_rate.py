"""
Customer Downgrade Rate KPI

The percentage of customers that move to a lower-tier service or product offering.
"""

CUSTOMER_DOWNGRADE_RATE = {
    "code": "CUSTOMER_DOWNGRADE_RATE",
    "name": "Customer Downgrade Rate",
    "description": "The percentage of customers that move to a lower-tier service or product offering.",
    "formula": "(Number of Customers Downgraded / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Downgraded / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The percentage of customers that move to a lower-tier service or product offering.",
    "expected_business_insights": "Indicates potential dissatisfaction or mismatch between customer needs and product offerings.",
    "measurement_approach": "Tracks the percentage of customers who move to a lower-tier service or product within a given timeframe.",
    "trend_analysis": """
    * An increasing customer downgrade rate may indicate dissatisfaction with current service or product offerings.
    * A decreasing rate could signal successful upselling efforts or improved customer satisfaction.
    """,
    "diagnostic_questions": """
    * Are there specific reasons why customers are downgrading their services or products?
    * How does our customer downgrade rate compare with industry benchmarks or competitors?
    """,
    "actionable_tips": """
    * Regularly survey customers to understand their needs and preferences.
    * Provide additional training or support for customers to maximize the value they receive from higher-tier offerings.
    * Review pricing strategies to ensure that the value proposition for higher-tier offerings is clear and compelling.
    """,
    "visualization_suggestions": """
    * Line charts showing the customer downgrade rate over time.
    * Pie charts illustrating the distribution of downgrades by product or service category.
    """,
    "risk_warnings": """
    * High customer downgrade rates can lead to decreased revenue and market share.
    * Frequent downgrades may indicate that the organization is not meeting customer expectations or needs.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track customer interactions and feedback.
    * Survey and feedback tools to gather insights from customers about their experiences.
    """,
    "integration_points": """
    * Integrate customer downgrade rate data with sales and marketing systems to understand the impact on revenue and customer acquisition.
    * Link with customer support platforms to identify and address common reasons for downgrades.
    """,
    "change_impact_analysis": """
    * Decreasing the customer downgrade rate can lead to increased customer lifetime value and loyalty.
    * However, efforts to reduce downgrades may require additional resources and investment in customer satisfaction initiatives.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
