"""
Sales Pipeline Growth KPI

The increase in the number of potential deals in the sales pipeline over a given period.
"""

from analytics_models import KPI

SALES_PIPELINE_GROWTH = KPI(
    name="Sales Pipeline Growth",
    code="SALES_PIPELINE_GROWTH",
    category="Inside Sales",
    
    # Core Definition
    description="The increase in the number of potential deals in the sales pipeline over a given period.",
    kpi_definition="The increase in the number of potential deals in the sales pipeline over a given period.",
    expected_business_insights="Tracks the health of the sales funnel and the potential for future revenue.",
    measurement_approach="Change in the number of opportunities or total value in the sales pipeline over time.",
    
    # Formula
    formula="(Current Pipeline Value - Previous Pipeline Value) / Previous Pipeline Value",
    calculation_formula="(Current Pipeline Value - Previous Pipeline Value) / Previous Pipeline Value",
    
    # Analysis
    trend_analysis="""
    * An increasing sales pipeline growth may indicate improved lead generation and marketing efforts.
    * A decreasing growth rate could signal challenges in converting leads to opportunities or a decrease in market demand.
    """,
    diagnostic_questions="""
    * What is the average time it takes for a lead to progress through the sales pipeline?
    * Are there specific stages in the pipeline where leads tend to drop off or stagnate?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement lead nurturing strategies to move potential deals through the pipeline more effectively.
    * Regularly review and update the qualification criteria for opportunities to ensure a healthy pipeline.
    * Provide ongoing training and support for sales representatives to improve their ability to move leads through the pipeline.
    """,
    visualization_suggestions="""
    * Funnel charts to visualize the progression of leads through each stage of the sales pipeline.
    * Line graphs to track the growth of the pipeline over time and identify any fluctuations.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A stagnant or declining sales pipeline growth can lead to reduced sales opportunities and revenue.
    * An excessively large pipeline without proper management can result in inefficiencies and wasted resources.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage leads throughout the pipeline.
    * Sales analytics tools to gain insights into the performance of the sales pipeline and identify areas for improvement.
    """,
    integration_points="""
    * Integrate the sales pipeline data with marketing automation systems to align lead generation efforts with the needs of the sales team.
    * Connect the pipeline with customer support systems to ensure a seamless transition from sales to post-sales service.
    """,
    change_impact_analysis="""
    * Improving the sales pipeline growth can lead to increased revenue and a more predictable sales process.
    * However, rapid growth without proper management can strain resources and lead to decreased quality of customer interactions.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
