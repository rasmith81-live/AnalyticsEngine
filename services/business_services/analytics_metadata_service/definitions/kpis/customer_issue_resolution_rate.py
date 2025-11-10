"""
Customer Issue Resolution Rate KPI

The percentage of all customer issues that are resolved satisfactorily.
"""

CUSTOMER_ISSUE_RESOLUTION_RATE = {
    "code": "CUSTOMER_ISSUE_RESOLUTION_RATE",
    "name": "Customer Issue Resolution Rate",
    "description": "The percentage of all customer issues that are resolved satisfactorily.",
    "formula": "(Number of Issues Resolved on First Interaction / Total Number of Issues) * 100",
    "calculation_formula": "(Number of Issues Resolved on First Interaction / Total Number of Issues) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The percentage of all customer issues that are resolved satisfactorily.",
    "expected_business_insights": "Reveals the efficiency and effectiveness of the support team, impacting customer satisfaction.",
    "measurement_approach": "Measures the percentage of customer issues that are resolved within the first interaction or a specified timeframe.",
    "trend_analysis": """
    * An increasing customer issue resolution rate may indicate improved customer service processes or better product quality.
    * A decreasing rate could signal a decline in customer satisfaction or an increase in product issues.
    """,
    "diagnostic_questions": """
    * Are there specific product lines or services that consistently have higher issue resolution rates?
    * How does our issue resolution rate compare with industry benchmarks or customer feedback?
    """,
    "actionable_tips": """
    * Implement regular customer feedback surveys to identify areas for improvement.
    * Provide additional training for customer service teams to handle complex issues more effectively.
    * Invest in product quality control measures to reduce the occurrence of customer issues.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of issue resolution rates over time.
    * Pie charts to compare the distribution of resolved and unresolved issues by category.
    """,
    "risk_warnings": """
    * A consistently low issue resolution rate can lead to customer churn and negative word-of-mouth.
    * High issue resolution rates may also indicate a lack of thorough problem-solving, leading to recurring issues.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track and manage customer issues and resolutions.
    * Quality management systems to identify and address recurring product issues.
    """,
    "integration_points": """
    * Integrate issue resolution rate data with customer feedback systems to gain a comprehensive view of customer satisfaction.
    * Link with product development processes to address recurring issues and improve product quality.
    """,
    "change_impact_analysis": """
    * Improving the issue resolution rate can lead to higher customer retention and loyalty.
    * However, a focus solely on increasing the rate may lead to rushed or inadequate resolutions, impacting overall customer satisfaction.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Support Ticket"], "replaces": ["CUSTOMER_PROBLEM_RESOLUTION_RATE"]},
    "modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"],
    "module_code": "CUSTOMER_SUCCESS",
}
