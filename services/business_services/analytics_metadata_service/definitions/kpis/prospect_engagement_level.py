"""
Prospect Engagement Level KPI

The level of interaction and interest shown by prospects during the sales process.
"""

from analytics_models import KPI

PROSPECT_ENGAGEMENT_LEVEL = KPI(
    name="Prospect Engagement Level",
    code="PROSPECT_ENGAGEMENT_LEVEL",
    category="Inside Sales",
    
    # Core Definition
    description="The level of interaction and interest shown by prospects during the sales process.",
    kpi_definition="The level of interaction and interest shown by prospects during the sales process.",
    expected_business_insights="Identifies how engaged prospects are, which can signal their interest level and likelihood to buy.",
    measurement_approach="Measures the depth of interaction with prospects, such as content engagement and participation in sales activities.",
    
    # Formula
    formula="Engagement Metrics (e.g., page views, downloads) / Number of Prospects",
    calculation_formula="Engagement Metrics (e.g., page views, downloads) / Number of Prospects",
    
    # Analysis
    trend_analysis="""
    * An increasing prospect engagement level may indicate a growing interest in the product or service being offered.
    * A decreasing engagement level could signal a need for adjustments in the sales approach or a lack of alignment between the product and the target audience.
    """,
    diagnostic_questions="""
    * Are there specific stages in the sales process where prospects tend to disengage?
    * What feedback have the sales team received from prospects regarding their level of engagement?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide sales training to improve communication and relationship-building skills.
    * Personalize the sales approach to better resonate with the needs and interests of prospects.
    * Implement a lead nurturing strategy to maintain engagement throughout the sales process.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of prospect engagement level over time.
    * Funnel charts to visualize the drop-off points in the sales process where engagement decreases.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low prospect engagement levels can lead to longer sales cycles and decreased conversion rates.
    * Consistently low engagement may indicate a need for reevaluation of the target audience or product positioning.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze prospect interactions.
    * Sales engagement platforms to automate and optimize outreach efforts.
    """,
    integration_points="""
    * Integrate prospect engagement data with marketing analytics to understand the effectiveness of lead generation efforts.
    * Link engagement levels with customer feedback systems to gather insights on the sales process from the prospect\'s perspective.
    """,
    change_impact_analysis="""
    * Increasing prospect engagement can lead to higher conversion rates and improved sales performance.
    * However, overly aggressive sales tactics to boost engagement may negatively impact brand reputation and long-term customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Lead", "Prospect", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
