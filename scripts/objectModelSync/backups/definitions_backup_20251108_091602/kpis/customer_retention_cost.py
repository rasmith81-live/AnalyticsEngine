"""
Customer Retention Cost KPI

The total cost associated with retaining an existing customer.
"""

from analytics_models import KPI

CUSTOMER_RETENTION_COST = KPI(
    name="Customer Retention Cost",
    code="CUSTOMER_RETENTION_COST",
    category="Customer Retention",
    
    # Core Definition
    description="The total cost associated with retaining an existing customer.",
    kpi_definition="The total cost associated with retaining an existing customer.",
    expected_business_insights="Gives insight into the investment required to keep customers and can be compared against the cost of acquiring new customers.",
    measurement_approach="Tracks the total costs associated with retaining an existing customer.",
    
    # Formula
    formula="Total Retention Costs / Number of Customers Retained",
    calculation_formula="Total Retention Costs / Number of Customers Retained",
    
    # Analysis
    trend_analysis="""
    * Increasing customer retention cost may indicate higher expenses in loyalty programs or customer support.
    * Decreasing cost could signal improved customer satisfaction and loyalty, leading to lower retention efforts.
    """,
    diagnostic_questions="""
    * Are there specific customer segments that require higher retention costs?
    * How does our customer retention cost compare with industry averages or benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in customer relationship management (CRM) systems to better understand and target high-cost segments.
    * Implement customer loyalty programs to increase retention without significantly increasing costs.
    * Regularly review and optimize customer support processes to reduce associated expenses.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer retention cost over time.
    * Pie charts to compare the distribution of retention costs across different customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High customer retention costs may erode profitability if not aligned with the value derived from retained customers.
    * Significant fluctuations in retention costs may indicate inconsistent customer experiences or ineffective retention strategies.
    """,
    tracking_tools="""
    * CRM software like Salesforce or HubSpot for tracking and managing customer retention efforts.
    * Customer loyalty platforms such as Smile.io or Yotpo to implement and monitor loyalty programs.
    """,
    integration_points="""
    * Integrate customer retention cost analysis with financial systems to understand its impact on overall profitability.
    * Link retention cost data with customer feedback and satisfaction metrics to identify areas for improvement.
    """,
    change_impact_analysis="""
    * Reducing customer retention costs may lead to improved profitability, but it should not compromise the quality of customer experience.
    * Increasing retention costs without a corresponding increase in customer value may indicate inefficiencies in retention strategies.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Sale"]
    }
)
