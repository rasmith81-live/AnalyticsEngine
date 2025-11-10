"""
Customer Success Software Adoption Rate KPI

The rate at which customer success software tools are adopted and effectively used by the team.
"""

from analytics_models import KPI

CUSTOMER_SUCCESS_SOFTWARE_ADOPTION_RATE = KPI(
    name="Customer Success Software Adoption Rate",
    code="CUSTOMER_SUCCESS_SOFTWARE_ADOPTION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The rate at which customer success software tools are adopted and effectively used by the team.",
    kpi_definition="The rate at which customer success software tools are adopted and effectively used by the team.",
    expected_business_insights="Indicates the relevance and usability of software solutions intended to enhance customer success.",
    measurement_approach="Tracks the percentage of customers who adopt and use the customer success software tools provided by the company.",
    
    # Formula
    formula="(Number of Customers Using the Software / Total Number of Customers) * 100",
    calculation_formula="(Number of Customers Using the Software / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing adoption rate may indicate better training and support for the customer success software tools.
    * A decreasing rate could signal resistance to change or a lack of perceived value in the software.
    """,
    diagnostic_questions="""
    * Are there specific features of the software that are underutilized or causing frustration for the team?
    * How does the adoption rate compare with industry benchmarks or with the initial goals set for implementation?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional training and resources to help users understand the benefits and best practices of the software.
    * Seek feedback from the team to identify any barriers to adoption and address them proactively.
    * Highlight success stories and use cases to demonstrate the positive impact of the software on the team\'s performance.
    """,
    visualization_suggestions="""
    * Line charts showing the adoption rate over time to identify any spikes or dips in usage.
    * Comparison charts to visualize the adoption rate across different teams or departments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low adoption rates may lead to inefficiencies and missed opportunities for leveraging the software\'s capabilities.
    * Resistance to using the software could indicate broader issues with change management or communication within the organization.
    """,
    tracking_tools="""
    * Customer success platforms like Gainsight or Totango to track and analyze user engagement with the software.
    * Collaboration tools such as Slack or Microsoft Teams to facilitate communication and knowledge sharing around the software.
    """,
    integration_points="""
    * Integrate adoption rate data with performance reviews and goal setting to align individual objectives with software utilization.
    * Link adoption rate metrics with customer feedback and satisfaction scores to understand the impact of the software on overall success.
    """,
    change_impact_analysis="""
    * Improving the adoption rate can lead to better customer retention and increased upsell opportunities.
    * On the other hand, low adoption rates may result in missed opportunities for proactive customer engagement and support.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product Adoption", "Sales Team"]
    }
)
