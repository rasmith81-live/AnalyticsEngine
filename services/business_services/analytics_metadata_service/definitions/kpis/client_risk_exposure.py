"""
Client Risk Exposure

The level of risk associated with a key account, based on factors like financial stability, market position, etc.
"""

CLIENT_RISK_EXPOSURE = {
    "code": "CLIENT_RISK_EXPOSURE",
    "name": "Client Risk Exposure",
    "description": "The level of risk associated with a key account, based on factors like financial stability, market position, etc.",
    "formula": "Revenue from Key Client / Total Revenue",
    "calculation_formula": "Revenue from Key Client / Total Revenue",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Client Risk Exposure to be added.",
    "trend_analysis": """



    * Increasing client risk exposure may indicate financial instability or market challenges for the key account.
    * Decreasing risk exposure could signal improved financial health or market position for the key account.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific factors contribute to the current level of risk exposure for the key account?
    * How does the client risk exposure compare to industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Regularly assess and monitor the financial stability and market dynamics of key accounts.
    * Diversify the customer portfolio to spread risk across multiple accounts.
    * Implement credit risk management strategies to mitigate potential financial challenges.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of client risk exposure over time.
    * Comparison charts to visualize risk exposure across different key accounts.
    
    
    
    """,
    "risk_warnings": """



    * High client risk exposure may lead to potential bad debt or financial losses.
    * Significant fluctuations in risk exposure could impact overall revenue and profitability.
    
    
    
    """,
    "tracking_tools": """



    * Financial analysis software to assess the creditworthiness and financial stability of key accounts.
    * Market research tools to track and analyze the market position of key accounts.
    
    
    
    """,
    "integration_points": """



    * Integrate client risk exposure data with financial management systems for comprehensive risk assessment.
    * Link risk exposure with sales forecasting to align sales strategies with potential risks.
    
    
    
    """,
    "change_impact_analysis": """



    * Changes in client risk exposure can impact credit terms, financing decisions, and overall business risk.
    * High client risk exposure may require additional resources for credit management and collection efforts.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Lost Sale", "Market Segment", "Renewal Management", "Revenue Forecast", "Sale", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.698428"},
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
                        751.2,
                        690.39,
                        694.87,
                        721.77,
                        808.61,
                        755.17,
                        820.61,
                        687.53,
                        749.53,
                        736.11,
                        801.71,
                        740.58
                ],
                "unit": "units"
        },
        "current": {
                "value": 740.58,
                "unit": "units",
                "change": -61.13,
                "change_percent": -7.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 746.51,
                "min": 687.53,
                "max": 820.61,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 146.62,
                        "percentage": 19.8
                },
                {
                        "category": "Segment B",
                        "value": 95.42,
                        "percentage": 12.9
                },
                {
                        "category": "Segment C",
                        "value": 161.36,
                        "percentage": 21.8
                },
                {
                        "category": "Segment D",
                        "value": 69.63,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 267.55,
                        "percentage": 36.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.475056",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Client Risk Exposure"
        }
    },
}
