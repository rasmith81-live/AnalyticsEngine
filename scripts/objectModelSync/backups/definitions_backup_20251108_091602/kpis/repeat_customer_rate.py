"""
Repeat Customer Rate KPI

The percentage of customers who make repeat purchases within a given time frame.
"""

from analytics_models import KPI

REPEAT_CUSTOMER_RATE = KPI(
    name="Repeat Customer Rate",
    code="REPEAT_CUSTOMER_RATE",
    category="Outside Sales",
    
    # Core Definition
    description="The percentage of customers who make repeat purchases within a given time frame.",
    kpi_definition="The percentage of customers who make repeat purchases within a given time frame.",
    expected_business_insights="Indicates customer loyalty and satisfaction with the company\'s products or services, influencing retention strategies.",
    measurement_approach="Tracks the percentage of customers that make multiple purchases over a specific period.",
    
    # Formula
    formula="(Number of Repeat Customers / Total Number of Customers) * 100",
    calculation_formula="(Number of Repeat Customers / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing repeat customer rate may indicate improved customer satisfaction and loyalty.
    * A decreasing rate could signal declining customer retention and the need for better post-sales support.
    """,
    diagnostic_questions="""
    * Are there specific products or services that have a higher repeat purchase rate?
    * What are the common reasons for customers not making repeat purchases?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement customer loyalty programs to incentivize repeat purchases.
    * Enhance post-sales support and follow-up to ensure customer satisfaction and encourage repeat business.
    * Personalize marketing and communication to strengthen customer relationships and encourage repeat purchases.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of repeat customer rate over time.
    * Pie charts comparing repeat customer rate by customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low repeat customer rate may lead to reduced revenue and profitability.
    * High competition and market saturation can make it challenging to improve the repeat customer rate.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer behavior and purchase history.
    * Marketing automation tools to personalize and automate customer communication for better retention.
    """,
    integration_points="""
    * Integrate repeat customer rate data with sales and marketing systems to align strategies for customer retention.
    * Link with customer feedback and satisfaction surveys to understand the factors influencing repeat purchases.
    """,
    change_impact_analysis="""
    * An improved repeat customer rate can lead to higher customer lifetime value and overall business growth.
    * Conversely, a declining repeat customer rate may indicate the need for significant changes in customer engagement and retention strategies.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
