"""
Account Escalation Rate KPI

The frequency at which customer issues are escalated to higher levels of customer service or management.
"""

ACCOUNT_ESCALATION_RATE = {
    "code": "ACCOUNT_ESCALATION_RATE",
    "name": "Account Escalation Rate",
    "description": "The frequency at which customer issues are escalated to higher levels of customer service or management.",
    "formula": "(Number of Escalated Cases / Total Number of Cases) * 100",
    "calculation_formula": "(Number of Escalated Cases / Total Number of Cases) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The frequency at which customer issues are escalated to higher levels of customer service or management.",
    "expected_business_insights": "Helps identify potential problems in service or product quality, indicating areas for improvement in customer support.",
    "measurement_approach": "Tracks the percentage of customer issues that get escalated to higher levels of support or management.",
    "trend_analysis": """
    * An increasing account escalation rate may indicate systemic issues with customer service or product quality that need to be addressed.
    * A decreasing rate could signal improvements in frontline customer support or better product reliability.
    """,
    "diagnostic_questions": """
    * Are there common reasons why customer issues are being escalated, and can these be addressed at the root cause?
    * How does our account escalation rate compare with industry benchmarks or with our competitors?
    """,
    "actionable_tips": """
    * Invest in ongoing training for customer service representatives to handle a wider range of issues without escalation.
    * Implement a feedback loop from escalated cases to identify recurring problems and address them systematically.
    * Consider implementing self-service options or improved documentation to empower customers to resolve issues without escalation.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of account escalation rates over time.
    * Pareto charts to identify the most common reasons for escalation.
    """,
    "risk_warnings": """
    * High account escalation rates can lead to customer churn and damage to the brand's reputation.
    * Chronic escalations may indicate deeper issues in product quality or customer service that need immediate attention.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track and analyze escalation patterns.
    * Quality management software to identify and address recurring product issues.
    """,
    "integration_points": """
    * Integrate account escalation data with customer satisfaction surveys to understand the impact of escalations on overall customer experience.
    * Link escalation data with product development and quality assurance processes to address root causes of customer issues.
    """,
    "change_impact_analysis": """
    * Reducing account escalation rates can lead to higher customer satisfaction and loyalty, positively impacting long-term revenue.
    * However, addressing escalation issues may require investments in training, technology, or product improvements.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Product", "Renewal Management", "Service Level Agreement", "Support Ticket"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
