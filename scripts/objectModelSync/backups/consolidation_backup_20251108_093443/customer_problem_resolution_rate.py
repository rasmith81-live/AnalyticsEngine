"""
Customer Problem Resolution Rate KPI

The percentage of customer issues that are resolved to the customer's satisfaction.
"""

from analytics_models import KPI

CUSTOMER_PROBLEM_RESOLUTION_RATE = KPI(
    name="Customer Problem Resolution Rate",
    code="CUSTOMER_PROBLEM_RESOLUTION_RATE",
    category="Sales Operations",
    
    # Core Definition
    description="The percentage of customer issues that are resolved to the customer\'s satisfaction.",
    kpi_definition="The percentage of customer issues that are resolved to the customer\'s satisfaction.",
    expected_business_insights="Indicates the efficiency and effectiveness of customer service and support teams.",
    measurement_approach="Measures the percentage of customer issues that are resolved within a set timeframe.",
    
    # Formula
    formula="(Number of Problems Resolved / Total Number of Problems Reported) * 100",
    calculation_formula="(Number of Problems Resolved / Total Number of Problems Reported) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer problem resolution rate may indicate improved customer service processes or better product quality.
    * A decreasing rate could signal issues with customer support or product reliability.
    """,
    diagnostic_questions="""
    * Are there common themes or patterns in the types of customer issues that are being resolved?
    * How does our customer problem resolution rate compare with industry benchmarks or customer satisfaction surveys?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in customer service training to improve the skills of support staff.
    * Implement a customer feedback system to quickly identify and address recurring issues.
    * Regularly review and update product documentation and FAQs to reduce customer confusion and issues.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer problem resolution rate over time.
    * Pareto charts to identify the most common types of customer issues and their resolution rates.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low customer problem resolution rate can lead to customer churn and negative word-of-mouth.
    * Consistently high resolution rates may indicate that the organization is not capturing and addressing all customer issues effectively.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage customer issues and resolutions.
    * Customer feedback and survey tools to gather insights on customer satisfaction and issue resolution.
    """,
    integration_points="""
    * Integrate customer problem resolution rate with customer satisfaction metrics to understand the overall impact on customer experience.
    * Link with product development and quality assurance processes to address recurring issues at the source.
    """,
    change_impact_analysis="""
    * Improving the customer problem resolution rate can lead to increased customer loyalty and positive brand reputation.
    * However, focusing solely on resolution rate may neglect the root causes of customer issues, leading to potential long-term negative impact on the business.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
