"""
Coaching Session Frequency KPI

The number of coaching sessions provided to each sales rep within a given time period.
"""

from analytics_models import KPI

COACHING_SESSION_FREQUENCY = KPI(
    name="Coaching Session Frequency",
    code="COACHING_SESSION_FREQUENCY",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The number of coaching sessions provided to each sales rep within a given time period.",
    kpi_definition="The number of coaching sessions provided to each sales rep within a given time period.",
    expected_business_insights="Reveals the emphasis on and regularity of coaching, which can impact sales rep development and performance.",
    measurement_approach="The number of coaching sessions held within a specified period, such as monthly or quarterly.",
    
    # Formula
    formula="Total Number of Coaching Sessions / Specified Time Period",
    calculation_formula="Total Number of Coaching Sessions / Specified Time Period",
    
    # Analysis
    trend_analysis="""
    * An increasing coaching session frequency may indicate a need for more support or development for sales reps.
    * A decreasing frequency could signal improved sales performance or a lack of focus on coaching from sales management.
    """,
    diagnostic_questions="""
    * Are there specific sales reps who consistently require more coaching sessions?
    * How does the coaching session frequency correlate with sales performance and targets?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular one-on-one coaching sessions to provide personalized support for each sales rep.
    * Utilize coaching tools and resources to make sessions more effective and impactful.
    * Encourage a culture of continuous learning and improvement within the sales team.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of coaching session frequency over time for each sales rep.
    * Comparison bar charts to visualize the variance in coaching session frequency among different sales reps.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low coaching session frequency may lead to underperformance and missed sales opportunities.
    * High coaching session frequency without improvement in sales performance may indicate ineffective coaching methods or other underlying issues.
    """,
    tracking_tools="""
    * Utilize sales coaching and training platforms such as Brainshark or Allego to track and analyze coaching session frequency.
    * Implement customer relationship management (CRM) systems to integrate coaching data with sales performance metrics.
    """,
    integration_points="""
    * Integrate coaching session frequency data with performance reviews and goal setting processes to align coaching efforts with individual sales targets.
    * Link coaching session frequency with sales forecasting and pipeline management to identify areas for improvement and development.
    """,
    change_impact_analysis="""
    * Increasing coaching session frequency may lead to improved sales performance and customer satisfaction, but could also require additional time and resources.
    * Conversely, a decrease in coaching session frequency may result in missed opportunities for development and growth within the sales team.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Coaching Session", "Deal", "Lead", "Opportunity", "Partner Training", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
