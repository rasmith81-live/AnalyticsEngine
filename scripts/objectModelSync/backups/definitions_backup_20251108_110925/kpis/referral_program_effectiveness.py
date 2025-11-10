"""
Referral Program Effectiveness KPI

The effectiveness of a referral program in generating new business through existing key accounts.
"""

from analytics_models import KPI

REFERRAL_PROGRAM_EFFECTIVENESS = KPI(
    name="Referral Program Effectiveness",
    code="REFERRAL_PROGRAM_EFFECTIVENESS",
    category="Key Account Management",
    
    # Core Definition
    description="The effectiveness of a referral program in generating new business through existing key accounts.",
    kpi_definition="The effectiveness of a referral program in generating new business through existing key accounts.",
    expected_business_insights="Reveals the impact of referrals on sales and can guide improvements to the referral program.",
    measurement_approach="Measures the success of a referral program in generating new business.",
    
    # Formula
    formula="(New Customers Acquired Through Referrals / Total Number of Referrals) * 100",
    calculation_formula="(New Customers Acquired Through Referrals / Total Number of Referrals) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing number of referrals from existing key accounts may indicate a growing satisfaction and loyalty among customers.
    * A decreasing number of referrals could signal dissatisfaction or a need for improvement in the referral program\'s incentives or processes.
    """,
    diagnostic_questions="""
    * What are the specific reasons why key accounts are or are not referring new business to us?
    * How does the referral program\'s performance compare to industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly solicit feedback from key accounts to understand their satisfaction and identify areas for improvement in the referral program.
    * Offer incentives or rewards for key accounts to encourage and recognize successful referrals.
    * Continuously evaluate and update the referral program to ensure it remains relevant and appealing to key accounts.
    """,
    visualization_suggestions="""
    * Line charts showing the number of referrals over time to identify any trends or patterns.
    * Pie charts to visualize the distribution of referrals by key account or industry.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A lack of referrals may indicate a weakened relationship with key accounts and potential loss of business in the future.
    * Over-reliance on referrals from key accounts may lead to vulnerability if those accounts reduce their business with the organization.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage interactions with key accounts and monitor referral activity.
    * Referral management platforms to streamline the process of tracking and rewarding successful referrals.
    """,
    integration_points="""
    * Integrate referral program data with sales and marketing systems to better understand the impact of referrals on overall business performance.
    * Link referral program performance with customer satisfaction metrics to assess the correlation between referrals and customer loyalty.
    """,
    change_impact_analysis="""
    * Improving the referral program can lead to increased sales and revenue from new business generated through key accounts.
    * However, a decline in referral effectiveness may require additional resources to address underlying issues and maintain strong relationships with key accounts.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Success Manager", "Key Account", "Key Account Manager", "Loyalty Program", "Quarterly Business Review", "Referral", "Renewal Management", "Sales Training Program"]
    }
)
