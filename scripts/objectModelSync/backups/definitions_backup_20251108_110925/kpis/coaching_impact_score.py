"""
Coaching Impact Score KPI

A metric that quantifies the impact of individual coaching sessions on sales performance.
"""

from analytics_models import KPI

COACHING_IMPACT_SCORE = KPI(
    name="Coaching Impact Score",
    code="COACHING_IMPACT_SCORE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="A metric that quantifies the impact of individual coaching sessions on sales performance.",
    kpi_definition="A metric that quantifies the impact of individual coaching sessions on sales performance.",
    expected_business_insights="Assesses the value and influence of coaching sessions on sales results, guiding future coaching strategies.",
    measurement_approach="A qualitative or quantitative measure of the effectiveness of sales coaching on performance improvements.",
    
    # Formula
    formula="Sum of Performance Improvement Measures Post-Coaching / Number of Coaching Sessions",
    calculation_formula="Sum of Performance Improvement Measures Post-Coaching / Number of Coaching Sessions",
    
    # Analysis
    trend_analysis="""
    * An increasing coaching impact score may indicate more effective coaching methods or a higher quality of coaching interactions.
    * A decreasing score could signal a decline in the effectiveness of coaching sessions or a lack of follow-through on coaching recommendations.
    """,
    diagnostic_questions="""
    * Are there specific sales metrics that have shown improvement following coaching sessions?
    * How do sales representatives perceive the value and impact of the coaching they receive?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular feedback loops to assess the impact of coaching on sales performance.
    * Provide additional training for sales managers to enhance their coaching skills and techniques.
    * Encourage sales managers to set clear, measurable goals for coaching sessions and track progress over time.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of coaching impact scores over time.
    * Comparison charts displaying the impact scores of different sales teams or individual sales managers.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low coaching impact score may indicate a need for a reevaluation of coaching strategies and approaches.
    * Highly variable impact scores across different sales teams may point to inconsistencies in coaching practices that need to be addressed.
    """,
    tracking_tools="""
    * Utilize sales performance management software that includes coaching impact score tracking and analysis features.
    * Implement customer relationship management (CRM) systems that can provide insights into the correlation between coaching and sales results.
    """,
    integration_points="""
    * Integrate coaching impact score data with sales performance evaluations to gain a comprehensive view of individual and team effectiveness.
    * Link coaching impact scores with employee development plans to align coaching efforts with career growth opportunities.
    """,
    change_impact_analysis="""
    * Improving coaching impact scores can lead to increased sales productivity and revenue generation.
    * Conversely, a decline in coaching impact may result in missed sales opportunities and decreased motivation among sales teams.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Coaching Session", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
