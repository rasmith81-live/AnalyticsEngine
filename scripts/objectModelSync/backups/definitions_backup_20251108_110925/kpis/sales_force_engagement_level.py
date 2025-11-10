"""
Sales Force Engagement Level KPI

The degree to which a sales representative actively engages in sales activities and goals.
"""

from analytics_models import KPI

SALES_FORCE_ENGAGEMENT_LEVEL = KPI(
    name="Sales Force Engagement Level",
    code="SALES_FORCE_ENGAGEMENT_LEVEL",
    category="Outside Sales",
    
    # Core Definition
    description="The degree to which a sales representative actively engages in sales activities and goals.",
    kpi_definition="The degree to which a sales representative actively engages in sales activities and goals.",
    expected_business_insights="Reflects on sales team motivation and productivity, which can inform management strategies and training programs.",
    measurement_approach="Measures the engagement and activity levels of the sales team, often through metrics like call volume, meeting frequency, and CRM use.",
    
    # Formula
    formula="No Standard Formula - This KPI is typically assessed through a combination of activity metrics and qualitative analysis.",
    calculation_formula="No Standard Formula - This KPI is typically assessed through a combination of activity metrics and qualitative analysis.",
    
    # Analysis
    trend_analysis="""
    * An increasing sales force engagement level may indicate a more motivated and productive sales team.
    * A decreasing engagement level could signal dissatisfaction, burnout, or lack of alignment with sales goals.
    """,
    diagnostic_questions="""
    * Are there specific sales activities or targets that sales representatives struggle to engage with?
    * How does the current engagement level compare with historical data or industry benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular feedback sessions and coaching to keep sales representatives motivated and aligned with goals.
    * Provide clear and achievable sales targets to maintain engagement and focus.
    * Utilize sales performance management software to track and analyze individual engagement levels.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of engagement levels over time for each sales representative.
    * Pie charts to compare the distribution of engagement levels across different sales territories or product lines.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low engagement levels can lead to decreased sales performance and missed opportunities.
    * High engagement levels without corresponding results may indicate misaligned goals or ineffective sales strategies.
    """,
    tracking_tools="""
    * CRM systems with built-in engagement tracking and reporting capabilities.
    * Sales enablement platforms to provide sales representatives with the necessary tools and resources for effective engagement.
    """,
    integration_points="""
    * Integrate engagement level data with performance reviews and incentive programs to align recognition and rewards with actual engagement.
    * Link engagement data with customer relationship management systems to understand the impact of engagement on customer interactions and satisfaction.
    """,
    change_impact_analysis="""
    * Improving sales force engagement can lead to increased sales productivity and revenue generation.
    * However, a focus solely on engagement without corresponding results may lead to inefficiencies and wasted resources.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Call", "Competitive Analysis", "Customer", "Goal", "Lead", "Outbound Call", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
