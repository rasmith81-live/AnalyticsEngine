"""
Year-over-Year Account Growth KPI

Metric to measure the growth of key accounts in terms of sales or revenue from one year to the next.
"""

from analytics_models import KPI

YEAR_OVER_YEAR_ACCOUNT_GROWTH = KPI(
    name="Year-over-Year Account Growth",
    code="YEAR_OVER_YEAR_ACCOUNT_GROWTH",
    category="Key Account Management",
    
    # Core Definition
    description="Metric to measure the growth of key accounts in terms of sales or revenue from one year to the next.",
    kpi_definition="Metric to measure the growth of key accounts in terms of sales or revenue from one year to the next.",
    expected_business_insights="Highlights the success of account management strategies in growing account revenue.",
    measurement_approach="Measures the percentage increase in revenue from an account compared to the previous year.",
    
    # Formula
    formula="(Current Year Revenue from Account - Previous Year Revenue from Account) / Previous Year Revenue from Account * 100",
    calculation_formula="(Current Year Revenue from Account - Previous Year Revenue from Account) / Previous Year Revenue from Account * 100",
    
    # Analysis
    trend_analysis="""
    * Year-over-year account growth may show consistent upward trends, indicating successful customer retention and expansion strategies.
    * Fluctuating growth rates could signal changes in market conditions, customer behavior, or internal sales efforts.
    """,
    diagnostic_questions="""
    * What specific factors contribute to the growth or decline of key accounts?
    * Are there any common characteristics among accounts that show significant growth versus those that stagnate or decline?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update key account management strategies to align with changing customer needs and market dynamics.
    * Invest in customer relationship management (CRM) tools to better track account growth and identify opportunities for upselling or cross-selling.
    * Provide ongoing training and support for sales teams to enhance their ability to nurture and grow key accounts.
    """,
    visualization_suggestions="""
    * Line charts to visualize the year-over-year growth trajectory for individual key accounts.
    * Pie charts to compare the contribution of different accounts to overall sales growth.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Stagnant or declining account growth may lead to increased customer attrition and revenue loss.
    * Rapid growth in key accounts without proper support or resources may strain operational capabilities and lead to service quality issues.
    """,
    tracking_tools="""
    * CRM systems with robust reporting and analytics capabilities to track account growth and customer interactions.
    * Data visualization tools to create clear and informative charts and graphs for presenting account growth trends.
    """,
    integration_points="""
    * Integrate account growth data with sales forecasting and resource allocation systems to ensure adequate support for expanding accounts.
    * Link account growth metrics with customer satisfaction surveys and feedback mechanisms to gauge the impact of growth on customer experience.
    """,
    change_impact_analysis="""
    * Positive account growth can lead to increased revenue, customer loyalty, and market share.
    * However, rapid growth may strain operational resources and require adjustments in service delivery and support processes.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
