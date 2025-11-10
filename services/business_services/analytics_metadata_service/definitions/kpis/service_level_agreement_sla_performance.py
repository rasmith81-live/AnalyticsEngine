"""
Service Level Agreement (SLA) Performance KPI

The rate at which a company meets the service expectations as outlined in SLAs with the customer.
"""

SERVICE_LEVEL_AGREEMENT_SLA_PERFORMANCE = {
    "code": "SERVICE_LEVEL_AGREEMENT_SLA_PERFORMANCE",
    "name": "Service Level Agreement (SLA) Performance",
    "description": "The rate at which a company meets the service expectations as outlined in SLAs with the customer.",
    "formula": "(Number of SLA Compliant Actions / Total Number of SLA Actions) * 100",
    "calculation_formula": "(Number of SLA Compliant Actions / Total Number of SLA Actions) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The rate at which a company meets the service expectations as outlined in SLAs with the customer.",
    "expected_business_insights": "Reflects the reliability of service delivery and can impact customer trust and satisfaction.",
    "measurement_approach": "Assesses compliance with agreed service levels specified in SLAs with customers.",
    "trend_analysis": """
    * Increasing SLA performance may indicate improved operational efficiency or better resource allocation.
    * Decreasing SLA performance could signal issues with service delivery, resource constraints, or increased customer demand.
    """,
    "diagnostic_questions": """
    * Are there specific service areas or customer segments where SLA performance consistently falls short?
    * How does our SLA performance compare with industry benchmarks or customer expectations?
    """,
    "actionable_tips": """
    * Invest in training and development for service teams to improve response times and resolution rates.
    * Implement automated systems for tracking and managing SLA commitments to ensure timely delivery of services.
    * Regularly review and update SLAs to align with changing customer needs and market conditions.
    """,
    "visualization_suggestions": """
    * Line charts showing SLA performance over time to identify trends and seasonality.
    * Pie charts illustrating the distribution of SLA performance across different service areas or customer segments.
    """,
    "risk_warnings": """
    * Poor SLA performance can lead to customer dissatisfaction, increased churn, and negative word-of-mouth.
    * Consistently low SLA performance may indicate systemic issues in service delivery that require immediate attention.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems with built-in SLA tracking and reporting capabilities.
    * Workflow management tools to streamline service delivery processes and ensure compliance with SLAs.
    """,
    "integration_points": """
    * Integrate SLA performance data with customer feedback systems to understand the impact of service levels on satisfaction.
    * Link SLA performance with workforce management systems to optimize resource allocation and scheduling.
    """,
    "change_impact_analysis": """
    * Improving SLA performance can lead to higher customer satisfaction and loyalty, positively impacting long-term revenue and profitability.
    * Conversely, declining SLA performance may result in increased customer complaints, escalations, and potential revenue loss.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Agreement", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Service Level Agreement"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
