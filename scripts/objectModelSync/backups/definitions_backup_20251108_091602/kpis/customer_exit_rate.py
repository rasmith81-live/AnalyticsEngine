"""
Customer Exit Rate KPI

The rate at which customers cease to do business with a company.
"""

from analytics_models import KPI

CUSTOMER_EXIT_RATE = KPI(
    name="Customer Exit Rate",
    code="CUSTOMER_EXIT_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The rate at which customers cease to do business with a company.",
    kpi_definition="The rate at which customers cease to do business with a company.",
    expected_business_insights="Identifies trends in customer loss and can prompt investigation into underlying causes.",
    measurement_approach="Tracks the percentage of customers who end their relationship with the company over a specific period.",
    
    # Formula
    formula="(Number of Customers Who Left / Total Number of Customers) * 100",
    calculation_formula="(Number of Customers Who Left / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer exit rate may indicate issues with product quality, customer service, or pricing.
    * A decreasing rate could signal improved customer satisfaction, loyalty programs, or targeted marketing efforts.
    """,
    diagnostic_questions="""
    * Are there common reasons cited by customers for ending their business relationship with us?
    * How does our customer exit rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement customer feedback mechanisms to understand the reasons for customer exits and address them proactively.
    * Invest in customer service training and resources to improve overall customer experience and retention.
    * Develop loyalty programs or incentives to encourage repeat business and reduce customer churn.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer exit rates over time.
    * Pie charts to visualize the distribution of customer exits by reason or customer segment.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High customer exit rates can lead to loss of revenue and market share.
    * Consistently high exit rates may indicate systemic issues that require immediate attention to prevent further loss.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify potential churn risks.
    * Social listening tools to monitor online conversations and sentiment about the brand.
    """,
    integration_points="""
    * Integrate customer exit rate data with sales and marketing systems to identify patterns and triggers for customer exits.
    * Link customer exit rate with customer feedback systems to gain deeper insights into the reasons behind exits.
    """,
    change_impact_analysis="""
    * Reducing customer exit rates can lead to increased customer lifetime value and higher overall revenue.
    * However, efforts to reduce exit rates may require increased investment in customer retention strategies and resources.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review"]
    }
)
