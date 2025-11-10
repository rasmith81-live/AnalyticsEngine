"""
Customer Account Growth Rate KPI

The rate at which customer accounts grow in terms of usage or added features over time.
"""

from analytics_models import KPI

CUSTOMER_ACCOUNT_GROWTH_RATE = KPI(
    name="Customer Account Growth Rate",
    code="CUSTOMER_ACCOUNT_GROWTH_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The rate at which customer accounts grow in terms of usage or added features over time.",
    kpi_definition="The rate at which customer accounts grow in terms of usage or added features over time.",
    expected_business_insights="Indicates the effectiveness of upselling and cross-selling strategies and customer satisfaction with the product or service.",
    measurement_approach="Measures the rate at which customer accounts are increasing in value over a specific period.",
    
    # Formula
    formula="(Total Revenue at the End of the Period - Total Revenue at the Start of the Period) / Total Revenue at the Start of the Period",
    calculation_formula="(Total Revenue at the End of the Period - Total Revenue at the Start of the Period) / Total Revenue at the Start of the Period",
    
    # Analysis
    trend_analysis="""
    * Increasing customer account growth rate may indicate higher customer satisfaction and loyalty.
    * A decreasing growth rate could signal a need for better customer engagement or a decline in the perceived value of the product or service.
    """,
    diagnostic_questions="""
    * Are there specific features or services that customers frequently request or inquire about?
    * How does our customer account growth rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly engage with customers to understand their evolving needs and preferences.
    * Offer incentives for customers to upgrade to higher-tiered plans or packages.
    * Provide personalized recommendations for additional features or services based on customer usage patterns.
    """,
    visualization_suggestions="""
    * Line charts showing the growth rate over time for individual customer accounts.
    * Stacked bar graphs comparing the growth rates of different customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A stagnant or declining growth rate may lead to customer churn and reduced revenue.
    * Rapid growth without proper support or resources may strain customer service and operational capabilities.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify opportunities for growth.
    * Usage analytics tools to understand how customers are engaging with the product or service.
    """,
    integration_points="""
    * Integrate customer account growth rate data with sales and marketing systems to align efforts towards customer expansion.
    * Link growth rate metrics with product development and innovation processes to prioritize features that drive customer adoption and retention.
    """,
    change_impact_analysis="""
    * Improving the customer account growth rate can lead to increased lifetime value of customers and higher overall revenue.
    * Conversely, a declining growth rate may necessitate a reevaluation of the product or service offering and customer engagement strategies.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Product Usage", "Revenue Forecast", "Sale"]
    }
)
