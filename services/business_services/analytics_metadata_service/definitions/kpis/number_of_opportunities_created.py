"""
Number of Opportunities Created KPI

The total number of sales opportunities created by the sales development team.
"""

NUMBER_OF_OPPORTUNITIES_CREATED = {
    "code": "NUMBER_OF_OPPORTUNITIES_CREATED",
    "name": "Number of Opportunities Created",
    "description": "The total number of sales opportunities created by the sales development team.",
    "formula": "Count of Leads Converted to Opportunities",
    "calculation_formula": "Count of Leads Converted to Opportunities",
    "category": "Sales Development",
    "is_active": True,
    "kpi_definition": "The total number of sales opportunities created by the sales development team.",
    "expected_business_insights": "Assesses the efficiency of lead qualification and potential for revenue growth.",
    "measurement_approach": "Tracks the number of qualified leads that are escalated to sales opportunities.",
    "trend_analysis": """
    * An increasing number of opportunities created may indicate a more effective sales development team or increased market demand.
    * A decreasing number of opportunities could signal issues with lead generation, sales outreach, or market saturation.
    """,
    "diagnostic_questions": """
    * Are there specific industries or segments where opportunities are consistently being created?
    * How does the number of opportunities created compare to the overall sales pipeline and conversion rates?
    """,
    "actionable_tips": """
    * Implement targeted marketing campaigns to generate more qualified leads for the sales development team.
    * Provide ongoing training and support for the sales development team to improve their lead generation and outreach strategies.
    * Regularly review and optimize the sales development process to identify and address any bottlenecks or inefficiencies.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of opportunities created over time.
    * Pie charts to visualize the distribution of opportunities by industry or segment.
    """,
    "risk_warnings": """
    * A low number of opportunities created may lead to a limited sales pipeline and reduced revenue potential.
    * An excessively high number of opportunities without proper qualification may strain the sales team and lead to inefficiencies.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track and manage sales opportunities effectively.
    * Sales engagement platforms to automate and streamline the outreach process for the sales development team.
    """,
    "integration_points": """
    * Integrate with marketing automation systems to ensure a seamless handoff of leads from marketing to the sales development team.
    * Connect with the sales team's CRM to provide visibility into the opportunities created and their progression through the sales pipeline.
    """,
    "change_impact_analysis": """
    * An increase in opportunities created can positively impact the overall sales performance and revenue generation.
    * However, a high number of unqualified opportunities may lead to wasted resources and decreased conversion rates.
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
}
