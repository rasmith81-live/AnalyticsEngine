"""
Upsell and Cross-Sell Rates KPI

The success rates of efforts to sell more expensive items or additional products to existing customers, indicating the effectiveness of sales strategies.
"""

UPSELL_AND_CROSS_SELL_RATES = {
    "code": "UPSELL_AND_CROSS_SELL_RATES",
    "name": "Upsell and Cross-Sell Rates",
    "description": "The success rates of efforts to sell more expensive items or additional products to existing customers, indicating the effectiveness of sales strategies.",
    "formula": "(Number of Upsell or Cross-sell Sales / Total Number of Transactions) * 100",
    "calculation_formula": "(Number of Upsell or Cross-sell Sales / Total Number of Transactions) * 100",
    "category": "Sales Performance",
    "is_active": True,
    "kpi_definition": "The success rates of efforts to sell more expensive items or additional products to existing customers, indicating the effectiveness of sales strategies.",
    "expected_business_insights": "Indicates effectiveness of sales strategies in maximizing customer value.",
    "measurement_approach": "Tracks the percentage of customers who purchase additional or complementary products.",
    "trend_analysis": """
    * An increasing upsell and cross-sell rate may indicate the effectiveness of sales strategies in identifying customer needs and preferences.
    * A decreasing rate could signal a need for reevaluation of sales tactics or a shift in customer behavior.
    """,
    "diagnostic_questions": """
    * Are there specific products or services that have higher success rates in upselling or cross-selling?
    * How does our upsell and cross-sell rate compare with industry benchmarks or competitors?
    """,
    "actionable_tips": """
    * Train sales teams to better understand customer needs and offer relevant upsell or cross-sell options.
    * Utilize customer data and insights to personalize upsell and cross-sell recommendations.
    * Implement targeted marketing campaigns to promote complementary products or upgrades to existing customers.
    """,
    "visualization_suggestions": """
    * Line charts showing upsell and cross-sell rates over time to identify trends and seasonality.
    * Pie charts to visualize the distribution of successful upsell and cross-sell efforts by product or service category.
    """,
    "risk_warnings": """
    * A low upsell and cross-sell rate may lead to missed revenue opportunities and underutilization of existing customer base.
    * Overly aggressive upselling or cross-selling tactics can result in customer dissatisfaction and potential churn.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track customer interactions and preferences for targeted upsell and cross-sell opportunities.
    * Analytics tools to analyze customer behavior and identify potential upsell or cross-sell opportunities.
    """,
    "integration_points": """
    * Integrate upsell and cross-sell data with customer support systems to provide a seamless experience for customers.
    * Link with inventory management systems to ensure availability of upsell or cross-sell items.
    """,
    "change_impact_analysis": """
    * An increase in upsell and cross-sell rates can positively impact revenue and customer lifetime value.
    * However, a focus solely on upselling and cross-selling may impact customer trust and loyalty if not done in a customer-centric manner.
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Success Manager", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Purchase History", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
}
