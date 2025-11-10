"""
Partner Influence on Customer Retention KPI

The impact channel partners have on retaining customers, often measured by customer renewal rates or repeat purchases through partners.
"""

from analytics_models import KPI

PARTNER_INFLUENCE_ON_CUSTOMER_RETENTION = KPI(
    name="Partner Influence on Customer Retention",
    code="PARTNER_INFLUENCE_ON_CUSTOMER_RETENTION",
    category="Channel Sales",
    
    # Core Definition
    description="The impact channel partners have on retaining customers, often measured by customer renewal rates or repeat purchases through partners.",
    kpi_definition="The impact channel partners have on retaining customers, often measured by customer renewal rates or repeat purchases through partners.",
    expected_business_insights="Highlights partner impact on customer loyalty and informs strategies to improve retention through partners.",
    measurement_approach="Assesses the role of partners in maintaining customer relationships and preventing churn.",
    
    # Formula
    formula="(Customer Retention Rate Attributable to Partners / Overall Customer Retention Rate) * 100",
    calculation_formula="(Customer Retention Rate Attributable to Partners / Overall Customer Retention Rate) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing partner influence on customer retention may indicate stronger relationships and better customer satisfaction.
    * A decreasing influence could signal dissatisfaction with partner performance or a shift in customer preferences.
    """,
    diagnostic_questions="""
    * Are there specific products or services where partners have a particularly strong or weak impact on customer retention?
    * How do our partner-influenced customer retention rates compare with direct sales retention rates?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide partners with additional training and resources to enhance their ability to retain customers.
    * Regularly review and assess partner performance to identify areas for improvement.
    * Implement customer feedback mechanisms to understand the impact of partners on retention.
    """,
    visualization_suggestions="""
    * Line charts showing partner-influenced customer retention rates over time.
    * Comparative bar graphs displaying retention rates for customers acquired through partners versus other channels.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Over-reliance on partners for customer retention may lead to vulnerability if partner relationships sour.
    * Weak partner influence on retention could result in lost opportunities for repeat business.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track and analyze customer retention data by channel.
    * Partner performance management software to assess and improve partner contributions to customer retention.
    """,
    integration_points="""
    * Integrate partner-influenced customer retention data with sales performance metrics to understand the overall impact of partners on revenue.
    * Link customer feedback systems with partner management platforms to gather insights on partner-influenced retention.
    """,
    change_impact_analysis="""
    * Improving partner influence on customer retention can lead to increased customer lifetime value and overall revenue growth.
    * Conversely, a decline in partner influence may require adjustments in channel strategy and resource allocation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Renewal Management", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
