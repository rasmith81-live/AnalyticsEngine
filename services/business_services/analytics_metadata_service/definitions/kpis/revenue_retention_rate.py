"""
Revenue Retention Rate KPI

The amount of revenue retained from existing customers over a given period, often excluding upsell and cross-sell revenues.
"""

REVENUE_RETENTION_RATE = {
    "code": "REVENUE_RETENTION_RATE",
    "name": "Revenue Retention Rate",
    "description": "The amount of revenue retained from existing customers over a given period, often excluding upsell and cross-sell revenues.",
    "formula": "((Starting Revenue - Revenue from Churned Customers) / Starting Revenue) * 100",
    "calculation_formula": "((Starting Revenue - Revenue from Churned Customers) / Starting Revenue) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The amount of revenue retained from existing customers over a given period, often excluding upsell and cross-sell revenues.",
    "expected_business_insights": "Gives a financial perspective on customer retention and the stability of revenue streams.",
    "measurement_approach": "Calculates the percentage of revenue retained from existing customers over a given period.",
    "trend_analysis": """
    * An increasing revenue retention rate may indicate successful customer loyalty programs or improved customer satisfaction.
    * A decreasing rate could signal increased competition, declining product quality, or poor customer service.
    """,
    "diagnostic_questions": """
    * What factors have contributed to the changes in our revenue retention rate?
    * Are there specific customer segments or product lines that are experiencing lower retention?
    """,
    "actionable_tips": """
    * Enhance customer support and after-sales services to improve overall customer experience.
    * Implement targeted marketing campaigns to re-engage existing customers and encourage repeat purchases.
    * Regularly gather feedback from customers to identify areas for improvement and address any concerns promptly.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of revenue retention rate over time.
    * Pie charts to visualize the distribution of retained revenue by customer segments or product categories.
    """,
    "risk_warnings": """
    * A declining revenue retention rate may lead to reduced overall revenue and market share.
    * High retention rates without corresponding revenue growth could indicate a lack of focus on acquiring new customers.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track customer interactions and identify opportunities for retention.
    * Data analytics tools to analyze customer behavior and preferences for targeted retention strategies.
    """,
    "integration_points": """
    * Integrate revenue retention rate analysis with sales and marketing systems to align efforts towards customer retention.
    * Link retention rate data with financial systems to understand the impact on overall revenue and profitability.
    """,
    "change_impact_analysis": """
    * Improving revenue retention can lead to increased customer lifetime value and overall business sustainability.
    * However, focusing solely on retention may lead to missed opportunities for growth through new customer acquisition.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale", "Subscription"]},
    "modules": ["CUSTOMER_RETENTION", "SALES_OPERATIONS"],
    "module_code": "CUSTOMER_RETENTION",
}
