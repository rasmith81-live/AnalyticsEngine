"""
Account Share of Wallet

The percentage of a customer's total spending for a category that is spent with the company.
"""

ACCOUNT_SHARE_OF_WALLET = {
    "code": "ACCOUNT_SHARE_OF_WALLET",
    "name": "Account Share of Wallet",
    "description": "The percentage of a customer's total spending for a category that is spent with the company.",
    "formula": "(Revenue from Customer / Customer's Total Spend in Category) * 100",
    "calculation_formula": "(Revenue from Customer / Customer's Total Spend in Category) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Account Share of Wallet to be added.",
    "trend_analysis": """



    * Increasing share of wallet may indicate successful cross-selling or upselling efforts.
    * Decreasing share of wallet could signal increased competition or customer dissatisfaction.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the main factors influencing the distribution of a customer's spending across different providers?
    * Are there specific products or services where we are losing share of wallet, and why?
    
    
    
    """,
    "actionable_tips": """



    * Implement targeted marketing campaigns to increase customer engagement and loyalty.
    * Enhance the value proposition of products or services to capture a larger share of customer spending.
    * Regularly review and optimize pricing strategies to remain competitive and maintain share of wallet.
    
    
    
    """,
    "visualization_suggestions": """



    * Pie charts to visually represent the distribution of a customer's spending across different categories or providers.
    * Line graphs to track changes in share of wallet over time for key accounts.
    
    
    
    """,
    "risk_warnings": """



    * Decreasing share of wallet may indicate a higher risk of customer churn or defection to competitors.
    * Over-reliance on a few key accounts for a large share of wallet can pose a risk if those accounts are lost.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) systems to track and analyze customer purchasing behavior.
    * Business Intelligence (BI) tools to identify trends and patterns in customer spending data.
    
    
    
    """,
    "integration_points": """



    * Integrate share of wallet data with sales and marketing systems to align efforts in capturing a larger share of customer spending.
    * Link with customer satisfaction and feedback systems to understand the impact of customer experience on share of wallet.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing share of wallet can lead to higher customer lifetime value and revenue generation.
    * However, aggressive tactics to capture share of wallet may impact customer satisfaction and long-term loyalty.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.634469"},
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
                        76.22,
                        64.81,
                        62.27,
                        79.49,
                        64.93,
                        61.84,
                        71.44,
                        74.67,
                        73.77,
                        76.14,
                        78.61,
                        66.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.71,
                "unit": "%",
                "change": -11.9,
                "change_percent": -15.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 70.91,
                "min": 61.84,
                "max": 79.49,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 15.69,
                        "percentage": 23.5
                },
                {
                        "category": "Mid-Market",
                        "value": 16.81,
                        "percentage": 25.2
                },
                {
                        "category": "Small Business",
                        "value": 7.09,
                        "percentage": 10.6
                },
                {
                        "category": "Strategic Partners",
                        "value": 2.95,
                        "percentage": 4.4
                },
                {
                        "category": "Other",
                        "value": 24.17,
                        "percentage": 36.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.339391",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Account Share of Wallet"
        }
    },
}
