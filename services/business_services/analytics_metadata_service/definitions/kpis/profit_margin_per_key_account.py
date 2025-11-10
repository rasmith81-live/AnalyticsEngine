"""
Profit Margin per Key Account KPI

The net profit margin generated from each key strategic account.
"""

from analytics_models import KPI

PROFIT_MARGIN_PER_KEY_ACCOUNT = KPI(
    name="Profit Margin per Key Account",
    code="PROFIT_MARGIN_PER_KEY_ACCOUNT",
    category="Key Account Management",
    
    # Core Definition
    description="The net profit margin generated from each key strategic account.",
    kpi_definition="The net profit margin generated from each key strategic account.",
    expected_business_insights="Gives insight into the profitability and pricing effectiveness of products or services provided to key accounts.",
    measurement_approach="Calculates the profit margin for each key account.",
    
    # Formula
    formula="(Total Profit from Key Account / Total Revenue from Key Account) * 100",
    calculation_formula="(Total Profit from Key Account / Total Revenue from Key Account) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing profit margins per key account may indicate successful upselling or cross-selling strategies.
    * Decreasing margins could signal increased competition or pricing pressures.
    """,
    diagnostic_questions="""
    * What factors have contributed to the changes in profit margins for each key account?
    * How do our profit margins compare with industry benchmarks or with margins from previous periods?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review pricing strategies and adjust them based on market conditions and customer value perception.
    * Focus on providing value-added services to key accounts to justify premium pricing and maintain healthy margins.
    * Implement cost-saving measures in operations to protect margins without sacrificing quality or service levels.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of profit margins per key account over time.
    * Pareto charts to identify the key accounts that contribute the most to overall profit margins.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Declining profit margins may lead to reduced profitability and financial instability.
    * Overreliance on a few key accounts for high margins can pose a risk if those accounts are lost or face financial difficulties.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track and analyze customer interactions and sales performance.
    * Financial analysis software to conduct detailed profitability analysis for each key account.
    """,
    integration_points="""
    * Integrate profit margin data with sales and marketing systems to align strategies with account profitability.
    * Link with financial systems to ensure accurate cost allocation and margin calculations.
    """,
    change_impact_analysis="""
    * Improving profit margins can lead to increased revenue and overall business growth.
    * However, aggressive margin improvement strategies may impact customer satisfaction and retention.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale", "Strategic Initiative", "Strategic Review"]
    }
)
