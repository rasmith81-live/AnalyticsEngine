"""
Customer Enablement Success Rate KPI

The success rate of customer enablement efforts, assessing how well customers are equipped to use the product or service.
"""

from analytics_models import KPI

CUSTOMER_ENABLEMENT_SUCCESS_RATE = KPI(
    name="Customer Enablement Success Rate",
    code="CUSTOMER_ENABLEMENT_SUCCESS_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The success rate of customer enablement efforts, assessing how well customers are equipped to use the product or service.",
    kpi_definition="The success rate of customer enablement efforts, assessing how well customers are equipped to use the product or service.",
    expected_business_insights="Shows the effectiveness of customer enablement strategies and resources in supporting customer success.",
    measurement_approach="Tracks the percentage of customers who successfully use resources and tools provided to them to achieve their goals.",
    
    # Formula
    formula="(Number of Customers Who Achieve Their Goals with Enablement Tools / Total Number of Customers Using the Tools) * 100",
    calculation_formula="(Number of Customers Who Achieve Their Goals with Enablement Tools / Total Number of Customers Using the Tools) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer enablement success rate may indicate improved onboarding processes or enhanced customer training programs.
    * A decreasing rate could signal issues with product complexity, lack of customer support, or ineffective training methods.
    """,
    diagnostic_questions="""
    * Are there specific features or aspects of the product that customers struggle to understand or utilize?
    * How does our customer enablement success rate compare with industry benchmarks or customer feedback?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in creating comprehensive and easily accessible product documentation and tutorials.
    * Provide ongoing customer support and training to address any usage challenges or questions.
    * Gather feedback from customers to continuously improve and tailor enablement efforts to their needs.
    """,
    visualization_suggestions="""
    * Line charts showing the customer enablement success rate over time.
    * Stacked bar graphs comparing success rates across different customer segments or product versions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low customer enablement success rate can lead to customer frustration and increased support requests.
    * Inadequate product understanding may result in underutilization and reduced customer satisfaction.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track customer interactions and training history.
    * Learning management systems (LMS) for creating and managing customer training materials.
    """,
    integration_points="""
    * Integrate customer enablement success rate data with customer satisfaction metrics to understand the impact of enablement efforts on overall satisfaction.
    * Link with product development and marketing teams to align enablement efforts with product updates and customer communication.
    """,
    change_impact_analysis="""
    * Improving customer enablement success can lead to higher product adoption and customer retention.
    * However, increased focus on customer enablement may require additional resources and time investment.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Enablement Platform", "Goal", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]
    }
)
