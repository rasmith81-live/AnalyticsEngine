"""
Sales Pipeline Velocity KPI

The time it takes for a lead to move through the sales pipeline and convert into a sale.
"""

from analytics_models import KPI

SALES_PIPELINE_VELOCITY = KPI(
    name="Sales Pipeline Velocity",
    code="SALES_PIPELINE_VELOCITY",
    category="Sales Operations",
    
    # Core Definition
    description="The time it takes for a lead to move through the sales pipeline and convert into a sale.",
    kpi_definition="The time it takes for a lead to move through the sales pipeline and convert into a sale.",
    expected_business_insights="Indicates the overall health and momentum of the sales process.",
    measurement_approach="Measures the speed at which deals move through the sales pipeline.",
    
    # Formula
    formula="(Number of Deals in Pipeline * Average Deal Size * Win Rate) / Length of Sales Cycle",
    calculation_formula="(Number of Deals in Pipeline * Average Deal Size * Win Rate) / Length of Sales Cycle",
    
    # Analysis
    trend_analysis="""
    * Shortening sales pipeline velocity may indicate improved lead qualification and sales process efficiency.
    * An increasing time to convert may signal issues with lead quality, sales team performance, or market conditions.
    """,
    diagnostic_questions="""
    * Are there specific stages in the sales pipeline where leads tend to stall or drop off?
    * How does our sales pipeline velocity compare with industry benchmarks or historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement lead scoring to prioritize high-quality leads and focus sales efforts more effectively.
    * Provide targeted training and support for sales teams to improve their ability to move leads through the pipeline.
    * Regularly review and optimize the sales process to identify and remove bottlenecks.
    """,
    visualization_suggestions="""
    * Line charts showing the average time spent at each stage of the sales pipeline.
    * Funnel charts to visualize the drop-off rates between pipeline stages.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Slow sales pipeline velocity can lead to missed revenue targets and reduced cash flow.
    * Rapid pipeline velocity without proper lead qualification can result in increased customer churn and decreased customer lifetime value.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track lead movement and identify areas for improvement.
    * Sales enablement tools to streamline the sales process and provide sales teams with the resources they need to move leads through the pipeline efficiently.
    """,
    integration_points="""
    * Integrate sales pipeline velocity with marketing automation systems to ensure a smooth transition from marketing-qualified leads to sales-qualified leads.
    * Link sales pipeline velocity with customer relationship management (CRM) systems to track the impact of lead movement on customer interactions and conversions.
    """,
    change_impact_analysis="""
    * Improving sales pipeline velocity can lead to increased revenue and improved sales team morale, but may also require additional resources and support.
    * Slowing down sales pipeline velocity to focus on lead quality and customer relationships may result in lower short-term sales, but can lead to higher customer satisfaction and long-term loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Deal", "Deal", "Lead", "Lead Qualification", "Lost Sale", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
