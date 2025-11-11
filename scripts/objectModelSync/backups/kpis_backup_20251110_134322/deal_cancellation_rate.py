"""
Deal Cancellation Rate KPI

The percentage of deals that are canceled after being initiated.
"""

DEAL_CANCELLATION_RATE = {
    "code": "DEAL_CANCELLATION_RATE",
    "name": "Deal Cancellation Rate",
    "description": "The percentage of deals that are canceled after being initiated.",
    "formula": "(Number of Deals Canceled / Total Number of Deals Initially Confirmed) * 100",
    "calculation_formula": "(Number of Deals Canceled / Total Number of Deals Initially Confirmed) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "kpi_definition": "The percentage of deals that are canceled after being initiated.",
    "expected_business_insights": "Identifies issues with the sales process or customer concerns leading to cancellations.",
    "measurement_approach": "Measures the percentage of deals canceled after being initially confirmed.",
    "trend_analysis": """
    * An increasing deal cancellation rate may indicate issues with the sales process, product quality, or customer satisfaction.
    * A decreasing rate could signal improved sales strategies, better product offerings, or enhanced customer service.
    """,
    "diagnostic_questions": """
    * Are there common reasons why deals are being canceled, such as pricing, product fit, or customer expectations?
    * How does our deal cancellation rate compare with industry benchmarks or with specific sales teams or regions?
    """,
    "actionable_tips": """
    * Implement thorough qualification processes to ensure that potential deals are a good fit for the company and the customer.
    * Provide additional sales training and resources to address common reasons for deal cancellations.
    * Regularly review and update sales strategies and product offerings to better meet customer needs and expectations.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend in deal cancellation rates over time.
    * Pie charts to compare reasons for deal cancellations, such as pricing, product fit, or customer dissatisfaction.
    """,
    "risk_warnings": """
    * High deal cancellation rates can lead to lost revenue and impact sales team morale.
    * Consistently high cancellation rates may indicate deeper issues with product-market fit or sales processes.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track and analyze deal cancellation reasons and trends.
    * Sales performance management software to identify areas for improvement and track the impact of sales strategies on deal cancellations.
    """,
    "integration_points": """
    * Integrate deal cancellation data with customer feedback systems to understand the reasons behind cancellations and improve customer satisfaction.
    * Link deal cancellation rates with sales forecasting and inventory management systems to adjust production and inventory levels accordingly.
    """,
    "change_impact_analysis": """
    * Reducing deal cancellation rates can lead to increased revenue and improved customer retention.
    * However, changes in sales strategies or product offerings to reduce cancellations may require additional resources and investment.
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
}
