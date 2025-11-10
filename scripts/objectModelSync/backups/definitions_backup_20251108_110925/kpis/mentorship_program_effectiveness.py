"""
Mentorship Program Effectiveness KPI

A measure of the impact of mentorship programs on new sales reps' performance and development.
"""

from analytics_models import KPI

MENTORSHIP_PROGRAM_EFFECTIVENESS = KPI(
    name="Mentorship Program Effectiveness",
    code="MENTORSHIP_PROGRAM_EFFECTIVENESS",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="A measure of the impact of mentorship programs on new sales reps\' performance and development.",
    kpi_definition="A measure of the impact of mentorship programs on new sales reps\' performance and development.",
    expected_business_insights="Evaluates the impact of mentoring on sales performance, which can inform program design and mentor selection.",
    measurement_approach="The degree of success of a mentorship program as measured by mentee performance improvements.",
    
    # Formula
    formula="Performance Metrics Pre and Post-Mentorship / Number of Mentees",
    calculation_formula="Performance Metrics Pre and Post-Mentorship / Number of Mentees",
    
    # Analysis
    trend_analysis="""
    * An increasing mentorship program effectiveness may indicate better onboarding processes and more impactful mentorship relationships.
    * A decreasing effectiveness could signal a need for reevaluation of the program structure or mentorship training.
    """,
    diagnostic_questions="""
    * Are there specific areas where new sales reps consistently struggle despite mentorship?
    * How does the effectiveness of our mentorship program compare to industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional training for mentors to improve their coaching and leadership skills.
    * Regularly gather feedback from new sales reps to identify areas for improvement in the mentorship program.
    * Pair new sales reps with mentors who have a track record of successful coaching and development.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of new sales reps\' performance over time in relation to the mentorship program effectiveness.
    * Comparison bar charts displaying the performance of new sales reps who have been through the mentorship program versus those who haven\'t.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low mentorship program effectiveness may result in higher turnover among new sales reps.
    * Ineffective mentorship can lead to missed sales opportunities and slower ramp-up times for new reps.
    """,
    tracking_tools="""
    * CRM systems with performance tracking capabilities to monitor the impact of mentorship on new sales reps\' development.
    * Learning management platforms to provide structured training and resources for mentors and new sales reps.
    """,
    integration_points="""
    * Integrate mentorship program effectiveness data with performance reviews and sales metrics to understand the correlation between mentorship and results.
    * Link mentorship program data with HR systems to track the long-term success and retention of new sales reps.
    """,
    change_impact_analysis="""
    * Improving mentorship program effectiveness can lead to higher sales performance and increased job satisfaction among new sales reps.
    * Conversely, a decline in effectiveness may result in a negative impact on overall sales team morale and productivity.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer Advocacy Program", "Customer Success Manager", "Loyalty Program", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
