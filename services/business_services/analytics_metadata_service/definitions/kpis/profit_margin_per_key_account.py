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
                        57.81,
                        62.99,
                        44.2,
                        43.24,
                        61.61,
                        46.89,
                        55.34,
                        61.4,
                        58.64,
                        62.35,
                        45.76,
                        45.97
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.97,
                "unit": "%",
                "change": 0.21,
                "change_percent": 0.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 53.85,
                "min": 43.24,
                "max": 62.99,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 10.21,
                        "percentage": 22.2
                },
                {
                        "category": "Mid-Market",
                        "value": 9.0,
                        "percentage": 19.6
                },
                {
                        "category": "Small Business",
                        "value": 4.11,
                        "percentage": 8.9
                },
                {
                        "category": "Strategic Partners",
                        "value": 4.19,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 18.46,
                        "percentage": 40.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.666810",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Profit Margin per Key Account"
        }
    },
}
