"""
Opportunity Win Rate KPI

The percentage of sales opportunities that are converted into actual sales.
"""

from analytics_models import KPI

OPPORTUNITY_WIN_RATE = KPI(
    name="Opportunity Win Rate",
    code="OPPORTUNITY_WIN_RATE",
    category="Sales Development",
    
    # Core Definition
    description="The percentage of sales opportunities that are converted into actual sales.",
    kpi_definition="The percentage of sales opportunities that are converted into actual sales.",
    expected_business_insights="Assesses the effectiveness of the sales team and strategies at closing deals.",
    measurement_approach="Measures the percentage of sales opportunities that are converted into actual sales.",
    
    # Formula
    formula="(Total Number of Won Opportunities / Total Number of Opportunities) * 100",
    calculation_formula="(Total Number of Won Opportunities / Total Number of Opportunities) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing opportunity win rate may indicate improved sales strategies or a growing market demand.
    * A decreasing rate could signal ineffective sales processes or increased competition.
    """,
    diagnostic_questions="""
    * What factors contribute to the successful conversion of sales opportunities?
    * Are there specific stages in the sales pipeline where opportunities are frequently lost?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide ongoing sales training and coaching to improve sales team performance.
    * Implement a lead scoring system to prioritize high-quality opportunities.
    * Regularly review and refine the sales process to identify and address bottlenecks.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of opportunity win rates over time.
    * Pie charts comparing win rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low opportunity win rate may indicate a need for significant changes in sales strategy or personnel.
    * High win rates without corresponding revenue growth could signal overcommitment or discounting.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze sales opportunities and outcomes.
    * Sales enablement platforms to provide sales teams with the necessary tools and resources to improve win rates.
    """,
    integration_points="""
    * Integrate opportunity win rate data with marketing analytics to understand the quality of leads generated.
    * Link win rates with customer feedback systems to identify areas for improvement in the sales process.
    """,
    change_impact_analysis="""
    * An increase in opportunity win rate can lead to higher revenue and improved sales team morale.
    * However, a focus solely on win rate may neglect the importance of customer satisfaction and long-term relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Expansion Opportunity", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"],
        "replaces": ["OPPORTUNITY_TO_SALE_RATIO"]}
)
