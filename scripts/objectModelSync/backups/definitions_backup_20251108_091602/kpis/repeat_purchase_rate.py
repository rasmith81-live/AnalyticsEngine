"""
Repeat Purchase Rate KPI

The percentage of customers who have made more than one purchase within a specific time frame.
"""

from analytics_models import KPI

REPEAT_PURCHASE_RATE = KPI(
    name="Repeat Purchase Rate",
    code="REPEAT_PURCHASE_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of customers who have made more than one purchase within a specific time frame.",
    kpi_definition="The percentage of customers who have made more than one purchase within a specific time frame.",
    expected_business_insights="Provides insights into customer loyalty and the effectiveness of retention tactics.",
    measurement_approach="Measures the percentage of customers who make more than one purchase over a specific time period.",
    
    # Formula
    formula="(Number of Customers with Multiple Purchases / Total Number of Customers) * 100",
    calculation_formula="(Number of Customers with Multiple Purchases / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing repeat purchase rate may indicate improved customer satisfaction and loyalty.
    * A decreasing rate could signal declining customer engagement or increased competition.
    """,
    diagnostic_questions="""
    * What factors contribute to the increase or decrease in repeat purchase rate?
    * Are there specific customer segments that show higher or lower repeat purchase rates?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement customer loyalty programs to incentivize repeat purchases.
    * Enhance customer service to ensure a positive post-purchase experience.
    * Personalize marketing efforts to encourage repeat purchases based on past behavior.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in repeat purchase rate over time.
    * Pie charts to compare repeat purchase rates across different customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining repeat purchase rate may lead to reduced revenue and market share.
    * High repeat purchase rates from a small customer segment may indicate over-reliance on a few key customers.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer behavior.
    * Data analytics tools to identify patterns and trends in customer purchasing behavior.
    """,
    integration_points="""
    * Integrate repeat purchase rate data with marketing automation systems to tailor campaigns for different customer segments.
    * Link with inventory management systems to ensure sufficient stock for frequently purchased items.
    """,
    change_impact_analysis="""
    * An increase in repeat purchase rate can lead to higher customer lifetime value and overall revenue.
    * However, focusing solely on repeat purchase rate may neglect the acquisition of new customers, impacting long-term growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Purchase History", "Sales Representative"]
    }
)
