"""
Sales Enablement Feedback Response Time KPI

The average time it takes for the Sales Enablement Team to respond to and act upon feedback from the sales team.
"""

from analytics_models import KPI

SALES_ENABLEMENT_FEEDBACK_RESPONSE_TIME = KPI(
    name="Sales Enablement Feedback Response Time",
    code="SALES_ENABLEMENT_FEEDBACK_RESPONSE_TIME",
    category="Sales Enablement",
    
    # Core Definition
    description="The average time it takes for the Sales Enablement Team to respond to and act upon feedback from the sales team.",
    kpi_definition="The average time it takes for the Sales Enablement Team to respond to and act upon feedback from the sales team.",
    expected_business_insights="Assesses the responsiveness and agility of the sales enablement team to address concerns and improve resources.",
    measurement_approach="Calculates the average time it takes for the sales enablement team to respond to feedback from the sales team.",
    
    # Formula
    formula="Average Time from Feedback Receipt to Response",
    calculation_formula="Average Time from Feedback Receipt to Response",
    
    # Analysis
    trend_analysis="""
    * An increasing response time may indicate a backlog of feedback that the Sales Enablement Team is struggling to address.
    * A decreasing response time can signal improved efficiency in addressing and acting upon sales team feedback.
    """,
    diagnostic_questions="""
    * Are there specific types of feedback that consistently take longer to address?
    * How does our response time compare with industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a feedback management system to prioritize and track incoming feedback.
    * Provide regular training and resources to the Sales Enablement Team to improve their ability to address feedback promptly.
    * Establish clear processes and responsibilities for handling and acting upon sales team feedback.
    """,
    visualization_suggestions="""
    * Line charts showing the average response time over time to identify any increasing or decreasing trends.
    * Bar graphs comparing response times for different types of feedback to pinpoint areas needing improvement.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long response times can lead to frustration and disengagement from the sales team, impacting overall performance.
    * Consistently high response times may indicate a lack of resources or inefficiencies within the Sales Enablement Team.
    """,
    tracking_tools="""
    * Feedback management software like SurveyMonkey or Qualtrics to streamline the collection and organization of feedback.
    * CRM systems with integrated feedback modules to directly link sales team feedback with action plans.
    """,
    integration_points="""
    * Integrate feedback response time tracking with performance management systems to align feedback handling with individual and team goals.
    * Link feedback response time with training and development programs to address any recurring issues or areas for improvement.
    """,
    change_impact_analysis="""
    * Improving response time can lead to better alignment between sales team needs and enablement support, potentially boosting overall sales performance.
    * However, focusing solely on reducing response time may lead to rushed or inadequate actions, impacting the quality of support provided.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer Feedback", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
