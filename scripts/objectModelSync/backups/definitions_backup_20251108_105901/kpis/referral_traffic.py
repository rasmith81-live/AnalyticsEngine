"""
Referral Traffic KPI

The amount of traffic coming to your site through existing customers referring new customers.
"""

from analytics_models import KPI

REFERRAL_TRAFFIC = KPI(
    name="Referral Traffic",
    code="REFERRAL_TRAFFIC",
    category="Customer Retention",
    
    # Core Definition
    description="The amount of traffic coming to your site through existing customers referring new customers.",
    kpi_definition="The amount of traffic coming to your site through existing customers referring new customers.",
    expected_business_insights="Indicates the effectiveness of referral marketing and partnerships, as well as customer advocacy.",
    measurement_approach="Tracks the number of visitors to a site that come through referral links from other sources.",
    
    # Formula
    formula="Total Number of Visitors via Referral Links",
    calculation_formula="Total Number of Visitors via Referral Links",
    
    # Analysis
    trend_analysis="""
    * An increasing referral traffic may indicate a growing customer base and positive word-of-mouth marketing.
    * A decreasing trend could signal a decline in customer satisfaction or engagement, leading to fewer referrals.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or products that are driving the majority of referral traffic?
    * How does our referral traffic compare with industry benchmarks or seasonal fluctuations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a customer referral program to incentivize existing customers to refer new ones.
    * Enhance customer experience to encourage positive word-of-mouth and increase referrals.
    * Regularly engage with existing customers through targeted marketing and personalized communication to keep them engaged and likely to refer others.
    """,
    visualization_suggestions="""
    * Line charts showing referral traffic over time to identify trends and patterns.
    * Pie charts to visualize the distribution of referral traffic by customer segments or products.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A decline in referral traffic may indicate underlying issues with customer satisfaction or loyalty.
    * Dependence on a few customers for the majority of referrals can pose a risk if their engagement decreases.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage customer referrals and engagement.
    * Social media monitoring tools to identify and leverage customer advocacy and referrals on social platforms.
    """,
    integration_points="""
    * Integrate referral traffic data with customer relationship management systems to better understand the impact of referrals on customer lifetime value.
    * Link referral traffic with sales and marketing systems to attribute referrals to specific campaigns or initiatives.
    """,
    change_impact_analysis="""
    * Increasing referral traffic can lead to higher customer acquisition at a lower cost, positively impacting overall sales performance.
    * Conversely, a decline in referral traffic may lead to increased customer acquisition costs and reduced sales efficiency.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Referral"]
    }
)
