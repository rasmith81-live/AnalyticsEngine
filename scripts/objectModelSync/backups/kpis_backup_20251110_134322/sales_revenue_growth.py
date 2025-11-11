"""
Sales Revenue Growth KPI

The growth in sales revenue over a specific period. A higher growth rate indicates effective training and coaching.
"""

SALES_REVENUE_GROWTH = {
    "code": "SALES_REVENUE_GROWTH",
    "name": "Sales Revenue Growth",
    "description": "The growth in sales revenue over a specific period. A higher growth rate indicates effective training and coaching.",
    "formula": "(Sales Revenue Post-Training - Sales Revenue Pre-Training) / Sales Revenue Pre-Training * 100",
    "calculation_formula": "(Sales Revenue Post-Training - Sales Revenue Pre-Training) / Sales Revenue Pre-Training * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The growth in sales revenue over a specific period. A higher growth rate indicates effective training and coaching.",
    "expected_business_insights": "Reflects the impact of sales training on overall revenue generation and business growth.",
    "measurement_approach": "The percentage increase in sales revenue over a specific period post-training.",
    "trend_analysis": """
    * A steady increase in sales revenue growth may indicate effective training and coaching methods that are positively impacting the sales team's performance.
    * An inconsistent or declining growth rate could signal a need for adjustments in the training and coaching strategies to better support the sales team.
    """,
    "diagnostic_questions": """
    * Are there specific sales territories or product lines that are driving the majority of the sales revenue growth?
    * How do the sales revenue growth trends align with the implementation of new training and coaching initiatives?
    """,
    "actionable_tips": """
    * Regularly assess and update the training and coaching programs to ensure they are aligned with the evolving needs of the sales team.
    * Provide ongoing support and resources to sales managers to effectively implement the training and coaching strategies with their teams.
    * Encourage a culture of continuous learning and skill development within the sales team to drive sustained sales revenue growth.
    """,
    "visualization_suggestions": """
    * Line charts showing the sales revenue growth over time to identify any consistent patterns or fluctuations.
    * Comparative bar charts to visualize the sales revenue growth across different sales territories or product categories.
    """,
    "risk_warnings": """
    * Overreliance on a few high-performing sales representatives may lead to inconsistent or unsustainable sales revenue growth.
    * Inadequate training and coaching may result in missed sales opportunities and hinder overall sales revenue growth.
    """,
    "tracking_tools": """
    * Sales performance management software to track individual and team sales metrics and identify areas for improvement.
    * Customer relationship management (CRM) systems to analyze customer interactions and identify potential sales opportunities for revenue growth.
    """,
    "integration_points": """
    * Integrate sales revenue growth data with marketing analytics to understand the impact of marketing efforts on driving sales.
    * Align sales revenue growth with financial reporting systems to track the overall impact on the organization's bottom line.
    """,
    "change_impact_analysis": """
    * Improving sales revenue growth can lead to increased profitability and overall business success.
    * However, rapid sales revenue growth may also strain operational resources and require adjustments in production or service delivery to meet increased demand.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
