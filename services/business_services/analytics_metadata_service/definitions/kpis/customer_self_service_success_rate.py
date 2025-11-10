"""
Customer Self-Service Success Rate KPI

The percentage of issues that customers resolve on their own, without direct intervention from customer support.
"""

CUSTOMER_SELF_SERVICE_SUCCESS_RATE = {
    "code": "CUSTOMER_SELF_SERVICE_SUCCESS_RATE",
    "name": "Customer Self-Service Success Rate",
    "description": "The percentage of issues that customers resolve on their own, without direct intervention from customer support.",
    "formula": "(Number of Self-Service Resolutions / Total Number of Self-Service Attempts) * 100",
    "calculation_formula": "(Number of Self-Service Resolutions / Total Number of Self-Service Attempts) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The percentage of issues that customers resolve on their own, without direct intervention from customer support.",
    "expected_business_insights": "Indicates the effectiveness of self-service resources and the potential for reducing support costs.",
    "measurement_approach": "Tracks the percentage of issues resolved or questions answered through self-service channels without direct assistance.",
    "trend_analysis": """
    * An increasing self-service success rate may indicate improved user experience and more intuitive product design.
    * A decreasing rate could signal complex or confusing product features that require additional support or a lack of easily accessible self-service resources.
    """,
    "diagnostic_questions": """
    * Are there common types of issues that customers struggle to resolve on their own?
    * How does our self-service success rate compare with industry benchmarks or with similar products in the market?
    """,
    "actionable_tips": """
    * Regularly update and improve self-service resources such as FAQs, tutorials, and knowledge bases.
    * Collect and analyze customer feedback to identify pain points in the self-service process and make necessary improvements.
    * Provide incentives for customers to utilize self-service options, such as exclusive content or discounts.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of self-service success rate over time.
    * Pie charts comparing the distribution of resolved issues between self-service and customer support.
    """,
    "risk_warnings": """
    * A consistently low self-service success rate may indicate a need for better user education or product simplification.
    * High reliance on customer support for issue resolution can lead to increased support costs and longer resolution times.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems with self-service analytics capabilities.
    * Customer feedback and survey tools to gather insights on self-service effectiveness.
    """,
    "integration_points": """
    * Integrate self-service success rate data with product development processes to prioritize features that improve user autonomy.
    * Link self-service analytics with customer relationship management systems to identify opportunities for proactive customer support.
    """,
    "change_impact_analysis": """
    * Improving the self-service success rate can lead to higher customer satisfaction and loyalty, positively impacting customer retention and lifetime value.
    * Conversely, a low self-service success rate may result in increased customer churn and negative word-of-mouth, affecting brand reputation.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Service Level Agreement", "Support Ticket"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
