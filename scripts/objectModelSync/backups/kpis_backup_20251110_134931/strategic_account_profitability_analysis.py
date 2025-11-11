"""
Strategic Account Profitability Analysis

A detailed analysis of profits derived from each strategic account, helping to identify the most valuable relationships.
"""

STRATEGIC_ACCOUNT_PROFITABILITY_ANALYSIS = {
    "code": "STRATEGIC_ACCOUNT_PROFITABILITY_ANALYSIS",
    "name": "Strategic Account Profitability Analysis",
    "description": "A detailed analysis of profits derived from each strategic account, helping to identify the most valuable relationships.",
    "formula": "Revenue from Strategic Account - Cost to Serve Strategic Account",
    "calculation_formula": "Revenue from Strategic Account - Cost to Serve Strategic Account",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Account Profitability Analysis to be added.",
    "trend_analysis": """

    * Increasing profitability from strategic accounts may indicate successful upselling or cross-selling efforts.
    * Decreasing profitability could signal increased competition or dissatisfaction with the current offerings.
    
    """,
    "diagnostic_questions": """

    * What specific products or services are driving the most profitability within each strategic account?
    * Are there any commonalities among the most profitable accounts that can be replicated with other accounts?
    
    """,
    "actionable_tips": """

    * Regularly review and adjust pricing strategies for each strategic account based on their profitability.
    * Invest in building stronger relationships with high-profit accounts through personalized service and tailored solutions.
    * Continuously monitor and analyze the cost-to-serve for each strategic account to ensure profitability is maintained.
    
    """,
    "visualization_suggestions": """

    * Pareto charts to identify the top contributing accounts to overall profitability.
    * Profitability trend lines for each strategic account over time to visualize performance shifts.
    
    """,
    "risk_warnings": """

    * Over-reliance on a small number of highly profitable accounts may pose a risk if they are lost or experience reduced profitability.
    * Ignoring lower-profitability accounts may lead to missed opportunities for growth and diversification.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) systems to track interactions and sales activities with strategic accounts.
    * Profitability analysis modules within enterprise resource planning (ERP) systems for detailed financial insights.
    
    """,
    "integration_points": """

    * Integrate profitability analysis with sales forecasting to align account management strategies with expected future performance.
    * Link profitability data with customer satisfaction metrics to understand the relationship between profitability and customer experience.
    
    """,
    "change_impact_analysis": """

    * Improving profitability from strategic accounts can lead to increased resources for investment in product development or market expansion.
    * Conversely, declining profitability may require cost-cutting measures or a reevaluation of the account management approach.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Competitive Analysis", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale", "Strategic Initiative", "Strategic Review"], "last_validated": "2025-11-10T13:43:24.814699"},
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
                        60.18,
                        61.38,
                        51.55,
                        50.17,
                        51.24,
                        50.37,
                        60.69,
                        44.5,
                        55.5,
                        46.79,
                        56.23,
                        53.05
                ],
                "unit": "%"
        },
        "current": {
                "value": 53.05,
                "unit": "%",
                "change": -3.18,
                "change_percent": -5.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 53.47,
                "min": 44.5,
                "max": 61.38,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.8,
                        "percentage": 20.4
                },
                {
                        "category": "Category B",
                        "value": 7.39,
                        "percentage": 13.9
                },
                {
                        "category": "Category C",
                        "value": 8.31,
                        "percentage": 15.7
                },
                {
                        "category": "Category D",
                        "value": 3.63,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 22.92,
                        "percentage": 43.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.814699",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Account Profitability Analysis"
        }
    },
}
