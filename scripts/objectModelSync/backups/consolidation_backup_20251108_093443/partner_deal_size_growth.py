"""
Partner Deal Size Growth KPI

The change in the average deal size closed by channel partners over time, indicating the partners' growing sales capability.
"""

from analytics_models import KPI

PARTNER_DEAL_SIZE_GROWTH = KPI(
    name="Partner Deal Size Growth",
    code="PARTNER_DEAL_SIZE_GROWTH",
    category="Channel Sales",
    
    # Core Definition
    description="The change in the average deal size closed by channel partners over time, indicating the partners\' growing sales capability.",
    kpi_definition="The change in the average deal size closed by channel partners over time, indicating the partners\' growing sales capability.",
    expected_business_insights="Signifies the capacity of partners to attract larger deals, contributing to overall revenue growth.",
    measurement_approach="Tracks the percentage increase in the average deal size secured by channel partners over time.",
    
    # Formula
    formula="((Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size) * 100",
    calculation_formula="((Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing partner deal size growth may indicate improved sales training and enablement for partners.
    * Decreasing growth could signal market saturation or a lack of new opportunities being pursued by partners.
    """,
    diagnostic_questions="""
    * Are there specific product lines or customer segments where partners are seeing the most significant deal size growth?
    * How does the partner deal size growth compare with industry benchmarks or competitors\' performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and resources to help partners target higher-value opportunities.
    * Encourage partners to focus on cross-selling and upselling to increase deal sizes.
    * Explore new market segments or industries where partners can pursue larger deals.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in average deal size over time for each partner.
    * Bar graphs comparing average deal sizes across different partner groups or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Rapid partner deal size growth may lead to increased competition and potential margin erosion.
    * Stagnant or declining deal size growth could indicate a need for reevaluation of the partner ecosystem and sales strategies.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems to track and analyze partner deal sizes and trends.
    * Business Intelligence (BI) tools to identify patterns and opportunities for deal size growth.
    """,
    integration_points="""
    * Integrate partner deal size data with sales performance metrics to understand the impact on overall revenue and profitability.
    * Link deal size growth with partner incentive and reward programs to align incentives with desired outcomes.
    """,
    change_impact_analysis="""
    * Increasing partner deal size growth can positively impact overall revenue and profitability.
    * However, it may also require adjustments in sales strategies and resource allocation to support larger deals.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
