"""
Partner Incentive Utilization Rate KPI

The rate at which channel partners make use of available incentives, which can indicate the effectiveness of incentive programs.
"""

from analytics_models import KPI

PARTNER_INCENTIVE_UTILIZATION_RATE = KPI(
    name="Partner Incentive Utilization Rate",
    code="PARTNER_INCENTIVE_UTILIZATION_RATE",
    category="Channel Sales",
    
    # Core Definition
    description="The rate at which channel partners make use of available incentives, which can indicate the effectiveness of incentive programs.",
    kpi_definition="The rate at which channel partners make use of available incentives, which can indicate the effectiveness of incentive programs.",
    expected_business_insights="Reveals the attractiveness and effectiveness of incentive programs in driving partner behavior.",
    measurement_approach="Measures the percentage of available incentives that are claimed and used by partners.",
    
    # Formula
    formula="(Value of Incentives Claimed by Partners / Total Value of Incentives Offered) * 100",
    calculation_formula="(Value of Incentives Claimed by Partners / Total Value of Incentives Offered) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing partner incentive utilization rate may indicate the effectiveness of incentive programs or improved partner engagement.
    * Decreasing utilization could signal a need to reevaluate the incentive structure or communication of available incentives to partners.
    """,
    diagnostic_questions="""
    * Are there specific types of incentives that are consistently underutilized?
    * How does our partner incentive utilization rate compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly communicate available incentives to partners and provide clear guidelines on how to utilize them.
    * Collect feedback from partners on the effectiveness of current incentives and make adjustments accordingly.
    * Offer training and support to help partners take full advantage of available incentives.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of partner incentive utilization rate over time.
    * Pie charts to compare the utilization rates of different types of incentives.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low partner incentive utilization rates may indicate a lack of partner engagement or dissatisfaction with the current incentive offerings.
    * High utilization rates for certain incentives may suggest an over-reliance on those incentives or a lack of diversity in the incentive programs.
    """,
    tracking_tools="""
    * Partner relationship management (PRM) software to track and analyze partner engagement and incentive utilization.
    * Data analytics tools to identify patterns and correlations between incentive utilization and partner performance.
    """,
    integration_points="""
    * Integrate partner incentive utilization data with sales performance metrics to understand the impact of incentives on overall sales results.
    * Link incentive utilization with partner feedback and satisfaction data to gain a comprehensive view of partner engagement.
    """,
    change_impact_analysis="""
    * Increasing partner incentive utilization can lead to higher sales and improved partner loyalty, but may also increase incentive costs.
    * Conversely, low utilization rates may result in missed sales opportunities and strained partner relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
