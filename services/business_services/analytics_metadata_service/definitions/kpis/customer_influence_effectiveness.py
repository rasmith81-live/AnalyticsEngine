"""
Customer Influence Effectiveness

The effectiveness of key accounts in influencing the market and bringing in additional business.
"""

CUSTOMER_INFLUENCE_EFFECTIVENESS = {
    "code": "CUSTOMER_INFLUENCE_EFFECTIVENESS",
    "name": "Customer Influence Effectiveness",
    "description": "The effectiveness of key accounts in influencing the market and bringing in additional business.",
    "formula": "Revenue from Influenced Leads / Total Number of Influenced Leads",
    "calculation_formula": "Revenue from Influenced Leads / Total Number of Influenced Leads",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Influence Effectiveness to be added.",
    "trend_analysis": """



    * Increasing customer influence effectiveness may indicate a growing market presence and strong relationships with key accounts.
    * Decreasing influence effectiveness could signal a loss of key accounts or a shift in market dynamics that diminishes the impact of existing relationships.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific key accounts that have shown a significant increase or decrease in their influence on the market?
    * How do our key accounts compare in terms of their ability to bring in additional business and influence market trends?
    
    
    
    """,
    "actionable_tips": """



    * Regularly assess the needs and expectations of key accounts to ensure their influence remains strong.
    * Invest in building deeper, more strategic partnerships with key accounts to enhance their ability to influence the market.
    * Provide key accounts with exclusive access to new products or services to further leverage their influence.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of customer influence effectiveness over time.
    * Comparison bar charts displaying the influence effectiveness of different key accounts.
    
    
    
    """,
    "risk_warnings": """



    * A decline in customer influence effectiveness could lead to a loss of market share and missed business opportunities.
    * Over-reliance on a small number of key accounts for market influence may pose a risk if those relationships deteriorate.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze the impact of key accounts on the market.
    * Social listening tools to monitor the online influence of key accounts and identify potential opportunities for business growth.
    
    
    
    """,
    "integration_points": """



    * Integrate customer influence effectiveness data with sales and marketing systems to align strategies with the most influential accounts.
    * Link customer influence metrics with product development and innovation processes to leverage key accounts for market insights.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving customer influence effectiveness can lead to increased market share and revenue growth.
    * Declining influence effectiveness may require a shift in sales and marketing strategies to identify new influential accounts or re-engage existing ones.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Lead", "Market Segment", "Quarterly Business Review", "Renewal Management", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.839338"},
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
                        87,
                        79,
                        79,
                        83,
                        88,
                        80,
                        96,
                        91,
                        62,
                        70,
                        93,
                        99
                ],
                "unit": "count"
        },
        "current": {
                "value": 99,
                "unit": "count",
                "change": 6,
                "change_percent": 6.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 83.92,
                "min": 62,
                "max": 99,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 28.76,
                        "percentage": 29.1
                },
                {
                        "category": "Existing Customers",
                        "value": 22.28,
                        "percentage": 22.5
                },
                {
                        "category": "VIP Customers",
                        "value": 10.49,
                        "percentage": 10.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.41,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 32.06,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.696763",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Influence Effectiveness"
        }
    },
}
