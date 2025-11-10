"""
Customer Incident Rate KPI

The frequency at which customers encounter issues or problems with the company's products or services.
"""

from analytics_models import KPI

CUSTOMER_INCIDENT_RATE = KPI(
    name="Customer Incident Rate",
    code="CUSTOMER_INCIDENT_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The frequency at which customers encounter issues or problems with the company\'s products or services.",
    kpi_definition="The frequency at which customers encounter issues or problems with the company\'s products or services.",
    expected_business_insights="Indicates the reliability of the product or service and the effectiveness of support operations.",
    measurement_approach="Tracks the number of support or service incidents reported by customers within a given timeframe.",
    
    # Formula
    formula="Total Number of Incidents Reported / Total Number of Customers",
    calculation_formula="Total Number of Incidents Reported / Total Number of Customers",
    
    # Analysis
    trend_analysis="""
    * An increasing customer incident rate may indicate declining product quality or service levels.
    * A decreasing rate could signal improved customer support or product enhancements.
    """,
    diagnostic_questions="""
    * Are there specific products or services that are consistently causing customer incidents?
    * How does our customer incident rate compare with industry standards or benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in customer service training to address and resolve issues more effectively.
    * Regularly gather and analyze customer feedback to identify areas for improvement.
    * Implement proactive communication strategies to manage customer expectations and prevent incidents.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer incident rates over time.
    * Pareto charts to identify the most common types of customer incidents.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High customer incident rates can lead to customer churn and negative word-of-mouth.
    * Consistently high incident rates may indicate systemic issues that could damage the company\'s reputation.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage customer incidents.
    * Quality management systems to identify and address root causes of customer incidents.
    """,
    integration_points="""
    * Integrate customer incident data with product development processes to prioritize improvements.
    * Link customer incident tracking with customer satisfaction surveys to understand the impact of incidents on overall satisfaction.
    """,
    change_impact_analysis="""
    * Reducing customer incident rates can lead to higher customer retention and loyalty.
    * However, addressing customer incidents may require increased resources and operational costs.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Sales Representative", "Service Level Agreement", "Support Ticket"]
    }
)
