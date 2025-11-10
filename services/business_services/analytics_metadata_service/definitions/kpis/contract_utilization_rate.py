"""
Contract Utilization Rate KPI

The percentage of contracted services or products that customers actually use.
"""

CONTRACT_UTILIZATION_RATE = {
    "code": "CONTRACT_UTILIZATION_RATE",
    "name": "Contract Utilization Rate",
    "description": "The percentage of contracted services or products that customers actually use.",
    "formula": "(Value of Services or Products Utilized / Total Contract Value) * 100",
    "calculation_formula": "(Value of Services or Products Utilized / Total Contract Value) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The percentage of contracted services or products that customers actually use.",
    "expected_business_insights": "Indicates customer engagement and satisfaction, can highlight underutilization or upsell opportunities.",
    "measurement_approach": "Assesses the extent to which customers are using the services or products they are contracted for.",
    "trend_analysis": """
    * An increasing contract utilization rate may indicate that customers are finding more value in the products or services, leading to higher usage.
    * A decreasing rate could signal dissatisfaction with the offerings, changes in customer needs, or ineffective communication about the benefits of the contracted items.
    """,
    "diagnostic_questions": """
    * Are there specific products or services that have a consistently low utilization rate?
    * How does our contract utilization rate compare with industry benchmarks or with historical data?
    """,
    "actionable_tips": """
    * Regularly communicate the value and benefits of the contracted items to customers to encourage usage.
    * Offer training or support to customers to help them maximize the benefits of the products or services they have contracted.
    * Regularly review and update the offerings to ensure they align with customer needs and expectations.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend in contract utilization rates over time.
    * Pie charts to compare the utilization rates of different products or services.
    """,
    "risk_warnings": """
    * Low contract utilization rates may lead to customer churn and lost revenue.
    * High utilization rates without corresponding customer satisfaction may indicate that the offerings are not meeting customer needs effectively.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track customer interactions and feedback related to the contracted items.
    * Data analytics tools to identify patterns and trends in customer usage data.
    """,
    "integration_points": """
    * Integrate contract utilization data with customer feedback and satisfaction metrics to gain a comprehensive understanding of customer perceptions.
    * Link utilization rates with sales and marketing data to align messaging and promotions with customer needs and usage patterns.
    """,
    "change_impact_analysis": """
    * Improving contract utilization rates can lead to increased customer satisfaction and loyalty, potentially impacting long-term revenue and profitability.
    * However, changes in offerings or communication strategies to improve utilization rates may require investment and could impact short-term profitability.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
