"""
Sales Call Abandonment Rate KPI

The rate at which potential customers abandon a sales call before it is completed.
"""

SALES_CALL_ABANDONMENT_RATE = {
    "code": "SALES_CALL_ABANDONMENT_RATE",
    "name": "Sales Call Abandonment Rate",
    "description": "The rate at which potential customers abandon a sales call before it is completed.",
    "formula": "(Number of Abandoned Sales Calls / Total Number of Sales Calls) * 100",
    "calculation_formula": "(Number of Abandoned Sales Calls / Total Number of Sales Calls) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The rate at which potential customers abandon a sales call before it is completed.",
    "expected_business_insights": "Highlights potential inefficiencies in the sales call process, which could be improved to prevent lost opportunities.",
    "measurement_approach": "Measures the percentage of sales calls that are not completed or are ended before connecting with a lead.",
    "trend_analysis": """
    * An increasing sales call abandonment rate may indicate a need for better sales training or a lack of understanding of customer needs.
    * A decreasing rate could signal improved sales techniques or better alignment between customer expectations and the sales process.
    """,
    "diagnostic_questions": """
    * Are there common reasons why potential customers abandon sales calls, such as pricing, product fit, or timing?
    * How does our sales call abandonment rate compare with industry benchmarks or with different sales teams within our organization?
    """,
    "actionable_tips": """
    * Provide additional sales training to address potential customer objections and improve sales techniques.
    * Implement a more targeted approach to qualifying leads to ensure better alignment between customer needs and the sales process.
    * Utilize customer feedback to understand common reasons for call abandonment and adjust sales strategies accordingly.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of sales call abandonment rate over time.
    * Pie charts to visualize the reasons for call abandonment, such as pricing, product fit, or timing issues.
    """,
    "risk_warnings": """
    * A high sales call abandonment rate can lead to lost sales opportunities and decreased revenue.
    * Frequent call abandonment may indicate a need for improvement in the sales process or product offerings.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track and analyze call abandonment rates and reasons.
    * Sales enablement platforms to provide sales teams with the necessary tools and resources to address customer objections and improve sales effectiveness.
    """,
    "integration_points": """
    * Integrate sales call abandonment rate with customer feedback systems to understand the reasons behind call abandonment and make necessary adjustments.
    * Link with sales performance management systems to identify trends and patterns in call abandonment across different sales teams and territories.
    """,
    "change_impact_analysis": """
    * Improving the sales call abandonment rate can lead to increased sales efficiency and customer satisfaction, but may require investment in sales training and resources.
    * A high call abandonment rate can impact the overall sales performance and customer perception of the brand, affecting long-term customer value and brand reputation.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Customer", "Lead", "Lead Qualification", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"],
    "module_code": "OUTSIDE_SALES",
}
