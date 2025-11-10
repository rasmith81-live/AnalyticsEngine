"""
Product Knowledge Competency KPI

The level of understanding the sales team has regarding the products they sell.
"""

PRODUCT_KNOWLEDGE_COMPETENCY = {
    "code": "PRODUCT_KNOWLEDGE_COMPETENCY",
    "name": "Product Knowledge Competency",
    "description": "The level of understanding the sales team has regarding the products they sell.",
    "formula": "(Number of Correct Answers / Total Number of Questions) * 100",
    "calculation_formula": "(Number of Correct Answers / Total Number of Questions) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The level of understanding the sales team has regarding the products they sell.",
    "expected_business_insights": "Highlights the sales team’s understanding of the products they sell, which is crucial for effective sales.",
    "measurement_approach": "Rate of correct answers on product knowledge assessments.",
    "trend_analysis": """
    * An increasing product knowledge competency may indicate improved training programs or a focus on continuous learning within the sales team.
    * A decreasing competency could signal high turnover, lack of training resources, or a shift in product offerings that the team is not fully prepared for.
    """,
    "diagnostic_questions": """
    * How often do we assess the product knowledge of our sales team members?
    * What resources and training opportunities are available to improve product knowledge competency?
    """,
    "actionable_tips": """
    * Implement regular product training sessions and assessments to ensure sales team members are up to date with product information.
    * Encourage collaboration between sales and product teams to share insights and updates on product features and benefits.
    * Utilize technology such as knowledge management systems to provide easy access to product information and resources for the sales team.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of product knowledge competency over time.
    * Radar charts comparing individual sales team members' product knowledge competency levels.
    """,
    "risk_warnings": """
    * Low product knowledge competency can lead to missed sales opportunities and decreased customer satisfaction.
    * High turnover within the sales team can negatively impact product knowledge competency and overall sales performance.
    """,
    "tracking_tools": """
    * Utilize learning management systems (LMS) to create and track product knowledge training modules.
    * Implement customer relationship management (CRM) systems with integrated product information to provide quick access for the sales team.
    """,
    "integration_points": """
    * Integrate product knowledge competency assessments with performance management systems to align individual goals with training needs.
    * Link product knowledge competency data with customer feedback and sales performance metrics to understand the impact on customer satisfaction and revenue.
    """,
    "change_impact_analysis": """
    * Improving product knowledge competency can lead to increased sales effectiveness and customer trust, ultimately impacting revenue and market share.
    * However, investing in extensive training and resources for product knowledge may impact short-term costs and resource allocation.
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Knowledge Base", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]},
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
}
