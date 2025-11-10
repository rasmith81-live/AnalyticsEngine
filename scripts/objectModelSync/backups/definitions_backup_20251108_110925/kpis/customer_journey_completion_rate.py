"""
Customer Journey Completion Rate KPI

The percentage of customers completing the intended journey or experience designed by the company.
"""

from analytics_models import KPI

CUSTOMER_JOURNEY_COMPLETION_RATE = KPI(
    name="Customer Journey Completion Rate",
    code="CUSTOMER_JOURNEY_COMPLETION_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of customers completing the intended journey or experience designed by the company.",
    kpi_definition="The percentage of customers completing the intended journey or experience designed by the company.",
    expected_business_insights="Indicates the effectiveness of the customer journey design and can point to barriers in the experience.",
    measurement_approach="Measures the percentage of customers who complete the intended journey or achieve a specific goal.",
    
    # Formula
    formula="(Number of Customers Completing the Journey / Total Number of Customers Starting the Journey) * 100",
    calculation_formula="(Number of Customers Completing the Journey / Total Number of Customers Starting the Journey) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer journey completion rate may indicate improved customer experience or more effective sales processes.
    * A decreasing rate could signal issues with product quality, customer service, or marketing effectiveness.
    """,
    diagnostic_questions="""
    * Are there specific touchpoints in the customer journey where a drop-off in completion occurs?
    * How does our customer journey completion rate compare with industry benchmarks or with our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Conduct customer journey mapping to identify pain points and optimize the experience.
    * Provide additional training and resources to sales and customer service teams to ensure they can effectively guide customers through the journey.
    * Implement feedback mechanisms to capture customer insights and improve the journey based on their input.
    """,
    visualization_suggestions="""
    * Funnel charts to visualize the drop-off at each stage of the customer journey.
    * Line graphs to track the trend of completion rates over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low completion rates can lead to lost sales and reduced customer loyalty.
    * Consistently high completion rates may indicate a lack of challenge or engagement in the customer journey, potentially leading to complacency or disinterest.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track customer interactions and identify areas for improvement.
    * Analytics tools to monitor and analyze customer behavior throughout the journey.
    """,
    integration_points="""
    * Integrate customer journey completion data with marketing automation platforms to personalize and optimize the journey for different customer segments.
    * Link completion rate with sales performance metrics to understand the impact on revenue and customer acquisition costs.
    """,
    change_impact_analysis="""
    * Improving the customer journey completion rate can lead to increased customer satisfaction and loyalty, potentially impacting long-term revenue and profitability.
    * However, changes in the completion rate may also affect sales team workload and resource allocation, requiring adjustments in sales management strategies.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager"]
    }
)
