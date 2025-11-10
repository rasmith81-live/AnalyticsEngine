"""
Average Issue Resolution Time KPI

The average time taken to resolve customer issues or complaints.
"""

from analytics_models import KPI

AVERAGE_ISSUE_RESOLUTION_TIME = KPI(
    name="Average Issue Resolution Time",
    code="AVERAGE_ISSUE_RESOLUTION_TIME",
    category="Customer Retention",
    
    # Core Definition
    description="The average time taken to resolve customer issues or complaints.",
    kpi_definition="The average time taken to resolve customer issues or complaints.",
    expected_business_insights="Indicates the efficiency of the customer support team and impacts customer satisfaction levels.",
    measurement_approach="Measures the average time taken to resolve customer issues or support tickets.",
    
    # Formula
    formula="Sum of All Issue Resolution Times / Total Number of Issues Resolved",
    calculation_formula="Sum of All Issue Resolution Times / Total Number of Issues Resolved",
    
    # Analysis
    trend_analysis="""
    * An increasing average issue resolution time may indicate growing customer service workload or inefficiencies in the resolution process.
    * A decreasing resolution time can signal improved customer service processes or a decline in the volume of customer issues.
    """,
    diagnostic_questions="""
    * Are there specific types of customer issues that consistently take longer to resolve?
    * How does our average resolution time compare with industry benchmarks or customer expectations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement customer service training programs to improve issue resolution efficiency.
    * Leverage customer feedback to identify recurring issues and proactively address them.
    * Invest in customer service technology to streamline issue tracking and resolution processes.
    """,
    visualization_suggestions="""
    * Line charts showing the average resolution time over different time periods to identify trends.
    * Pareto charts to prioritize the types of customer issues that contribute most to the resolution time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long resolution times can lead to customer frustration and dissatisfaction, impacting retention and loyalty.
    * Consistently high resolution times may indicate systemic issues in customer service operations that need to be addressed.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with built-in case management and resolution tracking capabilities.
    * Workflow automation tools to streamline and standardize the issue resolution process.
    """,
    integration_points="""
    * Integrate average resolution time tracking with customer feedback systems to understand the impact of resolution time on satisfaction.
    * Link resolution time data with employee performance management systems to identify training or resource needs.
    """,
    change_impact_analysis="""
    * Improving resolution time can enhance customer satisfaction and loyalty, leading to increased customer lifetime value.
    * However, overly aggressive reduction targets may compromise issue quality and customer satisfaction.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Support Ticket"]
    }
)
