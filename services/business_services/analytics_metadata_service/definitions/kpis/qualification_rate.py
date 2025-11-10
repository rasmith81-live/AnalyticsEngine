"""
Qualification Rate KPI

The percentage of new sales hires who pass the initial training and are deemed qualified to start selling.
"""

from analytics_models import KPI

QUALIFICATION_RATE = KPI(
    name="Qualification Rate",
    code="QUALIFICATION_RATE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The percentage of new sales hires who pass the initial training and are deemed qualified to start selling.",
    kpi_definition="The percentage of new sales hires who pass the initial training and are deemed qualified to start selling.",
    expected_business_insights="Shows the impact of training on a rep\'s ability to identify and qualify viable sales leads, which can improve sales efficiency.",
    measurement_approach="The percentage of leads that are qualified by sales reps as potential opportunities after training.",
    
    # Formula
    formula="(Number of Qualified Leads / Total Number of Leads) * 100",
    calculation_formula="(Number of Qualified Leads / Total Number of Leads) * 100",
    
    # Analysis
    trend_analysis="""
    * A rising qualification rate may indicate improvements in the effectiveness of sales training programs or better hiring practices.
    * A decreasing rate could signal issues with the quality of training, changes in the market, or challenges in finding suitable candidates.
    """,
    diagnostic_questions="""
    * What specific aspects of the training program are contributing to the increase or decrease in qualification rates?
    * Are there any common characteristics or traits among new hires who do not pass the initial training?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update training materials to ensure they align with the current market and sales strategies.
    * Provide additional support and resources for new hires who may be struggling to meet qualification standards.
    * Implement a mentorship or coaching program to help new hires integrate their training into practical sales skills.
    """,
    visualization_suggestions="""
    * Line charts showing qualification rates over time to identify long-term trends.
    * Comparison charts to analyze qualification rates across different training cohorts or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low qualification rates can lead to a decrease in overall sales performance and revenue.
    * Consistently high qualification rates may indicate that the training standards are not rigorous enough, leading to underprepared sales professionals.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track the progress and performance of new hires during training.
    * Sales performance management software to identify correlations between training outcomes and actual sales results.
    """,
    integration_points="""
    * Integrate qualification rate data with HR systems to analyze the impact of hiring practices on training outcomes.
    * Link qualification rates with sales performance data to understand the long-term effectiveness of the training program.
    """,
    change_impact_analysis="""
    * Improving qualification rates can lead to a more skilled and effective sales team, ultimately driving higher revenue and customer satisfaction.
    * Conversely, a decline in qualification rates may result in decreased sales performance and potential turnover among new hires.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lead", "Lead Qualification", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
