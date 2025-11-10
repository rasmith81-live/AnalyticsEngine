"""
Proposal Conversion Rate KPI

The percentage of proposals or quotes that result in a sale.
"""

from analytics_models import KPI

PROPOSAL_CONVERSION_RATE = KPI(
    name="Proposal Conversion Rate",
    code="PROPOSAL_CONVERSION_RATE",
    category="Sales Development",
    
    # Core Definition
    description="The percentage of proposals or quotes that result in a sale.",
    kpi_definition="The percentage of proposals or quotes that result in a sale.",
    expected_business_insights="Provides insight into the effectiveness of proposal content and sales follow-up strategies.",
    measurement_approach="Measures the percentage of proposals that result in a sale.",
    
    # Formula
    formula="(Total Number of Sales / Total Number of Proposals Sent) * 100",
    calculation_formula="(Total Number of Sales / Total Number of Proposals Sent) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing proposal conversion rate may indicate improved sales strategies or a higher quality of leads.
    * A decreasing rate could signal issues with the sales process, pricing, or product quality.
    """,
    diagnostic_questions="""
    * Are there specific products or services with consistently high or low proposal conversion rates?
    * How does our proposal conversion rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide sales teams with additional training and resources to improve their ability to close deals.
    * Regularly review and update pricing strategies to ensure competitiveness and value perception.
    * Implement customer feedback mechanisms to understand reasons for lost proposals and address any recurring issues.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of proposal conversion rates over time.
    * Pie charts to compare proposal conversion rates for different products or services.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low proposal conversion rate may lead to decreased revenue and market share.
    * An excessively high conversion rate may indicate underpricing or missed revenue opportunities.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze proposal outcomes.
    * Sales enablement platforms to provide sales teams with the necessary resources and content for effective selling.
    """,
    integration_points="""
    * Integrate proposal conversion rate data with marketing analytics to understand the quality of leads generated.
    * Link with customer relationship management systems to track the entire sales process from lead to conversion.
    """,
    change_impact_analysis="""
    * Improving the proposal conversion rate can lead to increased revenue and customer satisfaction.
    * However, a significant increase in conversion rate may also lead to capacity constraints and the need for additional resources to fulfill orders.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT", "SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lead", "Lost Sale", "Opportunity", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
