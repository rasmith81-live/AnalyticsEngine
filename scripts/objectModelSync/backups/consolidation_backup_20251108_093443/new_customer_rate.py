"""
New Customer Rate KPI

The rate at which new customers are acquired compared to returning customers.
"""

from analytics_models import KPI

NEW_CUSTOMER_RATE = KPI(
    name="New Customer Rate",
    code="NEW_CUSTOMER_RATE",
    category="Sales Operations",
    
    # Core Definition
    description="The rate at which new customers are acquired compared to returning customers.",
    kpi_definition="The rate at which new customers are acquired compared to returning customers.",
    expected_business_insights="Identifies growth in the company’s customer base and the effectiveness of acquisition strategies.",
    measurement_approach="Tracks the percentage of new customers out of all customers acquired in a period.",
    
    # Formula
    formula="(Number of New Customers / Total Number of Customers Acquired) * 100",
    calculation_formula="(Number of New Customers / Total Number of Customers Acquired) * 100",
    
    # Analysis
    trend_analysis="""
    * A rising new customer rate may indicate successful marketing efforts or an expanding customer base.
    * A decreasing rate could signal a decline in market appeal or customer retention issues.
    """,
    diagnostic_questions="""
    * What marketing strategies have been most effective in acquiring new customers?
    * How does our new customer rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in targeted marketing campaigns to reach new customer segments.
    * Enhance the onboarding process to improve new customer retention.
    * Offer incentives for referrals to attract new customers through existing customer networks.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of new customer rate over time.
    * Pie charts comparing the proportion of new customers to returning customers.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Overemphasis on acquiring new customers may neglect the needs of existing customers.
    * A declining new customer rate may indicate a loss of market relevance or competitive edge.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer acquisition data.
    * Marketing automation tools to streamline and optimize new customer acquisition processes.
    """,
    integration_points="""
    * Integrate new customer rate data with sales performance metrics to assess the impact on revenue growth.
    * Link with customer feedback systems to understand the experience of new customers and identify areas for improvement.
    """,
    change_impact_analysis="""
    * An increasing new customer rate may lead to higher sales revenue but could also strain resources for customer support and onboarding.
    * A decreasing new customer rate may result in slower revenue growth and impact overall market positioning.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES", "SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07"
        "replaces": ["NEW_CUSTOMER_RATIO"],
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
