"""
Partner Satisfaction Index KPI

A composite metric that measures the overall satisfaction of channel partners with the support, products, and services provided by the company.
"""

from analytics_models import KPI

PARTNER_SATISFACTION_INDEX = KPI(
    name="Partner Satisfaction Index",
    code="PARTNER_SATISFACTION_INDEX",
    category="Channel Sales",
    
    # Core Definition
    description="A composite metric that measures the overall satisfaction of channel partners with the support, products, and services provided by the company.",
    kpi_definition="A composite metric that measures the overall satisfaction of channel partners with the support, products, and services provided by the company.",
    expected_business_insights="Offers insights into partner sentiment and satisfaction, which can predict engagement and performance.",
    measurement_approach="Takes into account partners’ feedback on various aspects of the partnership.",
    
    # Formula
    formula="(Sum of Partner Satisfaction Scores / Number of Survey Responses) * 100",
    calculation_formula="(Sum of Partner Satisfaction Scores / Number of Survey Responses) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing Partner Satisfaction Index may indicate improved product quality, better support, or expanded service offerings.
    * A decreasing index could signal issues with product availability, support responsiveness, or overall partner experience.
    """,
    diagnostic_questions="""
    * Are there specific products or services that receive consistently lower satisfaction ratings from partners?
    * How does our Partner Satisfaction Index compare with industry benchmarks or with competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly solicit feedback from partners and act on their suggestions to improve satisfaction.
    * Invest in partner training and enablement to ensure they are equipped to represent and sell the company\'s products effectively.
    * Provide incentives or rewards for high-performing partners to encourage continued satisfaction and loyalty.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of Partner Satisfaction Index over time.
    * Comparison bar charts to visualize the satisfaction levels across different products or services.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low Partner Satisfaction Index can lead to decreased sales and market share as partners may choose to represent competing products.
    * Consistently low satisfaction ratings may indicate systemic issues that could harm the company\'s reputation in the channel.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track partner interactions and feedback.
    * Partner portal platforms to provide easy access to resources and support materials for partners.
    """,
    integration_points="""
    * Integrate Partner Satisfaction Index data with sales performance metrics to understand the impact of partner satisfaction on revenue.
    * Link partner feedback systems with product development and support teams to drive continuous improvement based on partner input.
    """,
    change_impact_analysis="""
    * Improving Partner Satisfaction Index can lead to increased sales, market share, and overall channel performance.
    * Conversely, a declining index may result in decreased revenue and partner loyalty, impacting long-term channel relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Feedback", "Enablement Feedback", "Key Account", "Key Account Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Partnership", "Product", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
