"""
Certification Achievement Rate KPI

The proportion of sales reps who achieve certification if applicable, through the training program.
"""

from analytics_models import KPI

CERTIFICATION_ACHIEVEMENT_RATE = KPI(
    name="Certification Achievement Rate",
    code="CERTIFICATION_ACHIEVEMENT_RATE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The proportion of sales reps who achieve certification if applicable, through the training program.",
    kpi_definition="The proportion of sales reps who achieve certification if applicable, through the training program.",
    expected_business_insights="Reflects the effectiveness of training programs in preparing sales reps for certification and the commitment of reps to professional development.",
    measurement_approach="The percentage of sales reps who attain certification after completing a designated training program.",
    
    # Formula
    formula="(Number of Sales Reps Achieving Certification / Number of Sales Reps Enrolled in the Certification Program) * 100",
    calculation_formula="(Number of Sales Reps Achieving Certification / Number of Sales Reps Enrolled in the Certification Program) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing certification achievement rate may indicate the effectiveness of the training program in preparing sales reps.
    * A decreasing rate could signal a need for program adjustments or changes in the sales team composition.
    """,
    diagnostic_questions="""
    * Are there specific areas of the training program where sales reps struggle to achieve certification?
    * How does the certification achievement rate compare with industry benchmarks or with different cohorts of sales reps?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional support and resources for sales reps who are struggling to achieve certification.
    * Regularly review and update the training program to ensure it aligns with the evolving needs and challenges of the sales team.
    * Implement mentorship or coaching programs to help sales reps prepare for certification.
    """,
    visualization_suggestions="""
    * Line charts showing the certification achievement rate over time.
    * Comparison bar charts to visualize the differences in certification achievement among different groups of sales reps.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low certification achievement rate may indicate a need for a more comprehensive review of the training program.
    * High variability in certification achievement rates among different sales reps may point to inconsistencies in the training or coaching process.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and manage sales reps\' progress in the training program.
    * Coaching and feedback tools to provide personalized support for sales reps aiming for certification.
    """,
    integration_points="""
    * Integrate certification achievement data with performance management systems to identify correlations between certification and sales success.
    * Link certification achievement with individual development plans to ensure ongoing improvement and career growth for sales reps.
    """,
    change_impact_analysis="""
    * Improving the certification achievement rate can lead to a more skilled and knowledgeable sales force, potentially increasing overall sales performance.
    * Conversely, a declining certification achievement rate may lead to decreased confidence and motivation among the sales team.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Certification", "Customer Advocacy Program", "Loyalty Program", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
