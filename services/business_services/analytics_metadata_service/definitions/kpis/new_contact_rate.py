"""
New Contact Rate KPI

The rate at which the sales team is generating new contacts or leads.
"""

from analytics_models import KPI

NEW_CONTACT_RATE = KPI(
    name="New Contact Rate",
    code="NEW_CONTACT_RATE",
    category="Inside Sales",
    
    # Core Definition
    description="The rate at which the sales team is generating new contacts or leads.",
    kpi_definition="The rate at which the sales team is generating new contacts or leads.",
    expected_business_insights="Assesses the ability of the sales team to expand the customer base and find new prospects.",
    measurement_approach="The percentage of new contacts made out of all sales efforts.",
    
    # Formula
    formula="(Number of New Contacts / Total Sales Efforts) * 100",
    calculation_formula="(Number of New Contacts / Total Sales Efforts) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing new contact rate may indicate successful marketing efforts or a growing market.
    * A decreasing rate could signal a need for revamped lead generation strategies or a shrinking target audience.
    """,
    diagnostic_questions="""
    * Are there specific demographics or industries that are responding more positively to our outreach efforts?
    * How does our new contact rate compare with industry benchmarks or seasonal fluctuations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Utilize targeted advertising and content marketing to reach new audiences.
    * Implement lead scoring to prioritize high-quality leads and focus efforts on the most promising contacts.
    * Regularly update and optimize the sales team\'s outreach scripts and messaging to improve response rates.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of new contact rates over time.
    * Pie charts to visualize the distribution of new contacts by source or demographic.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low new contact rate can lead to stagnation in sales growth and missed opportunities.
    * Relying on a single source for new contacts may pose a risk if that source becomes less effective or unavailable.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage new leads and contacts.
    * Sales engagement platforms to automate and streamline outreach efforts.
    """,
    integration_points="""
    * Integrate new contact rate tracking with marketing automation systems to align sales and marketing efforts.
    * Link new contact data with customer relationship management systems to ensure seamless lead nurturing and follow-up.
    """,
    change_impact_analysis="""
    * An increased new contact rate can lead to higher sales volume and revenue, but may also require additional resources for lead management and follow-up.
    * Conversely, a declining new contact rate can impact overall sales performance and market share, potentially leading to decreased revenue and growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lead", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
