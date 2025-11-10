"""
Mobile Learning Utilization Rate KPI

The percentage of training completed using mobile devices, indicating flexibility and accessibility.
"""

from analytics_models import KPI

MOBILE_LEARNING_UTILIZATION_RATE = KPI(
    name="Mobile Learning Utilization Rate",
    code="MOBILE_LEARNING_UTILIZATION_RATE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The percentage of training completed using mobile devices, indicating flexibility and accessibility.",
    kpi_definition="The percentage of training completed using mobile devices, indicating flexibility and accessibility.",
    expected_business_insights="Shows the adoption rate and perceived usefulness of mobile learning tools, influencing future training resource allocation.",
    measurement_approach="The percentage of mobile learning resources accessed by sales reps out of the total available.",
    
    # Formula
    formula="(Number of Mobile Learning Resources Accessed / Total Number of Mobile Learning Resources Available) * 100",
    calculation_formula="(Number of Mobile Learning Resources Accessed / Total Number of Mobile Learning Resources Available) * 100",
    
    # Analysis
    trend_analysis="""
    * Mobile learning utilization rate tends to increase over time as more employees adopt mobile training methods.
    * A decreasing trend may indicate issues with the accessibility or quality of mobile training platforms.
    """,
    diagnostic_questions="""
    * Are there specific barriers or challenges that prevent employees from utilizing mobile learning for training?
    * How does the mobile learning utilization rate compare with traditional training completion rates?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in user-friendly mobile learning platforms to encourage higher utilization rates.
    * Provide incentives or rewards for employees who complete training using mobile devices.
    * Offer technical support and training for employees who may be unfamiliar with mobile learning methods.
    """,
    visualization_suggestions="""
    * Line charts showing the increase or decrease in mobile learning utilization rate over time.
    * Comparison bar charts between mobile and traditional training completion rates.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low mobile learning utilization rates may indicate a disconnect between the training content and the mobile platform.
    * Failure to address low utilization rates can lead to a lack of training completion and knowledge gaps among the sales team.
    """,
    tracking_tools="""
    * Learning management systems with mobile compatibility for tracking and analyzing mobile learning utilization.
    * Mobile app analytics tools to understand user behavior and engagement with training content.
    """,
    integration_points="""
    * Integrate mobile learning utilization data with performance management systems to assess the impact of training on sales results.
    * Link mobile learning utilization with employee development plans to track individual progress and identify areas for improvement.
    """,
    change_impact_analysis="""
    * Increasing mobile learning utilization can lead to a more knowledgeable and adaptable sales team, potentially improving sales performance.
    * However, a lack of improvement in mobile learning utilization may result in stagnant or declining sales effectiveness.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
