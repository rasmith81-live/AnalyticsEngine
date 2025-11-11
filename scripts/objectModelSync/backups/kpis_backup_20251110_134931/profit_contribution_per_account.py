"""
Profit Contribution per Account

The contribution to profit from each key account, reflecting the value and cost efficiency of maintaining the account.
"""

PROFIT_CONTRIBUTION_PER_ACCOUNT = {
    "code": "PROFIT_CONTRIBUTION_PER_ACCOUNT",
    "name": "Profit Contribution per Account",
    "description": "The contribution to profit from each key account, reflecting the value and cost efficiency of maintaining the account.",
    "formula": "Revenue from Account - Costs Associated with Account",
    "calculation_formula": "Revenue from Account - Costs Associated with Account",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Profit Contribution per Account to be added.",
    "trend_analysis": """

    * Increasing profit contribution per account may indicate successful upselling or cross-selling efforts.
    * Decreasing profit contribution could signal increased costs or declining customer value.
    
    """,
    "diagnostic_questions": """

    * Are there specific accounts that consistently contribute the most to profit?
    * How does the profit contribution per account compare with the cost of maintaining those accounts?
    
    """,
    "actionable_tips": """

    * Implement targeted account management strategies to increase the value of high-profit accounts.
    * Review and optimize the cost structure associated with managing lower-profit accounts.
    
    """,
    "visualization_suggestions": """

    * Pareto charts to identify the top contributing accounts versus the rest.
    * Line graphs to track the trend of profit contribution per account over time.
    
    """,
    "risk_warnings": """

    * Over-reliance on a few high-profit accounts can pose a risk if they are lost or experience reduced business with the organization.
    * Ignoring low-profit accounts may lead to missed opportunities for growth or relationship-building.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) systems to track and analyze account-specific data.
    * Profitability analysis tools to understand the true cost and value of each key account.
    
    """,
    "integration_points": """

    * Integrate profit contribution data with sales and marketing systems to align efforts with the most valuable accounts.
    * Link with financial systems to understand the overall impact of account profitability on the organization's bottom line.
    
    """,
    "change_impact_analysis": """

    * Increasing profit contribution per account may lead to higher overall company profitability.
    * However, focusing solely on profit contribution without considering customer satisfaction and long-term value may lead to short-sighted decisions.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:43:23.988979"},
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
                        89,
                        80,
                        100,
                        59,
                        93,
                        89,
                        79,
                        70,
                        65,
                        84,
                        75,
                        76
                ],
                "unit": "count"
        },
        "current": {
                "value": 76,
                "unit": "count",
                "change": 1,
                "change_percent": 1.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 79.92,
                "min": 59,
                "max": 100,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 24.09,
                        "percentage": 31.7
                },
                {
                        "category": "Category B",
                        "value": 7.9,
                        "percentage": 10.4
                },
                {
                        "category": "Category C",
                        "value": 14.93,
                        "percentage": 19.6
                },
                {
                        "category": "Category D",
                        "value": 2.98,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 26.1,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.988979",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Profit Contribution per Account"
        }
    },
}
