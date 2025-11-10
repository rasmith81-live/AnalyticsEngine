"""
Partner Support Ticket Resolution Time KPI

The average time taken to resolve support tickets raised by channel partners, indicating the effectiveness of partner support.
"""

from analytics_models import KPI

PARTNER_SUPPORT_TICKET_RESOLUTION_TIME = KPI(
    name="Partner Support Ticket Resolution Time",
    code="PARTNER_SUPPORT_TICKET_RESOLUTION_TIME",
    category="Channel Sales",
    
    # Core Definition
    description="The average time taken to resolve support tickets raised by channel partners, indicating the effectiveness of partner support.",
    kpi_definition="The average time taken to resolve support tickets raised by channel partners, indicating the effectiveness of partner support.",
    expected_business_insights="Ensures timely support to partners, which can affect their performance and satisfaction.",
    measurement_approach="Measures the average time taken to resolve support tickets raised by partners.",
    
    # Formula
    formula="Average Time to Resolve Partner Support Tickets",
    calculation_formula="Average Time to Resolve Partner Support Tickets",
    
    # Analysis
    trend_analysis="""
    * Increasing resolution time may indicate a growing backlog of partner support tickets or inefficiencies in the support process.
    * Decreasing resolution time can signal improvements in support ticket prioritization, resource allocation, or issue resolution capabilities.
    """,
    diagnostic_questions="""
    * Are there specific types of support tickets that consistently take longer to resolve?
    * How does our partner support ticket resolution time compare to industry benchmarks or our own historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a ticket prioritization system to address urgent partner issues more quickly.
    * Provide additional training or resources to support agents to improve their ability to resolve issues efficiently.
    * Regularly review and optimize support processes to identify and eliminate bottlenecks.
    """,
    visualization_suggestions="""
    * Line charts showing the average resolution time over time to identify trends.
    * Stacked bar charts comparing resolution times for different types of support tickets.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long resolution times can lead to partner dissatisfaction and strained relationships.
    * Consistently high resolution times may indicate systemic issues in partner support that could impact overall channel performance.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with ticketing and support modules for tracking and managing partner support tickets.
    * Performance analytics tools to identify patterns and areas for improvement in the support process.
    """,
    integration_points="""
    * Integrate partner support ticket data with overall channel performance metrics to understand the impact of support on partner satisfaction and sales.
    * Link support ticket resolution time with resource allocation and capacity planning to ensure adequate support coverage.
    """,
    change_impact_analysis="""
    * Improving resolution time can enhance partner satisfaction and loyalty, leading to increased sales and revenue.
    * Conversely, prolonged resolution times can strain partner relationships and impact overall channel performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
