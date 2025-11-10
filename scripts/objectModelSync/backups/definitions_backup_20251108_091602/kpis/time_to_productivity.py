"""
Time to Productivity KPI

The time it takes for a new sales representative to reach full productivity.
"""

from analytics_models import KPI

TIME_TO_PRODUCTIVITY = KPI(
    name="Time to Productivity",
    code="TIME_TO_PRODUCTIVITY",
    category="Outside Sales",
    
    # Core Definition
    description="The time it takes for a new sales representative to reach full productivity.",
    kpi_definition="The time it takes for a new sales representative to reach full productivity.",
    expected_business_insights="Assists in evaluating the effectiveness of sales training programs and the speed at which new hires contribute to company goals.",
    measurement_approach="Tracks the time it takes for a new sales representative to reach predefined performance benchmarks.",
    
    # Formula
    formula="(Time from Hiring Date to Reaching Performance Benchmark)",
    calculation_formula="(Time from Hiring Date to Reaching Performance Benchmark)",
    
    # Analysis
    trend_analysis="""
    * Time to productivity may show an initial dip as new sales reps undergo training and onboarding.
    * Over time, the trend should show a steady increase as reps gain experience and build their client base.
    """,
    diagnostic_questions="""
    * Are there specific onboarding processes or training programs that have proven to accelerate time to productivity?
    * How does the time to productivity for new reps compare to industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement mentorship or shadowing programs to help new reps learn from experienced colleagues.
    * Provide ongoing training and support to ensure reps have the knowledge and tools they need to succeed.
    * Set clear and achievable goals for new reps to track their progress and motivate them to reach full productivity.
    """,
    visualization_suggestions="""
    * Line charts showing the average time to productivity for new reps over time.
    * Comparative bar charts displaying the time to productivity for different cohorts of new reps.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Extended time to productivity can lead to missed sales opportunities and lower revenue.
    * Rapid time to productivity without proper training can result in lower quality interactions and potential customer dissatisfaction.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track new rep activities and progress.
    * Sales training platforms to provide interactive and ongoing learning opportunities for new reps.
    """,
    integration_points="""
    * Integrate time to productivity data with sales performance metrics to identify correlations and areas for improvement.
    * Link with HR systems to align onboarding and training processes with the specific needs of the sales team.
    """,
    change_impact_analysis="""
    * Improving time to productivity can lead to increased sales and revenue, but may also require additional investment in training and support.
    * Conversely, a prolonged time to productivity can strain resources and impact overall team morale and performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES", "SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Benchmark", "Deal", "Lead", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
