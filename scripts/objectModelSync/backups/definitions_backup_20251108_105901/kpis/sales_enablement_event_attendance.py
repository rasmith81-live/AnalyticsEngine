"""
Sales Enablement Event Attendance KPI

The number or percentage of sales team members attending sales enablement events, such as workshops or webinars.
"""

from analytics_models import KPI

SALES_ENABLEMENT_EVENT_ATTENDANCE = KPI(
    name="Sales Enablement Event Attendance",
    code="SALES_ENABLEMENT_EVENT_ATTENDANCE",
    category="Sales Enablement",
    
    # Core Definition
    description="The number or percentage of sales team members attending sales enablement events, such as workshops or webinars.",
    kpi_definition="The number or percentage of sales team members attending sales enablement events, such as workshops or webinars.",
    expected_business_insights="Indicates the level of interest and commitment to continuous learning among the sales team.",
    measurement_approach="Measures the number of sales team members attending sales enablement events or training sessions.",
    
    # Formula
    formula="(Number of Attendees / Total Number of Sales Team Members) * 100",
    calculation_formula="(Number of Attendees / Total Number of Sales Team Members) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing attendance rate at sales enablement events may indicate a growing interest in professional development and a proactive sales team.
    * A decreasing attendance rate could signal disengagement, lack of perceived value in the events, or competing priorities that need to be addressed.
    """,
    diagnostic_questions="""
    * Are there specific events or topics that consistently attract higher attendance?
    * How does the attendance rate compare with the overall sales team performance and individual sales targets?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Offer incentives or recognition for active participation in sales enablement events to boost attendance.
    * Customize event topics and formats based on feedback and preferences from the sales team to increase relevance and engagement.
    * Provide easy access to event recordings or materials for team members who may have scheduling conflicts.
    """,
    visualization_suggestions="""
    * Line charts showing attendance rates over time for different events or types of events.
    * Pie charts comparing attendance rates by sales team members or departments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low attendance rates may lead to missed opportunities for skill development and knowledge sharing among the sales team.
    * Inconsistent attendance could indicate a lack of alignment between the content of the events and the needs of the sales team.
    """,
    tracking_tools="""
    * Event management platforms like Eventbrite or Cvent to streamline event planning and registration processes.
    * Sales performance management software that includes modules for tracking event attendance and correlating it with sales outcomes.
    """,
    integration_points="""
    * Integrate attendance data with individual performance metrics to identify correlations between event participation and sales results.
    * Link event attendance with learning and development systems to track the impact of sales enablement events on skill enhancement and knowledge retention.
    """,
    change_impact_analysis="""
    * Improving attendance rates can lead to a more knowledgeable and motivated sales team, potentially impacting overall sales performance and customer satisfaction.
    * Conversely, low attendance rates may indicate a need for reevaluation of the content and delivery of sales enablement events, impacting the effectiveness of the sales enablement program.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Churn Event", "Enablement Feedback", "Enablement Platform", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
