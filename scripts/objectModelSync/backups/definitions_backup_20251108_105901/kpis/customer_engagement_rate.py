"""
Customer Engagement Rate KPI

The level of interaction and engagement a customer has with the brand or sales team.
"""

from analytics_models import KPI

CUSTOMER_ENGAGEMENT_RATE = KPI(
    name="Customer Engagement Rate",
    code="CUSTOMER_ENGAGEMENT_RATE",
    category="Outside Sales",
    
    # Core Definition
    description="The level of interaction and engagement a customer has with the brand or sales team.",
    kpi_definition="The level of interaction and engagement a customer has with the brand or sales team.",
    expected_business_insights="Provides insights into customer loyalty and product/service relevance, which can inform engagement strategies.",
    measurement_approach="Measures the level of customer interaction with a company’s products or services.",
    
    # Formula
    formula="(Number of Engaged Customers / Total Customers) * 100",
    calculation_formula="(Number of Engaged Customers / Total Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer engagement rate may indicate successful marketing efforts or improved customer service.
    * A decreasing rate could signal a decline in brand relevance or customer satisfaction.
    """,
    diagnostic_questions="""
    * What specific interactions or touchpoints are included in the calculation of customer engagement?
    * How does the customer engagement rate vary across different customer segments or demographics?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a customer relationship management (CRM) system to better track and manage customer interactions.
    * Invest in training for the sales team to improve their ability to engage and build relationships with customers.
    * Regularly solicit feedback from customers to understand how to enhance their engagement with the brand.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer engagement rate over time.
    * Pie charts to illustrate the distribution of customer engagement across different channels or touchpoints.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low customer engagement rate may lead to decreased customer loyalty and retention.
    * High fluctuations in the engagement rate could indicate inconsistent customer experiences or ineffective marketing strategies.
    """,
    tracking_tools="""
    * Customer engagement platforms like HubSpot or Salesforce for tracking and managing customer interactions.
    * Social media monitoring tools to gauge customer engagement on various social platforms.
    """,
    integration_points="""
    * Integrate customer engagement data with sales performance metrics to understand the impact of engagement on sales outcomes.
    * Link customer engagement with customer support systems to ensure a seamless and consistent customer experience.
    """,
    change_impact_analysis="""
    * Improving customer engagement can lead to increased customer lifetime value and brand advocacy.
    * However, a focus solely on increasing engagement without considering quality may lead to superficial interactions that do not drive meaningful customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
