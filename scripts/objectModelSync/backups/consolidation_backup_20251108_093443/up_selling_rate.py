"""
Up-Selling Rate KPI

The rate at which more expensive or upgraded products are sold to an existing customer through channel partners.
"""

from analytics_models import KPI

UP_SELLING_RATE = KPI(
    name="Up-Selling Rate",
    code="UP_SELLING_RATE",
    category="Channel Sales",
    
    # Core Definition
    description="The rate at which more expensive or upgraded products are sold to an existing customer through channel partners.",
    kpi_definition="The rate at which more expensive or upgraded products are sold to an existing customer through channel partners.",
    expected_business_insights="Shows the effectiveness of partners in encouraging customers to upgrade or purchase more premium offerings.",
    measurement_approach="Measures the success rate of selling higher-tier products or more expensive services to existing customers through channel partners.",
    
    # Formula
    formula="(Number of Up-Sell Transactions / Total Number of Transactions) * 100",
    calculation_formula="(Number of Up-Sell Transactions / Total Number of Transactions) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing up-selling rate may indicate successful sales strategies or a growing customer base willing to upgrade.
    * A decreasing rate could signal missed opportunities for up-selling or a shift in customer preferences towards lower-priced options.
    """,
    diagnostic_questions="""
    * Are there specific products or customer segments that consistently show higher or lower up-selling rates?
    * How does our up-selling rate compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Train channel partners on the benefits and features of higher-tier products to increase their confidence in up-selling.
    * Implement targeted marketing campaigns to promote upgraded products to existing customers.
    * Offer incentives or rewards for channel partners who successfully up-sell to their customers.
    """,
    visualization_suggestions="""
    * Line charts showing the up-selling rate over time to identify trends and seasonal patterns.
    * Pie charts comparing the distribution of regular sales versus up-sells to visualize the proportion of upgraded products being sold.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low up-selling rate may indicate a lack of product knowledge or confidence among channel partners.
    * High up-selling rates without a corresponding increase in customer satisfaction or retention could signal pushy or misleading sales tactics.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer preferences and purchase history for targeted up-selling opportunities.
    * Sales performance analytics tools to identify top-performing channel partners and their up-selling strategies.
    """,
    integration_points="""
    * Integrate up-selling rate data with customer feedback and satisfaction scores to understand the impact of up-selling on overall customer experience.
    * Link up-selling rate tracking with inventory management systems to ensure availability of upgraded products for potential sales.
    """,
    change_impact_analysis="""
    * An increase in up-selling rate can positively impact revenue and customer lifetime value, but may require additional resources for product education and marketing.
    * Conversely, a decrease in up-selling rate may lead to missed revenue opportunities and could indicate a need for reevaluation of sales strategies and product offerings.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
