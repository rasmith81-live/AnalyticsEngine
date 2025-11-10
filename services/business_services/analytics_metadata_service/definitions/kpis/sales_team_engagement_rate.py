"""
Sales Team Engagement Rate KPI

The level of engagement and satisfaction of the sales team with the sales enablement program and support provided by the sales enablement team.
"""

from analytics_models import KPI

SALES_TEAM_ENGAGEMENT_RATE = KPI(
    name="Sales Team Engagement Rate",
    code="SALES_TEAM_ENGAGEMENT_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The level of engagement and satisfaction of the sales team with the sales enablement program and support provided by the sales enablement team.",
    kpi_definition="The level of engagement and satisfaction of the sales team with the sales enablement program and support provided by the sales enablement team.",
    expected_business_insights="Reflects the level of involvement and commitment of sales reps to collective success and learning.",
    measurement_approach="Measures the level of active participation by sales reps in team meetings, training, and other collaborative activities.",
    
    # Formula
    formula="(Number of Engaged Reps / Total Number of Sales Reps) * 100",
    calculation_formula="(Number of Engaged Reps / Total Number of Sales Reps) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales team engagement rate may indicate improved effectiveness of the sales enablement program and support, leading to higher satisfaction and productivity.
    * A decreasing rate could signal issues with the sales enablement program, lack of support, or dissatisfaction among the sales team, which may impact overall sales performance.
    """,
    diagnostic_questions="""
    * Are there specific aspects of the sales enablement program that the sales team finds most beneficial or lacking?
    * How does the sales team engagement rate compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly gather feedback from the sales team to understand their needs and challenges, and make adjustments to the sales enablement program accordingly.
    * Provide ongoing training and resources to ensure the sales team feels supported and equipped to meet their targets.
    * Recognize and reward sales team members who actively engage with the sales enablement program and contribute to its success.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of the sales team engagement rate over time.
    * Bar graphs comparing engagement rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low sales team engagement rate may lead to decreased sales performance, increased turnover, and negative impact on customer relationships.
    * Consistently low engagement rates could indicate systemic issues within the sales enablement program or organizational culture that need to be addressed.
    """,
    tracking_tools="""
    * CRM systems with built-in sales enablement features to track engagement and satisfaction levels of the sales team.
    * Survey and feedback tools to regularly collect input from the sales team on the effectiveness of the sales enablement program.
    """,
    integration_points="""
    * Integrate the sales team engagement rate with performance management systems to align individual and team goals with engagement metrics.
    * Link engagement data with training and development platforms to tailor resources and support to the specific needs of the sales team.
    """,
    change_impact_analysis="""
    * Improving the sales team engagement rate can lead to increased sales productivity, higher customer satisfaction, and improved overall sales performance.
    * Conversely, a low engagement rate may result in missed sales opportunities, decreased revenue, and negative impact on the company\'s reputation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Enablement Feedback", "Enablement Platform", "Lead", "Loyalty Program", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Support Ticket"]
    }
)
