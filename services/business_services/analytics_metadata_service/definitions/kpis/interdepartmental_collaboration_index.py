"""
Interdepartmental Collaboration Index KPI

A measure of the effectiveness of collaboration between the key account management team and other departments.
"""

INTERDEPARTMENTAL_COLLABORATION_INDEX = {
    "code": "INTERDEPARTMENTAL_COLLABORATION_INDEX",
    "name": "Interdepartmental Collaboration Index",
    "description": "A measure of the effectiveness of collaboration between the key account management team and other departments.",
    "formula": "Custom scoring based on frequency and quality of interdepartmental interactions",
    "calculation_formula": "Custom scoring based on frequency and quality of interdepartmental interactions",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "A measure of the effectiveness of collaboration between the key account management team and other departments.",
    "expected_business_insights": "Indicates the level of synergy between departments, which can impact customer experience and account growth.",
    "measurement_approach": "Measures the effectiveness and frequency of collaboration between departments involved in key account management.",
    "trend_analysis": """
    * An increasing interdepartmental collaboration index may indicate improved communication and alignment between key account management and other departments.
    * A decreasing index could signal breakdowns in collaboration, leading to inefficiencies and missed opportunities.
    """,
    "diagnostic_questions": """
    * Are there clear channels for communication and collaboration between key account management and other departments?
    * How do other departments perceive the level of collaboration with the key account management team?
    """,
    "actionable_tips": """
    * Establish regular cross-functional meetings to align on key account strategies and address any issues or challenges.
    * Implement shared KPIs and goals across departments to foster a sense of collective responsibility for key account success.
    * Utilize collaborative tools and technologies such as project management platforms or shared document repositories.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of the interdepartmental collaboration index over time.
    * Network diagrams to visually represent the connections and interactions between key account management and other departments.
    """,
    "risk_warnings": """
    * Poor interdepartmental collaboration can lead to missed opportunities, misaligned strategies, and ultimately, loss of key accounts.
    * Fragmented collaboration may result in duplicated efforts, conflicting messages to key accounts, and internal conflicts.
    """,
    "tracking_tools": """
    * Collaboration platforms like Microsoft Teams or Slack for real-time communication and file sharing.
    * Project management tools such as Asana or Trello to coordinate and track cross-departmental initiatives.
    """,
    "integration_points": """
    * Integrate the interdepartmental collaboration index with CRM systems to track the impact of collaboration on key account performance.
    * Link the index with performance management systems to align individual and team goals with collaborative efforts.
    """,
    "change_impact_analysis": """
    * Improved collaboration can lead to more effective account planning, better customer experiences, and increased revenue from key accounts.
    * On the other hand, poor collaboration can result in missed sales opportunities, customer dissatisfaction, and increased churn.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Renewal Management", "Sales Team"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
