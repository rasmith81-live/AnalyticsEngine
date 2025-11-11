"""
Sales Process Adherence Rate KPI

The percentage of sales reps following the prescribed sales process.
"""

SALES_PROCESS_ADHERENCE_RATE = {
    "code": "SALES_PROCESS_ADHERENCE_RATE",
    "name": "Sales Process Adherence Rate",
    "description": "The percentage of sales reps following the prescribed sales process.",
    "formula": "(Number of Sales Following the Process / Total Number of Sales) * 100",
    "calculation_formula": "(Number of Sales Following the Process / Total Number of Sales) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "kpi_definition": "The percentage of sales reps following the prescribed sales process.",
    "expected_business_insights": "Ensures consistency in sales activities and can predict success rates.",
    "measurement_approach": "Tracks compliance with the predefined sales process steps.",
    "trend_analysis": """
    * An increasing sales process adherence rate may indicate better training or improved understanding of the sales process among reps.
    * A decreasing rate could signal a need for process re-evaluation, changes in market conditions, or lack of enforcement from sales management.
    """,
    "diagnostic_questions": """
    * Are there specific stages of the sales process where adherence tends to drop off?
    * How does the sales process adherence rate vary among different sales teams or regions?
    """,
    "actionable_tips": """
    * Regularly review and update the sales process to ensure it aligns with current market conditions and customer needs.
    * Provide ongoing training and coaching to reinforce the importance of following the sales process.
    * Implement sales management tools and CRM systems that can track and report on sales process adherence.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of sales process adherence rate over time.
    * Comparison bar charts to visualize adherence rates across different sales teams or regions.
    """,
    "risk_warnings": """
    * Low sales process adherence can lead to inconsistent customer experiences and lost sales opportunities.
    * High adherence without flexibility can result in missed opportunities for creative problem-solving and relationship-building.
    """,
    "tracking_tools": """
    * CRM systems with built-in process adherence tracking and reporting capabilities.
    * Sales enablement platforms that provide guidance and support for following the sales process.
    """,
    "integration_points": """
    * Integrate sales process adherence data with performance management systems to align coaching and development efforts with individual needs.
    * Link adherence metrics with customer feedback and satisfaction scores to understand the impact on customer experience.
    """,
    "change_impact_analysis": """
    * Improving sales process adherence can lead to more predictable sales outcomes and better customer relationships.
    * However, overly rigid adherence may stifle innovation and creativity in sales approaches.
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
}
