"""
Cross-Selling Rate KPI

The rate at which additional products or services are sold to an existing customer through channel partners.
"""

from analytics_models import KPI

CROSS_SELLING_RATE = KPI(
    name="Cross-Selling Rate",
    code="CROSS_SELLING_RATE",
    category="Channel Sales",
    
    # Core Definition
    description="The rate at which additional products or services are sold to an existing customer through channel partners.",
    kpi_definition="The rate at which additional products or services are sold to an existing customer through channel partners.",
    expected_business_insights="Indicates the effectiveness of partners in leveraging existing relationships to expand the customer’s purchase.",
    measurement_approach="Measures the success rate of selling additional products or services to existing customers through channel partners.",
    
    # Formula
    formula="(Number of Customers Purchasing Additional Offerings / Total Number of Customers) * 100",
    calculation_formula="(Number of Customers Purchasing Additional Offerings / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing cross-selling rate may indicate successful upselling strategies or a growing understanding of customer needs.
    * A decreasing rate could signal a lack of effective cross-selling initiatives or a shift in customer preferences.
    """,
    diagnostic_questions="""
    * Are there specific products or services that are frequently cross-sold together?
    * How does our cross-selling rate compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Train channel partners on identifying cross-selling opportunities and effectively communicating additional value to customers.
    * Implement targeted marketing campaigns to promote complementary products or services to existing customers.
    * Utilize customer relationship management (CRM) systems to track customer preferences and suggest relevant cross-selling opportunities.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of cross-selling rate over time.
    * Pie charts illustrating the distribution of cross-sold products or services.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low cross-selling rate may lead to missed revenue opportunities and underutilization of existing customer base.
    * An excessively high rate may indicate aggressive sales tactics that could potentially alienate customers.
    """,
    tracking_tools="""
    * CRM systems with built-in cross-selling modules to track and manage cross-selling activities.
    * Data analytics tools to identify patterns and correlations between customer purchases for targeted cross-selling efforts.
    """,
    integration_points="""
    * Integrate cross-selling rate data with customer feedback systems to understand the impact of cross-selling on customer satisfaction.
    * Link cross-selling initiatives with sales performance metrics to measure the effectiveness of cross-selling strategies.
    """,
    change_impact_analysis="""
    * Improving the cross-selling rate can lead to increased customer lifetime value and overall revenue growth.
    * However, overly aggressive cross-selling tactics may result in customer churn and reputational damage.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
