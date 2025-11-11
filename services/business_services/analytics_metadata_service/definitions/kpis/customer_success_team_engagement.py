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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Prospect Engagement", "Sales Team", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.890211"},
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
                        569.97,
                        595.44,
                        532.49,
                        457.54,
                        595.02,
                        534.63,
                        464.53,
                        453.03,
                        547.11,
                        479.87,
                        548.05,
                        595.8
                ],
                "unit": "units"
        },
        "current": {
                "value": 595.8,
                "unit": "units",
                "change": 47.75,
                "change_percent": 8.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 531.12,
                "min": 453.03,
                "max": 595.8,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 183.84,
                        "percentage": 30.9
                },
                {
                        "category": "Existing Customers",
                        "value": 115.06,
                        "percentage": 19.3
                },
                {
                        "category": "VIP Customers",
                        "value": 98.06,
                        "percentage": 16.5
                },
                {
                        "category": "At-Risk Customers",
                        "value": 22.07,
                        "percentage": 3.7
                },
                {
                        "category": "Other",
                        "value": 176.77,
                        "percentage": 29.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.837169",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Success Team Engagement"
        }
    },
}
