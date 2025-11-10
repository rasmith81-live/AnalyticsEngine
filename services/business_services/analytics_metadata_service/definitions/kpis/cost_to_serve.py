"""
Cost to Serve KPI

The total cost associated with serving a particular customer or account.
"""

from analytics_models import KPI

COST_TO_SERVE = KPI(
    name="Cost to Serve",
    code="COST_TO_SERVE",
    category="Key Account Management",
    
    # Core Definition
    description="The total cost associated with serving a particular customer or account.",
    kpi_definition="The total cost associated with serving a particular customer or account.",
    expected_business_insights="Provides insights into profitability and efficiency, identifying key areas where cost savings can be made without affecting service quality.",
    measurement_approach="Calculates the total cost associated with servicing a particular customer or account.",
    
    # Formula
    formula="Total Costs to Serve Customer / Total Number of Customers",
    calculation_formula="Total Costs to Serve Customer / Total Number of Customers",
    
    # Analysis
    trend_analysis="""
    * The cost to serve may increase over time due to rising operational costs or changes in customer demands.
    * A decreasing cost to serve could indicate improved efficiency in serving customers or better negotiation with suppliers.
    """,
    diagnostic_questions="""
    * What are the main cost drivers for serving this particular customer or account?
    * Are there any inefficiencies in our current processes that are contributing to a higher cost to serve?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement cost-saving measures such as optimizing delivery routes or consolidating orders.
    * Negotiate better terms with suppliers or explore alternative sourcing options to reduce costs.
    * Regularly review and update pricing strategies to ensure profitability while remaining competitive.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of cost to serve over time.
    * Pie charts to visualize the breakdown of costs by category (e.g., transportation, handling, customer-specific services).
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High cost to serve may erode profit margins and impact overall business profitability.
    * Failure to address increasing costs could lead to loss of competitiveness in the market.
    """,
    tracking_tools="""
    * Enterprise resource planning (ERP) systems to track and analyze costs associated with serving customers.
    * Customer relationship management (CRM) software to understand customer needs and preferences, leading to more efficient and cost-effective service.
    """,
    integration_points="""
    * Integrate cost to serve data with financial systems to understand the impact on overall business performance.
    * Link cost to serve metrics with customer satisfaction data to identify areas for improvement.
    """,
    change_impact_analysis="""
    * Reducing the cost to serve may positively impact profitability, but it could also require initial investment in process improvements or technology.
    * Increased cost to serve may lead to higher prices for customers, potentially impacting customer retention and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Sale"]
    }
)
