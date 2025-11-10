"""
Annual Contract Value (ACV) KPI

The average annual contract value of subscriptions or service agreements for key accounts.
"""

ANNUAL_CONTRACT_VALUE_ACV = {
    "code": "ANNUAL_CONTRACT_VALUE_ACV",
    "name": "Annual Contract Value (ACV)",
    "description": "The average annual contract value of subscriptions or service agreements for key accounts.",
    "formula": "Total Value of Contract / Number of Years in Contract",
    "calculation_formula": "Total Value of Contract / Number of Years in Contract",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The average annual contract value of subscriptions or service agreements for key accounts.",
    "expected_business_insights": "Identifies the revenue a customer contributes annually, aiding in forecasting and resource allocation.",
    "measurement_approach": "Considers the total contract value normalized for a year.",
    "trend_analysis": """
    * Increasing ACV may indicate successful upselling or cross-selling efforts with key accounts.
    * Decreasing ACV could signal dissatisfaction or attrition among key accounts.
    """,
    "diagnostic_questions": """
    * Are there specific products or services that are driving the increase or decrease in ACV?
    * How does the ACV of key accounts compare to non-key accounts, and what insights can be gained from the comparison?
    """,
    "actionable_tips": """
    * Regularly review and adjust pricing strategies to maximize ACV without sacrificing customer satisfaction.
    * Invest in building stronger relationships with key accounts to increase loyalty and retention, ultimately leading to higher ACV.
    * Provide personalized solutions and offerings tailored to the specific needs and goals of key accounts.
    """,
    "visualization_suggestions": """
    * Line charts showing the ACV trends of key accounts over time.
    * Pie charts comparing the distribution of ACV across different products or services for key accounts.
    """,
    "risk_warnings": """
    * Significant fluctuations in ACV may indicate instability or uncertainty within key accounts, posing a risk to revenue projections.
    * Consistently low ACV may suggest that key accounts are not fully leveraging the value of the products or services, leading to potential churn.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track interactions and opportunities with key accounts.
    * Data analytics tools to identify patterns and correlations that can help optimize ACV strategies.
    """,
    "integration_points": """
    * Integrate ACV data with sales performance metrics to understand the impact of individual sales efforts on key account value.
    * Link ACV tracking with customer support systems to ensure that service levels align with the value provided to key accounts.
    """,
    "change_impact_analysis": """
    * Increasing ACV may lead to higher revenue and profitability, but it could also require additional resources to support the expanded value provided to key accounts.
    * Conversely, a decrease in ACV can impact overall sales performance and may require adjustments in sales strategies and customer engagement approaches.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Contract", "Key Account", "Key Account Manager", "Product", "Renewal Management", "Service Level Agreement"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
