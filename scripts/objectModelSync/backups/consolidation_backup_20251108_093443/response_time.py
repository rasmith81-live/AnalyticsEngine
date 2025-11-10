"""
Response Time KPI

The amount of time it takes for the Customer Success Team to respond to a customer inquiry or request for assistance. This KPI measures the team's efficiency in handling customer issues.
"""

from analytics_models import KPI

RESPONSE_TIME = KPI(
    name="Response Time",
    code="RESPONSE_TIME",
    category="Customer Success",
    
    # Core Definition
    description="The amount of time it takes for the Customer Success Team to respond to a customer inquiry or request for assistance. This KPI measures the team\'s efficiency in handling customer issues.",
    kpi_definition="The amount of time it takes for the Customer Success Team to respond to a customer inquiry or request for assistance. This KPI measures the team\'s efficiency in handling customer issues.",
    expected_business_insights="Assesses the speed and efficiency of the customer support team, impacting customer satisfaction.",
    measurement_approach="Measures the average time taken to respond to customer inquiries across various communication channels.",
    
    # Formula
    formula="Average Time Between Customer Inquiry and Response",
    calculation_formula="Average Time Between Customer Inquiry and Response",
    
    # Analysis
    trend_analysis="""
    * Increasing response times may indicate a growing workload for the Customer Success Team or inefficiencies in the support process.
    * Decreasing response times can signal improved team productivity, better resource allocation, or enhanced communication channels.
    """,
    diagnostic_questions="""
    * Are there specific types of customer inquiries that consistently take longer to address?
    * How do response times vary across different channels of customer communication (e.g., email, phone, chat)?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement automated ticketing systems to prioritize and route customer inquiries more efficiently.
    * Provide ongoing training and coaching to the Customer Success Team to enhance their problem-solving and communication skills.
    * Regularly review and optimize the customer support workflow to identify and eliminate bottlenecks.
    """,
    visualization_suggestions="""
    * Line charts showing the average response time over time to identify trends and seasonality.
    * Stacked bar charts comparing response times across different customer support channels.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long response times can lead to customer frustration, dissatisfaction, and potential churn.
    * Inconsistent or excessively short response times may indicate rushed or incomplete issue resolution, impacting customer satisfaction.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software with built-in ticketing and response time tracking capabilities.
    * Helpdesk platforms that offer automation, routing, and reporting features to streamline customer support operations.
    """,
    integration_points="""
    * Integrate response time data with customer feedback systems to understand the correlation between response times and customer satisfaction.
    * Link response time metrics with employee performance evaluations to incentivize timely and effective customer support.
    """,
    change_impact_analysis="""
    * Improving response times can enhance customer loyalty and retention, leading to increased customer lifetime value.
    * However, overly aggressive targets for response times may result in increased stress and burnout among customer support staff.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Team", "Support Ticket"]
    }
)
