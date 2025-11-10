"""
Sales Playbook Adoption Rate KPI

The rate at which the sales team adopts and utilizes the sales playbook in their processes.
"""

SALES_PLAYBOOK_ADOPTION_RATE = {
    "code": "SALES_PLAYBOOK_ADOPTION_RATE",
    "name": "Sales Playbook Adoption Rate",
    "description": "The rate at which the sales team adopts and utilizes the sales playbook in their processes.",
    "formula": "(Number of Reps Using Sales Playbook / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Reps Using Sales Playbook / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The rate at which the sales team adopts and utilizes the sales playbook in their processes.",
    "expected_business_insights": "Measures the level of buy-in and utilization of structured sales strategies and practices.",
    "measurement_approach": "Tracks the percentage of sales reps who are actively using the sales playbook in their sales activities.",
    "trend_analysis": """
    * An increasing sales playbook adoption rate may indicate better alignment with sales processes and improved sales performance.
    * A decreasing rate could signal resistance to change, lack of understanding of the playbook's value, or ineffective training and communication.
    """,
    "diagnostic_questions": """
    * Are there specific sections or tools within the sales playbook that are being underutilized?
    * How does the adoption rate correlate with sales performance metrics such as win rates or deal size?
    """,
    "actionable_tips": """
    * Provide regular training and reinforcement of the playbook's value and usage.
    * Incorporate the playbook into the sales team's daily routines and processes to encourage adoption.
    * Solicit feedback from the sales team to continuously improve the playbook's relevance and effectiveness.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of adoption rate over time.
    * Comparison charts displaying adoption rates across different sales teams or regions.
    """,
    "risk_warnings": """
    * Low adoption rates may lead to inconsistent sales processes and missed opportunities.
    * Resistance to the playbook may indicate deeper issues with sales team culture or leadership buy-in.
    """,
    "tracking_tools": """
    * Sales enablement platforms like Seismic or Highspot for tracking and analyzing playbook usage.
    * CRM systems with integrated playbook features to seamlessly incorporate the playbook into sales workflows.
    """,
    "integration_points": """
    * Integrate the playbook adoption rate with sales performance metrics to understand its impact on overall sales effectiveness.
    * Link the adoption rate with training and development systems to identify areas for improvement and reinforcement.
    """,
    "change_impact_analysis": """
    * Improving the adoption rate can lead to more consistent sales processes and better customer interactions.
    * However, pushing for higher adoption may require changes in sales culture and processes, which could initially impact productivity.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Product Adoption", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
