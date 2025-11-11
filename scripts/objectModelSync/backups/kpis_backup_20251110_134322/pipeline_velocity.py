"""
Pipeline Velocity KPI

The speed at which deals move through the sales pipeline.
"""

PIPELINE_VELOCITY = {
    "code": "PIPELINE_VELOCITY",
    "name": "Pipeline Velocity",
    "description": "The speed at which deals move through the sales pipeline.",
    "formula": "(Number of Opportunities * Deal Size * Conversion Rate) / Length of Sales Cycle",
    "calculation_formula": "(Number of Opportunities * Deal Size * Conversion Rate) / Length of Sales Cycle",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The speed at which deals move through the sales pipeline.",
    "expected_business_insights": "Provides insights into the efficiency of the sales process and can inform strategies for improvement.",
    "measurement_approach": "Calculates the speed at which deals move through the sales pipeline and generate revenue.",
    "trend_analysis": """
    * Increasing pipeline velocity may indicate improved sales processes or higher demand for products/services.
    * Decreasing velocity could signal inefficiencies in the sales pipeline or a decline in market interest.
    """,
    "diagnostic_questions": """
    * Are there specific stages in the sales pipeline where deals tend to get stuck?
    * How does our pipeline velocity compare with industry benchmarks or historical data?
    """,
    "actionable_tips": """
    * Implement sales automation tools to streamline the sales process and reduce bottlenecks.
    * Provide additional training and support for sales representatives to improve their efficiency and effectiveness.
    * Regularly review and optimize the sales pipeline stages to remove any unnecessary steps or delays.
    """,
    "visualization_suggestions": """
    * Line charts showing the average time deals spend in each stage of the pipeline over time.
    * Funnel charts to visualize the drop-off rates at each stage of the sales pipeline.
    """,
    "risk_warnings": """
    * High pipeline velocity without proper qualification may lead to an increase in unqualified leads and wasted resources.
    * Excessively low velocity may result in missed sales opportunities and revenue targets.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track and manage the sales pipeline.
    * Sales performance analytics tools to identify bottlenecks and areas for improvement.
    """,
    "integration_points": """
    * Integrate pipeline velocity data with marketing analytics to align sales and marketing efforts more effectively.
    * Link with customer support systems to understand how post-sales activities impact pipeline velocity.
    """,
    "change_impact_analysis": """
    * Increasing pipeline velocity may lead to higher sales volume but could also strain resources if not managed effectively.
    * Decreasing velocity may indicate a need for process improvement but could also impact revenue and market share.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Lead", "Opportunity", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
}
