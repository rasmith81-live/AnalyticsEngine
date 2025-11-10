"""
Training Participation Rate KPI

The percentage of eligible sales reps who actively participate in training programs.
"""

from analytics_models import KPI

TRAINING_PARTICIPATION_RATE = KPI(
    name="Training Participation Rate",
    code="TRAINING_PARTICIPATION_RATE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The percentage of eligible sales reps who actively participate in training programs.",
    kpi_definition="The percentage of eligible sales reps who actively participate in training programs.",
    expected_business_insights="Offers insights into the level of engagement and commitment to professional development within the organization.",
    measurement_approach="Includes metrics such as the total number of employees eligible for training and the number that actually completed the training sessions.",
    
    # Formula
    formula="(Number of Employees Who Completed Training / Total Number of Employees Eligible for Training) * 100",
    calculation_formula="(Number of Employees Who Completed Training / Total Number of Employees Eligible for Training) * 100",
    
    # Analysis
    trend_analysis="""
    * Training participation rate may show an initial increase as new training programs are introduced, followed by a gradual decline as the novelty wears off.
    * An upward trend could indicate a positive shift in the company culture towards continuous learning and development, while a downward trend may signal disengagement or lack of perceived value in the training programs.
    """,
    diagnostic_questions="""
    * What are the common reasons for sales reps to opt out of training programs?
    * How does the participation rate vary across different sales teams or regions, and what factors contribute to these differences?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Offer incentives or rewards for active participation in training programs to boost engagement.
    * Customize training content to be more relevant and tailored to the specific needs and challenges faced by the sales reps.
    * Implement a mentorship or coaching program to provide ongoing support and reinforcement of the training content.
    """,
    visualization_suggestions="""
    * Line charts showing the participation rate over time, with different lines representing different sales teams or regions for comparison.
    * Pie charts to illustrate the distribution of participation across different training programs or modules.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low participation rate may indicate a disconnect between the training content and the actual needs of the sales reps, leading to wasted resources and ineffective training.
    * High participation rates without corresponding improvements in sales performance may suggest that the training content is not impactful or that the application of the learning is lacking.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and analyze participation rates, completion rates, and feedback from sales reps regarding the training programs.
    * Survey and feedback tools to gather insights from sales reps about their training preferences and needs.
    """,
    integration_points="""
    * Integrate training participation data with sales performance metrics to identify correlations between training engagement and sales results.
    * Link participation rates with individual performance evaluations to assess the impact of training on individual sales rep effectiveness.
    """,
    change_impact_analysis="""
    * Improving the training participation rate can lead to a more knowledgeable and skilled sales force, potentially resulting in increased sales and customer satisfaction.
    * However, a high participation rate without tangible improvements in sales performance may indicate a need to reassess the quality and relevance of the training content.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
