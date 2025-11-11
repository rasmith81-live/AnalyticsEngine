"""
Customer Problem Resolution Time

The time it takes to resolve a customer’s issue or problem.
"""

CUSTOMER_PROBLEM_RESOLUTION_TIME = {
    "code": "CUSTOMER_PROBLEM_RESOLUTION_TIME",
    "name": "Customer Problem Resolution Time",
    "description": "The time it takes to resolve a customer\u2019s issue or problem.",
    "formula": "Sum of All Resolution Times / Total Number of Resolved Issues",
    "calculation_formula": "Sum of All Resolution Times / Total Number of Resolved Issues",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Problem Resolution Time to be added.",
    "trend_analysis": """


    * Increasing resolution time may indicate growing complexity of customer issues or inefficiencies in the support process.
    * Decreasing resolution time can signal improved customer service effectiveness or better alignment of resources with demand.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific types of customer problems that consistently take longer to resolve?
    * How does our resolution time compare with industry benchmarks or customer expectations?
    
    
    """,
    "actionable_tips": """


    * Implement customer service training programs to enhance problem-solving skills and efficiency.
    * Leverage technology such as CRM systems or ticketing platforms to streamline and prioritize issue resolution.
    * Regularly review and update customer support processes to identify and eliminate bottlenecks.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing resolution time trends over time periods (e.g., monthly or quarterly).
    * Pareto charts to identify the most common types of customer problems and their associated resolution times.
    
    
    """,
    "risk_warnings": """


    * Long resolution times can lead to customer dissatisfaction and potential loss of business.
    * Inconsistent or excessively long resolution times may indicate underlying issues in customer support operations.
    
    
    """,
    "tracking_tools": """


    * Customer service management software like Zendesk or Freshdesk to track and analyze resolution times.
    * Workflow automation tools to streamline and standardize issue resolution processes.
    
    
    """,
    "integration_points": """


    * Integrate resolution time tracking with customer feedback systems to gain insights into the impact of support on overall satisfaction.
    * Link resolution time data with employee performance metrics to identify training or resource allocation needs.
    
    
    """,
    "change_impact_analysis": """


    * Improving resolution time can enhance customer loyalty and retention, leading to increased lifetime value.
    * However, overly aggressive targets for resolution time may compromise the quality of support and customer satisfaction.
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Support Ticket"], "last_validated": "2025-11-10T13:49:32.860825"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        206,
                        200,
                        178,
                        205,
                        187,
                        194,
                        177,
                        216,
                        201,
                        198,
                        211,
                        217
                ],
                "unit": "count"
        },
        "current": {
                "value": 217,
                "unit": "count",
                "change": 6,
                "change_percent": 2.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 199.17,
                "min": 177,
                "max": 217,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 38.75,
                        "percentage": 17.9
                },
                {
                        "category": "Category B",
                        "value": 53.5,
                        "percentage": 24.7
                },
                {
                        "category": "Category C",
                        "value": 31.11,
                        "percentage": 14.3
                },
                {
                        "category": "Category D",
                        "value": 17.2,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 76.44,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.325300",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Problem Resolution Time"
        }
    },
}
