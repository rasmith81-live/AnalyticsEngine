"""
Loyalty Program Effectiveness

A measure of how much the loyalty program contributes to customer retention and repeat purchases.
"""

LOYALTY_PROGRAM_EFFECTIVENESS = {
    "code": "LOYALTY_PROGRAM_EFFECTIVENESS",
    "name": "Loyalty Program Effectiveness",
    "description": "A measure of how much the loyalty program contributes to customer retention and repeat purchases.",
    "formula": "Comparison of Customer Metrics With and Without Loyalty Program",
    "calculation_formula": "Comparison of Customer Metrics With and Without Loyalty Program",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Loyalty Program Effectiveness to be added.",
    "trend_analysis": """

    * An increasing loyalty program effectiveness may indicate improved customer engagement and satisfaction.
    * A decreasing effectiveness could signal a need for program adjustments or increased competition in the market.
    
    """,
    "diagnostic_questions": """

    * Are there specific aspects of the loyalty program that receive more positive feedback from customers?
    * How does the loyalty program's effectiveness compare with industry benchmarks or with competitors' programs?
    
    """,
    "actionable_tips": """

    * Regularly gather feedback from customers to understand what aspects of the loyalty program are most valued.
    * Offer personalized rewards and incentives based on individual customer preferences and behavior.
    * Continuously analyze and optimize the program based on customer data and market trends.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of repeat purchases and customer retention over time.
    * Pie charts illustrating the distribution of rewards redeemed by customers.
    
    """,
    "risk_warnings": """

    * Low loyalty program effectiveness may lead to decreased customer retention and reduced customer lifetime value.
    * Over-reliance on the loyalty program as the sole retention strategy may result in missed opportunities for other customer engagement initiatives.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and analyze customer behavior and engagement with the loyalty program.
    * Data analytics tools to gain insights from customer data and identify patterns in loyalty program participation.
    
    """,
    "integration_points": """

    * Integrate loyalty program data with sales and marketing systems to understand the impact of the program on overall customer behavior and purchasing patterns.
    * Link the loyalty program with customer support platforms to ensure a seamless experience for program participants.
    
    """,
    "change_impact_analysis": """

    * Improving loyalty program effectiveness can lead to increased customer retention and higher customer lifetime value.
    * However, changes to the program may require investment in technology and resources, impacting overall operational costs.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Loyalty Program", "Prospect Engagement", "Sales Representative", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.631788"},
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
                        460.22,
                        384.89,
                        440.43,
                        430.62,
                        458.25,
                        422.01,
                        464.07,
                        391.62,
                        505.88,
                        497.67,
                        431.78,
                        472.56
                ],
                "unit": "units"
        },
        "current": {
                "value": 472.56,
                "unit": "units",
                "change": 40.78,
                "change_percent": 9.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 446.67,
                "min": 384.89,
                "max": 505.88,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 134.82,
                        "percentage": 28.5
                },
                {
                        "category": "Category B",
                        "value": 73.74,
                        "percentage": 15.6
                },
                {
                        "category": "Category C",
                        "value": 52.89,
                        "percentage": 11.2
                },
                {
                        "category": "Category D",
                        "value": 56.26,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 154.85,
                        "percentage": 32.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.631788",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Loyalty Program Effectiveness"
        }
    },
}
