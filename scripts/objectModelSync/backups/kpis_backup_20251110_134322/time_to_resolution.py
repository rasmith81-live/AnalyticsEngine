"""
Time to Resolution KPI

The amount of time it takes for the Customer Success Team to resolve a customer issue. This KPI measures the team's effectiveness in providing timely solutions to customer problems.
"""

TIME_TO_RESOLUTION = {
    "code": "TIME_TO_RESOLUTION",
    "name": "Time to Resolution",
    "description": "The amount of time it takes for the Customer Success Team to resolve a customer issue. This KPI measures the team's effectiveness in providing timely solutions to customer problems.",
    "formula": "Average Time Between Ticket Creation and Resolution",
    "calculation_formula": "Average Time Between Ticket Creation and Resolution",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The amount of time it takes for the Customer Success Team to resolve a customer issue. This KPI measures the team's effectiveness in providing timely solutions to customer problems.",
    "expected_business_insights": "Assesses the efficiency of problem-solving processes and the impact on customer satisfaction.",
    "measurement_approach": "Tracks the average time taken to resolve a customer issue or support ticket from the time it is reported.",
    "trend_analysis": """
    * Increasing time to resolution may indicate growing customer issues or inefficiencies in the support process.
    * Decreasing time to resolution can signal improved customer support workflows or better product stability.
    """,
    "diagnostic_questions": """
    * Are there common patterns or root causes behind prolonged resolution times?
    * How does our time to resolution compare with industry benchmarks or customer expectations?
    """,
    "actionable_tips": """
    * Implement customer support automation to streamline issue identification and resolution.
    * Provide ongoing training and resources for the support team to enhance their problem-solving skills.
    * Regularly review and update support processes to eliminate bottlenecks and inefficiencies.
    """,
    "visualization_suggestions": """
    * Line charts showing the average time to resolution over time.
    * Pareto charts to identify the most common issues and their resolution times.
    """,
    "risk_warnings": """
    * Extended resolution times can lead to customer dissatisfaction and potential churn.
    * Consistently high resolution times may indicate systemic issues in product quality or customer support.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems with built-in support ticketing and tracking capabilities.
    * Workflow automation tools to streamline issue escalation and assignment.
    """,
    "integration_points": """
    * Integrate time to resolution data with customer satisfaction metrics to understand the impact of support performance on customer happiness.
    * Link resolution time tracking with product development systems to address recurring issues at their root.
    """,
    "change_impact_analysis": """
    * Reducing time to resolution can lead to higher customer satisfaction and loyalty, positively impacting long-term revenue.
    * However, overly aggressive targets for resolution times may sacrifice the quality of support provided.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Team", "Support Ticket"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
