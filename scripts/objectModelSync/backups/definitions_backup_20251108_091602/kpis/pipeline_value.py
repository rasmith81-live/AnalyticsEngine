"""
Pipeline Value KPI

The total value of the sales pipeline. A higher pipeline value indicates effective training and coaching.
"""

from analytics_models import KPI

PIPELINE_VALUE = KPI(
    name="Pipeline Value",
    code="PIPELINE_VALUE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The total value of the sales pipeline. A higher pipeline value indicates effective training and coaching.",
    kpi_definition="The total value of the sales pipeline. A higher pipeline value indicates effective training and coaching.",
    expected_business_insights="Indicates the potential future revenue and the health of the sales pipeline, influenced by effective training and sales tactics.",
    measurement_approach="The total dollar value of all opportunities in the sales pipeline at a given time.",
    
    # Formula
    formula="Sum of the Value of All Opportunities in the Sales Pipeline",
    calculation_formula="Sum of the Value of All Opportunities in the Sales Pipeline",
    
    # Analysis
    trend_analysis="""
    * An increasing pipeline value may indicate successful lead generation and effective sales strategies.
    * A decreasing pipeline value could signal challenges in converting leads or a decline in overall sales opportunities.
    """,
    diagnostic_questions="""
    * What are the main sources of leads contributing to the pipeline value?
    * Are there specific stages in the sales process where leads are dropping off, impacting the pipeline value?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and coaching focused on lead conversion and closing techniques.
    * Implement lead nurturing strategies to maintain and advance leads through the sales pipeline.
    * Regularly review and update the sales pipeline to ensure accuracy and relevance of opportunities.
    """,
    visualization_suggestions="""
    * Funnel charts to visualize the progression of leads through the sales pipeline.
    * Line graphs to track changes in pipeline value over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A stagnant or declining pipeline value may lead to missed sales targets and revenue goals.
    * An inflated pipeline value without corresponding sales may indicate inaccurate or inflated opportunity tracking.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage leads throughout the sales pipeline.
    * Sales analytics tools to gain insights into lead behavior and pipeline performance.
    """,
    integration_points="""
    * Integrate pipeline value tracking with sales forecasting to align sales strategies with anticipated revenue.
    * Link pipeline value with marketing analytics to assess the effectiveness of lead generation efforts.
    """,
    change_impact_analysis="""
    * Improving pipeline value can lead to increased revenue and sales team motivation.
    * However, a declining pipeline value may require adjustments in sales and marketing strategies, potentially impacting resource allocation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Coaching Session", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
