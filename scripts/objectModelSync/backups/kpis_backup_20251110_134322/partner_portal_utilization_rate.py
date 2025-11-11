"""
Partner Portal Utilization Rate KPI

The rate at which channel partners utilize the provided partner portal, which can indicate engagement and the portal's usefulness.
"""

PARTNER_PORTAL_UTILIZATION_RATE = {
    "code": "PARTNER_PORTAL_UTILIZATION_RATE",
    "name": "Partner Portal Utilization Rate",
    "description": "The rate at which channel partners utilize the provided partner portal, which can indicate engagement and the portal's usefulness.",
    "formula": "(Number of Active Users / Total Number of Partner Users) * 100",
    "calculation_formula": "(Number of Active Users / Total Number of Partner Users) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The rate at which channel partners utilize the provided partner portal, which can indicate engagement and the portal's usefulness.",
    "expected_business_insights": "Indicates the effectiveness and relevance of the partner portal as a tool for partner engagement and enablement.",
    "measurement_approach": "Tracks the frequency and extent of use of the partner portal for resources, training, and communication.",
    "trend_analysis": """
    * An increasing partner portal utilization rate may indicate improved partner engagement and satisfaction with the portal's resources.
    * A decreasing rate could signal a lack of awareness or dissatisfaction with the portal's content and functionality.
    """,
    "diagnostic_questions": """
    * Are there specific features or resources within the partner portal that are underutilized?
    * How does the partner portal utilization rate compare with industry benchmarks or with the introduction of new portal features?
    """,
    "actionable_tips": """
    * Regularly gather feedback from channel partners to understand their needs and preferences for portal content and tools.
    * Provide training and support to ensure partners are aware of and know how to effectively use the portal's resources.
    * Continuously update and improve the portal based on partner feedback and usage analytics.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of partner portal utilization rate over time.
    * Pie charts to visually represent the distribution of portal utilization across different partner segments or regions.
    """,
    "risk_warnings": """
    * A consistently low partner portal utilization rate may indicate a need for a complete overhaul of the portal's content and functionality.
    * High utilization in certain areas of the portal but low utilization in others could lead to uneven partner engagement and satisfaction.
    """,
    "tracking_tools": """
    * Partner relationship management (PRM) software to track and analyze partner interactions with the portal.
    * Content management systems to efficiently update and organize portal resources based on partner needs.
    """,
    "integration_points": """
    * Integrate partner portal utilization data with sales performance metrics to understand the impact of portal engagement on overall sales results.
    * Link portal utilization with partner training and certification systems to identify correlations between training completion and increased portal usage.
    """,
    "change_impact_analysis": """
    * Improving partner portal utilization can lead to better collaboration, increased sales, and stronger partner relationships.
    * However, changes in portal content or structure may initially disrupt partner workflows and require adaptation.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Lead", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Prospect Engagement", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
