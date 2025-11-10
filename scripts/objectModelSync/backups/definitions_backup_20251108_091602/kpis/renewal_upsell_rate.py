"""
Renewal Upsell Rate KPI

The percentage of renewal opportunities where an upsell was achieved.
"""

from analytics_models import KPI

RENEWAL_UPSELL_RATE = KPI(
    name="Renewal Upsell Rate",
    code="RENEWAL_UPSELL_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of renewal opportunities where an upsell was achieved.",
    kpi_definition="The percentage of renewal opportunities where an upsell was achieved.",
    expected_business_insights="Indicates the success of upsell strategies during the renewal process and customer willingness to expand their investment.",
    measurement_approach="Tracks the percentage of renewals that include an upgrade or additional purchase.",
    
    # Formula
    formula="(Number of Renewals with Upsell / Total Number of Renewals) * 100",
    calculation_formula="(Number of Renewals with Upsell / Total Number of Renewals) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing renewal upsell rate may indicate successful sales strategies and a strong understanding of customer needs.
    * A decreasing rate could signal missed opportunities for upselling or a decline in customer satisfaction and loyalty.
    """,
    diagnostic_questions="""
    * Are there specific products or services that consistently lead to successful upsells during renewals?
    * How does our renewal upsell rate compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Train sales teams to identify upsell opportunities and effectively communicate the value of additional products or services.
    * Implement customer segmentation strategies to tailor upsell offers based on specific customer needs and preferences.
    * Regularly review and update product or service offerings to ensure they align with customer demands and market trends.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of renewal upsell rates over time.
    * Pie charts to visualize the distribution of successful upsells by product or service category.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low renewal upsell rate may lead to missed revenue opportunities and reduced customer lifetime value.
    * Consistently high upsell rates could indicate aggressive or pushy sales tactics that may harm customer relationships.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify upsell opportunities.
    * Data analytics tools to analyze customer behavior and preferences for targeted upsell strategies.
    """,
    integration_points="""
    * Integrate renewal upsell rate data with customer feedback and satisfaction scores to understand the impact of upselling on overall customer experience.
    * Link upsell performance with sales compensation and incentive programs to align sales efforts with upsell goals.
    """,
    change_impact_analysis="""
    * Improving the renewal upsell rate can lead to increased revenue and customer loyalty, but may also require additional resources for sales training and customer segmentation.
    * Conversely, a declining upsell rate may indicate a need for reevaluation of sales strategies and product offerings to maintain competitiveness in the market.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Purchase History", "Renewal Management"]
    }
)
