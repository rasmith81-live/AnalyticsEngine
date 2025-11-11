"""
Competitive Win-back Rate

The rate at which lost customers from key accounts are regained from competitors.
"""

COMPETITIVE_WIN_BACK_RATE = {
    "code": "COMPETITIVE_WIN_BACK_RATE",
    "name": "Competitive Win-back Rate",
    "description": "The rate at which lost customers from key accounts are regained from competitors.",
    "formula": "(Number of Customers Won Back / Total Number of Customers Lost to Competitors) * 100",
    "calculation_formula": "(Number of Customers Won Back / Total Number of Customers Lost to Competitors) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Competitive Win-back Rate to be added.",
    "trend_analysis": """

    * An increasing competitive win-back rate may indicate successful strategies for regaining lost customers and outperforming competitors.
    * A decreasing rate could signal challenges in retaining or reacquiring lost customers, potentially due to stronger competitor offerings or poor customer experience.
    
    """,
    "diagnostic_questions": """

    * What specific actions or initiatives have contributed to the increase or decrease in the competitive win-back rate?
    * Are there common reasons or patterns behind the loss of key accounts to competitors, and how can these be addressed?
    
    """,
    "actionable_tips": """

    * Enhance customer relationship management to better understand the reasons for customer defection and tailor win-back strategies accordingly.
    * Regularly monitor competitor activities and offerings to identify areas where the organization can differentiate and regain lost customers.
    * Invest in customer experience improvements to reduce the likelihood of losing key accounts to competitors.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of competitive win-back rates over time.
    * Comparison bar charts displaying the organization's win-back rates versus those of key competitors.
    
    """,
    "risk_warnings": """

    * A consistently low competitive win-back rate may indicate a lack of effective strategies for regaining lost customers, leading to potential revenue loss.
    * High win-back rates may also suggest aggressive pricing or unsustainable efforts to win back customers, impacting profitability.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and manage win-back efforts and customer interactions.
    * Competitive intelligence tools to gather insights on competitor activities and customer preferences.
    
    """,
    "integration_points": """

    * Integrate win-back rate data with customer feedback and satisfaction metrics to understand the impact of win-back efforts on overall customer sentiment.
    * Link win-back strategies with sales and marketing automation systems to ensure consistent and targeted outreach to lost customers.
    
    """,
    "change_impact_analysis": """

    * Improving the competitive win-back rate can positively impact overall sales performance and customer retention, contributing to long-term revenue growth.
    * However, overly aggressive win-back strategies may strain customer relationships and brand reputation, affecting long-term customer loyalty.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Competitive Analysis", "Customer", "Key Account", "Key Account Manager", "Lost Sale", "Renewal Management"], "last_validated": "2025-11-10T13:43:23.131240"},
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
                        40.41,
                        35.77,
                        51.47,
                        35.87,
                        42.89,
                        48.09,
                        51.37,
                        45.24,
                        36.59,
                        33.99,
                        41.7,
                        51.06
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.06,
                "unit": "%",
                "change": 9.36,
                "change_percent": 22.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 42.87,
                "min": 33.99,
                "max": 51.47,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.27,
                        "percentage": 16.2
                },
                {
                        "category": "Category B",
                        "value": 7.25,
                        "percentage": 14.2
                },
                {
                        "category": "Category C",
                        "value": 10.63,
                        "percentage": 20.8
                },
                {
                        "category": "Category D",
                        "value": 2.82,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 22.09,
                        "percentage": 43.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.131240",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Competitive Win-back Rate"
        }
    },
}
