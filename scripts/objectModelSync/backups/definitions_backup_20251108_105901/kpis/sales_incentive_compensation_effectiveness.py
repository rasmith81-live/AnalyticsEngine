"""
Sales Incentive Compensation Effectiveness KPI

The effectiveness of incentive programs in motivating the sales team, assessed by improvements in sales performance.
"""

from analytics_models import KPI

SALES_INCENTIVE_COMPENSATION_EFFECTIVENESS = KPI(
    name="Sales Incentive Compensation Effectiveness",
    code="SALES_INCENTIVE_COMPENSATION_EFFECTIVENESS",
    category="Sales Performance",
    
    # Core Definition
    description="The effectiveness of incentive programs in motivating the sales team, assessed by improvements in sales performance.",
    kpi_definition="The effectiveness of incentive programs in motivating the sales team, assessed by improvements in sales performance.",
    expected_business_insights="Evaluates the return on investment for sales incentives and their impact on performance.",
    measurement_approach="Relates incentive compensation paid to the sales generated.",
    
    # Formula
    formula="Total Sales Generated / Total Incentive Compensation Paid",
    calculation_formula="Total Sales Generated / Total Incentive Compensation Paid",
    
    # Analysis
    trend_analysis="""
    * Increasing sales incentive compensation effectiveness may indicate a more motivated and productive sales team.
    * Decreasing effectiveness could signal a need for reevaluation of the incentive programs or underlying issues within the sales team.
    """,
    diagnostic_questions="""
    * Are there specific sales metrics that have shown improvement or decline in correlation with changes in the incentive programs?
    * How do sales team members perceive the effectiveness of the current incentive structure, and what suggestions do they have for improvement?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and adjust incentive programs based on feedback and performance data.
    * Consider non-monetary incentives such as recognition, career development opportunities, or flexible work arrangements.
    * Align incentive programs with individual sales goals and preferences to maximize motivation.
    """,
    visualization_suggestions="""
    * Line charts showing the correlation between changes in incentive programs and sales performance over time.
    * Pie charts comparing the distribution of sales performance improvements among different incentive categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low incentive effectiveness may lead to decreased morale and engagement within the sales team.
    * Over-reliance on monetary incentives could create a short-term focus on sales targets at the expense of long-term customer relationships.
    """,
    tracking_tools="""
    * CRM systems with built-in incentive tracking and performance analytics.
    * Sales performance management software that allows for easy experimentation with different incentive structures.
    """,
    integration_points="""
    * Integrate incentive effectiveness data with sales coaching and training programs to identify areas for improvement.
    * Link incentive data with customer feedback and satisfaction scores to understand the impact on overall customer experience.
    """,
    change_impact_analysis="""
    * Improving incentive effectiveness can lead to higher sales performance, but may also increase overall compensation costs.
    * Conversely, a decrease in effectiveness could result in lower sales and potentially impact overall revenue and profitability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Incentive", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
