"""
Account Development Rate

The rate at which existing accounts are expanded or developed with additional sales.
"""

ACCOUNT_DEVELOPMENT_RATE = {
    "code": "ACCOUNT_DEVELOPMENT_RATE",
    "name": "Account Development Rate",
    "description": "The rate at which existing accounts are expanded or developed with additional sales.",
    "formula": "(Current Period Sales from Account - Previous Period Sales from Account) / Previous Period Sales from Account * 100",
    "calculation_formula": "(Current Period Sales from Account - Previous Period Sales from Account) / Previous Period Sales from Account * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Account Development Rate to be added.",
    "trend_analysis": """

    * An increasing account development rate may indicate successful upselling or cross-selling efforts, as well as strong customer satisfaction leading to repeat business.
    * A decreasing rate could signal a lack of focus on existing accounts, increased competition eroding market share, or declining customer loyalty.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or services that have shown significant growth in existing accounts?
    * How does our account development rate compare with industry benchmarks or with our competitors?
    
    """,
    "actionable_tips": """

    * Implement a customer relationship management (CRM) system to track customer interactions and identify opportunities for account development.
    * Provide sales teams with training on consultative selling techniques to uncover additional needs within existing accounts.
    * Establish regular communication channels with existing customers to understand their evolving needs and provide tailored solutions.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the account development rate over time to identify trends and seasonality.
    * Pie charts to visualize the distribution of sales growth across different existing accounts or customer segments.
    
    """,
    "risk_warnings": """

    * A stagnant or declining account development rate may lead to missed revenue opportunities and reduced customer lifetime value.
    * Relying solely on new customer acquisition without focusing on existing account growth can lead to a less stable revenue stream.
    
    """,
    "tracking_tools": """

    * CRM software such as Salesforce or HubSpot for tracking customer interactions and identifying upsell or cross-sell opportunities.
    * Data analytics tools to segment existing accounts and identify patterns or opportunities for growth.
    
    """,
    "integration_points": """

    * Integrate account development rate data with sales performance metrics to understand the impact of existing account growth on overall sales effectiveness.
    * Link account development rate with customer satisfaction scores to assess the correlation between account growth and customer loyalty.
    
    """,
    "change_impact_analysis": """

    * Improving the account development rate can lead to increased customer retention and loyalty, ultimately impacting long-term revenue and profitability.
    * However, a narrow focus on account development without acquiring new customers may limit overall market expansion and growth potential.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:22.987217"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        50.29,
                        39.73,
                        53.77,
                        51.47,
                        50.18,
                        45.16,
                        56.75,
                        58.06,
                        54.17,
                        41.9,
                        42.45,
                        50.01
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.01,
                "unit": "%",
                "change": 7.56,
                "change_percent": 17.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 49.5,
                "min": 39.73,
                "max": 58.06,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.58,
                        "percentage": 17.2
                },
                {
                        "category": "Category B",
                        "value": 6.22,
                        "percentage": 12.4
                },
                {
                        "category": "Category C",
                        "value": 8.73,
                        "percentage": 17.5
                },
                {
                        "category": "Category D",
                        "value": 3.8,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 22.68,
                        "percentage": 45.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:22.987217",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Development Rate"
        }
    },
}
