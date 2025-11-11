"""
Key Account Growth Rate

The growth rate of sales within key accounts that are critical to the company's success.
"""

KEY_ACCOUNT_GROWTH_RATE = {
    "code": "KEY_ACCOUNT_GROWTH_RATE",
    "name": "Key Account Growth Rate",
    "description": "The growth rate of sales within key accounts that are critical to the company's success.",
    "formula": "(Current Period Revenue from Key Accounts - Previous Period Revenue from Key Accounts) / Previous Period Revenue from Key Accounts * 100",
    "calculation_formula": "(Current Period Revenue from Key Accounts - Previous Period Revenue from Key Accounts) / Previous Period Revenue from Key Accounts * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Key Account Growth Rate to be added.",
    "trend_analysis": """



    * Key account growth rate tends to increase as the company expands its product offerings or enters new markets.
    * A declining growth rate may indicate increased competition or a shift in customer preferences.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors have historically contributed to the growth of key accounts?
    * Are there specific industries or regions where key account growth is stronger or weaker?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and update key account strategies to align with changing market dynamics.
    * Invest in relationship-building activities and personalized sales approaches for key accounts.
    * Offer exclusive incentives or promotions to encourage repeat business and expansion within key accounts.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the growth rate of key accounts over time.
    * Pie charts comparing the contribution of different key accounts to overall sales growth.
    
    
    
    """,
    "risk_warnings": """



    * Over-reliance on a few key accounts can make the company vulnerable to economic downturns or changes in those specific industries.
    * Failure to nurture key accounts may result in lost opportunities and decreased overall sales growth.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track interactions and opportunities within key accounts.
    * Data analytics tools to identify patterns and opportunities for growth within key accounts.
    
    
    
    """,
    "integration_points": """



    * Integrate key account growth rate analysis with sales forecasting to align resources and strategies accordingly.
    * Link key account performance with marketing efforts to ensure consistent messaging and support for key accounts.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving key account growth rate can lead to increased revenue and market share, but may also require additional resources for account management.
    * A decline in key account growth rate can impact overall sales performance and may require strategic adjustments in product offerings or target markets.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.991694"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        60.29,
                        41.18,
                        51.21,
                        47.12,
                        48.3,
                        42.73,
                        56.14,
                        57.53,
                        51.51,
                        59.18,
                        41.58,
                        57.7
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.7,
                "unit": "%",
                "change": 16.12,
                "change_percent": 38.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 51.21,
                "min": 41.18,
                "max": 60.29,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 12.48,
                        "percentage": 21.6
                },
                {
                        "category": "Mid-Market",
                        "value": 7.65,
                        "percentage": 13.3
                },
                {
                        "category": "Small Business",
                        "value": 9.22,
                        "percentage": 16.0
                },
                {
                        "category": "Strategic Partners",
                        "value": 7.68,
                        "percentage": 13.3
                },
                {
                        "category": "Other",
                        "value": 20.67,
                        "percentage": 35.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.081384",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Key Account Growth Rate"
        }
    },
}
