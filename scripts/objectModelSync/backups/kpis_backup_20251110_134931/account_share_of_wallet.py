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
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:43:22.999678"},
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
                        563.07,
                        455.0,
                        422.89,
                        523.87,
                        502.7,
                        485.35,
                        425.82,
                        461.86,
                        457.63,
                        543.22,
                        469.05,
                        530.02
                ],
                "unit": "units"
        },
        "current": {
                "value": 530.02,
                "unit": "units",
                "change": 60.97,
                "change_percent": 13.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 486.71,
                "min": 422.89,
                "max": 563.07,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 147.14,
                        "percentage": 27.8
                },
                {
                        "category": "Category B",
                        "value": 91.01,
                        "percentage": 17.2
                },
                {
                        "category": "Category C",
                        "value": 63.5,
                        "percentage": 12.0
                },
                {
                        "category": "Category D",
                        "value": 50.44,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 177.93,
                        "percentage": 33.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:22.999678",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Account Share of Wallet"
        }
    },
}
