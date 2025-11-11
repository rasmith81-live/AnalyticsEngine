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
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Loyalty Program", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.037339"},
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
                        52.5,
                        61.88,
                        60.41,
                        61.82,
                        61.25,
                        49.98,
                        63.2,
                        66.92,
                        48.44,
                        54.0,
                        50.24,
                        57.84
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.84,
                "unit": "%",
                "change": 7.6,
                "change_percent": 15.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 57.37,
                "min": 48.44,
                "max": 66.92,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 11.99,
                        "percentage": 20.7
                },
                {
                        "category": "Existing Customers",
                        "value": 7.29,
                        "percentage": 12.6
                },
                {
                        "category": "VIP Customers",
                        "value": 11.78,
                        "percentage": 20.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.81,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 20.97,
                        "percentage": 36.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.181146",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Loyalty Program Participation Rate"
        }
    },
}
