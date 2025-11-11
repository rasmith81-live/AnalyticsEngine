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
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Competitive Analysis", "Customer", "Key Account", "Key Account Manager", "Lost Sale", "Renewal Management"], "last_validated": "2025-11-10T13:49:32.706591"},
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
                        78.35,
                        77.36,
                        67.54,
                        60.41,
                        71.72,
                        66.14,
                        70.72,
                        66.89,
                        67.56,
                        75.7,
                        77.59,
                        66.02
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.02,
                "unit": "%",
                "change": -11.57,
                "change_percent": -14.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 70.5,
                "min": 60.41,
                "max": 78.35,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 14.15,
                        "percentage": 21.4
                },
                {
                        "category": "Existing Customers",
                        "value": 10.16,
                        "percentage": 15.4
                },
                {
                        "category": "VIP Customers",
                        "value": 7.66,
                        "percentage": 11.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 7.97,
                        "percentage": 12.1
                },
                {
                        "category": "Other",
                        "value": 26.08,
                        "percentage": 39.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.495004",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Competitive Win-back Rate"
        }
    },
}
