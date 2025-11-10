"""
Customer Problem Resolution Time KPI

The time it takes to resolve a customer’s issue or problem.
"""

CUSTOMER_PROBLEM_RESOLUTION_TIME = {
    "code": "CUSTOMER_PROBLEM_RESOLUTION_TIME",
    "name": "Customer Problem Resolution Time",
    "description": "The time it takes to resolve a customer’s issue or problem.",
    "formula": "Sum of All Resolution Times / Total Number of Resolved Issues",
    "calculation_formula": "Sum of All Resolution Times / Total Number of Resolved Issues",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The time it takes to resolve a customer’s issue or problem.",
    "expected_business_insights": "Indicates the efficiency of customer service and impacts customer satisfaction and loyalty.",
    "measurement_approach": "Measures the average time it takes to resolve customer issues from the moment they're reported.",
    "trend_analysis": """
    * Increasing resolution time may indicate growing complexity of customer issues or inefficiencies in the support process.
    * Decreasing resolution time can signal improved customer service effectiveness or better alignment of resources with demand.
    """,
    "diagnostic_questions": """
    * Are there specific types of customer problems that consistently take longer to resolve?
    * How does our resolution time compare with industry benchmarks or customer expectations?
    """,
    "actionable_tips": """
    * Implement customer service training programs to enhance problem-solving skills and efficiency.
    * Leverage technology such as CRM systems or ticketing platforms to streamline and prioritize issue resolution.
    * Regularly review and update customer support processes to identify and eliminate bottlenecks.
    """,
    "visualization_suggestions": """
    * Line charts showing resolution time trends over time periods (e.g., monthly or quarterly).
    * Pareto charts to identify the most common types of customer problems and their associated resolution times.
    """,
    "risk_warnings": """
    * Long resolution times can lead to customer dissatisfaction and potential loss of business.
    * Inconsistent or excessively long resolution times may indicate underlying issues in customer support operations.
    """,
    "tracking_tools": """
    * Customer service management software like Zendesk or Freshdesk to track and analyze resolution times.
    * Workflow automation tools to streamline and standardize issue resolution processes.
    """,
    "integration_points": """
    * Integrate resolution time tracking with customer feedback systems to gain insights into the impact of support on overall satisfaction.
    * Link resolution time data with employee performance metrics to identify training or resource allocation needs.
    """,
    "change_impact_analysis": """
    * Improving resolution time can enhance customer loyalty and retention, leading to increased lifetime value.
    * However, overly aggressive targets for resolution time may compromise the quality of support and customer satisfaction.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Support Ticket"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
