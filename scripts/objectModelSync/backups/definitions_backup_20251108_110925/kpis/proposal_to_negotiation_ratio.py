"""
Proposal-to-Negotiation Ratio KPI

The ratio of proposals given to the number of negotiations started with potential customers.
"""

from analytics_models import KPI

PROPOSAL_TO_NEGOTIATION_RATIO = KPI(
    name="Proposal-to-Negotiation Ratio",
    code="PROPOSAL_TO_NEGOTIATION_RATIO",
    category="Outside Sales",
    
    # Core Definition
    description="The ratio of proposals given to the number of negotiations started with potential customers.",
    kpi_definition="The ratio of proposals given to the number of negotiations started with potential customers.",
    expected_business_insights="Indicates the sales team’s effectiveness in moving potential clients from proposal to negotiation stage.",
    measurement_approach="Compares the number of proposals sent to the number of negotiations that ensue.",
    
    # Formula
    formula="Number of Negotiations / Number of Proposals Sent * 100",
    calculation_formula="Number of Negotiations / Number of Proposals Sent * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing proposal-to-negotiation ratio may indicate that the sales team is becoming more effective at qualifying potential customers before entering negotiations.
    * A decreasing ratio could signal that the sales team is struggling to move potential customers from the proposal stage to negotiation, possibly due to ineffective proposals or lack of follow-up.
    """,
    diagnostic_questions="""
    * Are there specific factors that tend to result in successful negotiations after a proposal is given?
    * What feedback have potential customers provided about the proposals, and how can we use that feedback to improve our approach?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide sales training to improve the quality and effectiveness of proposals.
    * Implement a follow-up process to ensure that proposals are not left unaddressed and to gather feedback for improvement.
    * Analyze successful negotiations to identify common factors and incorporate them into the proposal process.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of the ratio over time to identify any consistent patterns or changes.
    * Stacked bar charts comparing the ratio across different sales representatives or regions to identify potential areas for improvement.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low proposal-to-negotiation ratio may indicate a need for more targeted lead generation or a review of the qualification process.
    * A high ratio could lead to missed opportunities if potential customers are not being effectively moved towards negotiation.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track the status of proposals and negotiations with potential customers.
    * Sales enablement platforms to create and manage high-quality, effective proposals.
    """,
    integration_points="""
    * Integrate the proposal-to-negotiation ratio with lead generation and qualification processes to ensure a consistent and effective sales pipeline.
    * Link the ratio with customer feedback systems to gather insights on the effectiveness of proposals and areas for improvement.
    """,
    change_impact_analysis="""
    * An improved proposal-to-negotiation ratio can lead to more efficient use of sales resources and potentially higher conversion rates.
    * However, a significant change in the ratio may require adjustments in sales strategies and resource allocation, potentially impacting short-term sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Proposal", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
