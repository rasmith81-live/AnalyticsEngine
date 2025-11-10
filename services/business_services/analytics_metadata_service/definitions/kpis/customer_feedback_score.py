"""
Customer Feedback Score KPI

The score given by key customers based on their feedback regarding products or services.
"""

CUSTOMER_FEEDBACK_SCORE = {
    "code": "CUSTOMER_FEEDBACK_SCORE",
    "name": "Customer Feedback Score",
    "description": "The score given by key customers based on their feedback regarding products or services.",
    "formula": "Sum of Customer Ratings / Total Number of Ratings",
    "calculation_formula": "Sum of Customer Ratings / Total Number of Ratings",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The score given by key customers based on their feedback regarding products or services.",
    "expected_business_insights": "Offers direct insight from customers about their satisfaction and areas for improvement.",
    "measurement_approach": "Aggregates customer ratings on various aspects of products or services.",
    "trend_analysis": """
    * Increasing customer feedback scores may indicate improved product quality or customer service.
    * Decreasing scores could signal declining satisfaction with products or services.
    """,
    "diagnostic_questions": """
    * What specific aspects of our products or services are contributing to higher or lower feedback scores?
    * How do our feedback scores compare with industry benchmarks or competitors?
    """,
    "actionable_tips": """
    * Implement regular customer feedback surveys to gather actionable insights for improvement.
    * Invest in training and development for sales and customer service teams to enhance customer experience.
    * Use feedback scores as a basis for continuous improvement initiatives across the organization.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of feedback scores over time.
    * Pie charts to visualize the distribution of feedback scores across different customer segments.
    """,
    "risk_warnings": """
    * Consistently low feedback scores can lead to customer churn and negative word-of-mouth.
    * Ignoring feedback scores may result in missed opportunities for improvement and innovation.
    """,
    "tracking_tools": """
    * Customer feedback management platforms like Medallia or Qualtrics for systematic collection and analysis of feedback.
    * CRM systems with built-in feedback tracking capabilities to integrate customer feedback data with sales management processes.
    """,
    "integration_points": """
    * Integrate customer feedback scores with performance management systems to align sales and service goals with customer satisfaction metrics.
    * Link feedback scores with product development and innovation processes to drive customer-centric improvements.
    """,
    "change_impact_analysis": """
    * Improving feedback scores can lead to increased customer retention and lifetime value.
    * However, changes in feedback scores may also require adjustments in product offerings or service delivery, impacting operational processes.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Key Account", "Key Account Manager", "Product", "Renewal Management"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
