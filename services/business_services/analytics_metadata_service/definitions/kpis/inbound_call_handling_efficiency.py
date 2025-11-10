"""
Inbound Call Handling Efficiency KPI

The effectiveness of the sales team in managing inbound sales calls and converting them into opportunities.
"""

from analytics_models import KPI

INBOUND_CALL_HANDLING_EFFICIENCY = KPI(
    name="Inbound Call Handling Efficiency",
    code="INBOUND_CALL_HANDLING_EFFICIENCY",
    category="Inside Sales",
    
    # Core Definition
    description="The effectiveness of the sales team in managing inbound sales calls and converting them into opportunities.",
    kpi_definition="The effectiveness of the sales team in managing inbound sales calls and converting them into opportunities.",
    expected_business_insights="Provides insights into the performance of sales reps in handling incoming calls and customer inquiries.",
    measurement_approach="Measures metrics like average handle time, calls per hour, and resolution rate.",
    
    # Formula
    formula="Sum of All Inbound Call Metrics / Number of Calls Handled",
    calculation_formula="Sum of All Inbound Call Metrics / Number of Calls Handled",
    
    # Analysis
    trend_analysis="""
    * An increasing inbound call handling efficiency may indicate improved sales team training or better call management processes.
    * A decreasing efficiency could signal issues with staffing, technology, or customer service quality.
    """,
    diagnostic_questions="""
    * Are there specific times of the day or week when inbound call handling efficiency tends to drop?
    * How does our inbound call handling efficiency compare with industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in call center technology to streamline call routing and improve response times.
    * Provide ongoing training and coaching for sales representatives to enhance their call handling skills.
    * Implement customer relationship management (CRM) systems to track and manage inbound sales leads more effectively.
    """,
    visualization_suggestions="""
    * Line charts showing the daily or weekly trends in inbound call handling efficiency.
    * Pie charts comparing the distribution of call outcomes (e.g., converted to opportunities, missed, etc.).
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low inbound call handling efficiency can result in missed sales opportunities and dissatisfied customers.
    * Chronic inefficiency may indicate underlying issues in sales processes or team performance.
    """,
    tracking_tools="""
    * Call tracking and analytics software to monitor call volumes, durations, and outcomes.
    * CRM systems with built-in call management features to streamline lead handling and follow-up.
    """,
    integration_points="""
    * Integrate inbound call handling efficiency data with sales performance metrics to understand the impact on overall sales results.
    * Link call handling data with customer feedback systems to identify areas for improvement in customer interactions.
    """,
    change_impact_analysis="""
    * Improving inbound call handling efficiency can lead to increased sales conversion rates and customer satisfaction.
    * However, overly aggressive efficiency targets may result in rushed or impersonal customer interactions, affecting long-term customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Call", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
