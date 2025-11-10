"""
Total Revenue per Customer KPI

The total revenue received from an average customer, which is useful for understanding the value generated from customer relationships.
"""

from analytics_models import KPI

TOTAL_REVENUE_PER_CUSTOMER = KPI(
    name="Total Revenue per Customer",
    code="TOTAL_REVENUE_PER_CUSTOMER",
    category="Sales Strategy",
    
    # Core Definition
    description="The total revenue received from an average customer, which is useful for understanding the value generated from customer relationships.",
    kpi_definition="The total revenue received from an average customer, which is useful for understanding the value generated from customer relationships.",
    expected_business_insights="Indicates the value of customers to the company and guides customer relationship management.",
    measurement_approach="Calculates the average revenue generated from each customer.",
    
    # Formula
    formula="Total Revenue / Total Number of Customers",
    calculation_formula="Total Revenue / Total Number of Customers",
    
    # Analysis
    trend_analysis="""
    * Increasing total revenue per customer may indicate successful upselling or cross-selling strategies.
    * Decreasing revenue per customer could signal declining customer loyalty or satisfaction.
    """,
    diagnostic_questions="""
    * What factors contribute to the increase or decrease in revenue per customer?
    * How does the revenue per customer compare to industry benchmarks or historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement personalized marketing and sales strategies to increase customer spend.
    * Focus on improving customer experience and satisfaction to retain and grow customer value.
    * Regularly review and adjust pricing strategies to maximize revenue per customer.
    """,
    visualization_suggestions="""
    * Line charts showing revenue per customer over time.
    * Pareto charts to identify the most valuable customers contributing to total revenue.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Overemphasis on short-term revenue gains may lead to customer churn and long-term revenue loss.
    * Failure to adapt to changing customer preferences and needs can result in declining revenue per customer.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer purchasing behavior.
    * Business intelligence tools to segment and analyze customer data for targeted sales strategies.
    """,
    integration_points="""
    * Integrate revenue per customer data with customer feedback systems to understand the correlation between satisfaction and spending.
    * Link with marketing automation platforms to personalize offers and promotions based on customer purchasing patterns.
    """,
    change_impact_analysis="""
    * Increasing revenue per customer may lead to higher profitability and improved customer lifetime value.
    * However, aggressive sales tactics to boost revenue per customer can negatively impact customer relationships and brand reputation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
