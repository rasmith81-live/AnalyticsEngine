"""
Loyalty Program Participation Rate

The percentage of customers participating in a company’s loyalty or rewards program.
"""

LOYALTY_PROGRAM_PARTICIPATION_RATE = {
    "code": "LOYALTY_PROGRAM_PARTICIPATION_RATE",
    "name": "Loyalty Program Participation Rate",
    "description": "The percentage of customers participating in a company\u2019s loyalty or rewards program.",
    "formula": "(Number of Loyalty Program Members / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Loyalty Program Members / Total Number of Customers) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Loyalty Program Participation Rate to be added.",
    "trend_analysis": """

    * An increasing loyalty program participation rate may indicate successful marketing efforts or enhanced program benefits that attract more customers.
    * A decreasing rate could signal dissatisfaction with the program, lack of awareness, or ineffective rewards, leading to potential customer churn.
    
    """,
    "diagnostic_questions": """

    * What are the primary reasons customers cite for participating or not participating in the loyalty program?
    * How does the participation rate vary across different customer segments or geographic regions?
    
    """,
    "actionable_tips": """

    * Regularly review and update the loyalty program to ensure it remains attractive and relevant to customers.
    * Personalize rewards and incentives based on individual customer preferences and purchase history.
    * Implement targeted marketing campaigns to promote the benefits of the loyalty program and encourage participation.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend in participation rate over time.
    * Pie charts comparing participation rates across different customer segments.
    
    """,
    "risk_warnings": """

    * A low participation rate may lead to reduced customer retention and lower overall sales.
    * High participation rates without corresponding increases in customer engagement or satisfaction could indicate a need for program adjustments.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and analyze customer participation data.
    * Marketing automation tools to personalize loyalty program communications and offers.
    
    """,
    "integration_points": """

    * Integrate participation rate data with customer feedback and satisfaction scores to understand the impact of the loyalty program on overall customer experience.
    * Link participation rates with sales performance metrics to assess the program's influence on purchasing behavior.
    
    """,
    "change_impact_analysis": """

    * An increase in participation rate may lead to higher customer lifetime value and improved brand advocacy.
    * Conversely, a decrease in participation could result in reduced customer loyalty and advocacy, impacting long-term sales and profitability.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Loyalty Program", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.633891"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
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
                        72.57,
                        70.91,
                        75.49,
                        75.06,
                        62.89,
                        65.06,
                        59.54,
                        74.29,
                        61.6,
                        71.38,
                        73.53,
                        68.78
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.78,
                "unit": "%",
                "change": -4.75,
                "change_percent": -6.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.26,
                "min": 59.54,
                "max": 75.49,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.79,
                        "percentage": 27.3
                },
                {
                        "category": "Category B",
                        "value": 11.84,
                        "percentage": 17.2
                },
                {
                        "category": "Category C",
                        "value": 8.3,
                        "percentage": 12.1
                },
                {
                        "category": "Category D",
                        "value": 6.54,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 23.31,
                        "percentage": 33.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.633891",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Loyalty Program Participation Rate"
        }
    },
}
