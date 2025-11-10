"""
Sales Role Play Effectiveness Score KPI

A measure of the effectiveness of role-play exercises in improving sales skills and performance.
"""

from analytics_models import KPI

SALES_ROLE_PLAY_EFFECTIVENESS_SCORE = KPI(
    name="Sales Role Play Effectiveness Score",
    code="SALES_ROLE_PLAY_EFFECTIVENESS_SCORE",
    category="Sales Enablement",
    
    # Core Definition
    description="A measure of the effectiveness of role-play exercises in improving sales skills and performance.",
    kpi_definition="A measure of the effectiveness of role-play exercises in improving sales skills and performance.",
    expected_business_insights="Assesses the value of role-play training in improving sales skills and closing techniques.",
    measurement_approach="Measures the impact of role-playing exercises on sales rep performance.",
    
    # Formula
    formula="Average Improvement Score Post-Role Play Exercises",
    calculation_formula="Average Improvement Score Post-Role Play Exercises",
    
    # Analysis
    trend_analysis="""
    * An increasing effectiveness score may indicate that sales skills are improving and positively impacting performance.
    * A decreasing score could signal a need for reevaluation of role-play exercises or a decline in sales performance.
    """,
    diagnostic_questions="""
    * Are there specific sales skills or scenarios where role-play exercises are particularly effective or ineffective?
    * How does the effectiveness score align with actual sales performance and customer feedback?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly update and refresh role-play scenarios to keep them relevant and challenging for sales teams.
    * Provide constructive feedback and coaching to sales representatives based on their performance in role-play exercises.
    * Use technology to simulate real-world sales scenarios and provide a more immersive role-play experience.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of the effectiveness score over time.
    * Comparison charts to visualize the effectiveness scores of different sales teams or individuals.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low effectiveness score may indicate a need for more comprehensive sales training and development.
    * High variability in the effectiveness score could suggest inconsistency in the quality of role-play exercises across different teams or regions.
    """,
    tracking_tools="""
    * Simulation software and virtual reality tools to create more realistic and engaging role-play scenarios.
    * Sales performance management platforms that can track and analyze the impact of role-play exercises on actual sales outcomes.
    """,
    integration_points="""
    * Integrate the effectiveness score with individual performance reviews and coaching sessions to align development efforts with specific needs.
    * Link the score with sales forecasting and pipeline management to identify potential areas for improvement in sales strategies.
    """,
    change_impact_analysis="""
    * Improving the effectiveness score can lead to increased sales productivity and better customer interactions.
    * Conversely, a declining score may indicate a negative impact on sales performance and customer satisfaction.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Enablement Feedback", "Enablement Platform", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
