"""
Outbound Calls per Day KPI

The number of outbound calls made by the Sales Development team per day. It provides insight into how active the team is in generating new leads and opportunities.
"""

OUTBOUND_CALLS_PER_DAY = {
    "code": "OUTBOUND_CALLS_PER_DAY",
    "name": "Outbound Calls per Day",
    "description": "The number of outbound calls made by the Sales Development team per day. It provides insight into how active the team is in generating new leads and opportunities.",
    "formula": "Total Outbound Calls / Number of Working Days",
    "calculation_formula": "Total Outbound Calls / Number of Working Days",
    "category": "Sales Development",
    "is_active": True,
    "kpi_definition": "The number of outbound calls made by the Sales Development team per day. It provides insight into how active the team is in generating new leads and opportunities.",
    "expected_business_insights": "Indicates sales rep activity levels and potential for lead generation and customer outreach.",
    "measurement_approach": "Measures the average number of outbound calls made by a sales rep each day.",
    "trend_analysis": """
    * An increasing number of outbound calls per day may indicate a proactive and engaged sales development team actively pursuing new leads.
    * A decreasing trend in outbound calls could signal potential issues with team motivation, lead generation strategies, or resource allocation.
    """,
    "diagnostic_questions": """
    * Are there specific time periods or days of the week when outbound call volume tends to be higher or lower?
    * What is the average conversion rate of outbound calls to qualified leads, and how does it correlate with the number of calls made?
    """,
    "actionable_tips": """
    * Implement call cadences and schedules to ensure consistent outbound call activity throughout the day and week.
    * Provide ongoing training and coaching to the sales development team to improve call quality and effectiveness.
    * Regularly review and update the lead generation strategy to ensure a steady flow of new prospects to call.
    """,
    "visualization_suggestions": """
    * Line charts showing the daily outbound call volume over time to identify patterns and fluctuations.
    * Comparison bar charts to visualize the outbound call performance of individual team members or regions.
    """,
    "risk_warnings": """
    * A consistently low number of outbound calls per day may lead to a lack of new leads and opportunities, impacting overall sales performance.
    * An excessively high number of calls without corresponding results could indicate inefficiencies in the lead generation or qualification process.
    """,
    "tracking_tools": """
    * CRM systems like Salesforce or HubSpot to track and analyze outbound call activity, lead status, and conversion rates.
    * Call tracking and analytics tools such as CallRail or Gong to monitor call quality and effectiveness.
    """,
    "integration_points": """
    * Integrate outbound call data with sales performance metrics to understand the impact of call activity on revenue generation.
    * Link outbound call activity with marketing campaign data to assess the effectiveness of lead generation efforts.
    """,
    "change_impact_analysis": """
    * Increasing outbound calls may lead to higher lead volume and potential revenue growth, but it could also impact the workload and stress levels of the sales development team.
    * Conversely, a decrease in outbound calls may result in a decline in new opportunities and sales, affecting overall business performance.
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Lead", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
}
