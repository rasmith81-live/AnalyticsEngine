"""
Average Time to Onboard New Sales Reps KPI

The average time it takes to get new sales reps up to speed and productive. A shorter time indicates better training and coaching.
"""

from analytics_models import KPI

AVERAGE_TIME_TO_ONBOARD_NEW_SALES_REPS = KPI(
    name="Average Time to Onboard New Sales Reps",
    code="AVERAGE_TIME_TO_ONBOARD_NEW_SALES_REPS",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The average time it takes to get new sales reps up to speed and productive. A shorter time indicates better training and coaching.",
    kpi_definition="The average time it takes to get new sales reps up to speed and productive. A shorter time indicates better training and coaching.",
    expected_business_insights="Reveals the efficiency and effectiveness of the sales onboarding process and its impact on time-to-productivity.",
    measurement_approach="The duration in days or weeks it takes for a new sales representative to go through the onboarding process until they are fully operational.",
    
    # Formula
    formula="Sum of Onboarding Duration for all New Sales Reps / Number of New Sales Reps",
    calculation_formula="Sum of Onboarding Duration for all New Sales Reps / Number of New Sales Reps",
    
    # Analysis
    trend_analysis="""
    * Decreasing average time to onboard new sales reps may indicate more effective training and coaching programs.
    * An increasing time to productivity could signal issues with training content, onboarding processes, or coaching effectiveness.
    """,
    diagnostic_questions="""
    * Are there specific areas or topics where new sales reps consistently struggle during onboarding?
    * How does the average onboarding time compare with industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement mentorship programs to provide new reps with ongoing support and guidance.
    * Utilize interactive and scenario-based training methods to improve retention and application of knowledge.
    * Regularly review and update training materials to ensure relevance and effectiveness.
    """,
    visualization_suggestions="""
    * Line charts showing the average onboarding time over different quarters or years.
    * Comparison bar graphs displaying the onboarding time for different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Extended onboarding times can lead to decreased sales productivity and missed revenue targets.
    * Prolonged onboarding may indicate a need for reevaluation of training and coaching strategies to prevent turnover or dissatisfaction among new reps.
    """,
    tracking_tools="""
    * Utilize learning management systems (LMS) to track and analyze the progress of new reps during onboarding.
    * Implement sales enablement platforms to provide access to training materials, resources, and best practices for new reps.
    """,
    integration_points="""
    * Integrate onboarding time data with performance management systems to assess the impact of training on sales results.
    * Link onboarding metrics with HR systems to identify correlations between onboarding success and employee retention.
    """,
    change_impact_analysis="""
    * Improving the average onboarding time can lead to increased sales efficiency and effectiveness.
    * However, rapid onboarding may also lead to gaps in knowledge and skill development, impacting long-term sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Coaching Session", "Customer Onboarding", "Deal", "Lead", "Opportunity", "Partner Training", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
