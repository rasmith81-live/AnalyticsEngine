"""
Sales Enablement Program Roi KPI

The return on investment of the sales enablement program in terms of revenue generated, cost savings, and productivity improvements.
"""

SALES_ENABLEMENT_PROGRAM_ROI = {
    "code": "SALES_ENABLEMENT_PROGRAM_ROI",
    "name": "Sales Enablement Program Roi",
    "description": "The return on investment of the sales enablement program in terms of revenue generated, cost savings, and productivity improvements.",
    "formula": "(Revenue Attributable to Sales Enablement - Cost of Sales Enablement) / Cost of Sales Enablement",
    "calculation_formula": "(Revenue Attributable to Sales Enablement - Cost of Sales Enablement) / Cost of Sales Enablement",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The return on investment of the sales enablement program in terms of revenue generated, cost savings, and productivity improvements.",
    "expected_business_insights": "Indicates the financial impact of the sales enablement program on sales results and profitability.",
    "measurement_approach": "Calculates the return on investment for the sales enablement program.",
    "trend_analysis": """
    * Increasing revenue generated from the sales enablement program may indicate positive performance shifts.
    * Decreasing cost savings or productivity improvements could signal negative performance trends.
    """,
    "diagnostic_questions": """
    * Are there specific sales enablement initiatives that have consistently led to revenue growth?
    * How does the cost savings and productivity improvements from the program compare with initial expectations?
    """,
    "actionable_tips": """
    * Regularly review and optimize the sales enablement content and training materials to ensure relevance and effectiveness.
    * Implement feedback mechanisms to gather insights from the sales team on the impact of the program on their performance.
    * Invest in technology that can automate and streamline sales enablement processes to improve efficiency.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of revenue generated over time.
    * Stacked bar charts comparing the cost savings and productivity improvements achieved each quarter.
    """,
    "risk_warnings": """
    * Failure to generate sufficient revenue from the program may lead to questions about its effectiveness and ROI.
    * Overemphasis on cost savings without considering the impact on sales team productivity and effectiveness.
    """,
    "tracking_tools": """
    * Sales enablement platforms like Highspot or Seismic for content management and analytics.
    * CRM systems with integrated sales enablement features to track the impact on revenue and productivity.
    """,
    "integration_points": """
    * Integrate sales enablement data with sales performance management systems to analyze the correlation between enablement efforts and sales results.
    * Link the program with customer relationship management (CRM) systems to understand the impact on customer acquisition and retention.
    """,
    "change_impact_analysis": """
    * Improving revenue generated from the program can positively impact overall sales team motivation and performance.
    * However, focusing solely on cost savings may lead to reduced investment in critical sales enablement resources and tools.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Enablement Feedback", "Enablement Platform", "Loyalty Program", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
