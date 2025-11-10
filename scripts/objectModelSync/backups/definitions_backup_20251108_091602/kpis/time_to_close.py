"""
Time to Close KPI

The time taken to close deals with channel partners.
"""

from analytics_models import KPI

TIME_TO_CLOSE = KPI(
    name="Time to Close",
    code="TIME_TO_CLOSE",
    category="Channel Sales",
    
    # Core Definition
    description="The time taken to close deals with channel partners.",
    kpi_definition="The time taken to close deals with channel partners.",
    expected_business_insights="Indicates the efficiency of the sales process and can influence sales strategy and forecasting.",
    measurement_approach="Tracks the average duration from when a sales opportunity is identified to when the deal is closed.",
    
    # Formula
    formula="Average Number of Days from Opportunity to Closed Deal",
    calculation_formula="Average Number of Days from Opportunity to Closed Deal",
    
    # Analysis
    trend_analysis="""
    * Increasing time to close may indicate challenges in partner engagement or deal negotiation.
    * Decreasing time to close can signal improved partner relationships or more efficient sales processes.
    """,
    diagnostic_questions="""
    * Are there specific partner segments or regions where the time to close is consistently longer?
    * How does our time to close compare with industry benchmarks or with direct sales cycles?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and resources to channel partners to help them navigate the sales process more effectively.
    * Streamline deal approval processes and provide clear guidelines for partner engagement to reduce unnecessary delays.
    * Regularly review and optimize the sales pipeline to identify and address potential bottlenecks.
    """,
    visualization_suggestions="""
    * Line charts tracking the average time to close over time to identify trends and seasonality.
    * Funnel charts to visualize the distribution of deals at different stages of the sales cycle.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long time to close can lead to partner frustration and disengagement, impacting future collaboration.
    * Consistently short time to close may indicate potential issues with deal quality or pricing strategies.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems to track and analyze partner interactions and deal progress.
    * Sales enablement platforms to provide partners with the necessary resources and support to expedite the sales process.
    """,
    integration_points="""
    * Integrate time to close data with partner performance metrics to identify correlations and opportunities for improvement.
    * Link time to close with lead generation and marketing efforts to assess the effectiveness of different lead sources.
    """,
    change_impact_analysis="""
    * Reducing time to close can lead to increased partner satisfaction and loyalty, potentially driving higher sales volumes.
    * However, overly aggressive efforts to shorten the sales cycle may result in rushed or suboptimal deals, impacting long-term partner relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Expansion Opportunity", "Lead", "Opportunity", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
