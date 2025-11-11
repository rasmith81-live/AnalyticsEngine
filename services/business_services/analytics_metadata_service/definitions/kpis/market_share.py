"""
Market Share

The percentage of market share held by the company within the key accounts.
"""

MARKET_SHARE = {
    "code": "MARKET_SHARE",
    "name": "Market Share",
    "description": "The percentage of market share held by the company within the key accounts.",
    "formula": "(Company's Sales Revenue / Total Market Sales Revenue) * 100",
    "calculation_formula": "(Company's Sales Revenue / Total Market Sales Revenue) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Market Share to be added.",
    "trend_analysis": """



    * Increasing market share within key accounts may indicate successful sales strategies and customer retention.
    * A decreasing market share could signal competitive pressures or dissatisfaction among key accounts.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors have contributed to the recent changes in market share within key accounts?
    * How does our market share compare with competitors within the same key accounts?
    
    
    
    """,
    "actionable_tips": """



    * Regularly assess customer needs and preferences to tailor offerings and maintain market share.
    * Provide exceptional customer service and support to solidify relationships and prevent attrition.
    * Implement targeted marketing and promotional campaigns to increase brand visibility and appeal within key accounts.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of market share percentage over time.
    * Pie charts comparing the distribution of market share among different key accounts.
    
    
    
    """,
    "risk_warnings": """



    * Decreasing market share may lead to reduced revenue and profitability.
    * Loss of market share within key accounts can indicate vulnerability to competitive threats.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and manage interactions with key accounts.
    * Market intelligence tools to gather insights on competitor activities and market trends.
    
    
    
    """,
    "integration_points": """



    * Integrate market share data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link market share analysis with customer feedback systems to understand the impact of customer satisfaction on market share.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing market share can lead to higher revenue and potentially lower customer acquisition costs.
    * However, aggressive tactics to gain market share may impact profitability and long-term customer relationships.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Market", "Customer", "Key Account", "Key Account Manager", "Market Segment", "Renewal Management", "Sale"], "last_validated": "2025-11-10T13:49:33.041150"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"],
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
                        75.94,
                        76.16,
                        61.85,
                        62.37,
                        71.2,
                        74.77,
                        75.34,
                        71.38,
                        61.93,
                        68.79,
                        59.53,
                        60.15
                ],
                "unit": "%"
        },
        "current": {
                "value": 60.15,
                "unit": "%",
                "change": 0.62,
                "change_percent": 1.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 68.28,
                "min": 59.53,
                "max": 76.16,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 14.12,
                        "percentage": 23.5
                },
                {
                        "category": "Channel Sales",
                        "value": 9.87,
                        "percentage": 16.4
                },
                {
                        "category": "Online Sales",
                        "value": 10.4,
                        "percentage": 17.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.89,
                        "percentage": 9.8
                },
                {
                        "category": "Other",
                        "value": 19.87,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.189666",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Market Share"
        }
    },
}
