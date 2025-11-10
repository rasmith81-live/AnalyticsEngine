"""
Account Saturation Index KPI

A measure of how deeply a company has penetrated a key account with its products or services.
"""

ACCOUNT_SATURATION_INDEX = {
    "code": "ACCOUNT_SATURATION_INDEX",
    "name": "Account Saturation Index",
    "description": "A measure of how deeply a company has penetrated a key account with its products or services.",
    "formula": "(Number of Products/Services Purchased by Account / Total Number of Relevant Products/Services) * 100",
    "calculation_formula": "(Number of Products/Services Purchased by Account / Total Number of Relevant Products/Services) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "A measure of how deeply a company has penetrated a key account with its products or services.",
    "expected_business_insights": "Highlights potential for further sales by identifying gaps in the product/service offering for each account.",
    "measurement_approach": "Measures the extent to which a customer has been sold the complete range of relevant products or services.",
    "trend_analysis": """
    * An increasing account saturation index may indicate successful cross-selling or upselling efforts within the key account.
    * A decreasing index could signal a loss of market share within the key account or increased competition.
    """,
    "diagnostic_questions": """
    * What specific products or services have contributed to the increase or decrease in the account saturation index?
    * How does the account saturation index compare with industry benchmarks or with the performance of other key accounts?
    """,
    "actionable_tips": """
    * Regularly review and update the key account strategy to ensure alignment with the account's evolving needs and goals.
    * Invest in training and development for the sales team to enhance their ability to identify and capitalize on cross-selling or upselling opportunities.
    * Implement a customer relationship management (CRM) system to track interactions and identify potential areas for deeper penetration within the key account.
    """,
    "visualization_suggestions": """
    * Line charts showing the account saturation index over time to identify trends and patterns.
    * Pie charts to visualize the distribution of products or services contributing to the account saturation index.
    """,
    "risk_warnings": """
    * A declining account saturation index may lead to decreased revenue and market share within the key account.
    * Overreliance on a single key account for a high account saturation index may pose a risk if the account experiences changes or challenges.
    """,
    "tracking_tools": """
    * CRM software such as Salesforce or HubSpot to track and manage key account relationships and opportunities.
    * Data analytics tools to identify patterns and opportunities for deeper penetration within the key account.
    """,
    "integration_points": """
    * Integrate the account saturation index with sales forecasting systems to align resource allocation and strategic planning.
    * Link the index with customer satisfaction metrics to ensure that deeper penetration efforts do not compromise overall satisfaction.
    """,
    "change_impact_analysis": """
    * Improving the account saturation index can lead to increased customer lifetime value and long-term loyalty.
    * However, overly aggressive tactics to increase the index may strain the relationship with the key account and impact overall customer satisfaction.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Product", "Renewal Management"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
