"""
Sales Pipeline Health KPI

The status of the opportunities in the sales pipeline, which can include the number of deals, their value, and the average time for deals to move through the pipeline.
"""

from analytics_models import KPI

SALES_PIPELINE_HEALTH = KPI(
    name="Sales Pipeline Health",
    code="SALES_PIPELINE_HEALTH",
    category="Sales Performance",
    
    # Core Definition
    description="The status of the opportunities in the sales pipeline, which can include the number of deals, their value, and the average time for deals to move through the pipeline.",
    kpi_definition="The status of the opportunities in the sales pipeline, which can include the number of deals, their value, and the average time for deals to move through the pipeline.",
    expected_business_insights="Provides a comprehensive view of expected sales and helps in forecasting and resource allocation.",
    measurement_approach="Combines the number of opportunities, value of opportunities, and conversion rates in the sales pipeline.",
    
    # Formula
    formula="Total Value of Sales Pipeline / Number of Opportunities in Pipeline",
    calculation_formula="Total Value of Sales Pipeline / Number of Opportunities in Pipeline",
    
    # Analysis
    trend_analysis="""
    * Increasing number of deals in the pipeline may indicate improved lead generation or sales efforts.
    * A decreasing average time for deals to move through the pipeline could signal more efficient sales processes or better-qualified leads.
    """,
    diagnostic_questions="""
    * What are the main reasons for deals stalling or getting stuck in the pipeline?
    * How does our sales pipeline health compare to industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a clear qualification process to ensure only high-potential opportunities enter the pipeline.
    * Regularly review and clean the pipeline to remove stale or low-value opportunities.
    * Provide ongoing training and support for sales reps to help them move deals through the pipeline more effectively.
    """,
    visualization_suggestions="""
    * Funnel charts to visualize the progression of deals through different stages of the pipeline.
    * Line charts to track changes in the number of deals and their value over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A bloated pipeline with low-quality opportunities can lead to wasted resources and decreased win rates.
    * Long average time for deals to move through the pipeline may indicate inefficiencies or bottlenecks in the sales process.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage opportunities in the pipeline.
    * Sales analytics tools to gain insights into the health and performance of the sales pipeline.
    """,
    integration_points="""
    * Integrate sales pipeline data with marketing and lead generation systems to ensure a steady flow of qualified opportunities.
    * Link pipeline health with sales forecasting and resource allocation for better sales management.
    """,
    change_impact_analysis="""
    * Improving sales pipeline health can lead to increased revenue and better sales team performance.
    * However, a sudden decrease in the number of deals in the pipeline may impact future revenue and require adjustments in sales strategies.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer Health Record", "Deal", "Lead", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
