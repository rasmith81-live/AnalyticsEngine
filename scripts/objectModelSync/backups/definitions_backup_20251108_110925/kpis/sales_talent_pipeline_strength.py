"""
Sales Talent Pipeline Strength KPI

The robustness of the internal pipeline for promoting trained and high-performing sales reps to advanced roles.
"""

from analytics_models import KPI

SALES_TALENT_PIPELINE_STRENGTH = KPI(
    name="Sales Talent Pipeline Strength",
    code="SALES_TALENT_PIPELINE_STRENGTH",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The robustness of the internal pipeline for promoting trained and high-performing sales reps to advanced roles.",
    kpi_definition="The robustness of the internal pipeline for promoting trained and high-performing sales reps to advanced roles.",
    expected_business_insights="Indicates the effectiveness of talent development strategies and the potential for sustaining a high-performing sales team.",
    measurement_approach="A measure of the quality and readiness of potential sales hires within the organization\'s recruitment pipeline.",
    
    # Formula
    formula="Qualitative Assessment or Readiness Rating",
    calculation_formula="Qualitative Assessment or Readiness Rating",
    
    # Analysis
    trend_analysis="""
    * An increasing pipeline strength may indicate successful sales training and development programs.
    * A decreasing pipeline strength could signal issues in retaining and promoting high-performing sales reps.
    """,
    diagnostic_questions="""
    * Are there specific stages in the pipeline where attrition rates are higher?
    * How does the pipeline strength compare with industry benchmarks or historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement mentorship programs to support the development of sales reps at different pipeline stages.
    * Regularly review and update promotion criteria to ensure alignment with evolving business needs.
    * Provide ongoing training and upskilling opportunities to enhance the readiness of sales reps for advanced roles.
    """,
    visualization_suggestions="""
    * Stacked bar charts showing the distribution of sales reps across different pipeline stages.
    * Trend lines to visualize the changes in pipeline strength over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low pipeline strength may lead to talent shortages in advanced sales roles, impacting overall sales performance.
    * High pipeline strength without corresponding promotion opportunities can lead to disengagement and attrition among sales reps.
    """,
    tracking_tools="""
    * CRM systems with pipeline tracking capabilities to monitor the progression of sales reps.
    * Performance management software to assess the readiness and potential of sales reps for advancement.
    """,
    integration_points="""
    * Integrate pipeline strength data with HR systems to align training and development initiatives with promotion opportunities.
    * Link pipeline strength with sales performance metrics to identify correlations between pipeline health and sales outcomes.
    """,
    change_impact_analysis="""
    * Improving pipeline strength can lead to a more robust and sustainable sales organization, but may require additional investment in training and development.
    * A declining pipeline strength can impact the overall talent pool available for critical sales roles, affecting revenue generation and customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
