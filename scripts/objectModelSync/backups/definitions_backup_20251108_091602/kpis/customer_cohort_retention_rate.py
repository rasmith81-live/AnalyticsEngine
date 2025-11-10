"""
Customer Cohort Retention Rate KPI

The retention rate of specific customer cohorts over time, which can highlight trends or patterns in customer loyalty.
"""

from analytics_models import KPI

CUSTOMER_COHORT_RETENTION_RATE = KPI(
    name="Customer Cohort Retention Rate",
    code="CUSTOMER_COHORT_RETENTION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The retention rate of specific customer cohorts over time, which can highlight trends or patterns in customer loyalty.",
    kpi_definition="The retention rate of specific customer cohorts over time, which can highlight trends or patterns in customer loyalty.",
    expected_business_insights="Offers detailed insights into how retention varies among different customer groups, guiding targeted retention strategies.",
    measurement_approach="Measures the retention rate of a specific group or cohort of customers over a given period.",
    
    # Formula
    formula="(Number of Customers Remaining from a Cohort / Total Number of Customers in the Cohort at the Start of the Period) * 100",
    calculation_formula="(Number of Customers Remaining from a Cohort / Total Number of Customers in the Cohort at the Start of the Period) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing customer cohort retention rate may indicate improved customer satisfaction or loyalty programs.
    * A decreasing rate could signal issues with product quality, customer service, or competitive pressures.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or product lines that are experiencing higher or lower retention rates?
    * How does our customer cohort retention rate compare with industry benchmarks or seasonal fluctuations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement targeted customer retention strategies based on customer segmentation and preferences.
    * Enhance product quality, customer service, and overall customer experience to improve retention rates.
    * Regularly communicate with customers to gather feedback and address any issues proactively.
    """,
    visualization_suggestions="""
    * Line charts showing the retention rate trends for different customer cohorts over time.
    * Cohort analysis graphs to compare the retention rates of different customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer cohort retention rates can lead to decreased revenue and market share.
    * Consistently declining retention rates may indicate fundamental issues with the product or service offering.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer interactions and feedback.
    * Customer survey tools to gather insights on customer satisfaction and loyalty.
    """,
    integration_points="""
    * Integrate customer cohort retention data with marketing automation platforms to personalize customer communication and engagement.
    * Link retention rate analysis with sales and product development processes to align offerings with customer needs and preferences.
    """,
    change_impact_analysis="""
    * Improving customer cohort retention can lead to increased customer lifetime value and positive word-of-mouth referrals.
    * Conversely, declining retention rates can impact overall sales performance and brand reputation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Loyalty Program", "Opportunity"]
    }
)
