"""
Customer Meeting Frequency KPI

The frequency at which meetings are held between the customer success team and individual customers.
"""

from analytics_models import KPI

CUSTOMER_MEETING_FREQUENCY = KPI(
    name="Customer Meeting Frequency",
    code="CUSTOMER_MEETING_FREQUENCY",
    category="Customer Success",
    
    # Core Definition
    description="The frequency at which meetings are held between the customer success team and individual customers.",
    kpi_definition="The frequency at which meetings are held between the customer success team and individual customers.",
    expected_business_insights="Indicates the level of personal attention and proactive engagement provided to customers.",
    measurement_approach="Measures the average number of times the customer success team meets with customers within a given period.",
    
    # Formula
    formula="Total Number of Customer Meetings / Total Number of Customers",
    calculation_formula="Total Number of Customer Meetings / Total Number of Customers",
    
    # Analysis
    trend_analysis="""
    * An increasing customer meeting frequency may indicate proactive customer engagement and a focus on building strong relationships.
    * A decreasing frequency could signal potential disengagement or dissatisfaction among customers, requiring immediate attention and intervention.
    """,
    diagnostic_questions="""
    * Are there specific customers or customer segments that have seen a decline in meeting frequency?
    * How does the meeting frequency align with customer satisfaction scores or feedback?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a structured customer success plan that includes regular touchpoints and check-ins.
    * Utilize customer relationship management (CRM) software to track and schedule customer meetings efficiently.
    * Encourage proactive communication and outreach from the customer success team to maintain a consistent meeting frequency.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of meeting frequency over time for individual customers or customer segments.
    * Comparison bar graphs to analyze meeting frequency across different customer success managers or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low meeting frequency may lead to customer churn or reduced lifetime value of customers.
    * Inconsistent or infrequent meetings can result in missed opportunities for upselling or cross-selling products or services.
    """,
    tracking_tools="""
    * CRM platforms like Salesforce or HubSpot for scheduling and tracking customer meetings.
    * Customer success management software such as Gainsight or Totango for comprehensive customer engagement and success planning.
    """,
    integration_points="""
    * Integrate meeting frequency data with customer feedback and satisfaction metrics to gain a holistic view of customer engagement.
    * Link meeting frequency with sales and revenue data to understand the impact of customer engagement on business performance.
    """,
    change_impact_analysis="""
    * Increasing meeting frequency may lead to higher customer retention and loyalty, positively impacting overall sales and revenue.
    * However, a significant increase in meeting frequency without proper alignment with customer needs and goals could lead to resource inefficiency and increased operational costs.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Meeting", "Sales Team"]
    }
)
