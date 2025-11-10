"""
Partner Loyalty Index KPI

A measure of the loyalty of channel partners, which can be determined through factors such as repeat business and long-term commitment.
"""

PARTNER_LOYALTY_INDEX = {
    "code": "PARTNER_LOYALTY_INDEX",
    "name": "Partner Loyalty Index",
    "description": "A measure of the loyalty of channel partners, which can be determined through factors such as repeat business and long-term commitment.",
    "formula": "Composite Score Based on Loyalty Metrics (e.g., NPS, Retention, Advocacy)",
    "calculation_formula": "Composite Score Based on Loyalty Metrics (e.g., NPS, Retention, Advocacy)",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "A measure of the loyalty of channel partners, which can be determined through factors such as repeat business and long-term commitment.",
    "expected_business_insights": "Reflects the strength of the partner relationship and predicts future collaboration and performance.",
    "measurement_approach": "Combines factors such as partner satisfaction, retention, and willingness to recommend the company.",
    "trend_analysis": """
    * An increasing partner loyalty index may indicate stronger relationships with channel partners and higher levels of trust and satisfaction.
    * A decreasing index could signal dissatisfaction, competition from other vendors, or changes in the partner's business strategy.
    """,
    "diagnostic_questions": """
    * What specific actions or programs have been implemented to strengthen relationships with channel partners?
    * Are there any recent changes in the market or industry that could be impacting partner loyalty?
    """,
    "actionable_tips": """
    * Regularly communicate with channel partners to understand their needs and challenges.
    * Provide training and support to help partners effectively sell and support your products or services.
    * Offer incentives or rewards for achieving sales targets and demonstrating loyalty.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of partner loyalty index over time.
    * Pie charts to compare the distribution of loyalty levels among different partners or regions.
    """,
    "risk_warnings": """
    * Low partner loyalty can lead to decreased sales and market share as partners may shift their focus to other vendors.
    * High partner turnover can result in increased costs associated with recruiting and training new partners.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) systems to track interactions and engagement with channel partners.
    * Partner Relationship Management (PRM) software to streamline partner communication and collaboration.
    """,
    "integration_points": """
    * Integrate partner loyalty data with sales performance metrics to understand the impact of partner relationships on overall sales results.
    * Link partner loyalty index with marketing efforts to align promotional activities with partner needs and preferences.
    """,
    "change_impact_analysis": """
    * Improving partner loyalty can lead to increased sales, market share, and brand advocacy.
    * Conversely, declining partner loyalty may result in decreased revenue and negative word-of-mouth, impacting overall business performance.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Loyalty Program", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
