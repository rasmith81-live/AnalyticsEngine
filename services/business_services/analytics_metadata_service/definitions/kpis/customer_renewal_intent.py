"""
Customer Renewal Intent KPI

The expressed intent of customers to renew their contracts or continue their subscription at the end of the current term.
"""

CUSTOMER_RENEWAL_INTENT = {
    "code": "CUSTOMER_RENEWAL_INTENT",
    "name": "Customer Renewal Intent",
    "description": "The expressed intent of customers to renew their contracts or continue their subscription at the end of the current term.",
    "formula": "(Number of Customers Indicating Positive Renewal Intent / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Indicating Positive Renewal Intent / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The expressed intent of customers to renew their contracts or continue their subscription at the end of the current term.",
    "expected_business_insights": "Predicts future revenue streams and identifies customers who may be at risk for churn.",
    "measurement_approach": "Measures the likelihood of customers to renew their contracts or continue their subscription based on surveys or behavioral cues.",
    "trend_analysis": """
    * Increasing customer renewal intent may indicate higher satisfaction with the product or service.
    * Decreasing renewal intent could signal issues with product quality, customer support, or competitive pressures.
    """,
    "diagnostic_questions": """
    * What are the main reasons customers cite for their intent to renew or not renew?
    * How does our customer renewal intent compare with industry benchmarks or with our historical data?
    """,
    "actionable_tips": """
    * Enhance customer support and engagement to address any concerns or issues that may be impacting renewal intent.
    * Regularly solicit feedback from customers to understand their needs and expectations, and make necessary adjustments.
    * Offer incentives or loyalty programs to encourage renewal and reward long-term customers.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of renewal intent over time.
    * Segmented bar charts comparing renewal intent across different customer segments or product categories.
    """,
    "risk_warnings": """
    * Low renewal intent may lead to revenue loss and indicate potential churn in the customer base.
    * High renewal intent without continuous improvement may lead to complacency and missed opportunities for growth.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track and analyze customer interactions and feedback.
    * Survey and feedback tools to gather and analyze customer sentiment and satisfaction data.
    """,
    "integration_points": """
    * Integrate renewal intent data with sales and marketing systems to align efforts in retaining customers.
    * Link renewal intent with product development and improvement processes to address any recurring issues.
    """,
    "change_impact_analysis": """
    * Improving renewal intent can lead to increased customer lifetime value and overall revenue growth.
    * Conversely, declining renewal intent may require additional resources to win back customers or acquire new ones.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Renewal Management", "Subscription"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
