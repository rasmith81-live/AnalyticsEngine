"""
Renewal Rate KPI

The percentage of customers who renew a subscription or service agreement.
"""

RENEWAL_RATE = {
    "code": "RENEWAL_RATE",
    "name": "Renewal Rate",
    "description": "The percentage of customers who renew a subscription or service agreement.",
    "formula": "(Number of Renewals / Number of Eligible Renewals) * 100",
    "calculation_formula": "(Number of Renewals / Number of Eligible Renewals) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The percentage of customers who renew a subscription or service agreement.",
    "expected_business_insights": "Reveals customer commitment and satisfaction with the product or service, essential for recurring revenue businesses.",
    "measurement_approach": "Measures the percentage of customers who renew their contracts or subscriptions.",
    "trend_analysis": """
    * A rising renewal rate may indicate improved customer satisfaction and loyalty.
    * A decreasing rate could signal increased competition or dissatisfaction with the product or service.
    """,
    "diagnostic_questions": """
    * Are there specific reasons why customers are not renewing their subscriptions or service agreements?
    * How does our renewal rate compare with industry benchmarks or with our historical data?
    """,
    "actionable_tips": """
    * Enhance the quality of customer service and support to increase satisfaction and retention.
    * Offer incentives or discounts for long-term commitments to encourage renewals.
    * Regularly communicate with customers to understand their needs and address any issues before renewal decisions are made.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of renewal rates over time.
    * Pie charts comparing renewal rates by customer segment or product/service category.
    """,
    "risk_warnings": """
    * A declining renewal rate can lead to reduced recurring revenue and impact overall sales performance.
    * High renewal rates without corresponding customer satisfaction may indicate a lack of competitive alternatives, posing a risk in the long term.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track customer interactions and identify opportunities for retention.
    * Survey tools to gather feedback from customers about their renewal decisions and experiences.
    """,
    "integration_points": """
    * Integrate renewal rate data with customer feedback systems to understand the reasons behind non-renewals.
    * Link renewal rate tracking with sales and marketing systems to align efforts towards customer retention.
    """,
    "change_impact_analysis": """
    * Improving the renewal rate can lead to increased customer lifetime value and overall revenue.
    * However, aggressive tactics to boost renewal rates may impact customer trust and brand reputation if not handled carefully.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Agreement", "Product", "Renewal Management", "Service Level Agreement", "Subscription"]},
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_RETENTION",
}
