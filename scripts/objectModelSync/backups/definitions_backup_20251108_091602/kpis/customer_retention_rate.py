"""
Customer Retention Rate KPI

The percentage of customers who continue to buy from the company over a set period of time.
"""

from analytics_models import KPI

CUSTOMER_RETENTION_RATE = KPI(
    name="Customer Retention Rate",
    code="CUSTOMER_RETENTION_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of customers who continue to buy from the company over a set period of time.",
    kpi_definition="The percentage of customers who continue to buy from the company over a set period of time.",
    expected_business_insights="Indicates how well the company maintains customer relationships and the stability of the customer base.",
    measurement_approach="Measures the percentage of customers who remain customers over a given period.",
    
    # Formula
    formula="((Number of Customers at End of Period - Number of New Customers Acquired During Period) / Number of Customers at Start of Period) * 100",
    calculation_formula="((Number of Customers at End of Period - Number of New Customers Acquired During Period) / Number of Customers at Start of Period) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer retention rate may indicate improved customer satisfaction and loyalty.
    * A decreasing rate could signal issues with product quality, customer service, or competitive pressures.
    """,
    diagnostic_questions="""
    * What factors contribute to our customer retention rate, such as product performance, pricing, or customer service?
    * Are there specific customer segments or demographics that show higher or lower retention rates?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Enhance customer service and support to address any issues that may be impacting retention.
    * Implement loyalty programs or incentives to encourage repeat purchases and strengthen relationships with customers.
    * Regularly solicit feedback from customers to identify areas for improvement and demonstrate responsiveness to their needs.
    """,
    visualization_suggestions="""
    * Line charts showing the customer retention rate over time to identify trends and seasonal variations.
    * Pie charts to compare retention rates across different customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining customer retention rate can lead to reduced revenue and market share.
    * High retention rates without corresponding growth may indicate a lack of new customer acquisition and potential market saturation.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify opportunities for retention improvement.
    * Survey and feedback tools to gather insights from customers about their experiences and reasons for staying or leaving.
    """,
    integration_points="""
    * Integrate customer retention data with sales and marketing systems to align efforts in retaining and acquiring customers.
    * Link retention rate with customer feedback platforms to address specific issues and measure the impact of improvements.
    """,
    change_impact_analysis="""
    * Improving customer retention can lead to increased customer lifetime value and reduced reliance on costly acquisition efforts.
    * However, focusing solely on retention may neglect the need for continuous growth and expansion into new markets.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity"]
    }
)
