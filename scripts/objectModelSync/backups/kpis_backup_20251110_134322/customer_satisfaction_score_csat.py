"""
Customer Satisfaction Score (CSAT) KPI

A metric that assesses how satisfied customers are with a company's products or services.
"""

CUSTOMER_SATISFACTION_SCORE_CSAT = {
    "code": "CUSTOMER_SATISFACTION_SCORE_CSAT",
    "name": "Customer Satisfaction Score (CSAT)",
    "description": "A metric that assesses how satisfied customers are with a company's products or services.",
    "formula": "Average of Customer Satisfaction Ratings on a Scale (e.g., 1-5)",
    "calculation_formula": "Average of Customer Satisfaction Ratings on a Scale (e.g., 1-5)",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "A metric that assesses how satisfied customers are with a company's products or services.",
    "expected_business_insights": "Provides immediate feedback on customer happiness and service performance, useful for quality monitoring.",
    "measurement_approach": "Measures customer satisfaction with a product, service, or experience, typically on a scale.",
    "trend_analysis": """
    * Increasing CSAT scores may indicate improved product quality or customer service.
    * Decreasing scores could signal issues with product performance, customer support, or overall satisfaction.
    """,
    "diagnostic_questions": """
    * What specific aspects of our products or services are contributing to higher or lower CSAT scores?
    * Are there common themes or patterns in customer feedback that correlate with changes in CSAT scores?
    """,
    "actionable_tips": """
    * Regularly solicit and act on customer feedback to address pain points and improve satisfaction.
    * Invest in training and development for customer-facing teams to enhance service quality.
    * Implement quality control measures to ensure products meet or exceed customer expectations.
    """,
    "visualization_suggestions": """
    * Line charts showing CSAT scores over time to identify trends and fluctuations.
    * Pie charts to visualize the distribution of satisfaction levels across different products or services.
    """,
    "risk_warnings": """
    * Low CSAT scores can lead to customer churn and negative word-of-mouth, impacting revenue and brand reputation.
    * Ignoring or neglecting customer feedback can result in missed opportunities for improvement and long-term success.
    """,
    "tracking_tools": """
    * Customer feedback and survey platforms like SurveyMonkey or Qualtrics for collecting and analyzing satisfaction data.
    * CRM systems with built-in CSAT tracking and reporting capabilities for seamless integration with customer interactions.
    """,
    "integration_points": """
    * Integrate CSAT data with customer relationship management systems to personalize interactions and address individual satisfaction concerns.
    * Link CSAT scores with product development and quality assurance processes to align improvements with customer needs.
    """,
    "change_impact_analysis": """
    * Improving CSAT scores can lead to increased customer loyalty and lifetime value, offsetting initial investment costs.
    * Conversely, declining CSAT scores may result in higher customer acquisition costs as a result of churn and negative reviews.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]},
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
    "module_code": "CUSTOMER_RETENTION",
}
