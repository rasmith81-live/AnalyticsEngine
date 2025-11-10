"""
Sales Team Satisfaction KPI

A metric assessing the job satisfaction levels of sales personnel, as higher satisfaction is often correlated with better performance.
"""

from analytics_models import KPI

SALES_TEAM_SATISFACTION = KPI(
    name="Sales Team Satisfaction",
    code="SALES_TEAM_SATISFACTION",
    category="Sales Strategy",
    
    # Core Definition
    description="A metric assessing the job satisfaction levels of sales personnel, as higher satisfaction is often correlated with better performance.",
    kpi_definition="A metric assessing the job satisfaction levels of sales personnel, as higher satisfaction is often correlated with better performance.",
    expected_business_insights="Assesses the overall contentment within the sales team, which can influence performance and retention.",
    measurement_approach="Includes metrics from surveys, turnover rates, and performance levels to gauge sales team morale.",
    
    # Formula
    formula="Qualitative and quantitative analysis, no standard formula",
    calculation_formula="Qualitative and quantitative analysis, no standard formula",
    
    # Analysis
    trend_analysis="""
    * Increasing sales team satisfaction may indicate better morale and motivation, leading to improved performance and retention.
    * Decreasing satisfaction levels could signal issues with leadership, compensation, or work environment that may impact sales outcomes.
    """,
    diagnostic_questions="""
    * What specific factors contribute to the satisfaction or dissatisfaction of the sales team?
    * How does the sales team satisfaction compare to industry benchmarks or historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly solicit feedback from the sales team and take action on their concerns to improve satisfaction.
    * Provide training and development opportunities to enhance skills and confidence within the sales team.
    * Implement recognition and reward programs to acknowledge and appreciate the efforts of the sales team.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales team satisfaction over time.
    * Comparison bar charts displaying satisfaction levels across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low sales team satisfaction can lead to increased turnover and recruitment costs.
    * Unaddressed dissatisfaction may result in decreased productivity and ultimately, lower sales performance.
    """,
    tracking_tools="""
    * Employee engagement platforms like Officevibe or TINYpulse for gathering and analyzing feedback from the sales team.
    * Performance management software to track individual and team satisfaction levels and identify areas for improvement.
    """,
    integration_points="""
    * Integrate sales team satisfaction data with performance management systems to understand the impact on sales results.
    * Link satisfaction metrics with HR systems to align improvement initiatives with broader organizational goals.
    """,
    change_impact_analysis="""
    * Improving sales team satisfaction can lead to higher customer satisfaction and loyalty, positively impacting overall business performance.
    * However, a focus solely on satisfaction without considering sales outcomes may lead to decreased efficiency and effectiveness.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Competitive Analysis", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
