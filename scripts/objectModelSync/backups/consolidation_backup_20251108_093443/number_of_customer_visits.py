"""
Number of Customer Visits KPI

The total number of in-person meetings the sales team has with potential or existing customers.
"""

from analytics_models import KPI

NUMBER_OF_CUSTOMER_VISITS = KPI(
    name="Number of Customer Visits",
    code="NUMBER_OF_CUSTOMER_VISITS",
    category="Outside Sales",
    
    # Core Definition
    description="The total number of in-person meetings the sales team has with potential or existing customers.",
    kpi_definition="The total number of in-person meetings the sales team has with potential or existing customers.",
    expected_business_insights="Provides a measure of customer engagement and sales activity, helping to assess the impact of face-to-face interactions.",
    measurement_approach="Tracks the total number of in-person visits made to customers.",
    
    # Formula
    formula="Sum of all Customer Visits",
    calculation_formula="Sum of all Customer Visits",
    
    # Analysis
    trend_analysis="""
    * An increasing number of customer visits may indicate a proactive sales team or a growing customer base.
    * A decreasing number of visits could signal a lack of sales team effectiveness or a shift in customer preferences towards remote communication.
    """,
    diagnostic_questions="""
    * Are there specific regions or customer segments that the sales team is neglecting in their visitation schedule?
    * How do the conversion rates from these visits compare to historical data or industry benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a customer relationship management (CRM) system to track and prioritize customer visits.
    * Provide sales training to improve the effectiveness of in-person meetings and increase conversion rates.
    * Regularly review and adjust the visitation schedule based on customer feedback and sales performance data.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer visits over time.
    * Geospatial maps to visualize the distribution of customer visits across different regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low number of customer visits may lead to missed sales opportunities and decreased customer engagement.
    * Over-reliance on in-person meetings may result in higher travel costs and inefficiencies.
    """,
    tracking_tools="""
    * CRM software like Salesforce or HubSpot for tracking and managing customer visits.
    * Route optimization tools to minimize travel time and maximize the number of visits in a day.
    """,
    integration_points="""
    * Integrate customer visit data with sales performance metrics to understand the impact of visits on overall sales results.
    * Link customer visit information with customer feedback systems to measure the effectiveness of in-person interactions.
    """,
    change_impact_analysis="""
    * Increasing the number of customer visits may lead to higher sales but also higher travel and entertainment expenses.
    * Reducing the number of visits may free up sales team time for other activities but could also result in decreased customer satisfaction and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Meeting", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
