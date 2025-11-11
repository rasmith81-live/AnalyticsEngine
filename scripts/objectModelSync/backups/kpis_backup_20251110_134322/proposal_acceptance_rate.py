"""
Proposal Acceptance Rate KPI

The percentage of proposals that are accepted by prospects or clients.
"""

PROPOSAL_ACCEPTANCE_RATE = {
    "code": "PROPOSAL_ACCEPTANCE_RATE",
    "name": "Proposal Acceptance Rate",
    "description": "The percentage of proposals that are accepted by prospects or clients.",
    "formula": "Number of Proposals Accepted / Total Number of Proposals Sent * 100",
    "calculation_formula": "Number of Proposals Accepted / Total Number of Proposals Sent * 100",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The percentage of proposals that are accepted by prospects or clients.",
    "expected_business_insights": "Reveals the effectiveness of proposal strategies and helps to identify areas for improvement in sales communications.",
    "measurement_approach": "Tracks the percentage of proposals that result in an agreement or sale.",
    "trend_analysis": """
    * An increasing proposal acceptance rate may indicate improved sales strategies or a growing demand for the product or service.
    * A decreasing rate could signal ineffective sales tactics, changes in market preferences, or increased competition.
    """,
    "diagnostic_questions": """
    * Are there specific sales representatives or teams with consistently higher or lower proposal acceptance rates?
    * What factors contribute to the acceptance or rejection of proposals, and how can those be addressed?
    """,
    "actionable_tips": """
    * Provide additional sales training and support to improve the quality and relevance of proposals.
    * Regularly review and update proposal templates and content to align with prospect needs and industry trends.
    * Implement a feedback loop to gather insights from rejected proposals and use that information to refine future proposals.
    """,
    "visualization_suggestions": """
    * Line charts showing the proposal acceptance rate over time to identify trends and seasonality.
    * Pie charts comparing acceptance rates by sales representative or by product/service category.
    """,
    "risk_warnings": """
    * A consistently low proposal acceptance rate can lead to missed revenue opportunities and decreased market share.
    * High acceptance rates without corresponding sales conversion may indicate overcommitment or unrealistic proposals.
    """,
    "tracking_tools": """
    * CRM systems like Salesforce or HubSpot to track proposal submissions and acceptance rates.
    * Proposal management software such as PandaDoc or Qwilr to streamline the creation and tracking of proposals.
    """,
    "integration_points": """
    * Integrate proposal acceptance data with sales performance metrics to understand the impact on overall revenue and customer acquisition costs.
    * Link with customer relationship management systems to analyze the correlation between accepted proposals and customer lifetime value.
    """,
    "change_impact_analysis": """
    * An improved proposal acceptance rate can lead to increased revenue and market share, but may also require adjustments in production or service delivery to meet demand.
    * Conversely, a declining acceptance rate may signal the need for product or service innovation, changes in pricing strategy, or adjustments in target markets.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lost Sale", "Partner Agreement", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]},
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
}
