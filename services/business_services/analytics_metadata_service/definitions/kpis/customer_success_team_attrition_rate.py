"""
Customer Success Team Attrition Rate

The rate at which customer success team members leave the company, either voluntarily or involuntarily.
"""

CUSTOMER_SUCCESS_TEAM_ATTRITION_RATE = {
    "code": "CUSTOMER_SUCCESS_TEAM_ATTRITION_RATE",
    "name": "Customer Success Team Attrition Rate",
    "description": "The rate at which customer success team members leave the company, either voluntarily or involuntarily.",
    "formula": "(Number of Customer Success Team Members Who Left / Total Number of Customer Success Team Members) * 100",
    "calculation_formula": "(Number of Customer Success Team Members Who Left / Total Number of Customer Success Team Members) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Success Team Attrition Rate to be added.",
    "trend_analysis": """



    * An increasing attrition rate may indicate issues with team morale, leadership, or company culture.
    * A decreasing rate could signal successful retention strategies, improved work environment, or better career development opportunities.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common reasons cited by departing team members, and are these issues being addressed?
    * How does our attrition rate compare with industry benchmarks or similar companies in our sector?
    
    
    
    """,
    "actionable_tips": """



    * Conduct exit interviews to understand the reasons behind voluntary departures and take action based on feedback.
    * Invest in professional development and career growth opportunities to increase employee satisfaction and retention.
    * Regularly assess and improve the work environment and company culture to reduce turnover.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing attrition rates over time to identify trends and patterns.
    * Pie charts to visualize the reasons for attrition and their relative impact on the overall rate.
    
    
    
    """,
    "risk_warnings": """



    * High attrition rates can disrupt team dynamics, reduce productivity, and increase recruitment and training costs.
    * Consistently high turnover may indicate systemic issues that could affect overall company performance and reputation.
    
    
    
    """,
    "tracking_tools": """



    * Human resources management software to track and analyze turnover data and identify potential areas for improvement.
    * Employee engagement platforms to gather feedback and measure satisfaction levels within the customer success team.
    
    
    
    """,
    "integration_points": """



    * Integrate attrition rate data with performance evaluations and feedback systems to identify potential correlations and areas for improvement.
    * Link turnover metrics with customer satisfaction scores to understand the impact of team stability on customer success.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing attrition can lead to a more stable and productive team, potentially improving customer satisfaction and long-term business performance.
    * However, efforts to reduce attrition may require investments in training, development, and employee support programs.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Sales Team"], "last_validated": "2025-11-10T13:49:32.889165"},
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
                        51.09,
                        53.78,
                        46.16,
                        63.8,
                        49.82,
                        62.07,
                        51.7,
                        45.08,
                        52.98,
                        62.49,
                        52.68,
                        51.23
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.23,
                "unit": "%",
                "change": -1.45,
                "change_percent": -2.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 53.57,
                "min": 45.08,
                "max": 63.8,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 12.79,
                        "percentage": 25.0
                },
                {
                        "category": "Existing Customers",
                        "value": 10.42,
                        "percentage": 20.3
                },
                {
                        "category": "VIP Customers",
                        "value": 6.62,
                        "percentage": 12.9
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.41,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 16.99,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.833658",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Success Team Attrition Rate"
        }
    },
}
