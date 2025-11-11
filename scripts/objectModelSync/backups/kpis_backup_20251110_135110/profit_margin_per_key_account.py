"""
Profit Margin per Key Account

The net profit margin generated from each key strategic account.
"""

PROFIT_MARGIN_PER_KEY_ACCOUNT = {
    "code": "PROFIT_MARGIN_PER_KEY_ACCOUNT",
    "name": "Profit Margin per Key Account",
    "description": "The net profit margin generated from each key strategic account.",
    "formula": "(Total Profit from Key Account / Total Revenue from Key Account) * 100",
    "calculation_formula": "(Total Profit from Key Account / Total Revenue from Key Account) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Profit Margin per Key Account to be added.",
    "trend_analysis": """


    * Increasing profit margins per key account may indicate successful upselling or cross-selling strategies.
    * Decreasing margins could signal increased competition or pricing pressures.
    
    
    """,
    "diagnostic_questions": """


    * What factors have contributed to the changes in profit margins for each key account?
    * How do our profit margins compare with industry benchmarks or with margins from previous periods?
    
    
    """,
    "actionable_tips": """


    * Regularly review pricing strategies and adjust them based on market conditions and customer value perception.
    * Focus on providing value-added services to key accounts to justify premium pricing and maintain healthy margins.
    * Implement cost-saving measures in operations to protect margins without sacrificing quality or service levels.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of profit margins per key account over time.
    * Pareto charts to identify the key accounts that contribute the most to overall profit margins.
    
    
    """,
    "risk_warnings": """


    * Declining profit margins may lead to reduced profitability and financial instability.
    * Overreliance on a few key accounts for high margins can pose a risk if those accounts are lost or face financial difficulties.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems to track and analyze customer interactions and sales performance.
    * Financial analysis software to conduct detailed profitability analysis for each key account.
    
    
    """,
    "integration_points": """


    * Integrate profit margin data with sales and marketing systems to align strategies with account profitability.
    * Link with financial systems to ensure accurate cost allocation and margin calculations.
    
    
    """,
    "change_impact_analysis": """


    * Improving profit margins can lead to increased revenue and overall business growth.
    * However, aggressive margin improvement strategies may impact customer satisfaction and retention.
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale", "Strategic Initiative", "Strategic Review"], "last_validated": "2025-11-10T13:49:33.281857"},
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
                        481,
                        485,
                        466,
                        486,
                        492,
                        463,
                        502,
                        503,
                        509,
                        508,
                        473,
                        464
                ],
                "unit": "count"
        },
        "current": {
                "value": 464,
                "unit": "count",
                "change": -9,
                "change_percent": -1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 486.0,
                "min": 463,
                "max": 509,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 118.18,
                        "percentage": 25.5
                },
                {
                        "category": "Category B",
                        "value": 52.24,
                        "percentage": 11.3
                },
                {
                        "category": "Category C",
                        "value": 75.29,
                        "percentage": 16.2
                },
                {
                        "category": "Category D",
                        "value": 45.74,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 172.55,
                        "percentage": 37.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.992726",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Profit Margin per Key Account"
        }
    },
}
