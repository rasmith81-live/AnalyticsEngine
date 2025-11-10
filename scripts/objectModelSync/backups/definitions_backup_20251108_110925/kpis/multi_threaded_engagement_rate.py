"""
Multi-threaded Engagement Rate KPI

The percentage of deals where multiple contacts or decision-makers at the prospect's organization are engaged in the sales process.
"""

from analytics_models import KPI

MULTI_THREADED_ENGAGEMENT_RATE = KPI(
    name="Multi-threaded Engagement Rate",
    code="MULTI_THREADED_ENGAGEMENT_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of deals where multiple contacts or decision-makers at the prospect\'s organization are engaged in the sales process.",
    kpi_definition="The percentage of deals where multiple contacts or decision-makers at the prospect\'s organization are engaged in the sales process.",
    expected_business_insights="Illustrates the depth of engagement and relationship building with client organizations, potentially leading to more secure deals.",
    measurement_approach="Measures the percentage of deals involving multiple contacts or stakeholders within a client organization.",
    
    # Formula
    formula="(Number of Multi-threaded Deals / Total Number of Deals) * 100",
    calculation_formula="(Number of Multi-threaded Deals / Total Number of Deals) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing multi-threaded engagement rate may indicate a more collaborative and inclusive sales approach, leading to higher deal success rates.
    * A decreasing rate could signal a lack of buy-in from key decision-makers or a failure to effectively engage with multiple stakeholders in the sales process.
    """,
    diagnostic_questions="""
    * Are there specific deals or industries where multi-threaded engagement is more or less common?
    * How do our win rates compare between deals with single-threaded engagement versus multi-threaded engagement?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Encourage sales teams to identify and engage with multiple stakeholders within the prospect\'s organization early in the sales process.
    * Provide training and resources to help sales reps navigate complex decision-making structures and build relationships with various contacts.
    * Implement a CRM system that tracks and encourages multi-threaded engagement throughout the sales cycle.
    """,
    visualization_suggestions="""
    * Stacked bar charts comparing win rates between single-threaded and multi-threaded engagement deals.
    * Line graphs showing the correlation between the number of engaged contacts and deal progression.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low multi-threaded engagement rate may lead to missed opportunities and longer sales cycles.
    * Relying too heavily on a single point of contact within the prospect\'s organization can increase the risk of deals falling through if that contact leaves or changes their position.
    """,
    tracking_tools="""
    * CRM platforms with robust contact management and relationship tracking features.
    * Sales enablement tools that provide insights into the engagement levels of various contacts within a prospect\'s organization.
    """,
    integration_points="""
    * Integrate multi-threaded engagement data with sales forecasting and pipeline management systems to better predict deal outcomes.
    * Link engagement metrics with customer relationship management systems to ensure a cohesive and coordinated approach to customer interactions.
    """,
    change_impact_analysis="""
    * Improving multi-threaded engagement can lead to more comprehensive and effective sales strategies, potentially increasing overall revenue and customer satisfaction.
    * However, changes in engagement approaches may require adjustments in sales processes and resource allocation, impacting operational efficiency.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Prospect", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
