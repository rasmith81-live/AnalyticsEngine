"""
Sales Technology Adoption Rate KPI

The percentage of sales reps who have adopted and are effectively using the sales technology provided by the sales enablement team, such as CRM and sales automation tools.
"""

SALES_TECHNOLOGY_ADOPTION_RATE = {
    "code": "SALES_TECHNOLOGY_ADOPTION_RATE",
    "name": "Sales Technology Adoption Rate",
    "description": "The percentage of sales reps who have adopted and are effectively using the sales technology provided by the sales enablement team, such as CRM and sales automation tools.",
    "formula": "(Number of Reps Using Sales Tech / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Reps Using Sales Tech / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The percentage of sales reps who have adopted and are effectively using the sales technology provided by the sales enablement team, such as CRM and sales automation tools.",
    "expected_business_insights": "Indicates how well the sales team integrates technology into their processes for efficiency and effectiveness.",
    "measurement_approach": "Tracks the percentage of sales reps using the provided sales technologies.",
    "trend_analysis": """
    * An increasing adoption rate may indicate successful onboarding processes and the effectiveness of the sales technology.
    * A decreasing rate could signal resistance to change, lack of training, or issues with the usability of the technology.
    """,
    "diagnostic_questions": """
    * Are there specific features of the sales technology that sales reps struggle with or find unnecessary?
    * How does the adoption rate vary across different sales teams or regions, and what factors may contribute to these differences?
    """,
    "actionable_tips": """
    * Provide comprehensive training and ongoing support to ensure sales reps are comfortable and proficient with the technology.
    * Solicit feedback from sales reps to identify pain points and areas for improvement in the sales technology.
    * Recognize and reward early adopters to encourage others to embrace the technology.
    """,
    "visualization_suggestions": """
    * Line charts showing the adoption rate over time, broken down by individual sales reps or teams.
    * Comparison bar charts to visualize the adoption rates across different sales technologies or modules.
    """,
    "risk_warnings": """
    * Low adoption rates can lead to underutilization of expensive sales technology investments and hinder overall sales performance.
    * Inadequate adoption may also result in incomplete or inaccurate data in the CRM, impacting decision-making and forecasting.
    """,
    "tracking_tools": """
    * CRM analytics tools to track user engagement and identify areas for improvement in the sales technology adoption process.
    * Sales enablement platforms that offer training modules and resources for sales reps to enhance their proficiency with the technology.
    """,
    "integration_points": """
    * Integrate sales technology adoption data with performance metrics to understand the correlation between technology usage and sales outcomes.
    * Link adoption rates with HR systems to assess the impact of training and onboarding programs on technology adoption.
    """,
    "change_impact_analysis": """
    * Improving sales technology adoption can lead to more accurate sales data, better forecasting, and improved customer relationship management.
    * However, pushing for rapid adoption without proper support can result in frustration and decreased productivity among sales reps.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Product Adoption", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
