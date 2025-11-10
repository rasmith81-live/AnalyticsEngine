"""
Sales Team Attrition Rate KPI

The rate at which sales personnel leave the sales team over a given period.
"""

from analytics_models import KPI

SALES_TEAM_ATTRITION_RATE = KPI(
    name="Sales Team Attrition Rate",
    code="SALES_TEAM_ATTRITION_RATE",
    category="Inside Sales",
    
    # Core Definition
    description="The rate at which sales personnel leave the sales team over a given period.",
    kpi_definition="The rate at which sales personnel leave the sales team over a given period.",
    expected_business_insights="Serves as an indicator of the health of the sales environment and can signal issues in management or job satisfaction.",
    measurement_approach="The rate at which sales staff leave the company.",
    
    # Formula
    formula="(Number of Sales Staff Departures / Average Number of Sales Staff) * 100",
    calculation_formula="(Number of Sales Staff Departures / Average Number of Sales Staff) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales team attrition rate may indicate issues with employee satisfaction, training, or management.
    * A decreasing rate could signal successful retention strategies, improved hiring practices, or a shift in market conditions.
    """,
    diagnostic_questions="""
    * What are the primary reasons for sales team members leaving the organization?
    * Are there patterns or commonalities among the departing sales personnel?
    * How does our sales team attrition rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in ongoing training and development programs to enhance skills and career growth opportunities for sales team members.
    * Regularly review and update compensation and benefits packages to remain competitive and attractive to top sales talent.
    * Implement mentorship or coaching programs to provide support and guidance for new and existing sales team members.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales team attrition rate over time.
    * Bar graphs comparing attrition rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High sales team attrition can lead to a loss of institutional knowledge and disrupt team dynamics.
    * Consistently high attrition rates may indicate systemic issues within the organization that could affect overall performance and morale.
    """,
    tracking_tools="""
    * Employee engagement and feedback platforms to gather insights and address concerns proactively.
    * HR management systems to track turnover, identify trends, and implement targeted retention strategies.
    """,
    integration_points="""
    * Integrate sales team attrition data with performance reviews and feedback to identify potential areas for improvement.
    * Link attrition rates with sales productivity metrics to understand the impact of turnover on overall sales performance.
    """,
    change_impact_analysis="""
    * High turnover can disrupt team dynamics and affect overall sales productivity and customer relationships.
    * Reducing attrition can lead to a more stable and motivated sales team, potentially improving customer satisfaction and revenue generation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
