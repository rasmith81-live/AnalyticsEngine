"""
Channel Sales Growth KPI

The year-over-year growth in revenue from channel partner sales.
"""

CHANNEL_SALES_GROWTH = {
    "code": "CHANNEL_SALES_GROWTH",
    "name": "Channel Sales Growth",
    "description": "The year-over-year growth in revenue from channel partner sales.",
    "formula": "((Current Period Channel Sales - Previous Period Channel Sales) / Previous Period Channel Sales) * 100",
    "calculation_formula": "((Current Period Channel Sales - Previous Period Channel Sales) / Previous Period Channel Sales) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The year-over-year growth in revenue from channel partner sales.",
    "expected_business_insights": "Reflects the performance and scaling of the channel sales strategy over time.",
    "measurement_approach": "Measures the percentage increase in sales made through channel partners over a given period.",
    "trend_analysis": """
    * Channel Sales Growth tends to show seasonal fluctuations, with higher growth during peak sales periods and lower growth during off-peak times.
    * An overall upward trend in Channel Sales Growth may indicate successful partner recruitment and enablement, while a downward trend could signal issues with partner performance or market saturation.
    """,
    "diagnostic_questions": """
    * What specific products or services are driving the most growth through channel partners?
    * Are there any common factors among underperforming channel partners that could be addressed to improve overall growth?
    """,
    "actionable_tips": """
    * Invest in targeted partner training and enablement programs to improve sales effectiveness.
    * Regularly review and optimize the partner portfolio to ensure alignment with market demand and company objectives.
    * Implement incentive programs to motivate and reward high-performing channel partners.
    """,
    "visualization_suggestions": """
    * Line charts showing year-over-year revenue growth from channel sales.
    * Pie charts illustrating the contribution of different partners or regions to overall channel sales growth.
    """,
    "risk_warnings": """
    * Over-reliance on a small number of channel partners may create vulnerability to market changes or partner performance issues.
    * Insufficient support for channel partners could lead to missed sales opportunities and decreased overall growth.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) systems to track and manage partner interactions and performance.
    * Partner Relationship Management (PRM) platforms to streamline partner communication and collaboration.
    """,
    "integration_points": """
    * Integrate Channel Sales Growth data with overall sales performance metrics to gain a comprehensive view of revenue generation.
    * Link Channel Sales Growth with marketing analytics to assess the effectiveness of partner-focused marketing efforts.
    """,
    "change_impact_analysis": """
    * Improving Channel Sales Growth can lead to increased market share and revenue, but may also require additional resources for partner support and management.
    * A decline in Channel Sales Growth could impact overall company performance and market competitiveness, especially if direct sales are not able to compensate for the decrease.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
