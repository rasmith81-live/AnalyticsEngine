"""
Service Level Agreement (SLA) Compliance Rate KPI

The rate at which the customer success team adheres to the agreed-upon service levels in SLAs with customers.
"""

SERVICE_LEVEL_AGREEMENT_SLA_COMPLIANCE_RATE = {
    "code": "SERVICE_LEVEL_AGREEMENT_SLA_COMPLIANCE_RATE",
    "name": "Service Level Agreement (SLA) Compliance Rate",
    "description": "The rate at which the customer success team adheres to the agreed-upon service levels in SLAs with customers.",
    "formula": "(Number of SLA Compliant Resolutions / Total Number of SLA Bound Requests) * 100",
    "calculation_formula": "(Number of SLA Compliant Resolutions / Total Number of SLA Bound Requests) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The rate at which the customer success team adheres to the agreed-upon service levels in SLAs with customers.",
    "expected_business_insights": "Indicates the reliability and performance of the support team, impacting customer trust and satisfaction.",
    "measurement_approach": "Tracks the percentage of service requests or incidents resolved within the agreed-upon timeframes outlined in SLAs.",
    "trend_analysis": """
    * An increasing SLA compliance rate may indicate improved customer success processes and better alignment with customer needs.
    * A decreasing rate could signal issues in resource allocation, communication, or customer expectations management.
    """,
    "diagnostic_questions": """
    * Are there specific SLAs or customer segments where compliance is consistently lower?
    * How do our SLA compliance rates compare with industry benchmarks or customer feedback?
    """,
    "actionable_tips": """
    * Regularly review and update SLAs to ensure they reflect current customer needs and the capabilities of the customer success team.
    * Invest in training and resources for the customer success team to better meet SLA requirements.
    * Implement automated systems for tracking and managing SLA compliance to reduce manual errors and delays.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of SLA compliance rates over time.
    * Pie charts comparing SLA compliance rates across different customer segments or service offerings.
    """,
    "risk_warnings": """
    * Low SLA compliance rates can lead to customer dissatisfaction and potential churn.
    * Consistently high compliance rates may indicate overcommitment or underutilization of resources.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems with built-in SLA tracking and reporting capabilities.
    * Workflow automation tools to streamline and standardize the process of managing and fulfilling SLAs.
    """,
    "integration_points": """
    * Integrate SLA compliance data with customer feedback and satisfaction metrics to understand the impact on overall customer experience.
    * Link SLA compliance tracking with resource management systems to ensure adequate allocation of personnel and resources.
    """,
    "change_impact_analysis": """
    * Improving SLA compliance can enhance customer satisfaction and loyalty, leading to increased customer lifetime value.
    * However, overcommitting to SLAs without the necessary resources can strain the customer success team and impact employee morale.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Agreement", "Product", "Sales Team", "Service Level Agreement"]},
    "modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "CUSTOMER_SUCCESS",
}
