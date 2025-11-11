"""
Customer Success Team Engagement KPI

The level of engagement and satisfaction of the customer success team members in their roles.
"""

CUSTOMER_SUCCESS_TEAM_ENGAGEMENT = {
    "code": "CUSTOMER_SUCCESS_TEAM_ENGAGEMENT",
    "name": "Customer Success Team Engagement",
    "description": "The level of engagement and satisfaction of the customer success team members in their roles.",
    "formula": "Average Engagement Score Across Customer Success Team Members",
    "calculation_formula": "Average Engagement Score Across Customer Success Team Members",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The level of engagement and satisfaction of the customer success team members in their roles.",
    "expected_business_insights": "Reflects team morale and effectiveness, which can impact customer satisfaction and retention.",
    "measurement_approach": "Assesses the level of involvement, motivation, and commitment of the customer success team, often through surveys or performance metrics.",
    "trend_analysis": """
    * Increasing engagement and satisfaction may indicate a positive trend in customer success team performance and effectiveness.
    * Decreasing engagement levels could signal potential issues with team morale, workload, or leadership support.
    """,
    "diagnostic_questions": """
    * Are there specific factors contributing to the level of engagement and satisfaction within the customer success team?
    * How does the current engagement compare to historical data or industry benchmarks?
    """,
    "actionable_tips": """
    * Implement regular feedback mechanisms to understand the challenges and needs of the customer success team.
    * Provide professional development opportunities and resources to support the growth and well-being of team members.
    * Establish clear communication channels and expectations to ensure alignment and motivation within the team.
    """,
    "visualization_suggestions": """
    * Line charts showing engagement levels over time to identify trends and patterns.
    * Heat maps to visualize areas of high and low satisfaction within the team.
    """,
    "risk_warnings": """
    * Low engagement and satisfaction levels can lead to higher turnover and decreased productivity within the customer success team.
    * Unaddressed issues with team engagement may result in negative impacts on customer relationships and retention.
    """,
    "tracking_tools": """
    * Employee engagement survey platforms to gather and analyze feedback from the customer success team.
    * Performance management software to track individual and team satisfaction metrics over time.
    """,
    "integration_points": """
    * Integrate engagement and satisfaction data with performance reviews and goal-setting processes to align individual and team objectives.
    * Link engagement metrics with customer feedback and retention data to understand the impact on overall business outcomes.
    """,
    "change_impact_analysis": """
    * Improving team engagement and satisfaction can lead to better customer relationships and increased retention rates.
    * Conversely, low team engagement may result in decreased customer satisfaction and potential revenue loss.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Prospect Engagement", "Sales Team", "Service Level Agreement"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
