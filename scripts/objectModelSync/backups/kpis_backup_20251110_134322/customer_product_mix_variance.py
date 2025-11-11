"""
Customer Product Mix Variance KPI

The variance in product mix purchased by key accounts over time.
"""

CUSTOMER_PRODUCT_MIX_VARIANCE = {
    "code": "CUSTOMER_PRODUCT_MIX_VARIANCE",
    "name": "Customer Product Mix Variance",
    "description": "The variance in product mix purchased by key accounts over time.",
    "formula": "(Current Period Product Mix Revenue - Previous Period Product Mix Revenue) / Previous Period Product Mix Revenue * 100",
    "calculation_formula": "(Current Period Product Mix Revenue - Previous Period Product Mix Revenue) / Previous Period Product Mix Revenue * 100",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The variance in product mix purchased by key accounts over time.",
    "expected_business_insights": "Identifies changes in buying patterns which could indicate shifts in customer needs or market trends.",
    "measurement_approach": "Analyzes the variance in the types of products purchased by customers over time.",
    "trend_analysis": """
    * Shifts towards a more diverse product mix may indicate increased customer engagement and satisfaction.
    * A consistent or increasing reliance on a narrow range of products could signal potential risks associated with over-reliance on specific items.
    """,
    "diagnostic_questions": """
    * Are there specific products that are consistently over or under-purchased by key accounts?
    * How does the product mix variance align with our overall sales strategy and customer segmentation?
    """,
    "actionable_tips": """
    * Regularly review and adjust product offerings to align with changing customer preferences and market trends.
    * Implement targeted marketing and sales strategies to promote under-purchased products and balance the product mix.
    * Provide incentives for key accounts to diversify their product mix, potentially through bundled offerings or volume discounts.
    """,
    "visualization_suggestions": """
    * Stacked bar charts comparing product mix variance over different time periods.
    * Line charts showing the trend of individual product categories within the mix over time.
    """,
    "risk_warnings": """
    * Over-reliance on a small number of products may lead to vulnerability if demand for those products decreases.
    * Significant shifts in product mix without proper analysis and planning could lead to inventory imbalances and increased carrying costs.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track and analyze purchasing patterns of key accounts.
    * Advanced analytics tools to identify correlations between product mix variance and other key performance indicators.
    """,
    "integration_points": """
    * Integrate product mix variance analysis with sales and marketing systems to align product offerings with customer needs and preferences.
    * Link with inventory management systems to ensure that the product mix aligns with available stock levels and production capabilities.
    """,
    "change_impact_analysis": """
    * Improving product mix variance can lead to increased revenue and customer satisfaction, but may require adjustments in inventory management and marketing strategies.
    * Conversely, a negative shift in product mix variance could impact profitability and customer loyalty, requiring targeted interventions to address the issue.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Product", "Product Adoption", "Product Usage", "Renewal Management", "Revenue Forecast", "Sale"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
