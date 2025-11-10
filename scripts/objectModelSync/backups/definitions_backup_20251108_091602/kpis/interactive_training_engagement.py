"""
Interactive Training Engagement KPI

The level of interaction and participation of sales reps in training sessions that require active engagement.
"""

from analytics_models import KPI

INTERACTIVE_TRAINING_ENGAGEMENT = KPI(
    name="Interactive Training Engagement",
    code="INTERACTIVE_TRAINING_ENGAGEMENT",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The level of interaction and participation of sales reps in training sessions that require active engagement.",
    kpi_definition="The level of interaction and participation of sales reps in training sessions that require active engagement.",
    expected_business_insights="Highlights the engagement and interactivity of training sessions, which can correlate with training effectiveness.",
    measurement_approach="The level of sales rep participation and involvement in interactive training activities.",
    
    # Formula
    formula="Number of Interactive Activities Completed / Total Number of Interactive Activities Offered",
    calculation_formula="Number of Interactive Activities Completed / Total Number of Interactive Activities Offered",
    
    # Analysis
    trend_analysis="""
    * Increasing interactive training engagement may indicate a more motivated and engaged sales team.
    * Decreasing engagement could signal a need for more dynamic and interactive training methods.
    """,
    diagnostic_questions="""
    * Are there specific training topics or sessions that consistently receive higher engagement?
    * How does the level of engagement in training sessions correlate with sales performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement gamification elements in training to increase engagement and participation.
    * Encourage open discussions and role-playing exercises to make training sessions more interactive.
    * Use real-life scenarios and case studies to make training content more relatable and engaging.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of engagement levels over time.
    * Comparison bar charts to visualize engagement levels across different training topics or sessions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low engagement in training may lead to a lack of knowledge retention and application in real sales scenarios.
    * Consistently low engagement could indicate a disconnect between the training content and the needs of the sales team.
    """,
    tracking_tools="""
    * Utilize learning management systems (LMS) to track and analyze engagement metrics in training sessions.
    * Use survey and feedback tools to gather insights from sales reps about the effectiveness of training sessions.
    """,
    integration_points="""
    * Integrate engagement data with sales performance metrics to understand the impact of training on actual results.
    * Link engagement data with individual performance evaluations to identify correlations between engagement and sales success.
    """,
    change_impact_analysis="""
    * Increasing engagement in training may lead to improved sales performance and customer satisfaction.
    * However, changes in training methods to boost engagement may require additional resources and time investment.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Lead", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"]
    }
)
