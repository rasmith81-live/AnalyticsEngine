"""
Upsell/cross-sell Ratio

The ratio of additional products or services sold to existing key accounts.
"""

UPSELLCROSS_SELL_RATIO = {
    "code": "UPSELLCROSS_SELL_RATIO",
    "name": "Upsell/cross-sell Ratio",
    "description": "The ratio of additional products or services sold to existing key accounts.",
    "formula": "(Number of Upsell/Cross-sell Sales / Total Number of Transactions) * 100",
    "calculation_formula": "(Number of Upsell/Cross-sell Sales / Total Number of Transactions) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Upsell/cross-sell Ratio to be added.",
    "trend_analysis": """


    * An increasing upsell/cross-sell ratio may indicate successful sales strategies or a strong understanding of customer needs.
    * A decreasing ratio could signal a lack of focus on customer retention or a failure to identify additional sales opportunities.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific products or services that are frequently upsold or cross-sold to key accounts?
    * How does our upsell/cross-sell ratio compare with industry benchmarks or with historical data?
    
    
    """,
    "actionable_tips": """


    * Train sales teams to identify upsell and cross-sell opportunities during customer interactions.
    * Implement a customer relationship management (CRM) system to track customer preferences and purchase history.
    * Offer bundled discounts or promotions to incentivize additional purchases from key accounts.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the upsell/cross-sell ratio over time to identify trends and seasonality.
    * Pie charts to visualize the distribution of additional products or services sold to key accounts.
    
    
    """,
    "risk_warnings": """


    * A low upsell/cross-sell ratio may lead to missed revenue opportunities and reduced customer lifetime value.
    * Overemphasis on upselling and cross-selling may lead to customer dissatisfaction if not done thoughtfully.
    
    
    """,
    "tracking_tools": """


    * CRM systems with built-in upsell/cross-sell tracking capabilities, such as Salesforce or HubSpot.
    * Data analytics tools to identify patterns and preferences of key accounts for targeted upselling and cross-selling.
    
    
    """,
    "integration_points": """


    * Integrate upsell/cross-sell data with customer support systems to provide personalized recommendations during customer interactions.
    * Link with inventory management systems to ensure availability of additional products or services for key accounts.
    
    
    """,
    "change_impact_analysis": """


    * Improving the upsell/cross-sell ratio can lead to increased revenue and customer satisfaction, but may require additional resources for personalized sales efforts.
    * Conversely, a declining ratio may indicate a need for reevaluation of sales strategies and customer relationship management.
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Product", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.769586"},
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
                        53.64,
                        43.56,
                        55.19,
                        38.07,
                        38.56,
                        54.81,
                        44.63,
                        50.56,
                        54.22,
                        47.73,
                        44.87,
                        55.27
                ],
                "unit": "%"
        },
        "current": {
                "value": 55.27,
                "unit": "%",
                "change": 10.4,
                "change_percent": 23.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 48.43,
                "min": 38.07,
                "max": 55.27,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.1,
                        "percentage": 21.9
                },
                {
                        "category": "Category B",
                        "value": 11.42,
                        "percentage": 20.7
                },
                {
                        "category": "Category C",
                        "value": 7.91,
                        "percentage": 14.3
                },
                {
                        "category": "Category D",
                        "value": 3.45,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 20.39,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.183893",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Upsell/cross-sell Ratio"
        }
    },
}
