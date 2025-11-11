"""
Sales Pipeline KPI

The total value of potential sales opportunities within the key accounts.
"""

SALES_PIPELINE = {
    "code": "SALES_PIPELINE",
    "name": "Sales Pipeline",
    "description": "The total value of potential sales opportunities within the key accounts.",
    "formula": "Listing of all active deals categorized by sales stage",
    "calculation_formula": "Listing of all active deals categorized by sales stage",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The total value of potential sales opportunities within the key accounts.",
    "expected_business_insights": "Provides a visual representation of sales prospects and potential revenue, aiding in sales forecasting and resource allocation.",
    "measurement_approach": "Tracks the number of deals in various stages of the sales process.",
    "trend_analysis": """
    * Increasing sales pipeline value may indicate successful lead generation and account expansion efforts.
    * A decreasing pipeline value could signal challenges in converting leads or retaining existing business.
    """,
    "diagnostic_questions": """
    * What is the average time it takes to move opportunities through the sales pipeline?
    * Are there specific stages in the pipeline where opportunities tend to stall or drop off?
    """,
    "actionable_tips": """
    * Implement a structured sales process to move opportunities through the pipeline more efficiently.
    * Provide targeted training and resources to sales teams to improve their ability to qualify and close opportunities.
    * Regularly review and update the sales pipeline to ensure it accurately reflects the current state of potential opportunities.
    """,
    "visualization_suggestions": """
    * Funnel charts to visualize the progression of opportunities through different stages of the pipeline.
    * Line graphs to track changes in pipeline value over time.
    """,
    "risk_warnings": """
    * A stagnant or declining sales pipeline value may lead to missed revenue targets and decreased market share.
    * An overly optimistic pipeline may result in resource allocation to opportunities that are unlikely to close.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track and manage opportunities within the pipeline.
    * Sales analytics tools to gain insights into the health and movement of the sales pipeline.
    """,
    "integration_points": """
    * Integrate the sales pipeline with marketing automation systems to ensure a steady flow of qualified leads.
    * Connect the pipeline with financial forecasting and resource planning systems to align sales targets with operational capabilities.
    """,
    "change_impact_analysis": """
    * Improving the sales pipeline can lead to increased revenue and market share, but may also require additional resources and investment in sales and marketing efforts.
    * A declining pipeline value can impact overall business performance and may require strategic adjustments in sales and marketing strategies.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Deal", "Key Account", "Key Account Manager", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
