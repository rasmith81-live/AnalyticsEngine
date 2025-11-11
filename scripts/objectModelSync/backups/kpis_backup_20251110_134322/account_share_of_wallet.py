"""
Account Share of Wallet KPI

The percentage of a customer's total spending for a category that is spent with the company.
"""

ACCOUNT_SHARE_OF_WALLET = {
    "code": "ACCOUNT_SHARE_OF_WALLET",
    "name": "Account Share of Wallet",
    "description": "The percentage of a customer's total spending for a category that is spent with the company.",
    "formula": "(Revenue from Customer / Customer's Total Spend in Category) * 100",
    "calculation_formula": "(Revenue from Customer / Customer's Total Spend in Category) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The percentage of a customer's total spending for a category that is spent with the company.",
    "expected_business_insights": "Provides insight into customer loyalty and potential revenue growth by increasing the share of customer spend.",
    "measurement_approach": "Estimates the percentage of a customer's total spending within a category that is captured by the company.",
    "trend_analysis": """
    * Increasing share of wallet may indicate successful cross-selling or upselling efforts.
    * Decreasing share of wallet could signal increased competition or customer dissatisfaction.
    """,
    "diagnostic_questions": """
    * What are the main factors influencing the distribution of a customer's spending across different providers?
    * Are there specific products or services where we are losing share of wallet, and why?
    """,
    "actionable_tips": """
    * Implement targeted marketing campaigns to increase customer engagement and loyalty.
    * Enhance the value proposition of products or services to capture a larger share of customer spending.
    * Regularly review and optimize pricing strategies to remain competitive and maintain share of wallet.
    """,
    "visualization_suggestions": """
    * Pie charts to visually represent the distribution of a customer's spending across different categories or providers.
    * Line graphs to track changes in share of wallet over time for key accounts.
    """,
    "risk_warnings": """
    * Decreasing share of wallet may indicate a higher risk of customer churn or defection to competitors.
    * Over-reliance on a few key accounts for a large share of wallet can pose a risk if those accounts are lost.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) systems to track and analyze customer purchasing behavior.
    * Business Intelligence (BI) tools to identify trends and patterns in customer spending data.
    """,
    "integration_points": """
    * Integrate share of wallet data with sales and marketing systems to align efforts in capturing a larger share of customer spending.
    * Link with customer satisfaction and feedback systems to understand the impact of customer experience on share of wallet.
    """,
    "change_impact_analysis": """
    * Increasing share of wallet can lead to higher customer lifetime value and revenue generation.
    * However, aggressive tactics to capture share of wallet may impact customer satisfaction and long-term loyalty.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
