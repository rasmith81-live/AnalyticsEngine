"""
Sales Quota Achievement KPI

The percentage of sales quota achieved by the outside sales team.
"""

from analytics_models import KPI

SALES_QUOTA_ACHIEVEMENT = KPI(
    name="Sales Quota Achievement",
    code="SALES_QUOTA_ACHIEVEMENT",
    category="Outside Sales",
    
    # Core Definition
    description="The percentage of sales quota achieved by the outside sales team.",
    kpi_definition="The percentage of sales quota achieved by the outside sales team.",
    expected_business_insights="Helps assess the appropriateness of sales targets and the effectiveness of the sales team in meeting their goals.",
    measurement_approach="Measures the percentage of sales quota met or exceeded by the sales team.",
    
    # Formula
    formula="(Total Sales Revenue / Sales Quota) * 100",
    calculation_formula="(Total Sales Revenue / Sales Quota) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing sales quota achievement may indicate improved sales strategies or market conditions.
    * Decreasing achievement could signal challenges in the sales process, changes in customer behavior, or increased competition.
    """,
    diagnostic_questions="""
    * What factors have contributed to the increase/decrease in sales quota achievement?
    * Are there specific regions or product lines that are driving the changes in sales quota achievement?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and support to the team to improve performance.
    * Adjust sales territories or target markets to better align with opportunities for success.
    * Implement a more robust sales incentive program to motivate the team and drive results.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in sales quota achievement over time.
    * Comparison bar charts displaying achievement by individual sales representatives or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently low sales quota achievement may lead to missed revenue targets and financial instability.
    * High achievement without sustainable strategies could lead to burnout and decreased long-term performance.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track sales activities and customer interactions.
    * Sales performance analytics tools to identify areas for improvement and track progress.
    """,
    integration_points="""
    * Integrate sales quota achievement data with financial reporting to understand the impact on overall revenue.
    * Link achievement metrics with individual performance evaluations and incentive programs.
    """,
    change_impact_analysis="""
    * Improving sales quota achievement can positively impact revenue and overall business performance.
    * However, changes in achievement may also affect employee morale and motivation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Quota Plan", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
