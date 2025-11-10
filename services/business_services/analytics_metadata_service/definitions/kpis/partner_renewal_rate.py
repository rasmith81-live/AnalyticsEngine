"""
Partner Renewal Rate KPI

The rate at which channel partners renew their contracts or agreements with the company.
"""

from analytics_models import KPI

PARTNER_RENEWAL_RATE = KPI(
    name="Partner Renewal Rate",
    code="PARTNER_RENEWAL_RATE",
    category="Channel Sales",
    
    # Core Definition
    description="The rate at which channel partners renew their contracts or agreements with the company.",
    kpi_definition="The rate at which channel partners renew their contracts or agreements with the company.",
    expected_business_insights="Indicates partner satisfaction and the health of long-term relationships, guiding retention strategies.",
    measurement_approach="Calculates the percentage of partners who renew their contracts or agreements with the company.",
    
    # Formula
    formula="(Number of Partners Renewing / Number of Partners Up for Renewal) * 100",
    calculation_formula="(Number of Partners Renewing / Number of Partners Up for Renewal) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing partner renewal rate may indicate improved satisfaction with the company\'s products or services.
    * Decreasing renewal rate could signal dissatisfaction, increased competition, or changes in the partner\'s business strategy.
    """,
    diagnostic_questions="""
    * Are there specific reasons partners cite for not renewing their contracts?
    * How does our partner renewal rate compare with industry averages or with our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Enhance partner support and communication to address any concerns or issues that may lead to non-renewal.
    * Regularly review and update the value proposition for partners to ensure it aligns with their evolving needs and market conditions.
    * Provide incentives for partners to renew, such as early renewal discounts or additional marketing support.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in partner renewal rates over time.
    * Pie charts comparing renewal rates across different partner segments or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low partner renewal rates can result in loss of revenue and market share.
    * High partner churn can damage the company\'s reputation and make it less attractive to potential new partners.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems to track partner interactions and identify potential renewal risks.
    * Partner portal or management software to streamline communication and support for partners.
    """,
    integration_points="""
    * Integrate partner renewal data with sales and marketing systems to identify opportunities for proactive engagement.
    * Link renewal rates with partner performance metrics to assess the overall impact on the company\'s sales and market presence.
    """,
    change_impact_analysis="""
    * Improving partner renewal rates can lead to increased revenue and market stability.
    * Conversely, a decline in renewal rates may require adjustments in sales and marketing strategies to attract new partners and customers.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Contract", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Renewal Management", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
