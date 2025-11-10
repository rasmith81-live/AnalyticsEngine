"""
Customer Success Team Attrition Rate KPI

The rate at which customer success team members leave the company, either voluntarily or involuntarily.
"""

from analytics_models import KPI

CUSTOMER_SUCCESS_TEAM_ATTRITION_RATE = KPI(
    name="Customer Success Team Attrition Rate",
    code="CUSTOMER_SUCCESS_TEAM_ATTRITION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The rate at which customer success team members leave the company, either voluntarily or involuntarily.",
    kpi_definition="The rate at which customer success team members leave the company, either voluntarily or involuntarily.",
    expected_business_insights="Highlights the stability of the customer success team and potential impacts on service continuity and customer relationships.",
    measurement_approach="Measures the rate at which customer success team members leave the company within a given period.",
    
    # Formula
    formula="(Number of Customer Success Team Members Who Left / Total Number of Customer Success Team Members) * 100",
    calculation_formula="(Number of Customer Success Team Members Who Left / Total Number of Customer Success Team Members) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing attrition rate may indicate issues with team morale, leadership, or company culture.
    * A decreasing rate could signal successful retention strategies, improved work environment, or better career development opportunities.
    """,
    diagnostic_questions="""
    * Are there common reasons cited by departing team members, and are these issues being addressed?
    * How does our attrition rate compare with industry benchmarks or similar companies in our sector?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Conduct exit interviews to understand the reasons behind voluntary departures and take action based on feedback.
    * Invest in professional development and career growth opportunities to increase employee satisfaction and retention.
    * Regularly assess and improve the work environment and company culture to reduce turnover.
    """,
    visualization_suggestions="""
    * Line charts showing attrition rates over time to identify trends and patterns.
    * Pie charts to visualize the reasons for attrition and their relative impact on the overall rate.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High attrition rates can disrupt team dynamics, reduce productivity, and increase recruitment and training costs.
    * Consistently high turnover may indicate systemic issues that could affect overall company performance and reputation.
    """,
    tracking_tools="""
    * Human resources management software to track and analyze turnover data and identify potential areas for improvement.
    * Employee engagement platforms to gather feedback and measure satisfaction levels within the customer success team.
    """,
    integration_points="""
    * Integrate attrition rate data with performance evaluations and feedback systems to identify potential correlations and areas for improvement.
    * Link turnover metrics with customer satisfaction scores to understand the impact of team stability on customer success.
    """,
    change_impact_analysis="""
    * Reducing attrition can lead to a more stable and productive team, potentially improving customer satisfaction and long-term business performance.
    * However, efforts to reduce attrition may require investments in training, development, and employee support programs.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Sales Team"]
    }
)
