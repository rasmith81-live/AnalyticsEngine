"""
Number of Active Prospects KPI

The total number of prospects that are currently being engaged by the sales team.
"""

from analytics_models import KPI

NUMBER_OF_ACTIVE_PROSPECTS = KPI(
    name="Number of Active Prospects",
    code="NUMBER_OF_ACTIVE_PROSPECTS",
    category="Sales Development",
    
    # Core Definition
    description="The total number of prospects that are currently being engaged by the sales team.",
    kpi_definition="The total number of prospects that are currently being engaged by the sales team.",
    expected_business_insights="Provides an indication of the sales pipeline health and potential future business.",
    measurement_approach="Tracks the total number of potential customers currently engaged with the sales process.",
    
    # Formula
    formula="Count of Prospects Currently in the Sales Pipeline",
    calculation_formula="Count of Prospects Currently in the Sales Pipeline",
    
    # Analysis
    trend_analysis="""
    * An increasing number of active prospects may indicate a growing market or improved lead generation efforts.
    * A decreasing number could signal a lack of new leads or a shift in the target market\'s interest.
    """,
    diagnostic_questions="""
    * Are there specific industries or regions where the number of active prospects is consistently higher or lower?
    * What strategies or channels have been most effective in generating new prospects?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement targeted marketing campaigns to reach new prospects in untapped industries or regions.
    * Regularly review and update the sales team\'s prospecting techniques to adapt to changing market dynamics.
    * Utilize customer relationship management (CRM) software to track and manage prospect engagement more effectively.
    """,
    visualization_suggestions="""
    * Line charts to visualize the trend in the number of active prospects over time.
    * Pie charts to compare the distribution of active prospects across different industries or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low number of active prospects may lead to a stagnant sales pipeline and reduced revenue opportunities.
    * An excessively high number of prospects without proper qualification may strain the sales team\'s resources and lead to inefficiencies.
    """,
    tracking_tools="""
    * Lead management software such as HubSpot or Salesforce to track and manage prospect interactions.
    * Data analytics tools to identify patterns and trends in prospect engagement for targeted outreach.
    """,
    integration_points="""
    * Integrate prospect data with marketing automation platforms to align sales and marketing efforts for better lead nurturing.
    * Link prospect information with customer relationship management systems to provide a comprehensive view of the sales pipeline.
    """,
    change_impact_analysis="""
    * An increase in the number of active prospects can lead to higher sales volume but may also require additional resources for effective management.
    * A decrease in prospects may prompt a need for strategic shifts in marketing and sales tactics to reinvigorate lead generation efforts.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
