"""
Content Utilization Rate KPI

The rate at which sales enablement materials are used by the sales team in their sales process.
"""

CONTENT_UTILIZATION_RATE = {
    "code": "CONTENT_UTILIZATION_RATE",
    "name": "Content Utilization Rate",
    "description": "The rate at which sales enablement materials are used by the sales team in their sales process.",
    "formula": "(Number of Times Content is Used / Total Available Content Pieces) * 100",
    "calculation_formula": "(Number of Times Content is Used / Total Available Content Pieces) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The rate at which sales enablement materials are used by the sales team in their sales process.",
    "expected_business_insights": "Indicates the relevance and effectiveness of sales materials, and can help identify gaps in content provision.",
    "measurement_approach": "Measures how frequently sales collateral and content are used by the sales team.",
    "trend_analysis": """
    * Increasing content utilization rate may indicate better alignment of sales materials with customer needs.
    * Decreasing rate could signal a lack of awareness or training on available sales enablement resources.
    """,
    "diagnostic_questions": """
    * Are there specific sales enablement materials that are consistently underutilized?
    * How does the content utilization rate correlate with sales performance and conversion metrics?
    """,
    "actionable_tips": """
    * Regularly communicate the availability and benefits of sales enablement materials to the sales team.
    * Collect feedback from the sales team to understand their needs and preferences for sales enablement content.
    * Provide training and guidance on how to effectively use sales enablement materials in the sales process.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of content utilization rate over time.
    * Stacked bar charts comparing the utilization rates of different types of sales enablement materials.
    """,
    "risk_warnings": """
    * Low content utilization rate may lead to missed sales opportunities and decreased productivity.
    * High content utilization rate without corresponding sales performance improvements may indicate ineffective or irrelevant sales enablement materials.
    """,
    "tracking_tools": """
    * Sales enablement platforms like Seismic or Highspot for tracking and analyzing content utilization.
    * Customer relationship management (CRM) systems to link content utilization with sales outcomes.
    """,
    "integration_points": """
    * Integrate content utilization data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link content utilization with training and development programs to ensure alignment with sales strategies.
    """,
    "change_impact_analysis": """
    * Improving content utilization rate can lead to better customer engagement and higher conversion rates.
    * However, increasing the utilization rate without maintaining content quality can negatively impact the sales process and customer experience.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
