"""
New Business from Referrals KPI

The amount of new business generated through referrals from existing key accounts.
"""

from analytics_models import KPI

NEW_BUSINESS_FROM_REFERRALS = KPI(
    name="New Business from Referrals",
    code="NEW_BUSINESS_FROM_REFERRALS",
    category="Key Account Management",
    
    # Core Definition
    description="The amount of new business generated through referrals from existing key accounts.",
    kpi_definition="The amount of new business generated through referrals from existing key accounts.",
    expected_business_insights="Showcases the effectiveness of referral programs and customer satisfaction.",
    measurement_approach="Measures the amount of new business generated from customer referrals.",
    
    # Formula
    formula="Revenue from Referred Customers / Total Revenue",
    calculation_formula="Revenue from Referred Customers / Total Revenue",
    
    # Analysis
    trend_analysis="""
    * Increasing new business from referrals may indicate a strong relationship with existing key accounts and a high level of customer satisfaction.
    * A decreasing trend could signal a need to improve the quality of service or products offered to existing key accounts, leading to fewer referrals.
    """,
    diagnostic_questions="""
    * Are there specific key accounts that consistently provide more referrals than others?
    * How does the conversion rate of referrals compare to other lead generation sources?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a formal referral program to incentivize existing key accounts to refer new business.
    * Regularly communicate with key accounts to ensure their needs are being met and to encourage them to refer others.
    * Provide exceptional service and value to existing key accounts to naturally generate more referrals.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of new business from referrals over time.
    * Pie charts comparing the percentage of new business from referrals versus other sources.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low levels of new business from referrals may indicate a lack of satisfaction or loyalty among existing key accounts.
    * Relying too heavily on referrals may limit the diversity of the customer base and increase vulnerability to changes in the referral network.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage referral activities from key accounts.
    * Referral tracking tools to identify which key accounts are providing the most referrals and which ones need more attention.
    """,
    integration_points="""
    * Integrate referral tracking with sales performance metrics to understand the impact of referrals on overall sales results.
    * Link referral data with customer satisfaction surveys to correlate referral activity with customer loyalty and satisfaction levels.
    """,
    change_impact_analysis="""
    * Increasing new business from referrals can lead to a more predictable and sustainable sales pipeline, reducing the reliance on other lead generation methods.
    * However, a decrease in new business from referrals may require additional investment in other lead generation strategies to maintain sales growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Quarterly Business Review", "Renewal Management", "Revenue Forecast", "Sale"]
    }
)
