"""
Sales Support Ticket Resolution Time KPI

The average time taken to resolve sales-related support tickets.
"""

from analytics_models import KPI

SALES_SUPPORT_TICKET_RESOLUTION_TIME = KPI(
    name="Sales Support Ticket Resolution Time",
    code="SALES_SUPPORT_TICKET_RESOLUTION_TIME",
    category="Sales Operations",
    
    # Core Definition
    description="The average time taken to resolve sales-related support tickets.",
    kpi_definition="The average time taken to resolve sales-related support tickets.",
    expected_business_insights="Assesses the responsiveness and efficiency of the sales support team.",
    measurement_approach="Measures the average time taken to resolve a sales support ticket.",
    
    # Formula
    formula="Average Time Taken to Resolve Sales Support Tickets",
    calculation_formula="Average Time Taken to Resolve Sales Support Tickets",
    
    # Analysis
    trend_analysis="""
    * Increasing resolution time may indicate a backlog of support tickets or inefficiencies in the support process.
    * Decreasing resolution time can signal improvements in support team productivity or better prioritization of sales-related issues.
    """,
    diagnostic_questions="""
    * Are there specific types of sales support tickets that consistently take longer to resolve?
    * How does our resolution time compare with industry benchmarks or customer expectations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a ticket prioritization system to ensure urgent sales-related issues are addressed promptly.
    * Provide ongoing training and resources to support agents to improve their efficiency in resolving sales-related tickets.
    * Utilize automation and self-service options to handle common sales support issues more quickly.
    """,
    visualization_suggestions="""
    * Line charts showing the average resolution time over time to identify trends and patterns.
    * Stacked bar charts comparing resolution times for different types of sales support tickets.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long resolution times can lead to frustrated customers and potential loss of sales opportunities.
    * Consistently high resolution times may indicate underlying issues in the sales support process that could impact overall sales performance.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with ticketing functionality to track and manage sales support tickets.
    * Performance analytics tools to identify bottlenecks and inefficiencies in the sales support process.
    """,
    integration_points="""
    * Integrate sales support ticket data with sales performance metrics to understand the impact of support resolution times on sales outcomes.
    * Link with customer feedback systems to gather insights on the impact of support resolution times on customer satisfaction.
    """,
    change_impact_analysis="""
    * Reducing resolution time can lead to improved customer satisfaction and potentially higher sales conversion rates.
    * However, overly aggressive focus on speed may impact the quality of support provided and long-term customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
