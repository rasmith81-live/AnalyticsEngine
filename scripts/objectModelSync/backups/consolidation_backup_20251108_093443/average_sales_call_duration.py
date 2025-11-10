"""
Average Sales Call Duration KPI

The average length of time of a sales call.
"""

from analytics_models import KPI

AVERAGE_SALES_CALL_DURATION = KPI(
    name="Average Sales Call Duration",
    code="AVERAGE_SALES_CALL_DURATION",
    category="Inside Sales",
    
    # Core Definition
    description="The average length of time of a sales call.",
    kpi_definition="The average length of time of a sales call.",
    expected_business_insights="Offers insights into the efficiency of sales calls and whether more or less time should be spent on calls to optimize sales.",
    measurement_approach="The average length of time spent on sales calls.",
    
    # Formula
    formula="Total Time of Sales Calls / Number of Sales Calls",
    calculation_formula="Total Time of Sales Calls / Number of Sales Calls",
    
    # Analysis
    trend_analysis="""
    * An increasing average sales call duration may indicate more in-depth conversations with potential customers, potentially leading to higher quality leads and better conversion rates.
    * A decreasing duration could signal a more efficient sales process, but it may also indicate rushed or incomplete interactions with prospects.
    """,
    diagnostic_questions="""
    * Are there specific sales reps or teams that consistently have longer or shorter call durations?
    * How does the average call duration correlate with the conversion rates and overall sales performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide sales training and coaching to help reps engage in more effective and efficient conversations with prospects.
    * Implement call monitoring and analysis tools to identify areas for improvement in sales call quality and duration.
    * Encourage sales reps to focus on active listening and asking relevant, open-ended questions to keep the conversation engaging and productive.
    """,
    visualization_suggestions="""
    * Line charts showing the average call duration over time for individual sales reps or teams.
    * Comparative bar charts displaying the average call duration for different product lines or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Excessively long call durations may lead to decreased productivity and missed opportunities to engage with other prospects.
    * Very short call durations could indicate a lack of thoroughness in the sales process, potentially resulting in lost sales opportunities.
    """,
    tracking_tools="""
    * CRM systems with call tracking and recording capabilities to analyze and improve sales call effectiveness.
    * Sales engagement platforms that provide insights into prospect behavior and interaction patterns during sales calls.
    """,
    integration_points="""
    * Integrate average call duration data with customer relationship management (CRM) systems to understand the impact of call length on customer relationships and sales outcomes.
    * Link call duration metrics with sales performance data to identify correlations between call quality and conversion rates.
    """,
    change_impact_analysis="""
    * Improving average call duration can lead to better customer relationships and higher conversion rates, but it may also require additional resources for training and technology.
    * Significantly reducing call durations without maintaining quality could lead to missed opportunities and decreased sales effectiveness.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Call", "Deal", "Lead", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
