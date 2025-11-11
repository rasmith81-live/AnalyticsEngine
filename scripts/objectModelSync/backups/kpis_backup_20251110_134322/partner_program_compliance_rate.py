"""
Partner Program Compliance Rate KPI

The rate at which channel partners comply with the terms and conditions of the partner program.
"""

PARTNER_PROGRAM_COMPLIANCE_RATE = {
    "code": "PARTNER_PROGRAM_COMPLIANCE_RATE",
    "name": "Partner Program Compliance Rate",
    "description": "The rate at which channel partners comply with the terms and conditions of the partner program.",
    "formula": "(Number of Compliant Partners / Total Number of Partners) * 100",
    "calculation_formula": "(Number of Compliant Partners / Total Number of Partners) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The rate at which channel partners comply with the terms and conditions of the partner program.",
    "expected_business_insights": "Ensures partners are aligned with program guidelines, maintaining program integrity and effectiveness.",
    "measurement_approach": "Calculates the percentage of partners adhering to the rules and requirements of the partner program.",
    "trend_analysis": """
    * An increasing partner program compliance rate may indicate better understanding and adherence to the program's terms and conditions.
    * A decreasing rate could signal a lack of clarity or communication regarding the program requirements, leading to non-compliance.
    """,
    "diagnostic_questions": """
    * Are there specific aspects of the partner program that partners struggle to comply with?
    * How does our partner program compliance rate compare with industry benchmarks or with historical data?
    """,
    "actionable_tips": """
    * Provide regular training and resources to ensure partners fully understand and can comply with the program requirements.
    * Implement a clear and transparent communication strategy to keep partners informed about any updates or changes to the program.
    * Offer incentives for maintaining high compliance rates to motivate partners to adhere to the program terms.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of compliance rates over time.
    * Pie charts comparing compliance rates across different partner segments or regions.
    """,
    "risk_warnings": """
    * Low compliance rates can lead to inconsistent branding and customer experience, impacting overall sales performance.
    * Inconsistent compliance may also result in legal or financial risks for the organization.
    """,
    "tracking_tools": """
    * Partner relationship management (PRM) software to track and manage partner program compliance.
    * Learning management systems (LMS) to deliver training and educational materials to partners.
    """,
    "integration_points": """
    * Integrate compliance data with sales performance metrics to understand the impact of partner program adherence on overall sales results.
    * Link compliance tracking with contract management systems to ensure partners are meeting contractual obligations.
    """,
    "change_impact_analysis": """
    * Improving partner program compliance can lead to a more consistent and positive customer experience, potentially increasing customer retention and loyalty.
    * However, stringent compliance requirements may also deter potential partners from joining the program, impacting partner acquisition and network growth.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Advocacy Program", "Loyalty Program", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
