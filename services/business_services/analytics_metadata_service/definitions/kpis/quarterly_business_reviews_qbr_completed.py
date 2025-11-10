"""
Quarterly Business Reviews (QBR) Completed KPI

The number of quarterly business reviews conducted with clients to ensure satisfaction and address any concerns.
"""

QUARTERLY_BUSINESS_REVIEWS_QBR_COMPLETED = {
    "code": "QUARTERLY_BUSINESS_REVIEWS_QBR_COMPLETED",
    "name": "Quarterly Business Reviews (QBR) Completed",
    "description": "The number of quarterly business reviews conducted with clients to ensure satisfaction and address any concerns.",
    "formula": "Total Number of QBRs Completed",
    "calculation_formula": "Total Number of QBRs Completed",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The number of quarterly business reviews conducted with clients to ensure satisfaction and address any concerns.",
    "expected_business_insights": "Assesses the strength of customer relationships and opportunities for strategic alignment and growth.",
    "measurement_approach": "Counts the number of formal reviews conducted with customers on a quarterly basis.",
    "trend_analysis": """
    * An increasing number of completed QBRs may indicate a proactive approach to customer satisfaction and relationship management.
    * A decreasing number of QBRs could signal a decline in customer engagement or potential dissatisfaction.
    """,
    "diagnostic_questions": """
    * Are there specific clients or industries where QBRs are consistently missed?
    * What feedback have we received from clients during QBRs, and how have we addressed any concerns raised?
    """,
    "actionable_tips": """
    * Implement a standardized process for scheduling and conducting QBRs with all clients.
    * Train sales teams on effective QBR techniques and communication skills to ensure meaningful interactions with clients.
    * Utilize customer relationship management (CRM) software to track and manage QBR schedules and outcomes.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of completed QBRs over time.
    * Pie charts to compare the distribution of completed QBRs across different client segments or industries.
    """,
    "risk_warnings": """
    * Low QBR completion rates may lead to decreased customer retention and potential loss of business.
    * Failure to address concerns raised during QBRs can result in negative word-of-mouth and reputation damage.
    """,
    "tracking_tools": """
    * CRM systems with built-in QBR scheduling and tracking capabilities.
    * Survey and feedback tools to gather client input before and after QBRs.
    """,
    "integration_points": """
    * Integrate QBR completion data with sales performance metrics to understand the impact of client engagement on overall sales results.
    * Link QBR outcomes with customer support systems to ensure timely resolution of any issues identified during the reviews.
    """,
    "change_impact_analysis": """
    * Improving QBR completion rates can lead to better customer retention and increased lifetime value of clients.
    * Conversely, a decline in QBR completion may result in decreased customer loyalty and potential revenue loss.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
