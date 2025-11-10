"""
Net Promoter Score (NPS) KPI

A metric that gauges how likely a customer is to recommend a product or service to others. This KPI measures the satisfaction level of customers with the company's product or service.
"""

NET_PROMOTER_SCORE_NPS = {
    "code": "NET_PROMOTER_SCORE_NPS",
    "name": "Net Promoter Score (NPS)",
    "description": "A metric that gauges how likely a customer is to recommend a product or service to others. This KPI measures the satisfaction level of customers with the company's product or service.",
    "formula": "(Percentage of Promoters - Percentage of Detractors) * 100",
    "calculation_formula": "(Percentage of Promoters - Percentage of Detractors) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "A metric that gauges how likely a customer is to recommend a product or service to others. This KPI measures the satisfaction level of customers with the company's product or service.",
    "expected_business_insights": "Provides a gauge of overall customer satisfaction and loyalty, and can predict business growth.",
    "measurement_approach": "Calculates the likelihood that customers would recommend the company's product or service to others.",
    "trend_analysis": """
    * An increasing NPS may indicate improved product quality or customer service, leading to higher customer satisfaction.
    * A decreasing NPS could signal issues with product performance, customer support, or overall customer experience.
    """,
    "diagnostic_questions": """
    * Are there specific aspects of the product or service that customers frequently praise or criticize?
    * How does our NPS compare with industry benchmarks or competitors in the same market?
    """,
    "actionable_tips": """
    * Invest in customer feedback mechanisms to understand the root causes of high or low NPS scores.
    * Implement customer service training programs to improve interactions and resolve issues effectively.
    * Regularly review and act on customer feedback to address pain points and enhance positive experiences.
    """,
    "visualization_suggestions": """
    * Line charts showing NPS trends over time to identify patterns and changes in customer sentiment.
    * Word clouds to visualize common themes in customer feedback related to NPS scores.
    """,
    "risk_warnings": """
    * Low NPS scores can lead to customer churn and negative word-of-mouth, impacting future sales and brand reputation.
    * Consistently high NPS scores may create complacency, masking underlying issues that need attention.
    """,
    "tracking_tools": """
    * Customer feedback and survey platforms like SurveyMonkey or Qualtrics to collect and analyze NPS data.
    * CRM systems to track customer interactions and identify areas for improvement based on NPS feedback.
    """,
    "integration_points": """
    * Integrate NPS data with customer relationship management (CRM) systems to align customer feedback with individual customer profiles.
    * Link NPS scores with sales and marketing platforms to tailor messaging and offers based on customer sentiment.
    """,
    "change_impact_analysis": """
    * Improving NPS can lead to increased customer retention and loyalty, positively impacting long-term revenue and profitability.
    * Conversely, declining NPS scores can result in reduced customer lifetime value and hinder the company's growth prospects.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
