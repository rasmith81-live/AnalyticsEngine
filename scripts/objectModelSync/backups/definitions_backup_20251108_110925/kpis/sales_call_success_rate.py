"""
Sales Call Success Rate KPI

The percentage of sales calls that result in a positive outcome, such as moving a lead to the next stage in the pipeline.
"""

from analytics_models import KPI

SALES_CALL_SUCCESS_RATE = KPI(
    name="Sales Call Success Rate",
    code="SALES_CALL_SUCCESS_RATE",
    category="Inside Sales",
    
    # Core Definition
    description="The percentage of sales calls that result in a positive outcome, such as moving a lead to the next stage in the pipeline.",
    kpi_definition="The percentage of sales calls that result in a positive outcome, such as moving a lead to the next stage in the pipeline.",
    expected_business_insights="Evaluates the effectiveness of sales calls in advancing the sales process.",
    measurement_approach="The percentage of sales calls that result in a desired outcome, such as an appointment or sale.",
    
    # Formula
    formula="(Number of Successful Sales Calls / Total Number of Sales Calls) * 100",
    calculation_formula="(Number of Successful Sales Calls / Total Number of Sales Calls) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales call success rate may indicate improved lead qualification or more effective sales strategies.
    * A decreasing rate could signal issues with lead quality, sales team performance, or changes in the market.
    """,
    diagnostic_questions="""
    * Are there specific sales tactics or scripts that consistently lead to positive outcomes?
    * How does our sales call success rate compare with industry benchmarks or historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide ongoing sales training and coaching to improve communication and closing skills.
    * Regularly review and update lead qualification criteria to ensure sales calls are focused on high-potential leads.
    * Implement a customer relationship management (CRM) system to track and analyze sales call outcomes.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in sales call success rate over time.
    * Pie charts comparing success rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low success rate can lead to wasted resources and demotivated sales teams.
    * A sudden drop in success rate may indicate external factors affecting the market or customer behavior.
    """,
    tracking_tools="""
    * CRM software with call tracking and analytics capabilities to monitor and analyze sales call outcomes.
    * Sales enablement platforms to provide sales teams with the tools and resources needed to improve success rates.
    """,
    integration_points="""
    * Integrate sales call success rate data with lead generation and marketing systems to understand the quality of leads being generated.
    * Link success rate metrics with individual sales performance data to identify coaching and training opportunities.
    """,
    change_impact_analysis="""
    * Improving the sales call success rate can lead to increased revenue and customer satisfaction.
    * However, a focus solely on success rate may neglect the quality of customer interactions and long-term relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Appointment", "Call", "Customer Success Manager", "Lead", "Lead Qualification", "Lost Sale", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
