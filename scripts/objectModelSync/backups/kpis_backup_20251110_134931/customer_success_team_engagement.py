"""
Customer Success Team Engagement

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
    "full_kpi_definition": "Complete definition for Customer Success Team Engagement to be added.",
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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Prospect Engagement", "Sales Team", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.372519"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        638.71,
                        751.32,
                        741.2,
                        707.41,
                        673.43,
                        724.67,
                        731.08,
                        692.05,
                        641.7,
                        708.02,
                        735.47,
                        766.5
                ],
                "unit": "units"
        },
        "current": {
                "value": 766.5,
                "unit": "units",
                "change": 31.03,
                "change_percent": 4.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 709.3,
                "min": 638.71,
                "max": 766.5,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 218.94,
                        "percentage": 28.6
                },
                {
                        "category": "Category B",
                        "value": 185.3,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 65.55,
                        "percentage": 8.6
                },
                {
                        "category": "Category D",
                        "value": 64.16,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 232.55,
                        "percentage": 30.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.372519",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Success Team Engagement"
        }
    },
}
