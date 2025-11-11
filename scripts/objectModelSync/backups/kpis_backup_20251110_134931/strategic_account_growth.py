"""
Strategic Account Growth

The year-over-year revenue growth for key strategic accounts, indicating account managers' success in growing accounts.
"""

STRATEGIC_ACCOUNT_GROWTH = {
    "code": "STRATEGIC_ACCOUNT_GROWTH",
    "name": "Strategic Account Growth",
    "description": "The year-over-year revenue growth for key strategic accounts, indicating account managers' success in growing accounts.",
    "formula": "(Current Period Revenue from Strategic Account - Previous Period Revenue from Strategic Account) / Previous Period Revenue from Strategic Account * 100",
    "calculation_formula": "(Current Period Revenue from Strategic Account - Previous Period Revenue from Strategic Account) / Previous Period Revenue from Strategic Account * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Account Growth to be added.",
    "trend_analysis": """

    * Consistent year-over-year growth may indicate effective account management strategies and strong customer relationships.
    * Fluctuations in growth rates could be influenced by changes in market conditions, customer needs, or competitive landscape.
    
    """,
    "diagnostic_questions": """

    * What specific actions or initiatives have contributed to the growth in strategic accounts?
    * Are there any external factors or market shifts that have impacted the revenue growth in key accounts?
    
    """,
    "actionable_tips": """

    * Regularly review and update account plans to align with evolving customer needs and market dynamics.
    * Invest in training and development for account managers to enhance their strategic account management skills.
    * Implement a customer feedback mechanism to continuously assess satisfaction and identify opportunities for growth.
    
    """,
    "visualization_suggestions": """

    * Line charts showing revenue growth trends for individual strategic accounts over time.
    * Pareto charts to identify the top contributing accounts to overall growth.
    
    """,
    "risk_warnings": """

    * Over-reliance on a few key accounts for growth may pose a risk if those accounts experience downturns.
    * Failure to adapt to changing customer needs and market trends could result in stagnant or declining growth rates.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track interactions and opportunities with key accounts.
    * Data analytics tools to identify patterns and insights within the revenue growth data.
    
    """,
    "integration_points": """

    * Integrate strategic account growth data with sales forecasting to align resources and strategies for future growth.
    * Link account growth metrics with customer satisfaction surveys to understand the relationship between growth and customer experience.
    
    """,
    "change_impact_analysis": """

    * Increased strategic account growth can positively impact overall sales performance and contribute to the company's bottom line.
    * However, rapid growth in key accounts may require additional resources and support to maintain service levels and customer satisfaction.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale", "Sales Representative", "Strategic Initiative", "Strategic Review"], "last_validated": "2025-11-10T13:43:24.811508"},
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
                        64.0,
                        77.84,
                        76.0,
                        65.76,
                        66.89,
                        77.85,
                        74.16,
                        75.05,
                        74.76,
                        60.65,
                        77.5,
                        63.41
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.41,
                "unit": "%",
                "change": -14.09,
                "change_percent": -18.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 71.16,
                "min": 60.65,
                "max": 77.85,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.09,
                        "percentage": 19.1
                },
                {
                        "category": "Category B",
                        "value": 17.79,
                        "percentage": 28.1
                },
                {
                        "category": "Category C",
                        "value": 11.52,
                        "percentage": 18.2
                },
                {
                        "category": "Category D",
                        "value": 6.27,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 15.74,
                        "percentage": 24.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.811508",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Account Growth"
        }
    },
}
