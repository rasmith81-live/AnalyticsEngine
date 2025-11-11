"""
Sales Onboarding Efficiency KPI

The efficiency of the sales onboarding process, measured by the time it takes for new hires to reach full productivity.
"""

SALES_ONBOARDING_EFFICIENCY = {
    "code": "SALES_ONBOARDING_EFFICIENCY",
    "name": "Sales Onboarding Efficiency",
    "description": "The efficiency of the sales onboarding process, measured by the time it takes for new hires to reach full productivity.",
    "formula": "Time to Reach Full Productivity / Average Onboarding Duration",
    "calculation_formula": "Time to Reach Full Productivity / Average Onboarding Duration",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The efficiency of the sales onboarding process, measured by the time it takes for new hires to reach full productivity.",
    "expected_business_insights": "Indicates the quality of onboarding processes and the time to value for new hires.",
    "measurement_approach": "Assesses the speed and effectiveness with which new sales reps become fully productive.",
    "trend_analysis": """
    * Shortening onboarding times may indicate more effective training and support for new sales hires.
    * An increasing onboarding time could signal issues with training programs, sales processes, or the quality of new hires.
    """,
    "diagnostic_questions": """
    * What are the key milestones or checkpoints in our onboarding process, and how are they being measured?
    * Are there specific areas or skills where new hires consistently struggle to reach full productivity?
    """,
    "actionable_tips": """
    * Implement mentorship programs to provide ongoing support and guidance for new hires.
    * Regularly review and update training materials and processes to ensure they are relevant and effective.
    * Utilize technology and simulations to provide realistic sales scenarios for new hires to practice and learn from.
    """,
    "visualization_suggestions": """
    * Line charts showing the average time to full productivity for new hires over time.
    * Comparison bar charts to visualize the onboarding efficiency of different sales teams or regions.
    """,
    "risk_warnings": """
    * Extended onboarding times can lead to decreased sales performance and missed opportunities.
    * Rapidly changing market conditions or product offerings may require frequent updates to the onboarding process.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) to track and manage the progress of new hires through the onboarding process.
    * Customer relationship management (CRM) software to monitor the sales performance of new hires after onboarding.
    """,
    "integration_points": """
    * Integrate onboarding data with HR systems to identify correlations between onboarding success and hiring practices.
    * Connect onboarding metrics with sales performance data to assess the long-term impact of the onboarding process.
    """,
    "change_impact_analysis": """
    * Improving onboarding efficiency can lead to faster revenue generation and increased sales team effectiveness.
    * However, rushing the onboarding process may result in lower quality sales interactions and reduced customer satisfaction.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Onboarding", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
