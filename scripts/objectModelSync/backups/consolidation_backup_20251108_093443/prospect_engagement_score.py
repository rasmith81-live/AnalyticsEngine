"""
Prospect Engagement Score KPI

A measure of how involved and interested prospects are during sales interactions.
"""

from analytics_models import KPI

PROSPECT_ENGAGEMENT_SCORE = KPI(
    name="Prospect Engagement Score",
    code="PROSPECT_ENGAGEMENT_SCORE",
    category="Sales Development",
    
    # Core Definition
    description="A measure of how involved and interested prospects are during sales interactions.",
    kpi_definition="A measure of how involved and interested prospects are during sales interactions.",
    expected_business_insights="Helps prioritize prospects based on engagement level and likelihood to buy.",
    measurement_approach="Assigns a numerical value to prospects based on engagement activities such as website visits, email opens, etc.",
    
    # Formula
    formula="Sum of Engagement Activities Scores for Each Prospect",
    calculation_formula="Sum of Engagement Activities Scores for Each Prospect",
    
    # Analysis
    trend_analysis="""
    * An increasing prospect engagement score may indicate a growing interest in the products or services being offered.
    * A decreasing score could signal a lack of interest or ineffective sales interactions.
    """,
    diagnostic_questions="""
    * Are there specific sales tactics or communication channels that result in higher prospect engagement?
    * How does the prospect engagement score correlate with the conversion rate from prospects to customers?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Train sales representatives on effective communication and relationship-building techniques.
    * Utilize customer relationship management (CRM) software to track and analyze prospect interactions.
    * Personalize sales pitches and interactions based on prospect behavior and preferences.
    """,
    visualization_suggestions="""
    * Line charts showing the prospect engagement score over time.
    * Scatter plots to visualize the relationship between prospect engagement and conversion rates.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low prospect engagement score may lead to missed sales opportunities and revenue loss.
    * Overly aggressive sales tactics to boost engagement could result in a negative brand image and potential customer alienation.
    """,
    tracking_tools="""
    * CRM systems with engagement tracking capabilities, such as Salesforce or HubSpot.
    * Social listening tools to monitor prospect interactions and sentiment on social media platforms.
    """,
    integration_points="""
    * Integrate prospect engagement data with marketing automation platforms to align sales and marketing efforts.
    * Link prospect engagement scores with customer feedback systems to gain a holistic view of customer satisfaction.
    """,
    change_impact_analysis="""
    * Improving prospect engagement can lead to higher conversion rates and increased sales revenue.
    * However, overly aggressive tactics may negatively impact brand reputation and long-term customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT", "SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Lead", "Prospect", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
