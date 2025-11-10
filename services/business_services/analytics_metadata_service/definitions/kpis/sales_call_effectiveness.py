"""
Sales Call Effectiveness KPI

The effectiveness of sales calls based on outcomes such as lead generation or deal closure.
"""

SALES_CALL_EFFECTIVENESS = {
    "code": "SALES_CALL_EFFECTIVENESS",
    "name": "Sales Call Effectiveness",
    "description": "The effectiveness of sales calls based on outcomes such as lead generation or deal closure.",
    "formula": "No Standard Formula - This KPI is typically assessed through qualitative analysis and specific performance metrics.",
    "calculation_formula": "No Standard Formula - This KPI is typically assessed through qualitative analysis and specific performance metrics.",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The effectiveness of sales calls based on outcomes such as lead generation or deal closure.",
    "expected_business_insights": "Provides insights into the sales team’s communication skills and ability to achieve desired outcomes from calls.",
    "measurement_approach": "Evaluates the quality and outcomes of sales calls, often through qualitative assessments or performance metrics.",
    "trend_analysis": """
    * An increasing sales call effectiveness may indicate improved targeting or messaging in the sales process.
    * A decreasing effectiveness could signal changes in customer needs or increased competition.
    """,
    "diagnostic_questions": """
    * Are there specific customer segments or industries where sales call effectiveness is consistently high or low?
    * How do our sales call outcomes compare with industry benchmarks or historical data?
    """,
    "actionable_tips": """
    * Provide additional sales training and resources to improve sales call quality.
    * Regularly review and update sales scripts and messaging to align with customer needs and market trends.
    * Implement a CRM system to track and analyze sales call outcomes for better insights and decision-making.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of lead generation and deal closure rates over time.
    * Pie charts comparing the distribution of successful outcomes across different sales representatives or territories.
    """,
    "risk_warnings": """
    * Low sales call effectiveness can lead to wasted resources and missed opportunities for revenue generation.
    * Consistently high effectiveness may indicate a lack of challenging targets or missed opportunities for growth.
    """,
    "tracking_tools": """
    * CRM systems like Salesforce or HubSpot for tracking and analyzing sales call data.
    * Sales enablement platforms to provide sales teams with the necessary tools and resources for effective calls.
    """,
    "integration_points": """
    * Integrate sales call effectiveness data with customer relationship management systems to better understand the impact on overall customer relationships.
    * Link with marketing automation platforms to align sales calls with marketing efforts and messaging.
    """,
    "change_impact_analysis": """
    * Improving sales call effectiveness can lead to increased revenue and customer satisfaction, but may also require additional investment in training and technology.
    * Conversely, a decline in effectiveness can impact overall sales performance and customer retention.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Channel Deal", "Competitive Analysis", "Deal", "Lead", "Lead Qualification", "Outbound Call", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "OUTSIDE_SALES",
}
