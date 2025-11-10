"""
Expansion Revenue Rate KPI

The rate at which existing customers increase spending through upsells or cross-sells.
"""

EXPANSION_REVENUE_RATE = {
    "code": "EXPANSION_REVENUE_RATE",
    "name": "Expansion Revenue Rate",
    "description": "The rate at which existing customers increase spending through upsells or cross-sells.",
    "formula": "(New Revenue from Existing Customers / Total Revenue from Existing Customers) * 100",
    "calculation_formula": "(New Revenue from Existing Customers / Total Revenue from Existing Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The rate at which existing customers increase spending through upsells or cross-sells.",
    "expected_business_insights": "Reveals the effectiveness of account management and the potential for organic growth from the current customer base.",
    "measurement_approach": "Measures the increase in revenue from existing customers through upselling or cross-selling additional products or services.",
    "trend_analysis": """
    * Expansion revenue rate tends to increase as customers become more familiar with the product or service and see the value in additional offerings.
    * A decreasing expansion revenue rate could indicate a lack of effective upselling or cross-selling strategies, or a disconnect between customer needs and available offerings.
    """,
    "diagnostic_questions": """
    * Are there specific customer segments or industries that are more receptive to upsells or cross-sells?
    * How does our expansion revenue rate compare to industry benchmarks or to our own historical performance?
    """,
    "actionable_tips": """
    * Train sales teams to identify upsell and cross-sell opportunities during customer interactions.
    * Personalize upsell and cross-sell recommendations based on customer behavior and preferences.
    * Regularly review and update the product or service portfolio to ensure relevant and attractive offerings for existing customers.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of expansion revenue rate over time.
    * Pie charts illustrating the proportion of revenue coming from upsells versus cross-sells.
    """,
    "risk_warnings": """
    * A stagnant or declining expansion revenue rate may lead to missed revenue opportunities and reduced customer lifetime value.
    * Overly aggressive upselling or cross-selling tactics can result in customer dissatisfaction and potential churn.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems with built-in upsell and cross-sell tracking capabilities.
    * Marketing automation platforms for targeted upsell and cross-sell campaigns.
    """,
    "integration_points": """
    * Integrate expansion revenue rate data with customer feedback and satisfaction scores to understand the impact of upselling and cross-selling on customer experience.
    * Link with inventory and supply chain systems to ensure the availability of products or services being upsold or cross-sold.
    """,
    "change_impact_analysis": """
    * Improving the expansion revenue rate can lead to increased customer lifetime value and overall revenue growth.
    * However, overly aggressive upselling or cross-selling can strain customer relationships and impact brand reputation.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Expansion Opportunity", "Revenue Forecast", "Sale"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
