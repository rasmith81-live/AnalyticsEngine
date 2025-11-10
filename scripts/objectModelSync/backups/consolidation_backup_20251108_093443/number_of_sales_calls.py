"""
Number of Sales Calls KPI

The total number of sales-related calls made by the outside sales team.
"""

from analytics_models import KPI

NUMBER_OF_SALES_CALLS = KPI(
    name="Number of Sales Calls",
    code="NUMBER_OF_SALES_CALLS",
    category="Outside Sales",
    
    # Core Definition
    description="The total number of sales-related calls made by the outside sales team.",
    kpi_definition="The total number of sales-related calls made by the outside sales team.",
    expected_business_insights="Helps measure sales activity levels and can indicate the level of effort being put into reaching potential customers.",
    measurement_approach="Counts the total number of sales-related calls made by the sales team.",
    
    # Formula
    formula="Sum of all Sales Calls Made",
    calculation_formula="Sum of all Sales Calls Made",
    
    # Analysis
    trend_analysis="""
    * An increasing number of sales calls may indicate a proactive sales team or a push to meet higher sales targets.
    * A decreasing number of sales calls could signal a lack of engagement or challenges in reaching potential clients.
    """,
    diagnostic_questions="""
    * Are the sales calls evenly distributed across the sales team, or are there individuals who are making significantly more or fewer calls?
    * How do the number of sales calls correlate with actual sales performance and conversion rates?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a CRM system to track and manage sales calls more effectively.
    * Provide regular training and coaching to the sales team on effective sales call techniques and strategies.
    * Encourage the use of technology such as automated dialing systems to increase the volume of sales calls without sacrificing quality.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales calls over time.
    * Pie charts to compare the distribution of sales calls among different team members or territories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A high number of sales calls without corresponding sales may indicate inefficiencies in the sales process or poor lead quality.
    * A low number of sales calls may result in missed opportunities and reduced sales performance.
    """,
    tracking_tools="""
    * Utilize sales engagement platforms like Outreach or SalesLoft to streamline and track sales call activities.
    * Integrate with communication tools such as Zoom or Microsoft Teams for virtual sales calls and meetings.
    """,
    integration_points="""
    * Integrate sales call data with customer relationship management (CRM) systems to better understand the impact of calls on the sales pipeline.
    * Link sales call metrics with marketing automation platforms to align sales efforts with marketing campaigns and lead generation activities.
    """,
    change_impact_analysis="""
    * An increase in the number of sales calls may lead to higher sales volume but could also result in increased pressure on the sales team.
    * A decrease in sales calls may free up time for more personalized and effective sales interactions but could also reduce the overall outreach and lead generation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
