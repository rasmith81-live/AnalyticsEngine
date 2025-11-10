"""
Sales Enablement Content Refresh Rate KPI

The frequency at which sales enablement content is reviewed and updated to maintain relevance.
"""

from analytics_models import KPI

SALES_ENABLEMENT_CONTENT_REFRESH_RATE = KPI(
    name="Sales Enablement Content Refresh Rate",
    code="SALES_ENABLEMENT_CONTENT_REFRESH_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The frequency at which sales enablement content is reviewed and updated to maintain relevance.",
    kpi_definition="The frequency at which sales enablement content is reviewed and updated to maintain relevance.",
    expected_business_insights="Ensures that sales enablement materials remain current and effective, adapting to market changes and customer feedback.",
    measurement_approach="Tracks how often sales enablement content is updated or replaced.",
    
    # Formula
    formula="(Number of Content Updates / Total Number of Content Pieces) * 100",
    calculation_formula="(Number of Content Updates / Total Number of Content Pieces) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing content refresh rate may indicate a proactive approach to keeping sales materials up to date and relevant.
    * A decreasing rate could signal a lack of attention to the importance of maintaining current sales enablement content.
    """,
    diagnostic_questions="""
    * Are there specific types of content that are frequently outdated or irrelevant?
    * How does our content refresh rate compare with industry standards or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a regular schedule for content review and updates, ensuring all materials are reviewed at least quarterly.
    * Utilize feedback from the sales team to identify areas where content updates are most needed.
    * Invest in sales enablement tools that facilitate easy content management and updates.
    """,
    visualization_suggestions="""
    * Line charts showing the frequency of content updates over time.
    * Stacked bar graphs comparing the refresh rates of different types of sales enablement content.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Outdated content can lead to misinformation being presented to potential customers, damaging the sales process.
    * A low refresh rate may result in sales teams relying on obsolete materials, impacting their effectiveness.
    """,
    tracking_tools="""
    * Content management systems like Salesforce or HubSpot for organizing and updating sales enablement materials.
    * Analytics tools to track the usage and effectiveness of sales content, identifying areas in need of updates.
    """,
    integration_points="""
    * Integrate content refresh rate tracking with sales performance metrics to understand the impact of updated materials on sales outcomes.
    * Link with customer relationship management (CRM) systems to ensure that sales teams have access to the most current materials when engaging with prospects and clients.
    """,
    change_impact_analysis="""
    * Improving the content refresh rate can lead to more effective sales conversations and higher conversion rates.
    * However, dedicating resources to content updates may impact other marketing or sales initiatives, requiring a balance of priorities.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
