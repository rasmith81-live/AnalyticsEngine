"""
Customer Feedback Response Rate KPI

The percentage of customers who provide feedback when asked.
"""

CUSTOMER_FEEDBACK_RESPONSE_RATE = {
    "code": "CUSTOMER_FEEDBACK_RESPONSE_RATE",
    "name": "Customer Feedback Response Rate",
    "description": "The percentage of customers who provide feedback when asked.",
    "formula": "(Number of Feedback Responses / Number of Feedback Requests) * 100",
    "calculation_formula": "(Number of Feedback Responses / Number of Feedback Requests) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The percentage of customers who provide feedback when asked.",
    "expected_business_insights": "Highlights customer engagement and the potential to gather valuable insights for service improvements.",
    "measurement_approach": "Measures the percentage of customers who provide feedback when asked.",
    "trend_analysis": """
    * An increasing customer feedback response rate may indicate improved customer engagement and satisfaction.
    * A decreasing rate could signal a decline in customer willingness to provide feedback, potentially indicating dissatisfaction or disengagement.
    """,
    "diagnostic_questions": """
    * Are there specific touchpoints in the customer journey where feedback requests are more successful?
    * How does our customer feedback response rate compare with industry benchmarks or with our competitors?
    """,
    "actionable_tips": """
    * Implement a more targeted and personalized approach to requesting feedback from customers.
    * Offer incentives or rewards for customers who provide feedback to increase participation.
    * Regularly communicate the actions taken based on customer feedback to demonstrate the value of their input.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of customer feedback response rate over time.
    * Pie charts to visualize the distribution of feedback responses by category or satisfaction level.
    """,
    "risk_warnings": """
    * A low customer feedback response rate may lead to a lack of understanding of customer needs and preferences.
    * Ignoring customer feedback can result in decreased customer loyalty and retention.
    """,
    "tracking_tools": """
    * Customer feedback management platforms like SurveyMonkey or Qualtrics for collecting and analyzing feedback.
    * Customer relationship management (CRM) systems to track customer interactions and feedback requests.
    """,
    "integration_points": """
    * Integrate customer feedback data with sales and marketing systems to align strategies with customer preferences.
    * Link feedback responses with product development and service improvement processes to drive continuous improvement.
    """,
    "change_impact_analysis": """
    * Improving the customer feedback response rate can lead to better product-market fit and increased customer lifetime value.
    * Conversely, a low response rate may result in missed opportunities for innovation and customer-centric improvements.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback"]},
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_RETENTION",
}
