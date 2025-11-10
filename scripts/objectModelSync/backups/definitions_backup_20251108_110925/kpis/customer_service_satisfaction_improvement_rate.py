"""
Customer Service Satisfaction Improvement Rate KPI

The rate of improvement in customer satisfaction scores over time.
"""

from analytics_models import KPI

CUSTOMER_SERVICE_SATISFACTION_IMPROVEMENT_RATE = KPI(
    name="Customer Service Satisfaction Improvement Rate",
    code="CUSTOMER_SERVICE_SATISFACTION_IMPROVEMENT_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The rate of improvement in customer satisfaction scores over time.",
    kpi_definition="The rate of improvement in customer satisfaction scores over time.",
    expected_business_insights="Indicates how service changes are perceived by customers and if service quality is improving.",
    measurement_approach="Measures the change in customer satisfaction with service over time.",
    
    # Formula
    formula="(Current Period CSAT - Previous Period CSAT) / Previous Period CSAT",
    calculation_formula="(Current Period CSAT - Previous Period CSAT) / Previous Period CSAT",
    
    # Analysis
    trend_analysis="""
    * An increasing customer service satisfaction improvement rate may indicate better customer service training or improved processes.
    * A decreasing rate could signal issues with customer service quality or communication.
    """,
    diagnostic_questions="""
    * Are there specific areas or touchpoints where customers consistently report lower satisfaction?
    * How does our customer service satisfaction improvement rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in ongoing training and development for customer service teams.
    * Implement feedback mechanisms to capture customer sentiment and identify areas for improvement.
    * Regularly review and update customer service processes based on feedback and performance data.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer satisfaction improvement over time.
    * Pie charts to visualize the distribution of satisfaction scores across different touchpoints or channels.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer service satisfaction improvement rates can lead to customer churn and negative word-of-mouth.
    * Consistently high improvement rates may indicate a lack of granularity in the measurement, potentially masking specific areas that need attention.
    """,
    tracking_tools="""
    * Customer feedback and survey tools like SurveyMonkey or Qualtrics to gather and analyze customer satisfaction data.
    * Customer relationship management (CRM) systems to track interactions and monitor customer service performance.
    """,
    integration_points="""
    * Integrate customer service satisfaction data with employee performance evaluations to align incentives with customer satisfaction goals.
    * Link customer service satisfaction metrics with sales data to understand the impact on customer retention and lifetime value.
    """,
    change_impact_analysis="""
    * Improving customer service satisfaction can lead to increased customer loyalty and repeat business.
    * However, focusing solely on improvement rates without considering the quality of service provided may lead to superficial improvements that do not address underlying issues.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Service Level Agreement"]
    }
)
