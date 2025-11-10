"""
Lead-to-Opportunity Ratio KPI

The ratio of leads that are converted into sales opportunities.
"""

LEAD_TO_OPPORTUNITY_RATIO = {
    "code": "LEAD_TO_OPPORTUNITY_RATIO",
    "name": "Lead-to-Opportunity Ratio",
    "description": "The ratio of leads that are converted into sales opportunities.",
    "formula": "Number of Opportunities Created / Number of Qualified Leads * 100",
    "calculation_formula": "Number of Opportunities Created / Number of Qualified Leads * 100",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The ratio of leads that are converted into sales opportunities.",
    "expected_business_insights": "Offers insights into the lead qualification process and the sales team’s ability to turn leads into potential sales.",
    "measurement_approach": "Compares the number of qualified leads to the number of opportunities created.",
    "trend_analysis": """
    * An increasing lead-to-opportunity ratio may indicate improved lead quality or more effective sales strategies.
    * A decreasing ratio could signal issues with lead nurturing or a decline in the overall demand for the product or service.
    """,
    "diagnostic_questions": """
    * Are there specific lead sources that consistently result in higher conversion rates?
    * How does our lead-to-opportunity ratio compare with industry benchmarks or historical data?
    """,
    "actionable_tips": """
    * Implement lead scoring to prioritize high-quality leads for follow-up.
    * Provide additional sales training to improve lead conversion techniques.
    * Regularly review and optimize the lead nurturing process to ensure leads are being effectively moved through the sales funnel.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of lead-to-opportunity ratio over time.
    * Pie charts comparing lead sources and their respective conversion rates.
    """,
    "risk_warnings": """
    * A low lead-to-opportunity ratio may result in wasted resources on low-quality leads.
    * A high ratio could indicate missed opportunities for potential sales growth.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track and analyze lead conversion data.
    * Marketing automation tools to streamline lead nurturing processes and improve conversion rates.
    """,
    "integration_points": """
    * Integrate lead-to-opportunity ratio tracking with marketing and sales platforms to align efforts and improve lead quality.
    * Link with customer relationship management systems to ensure a seamless transition from lead to opportunity.
    """,
    "change_impact_analysis": """
    * Improving the lead-to-opportunity ratio can lead to increased sales revenue and better overall sales performance.
    * However, a significant change in the ratio may require adjustments in resource allocation and sales strategies.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Expansion Opportunity", "Lead", "Lead Qualification", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "OUTSIDE_SALES",
}
