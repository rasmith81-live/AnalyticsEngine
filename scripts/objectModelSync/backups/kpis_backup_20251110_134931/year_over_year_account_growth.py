"""
Year-over-Year Account Growth

Metric to measure the growth of key accounts in terms of sales or revenue from one year to the next.
"""

YEAR_OVER_YEAR_ACCOUNT_GROWTH = {
    "code": "YEAR_OVER_YEAR_ACCOUNT_GROWTH",
    "name": "Year-over-Year Account Growth",
    "description": "Metric to measure the growth of key accounts in terms of sales or revenue from one year to the next.",
    "formula": "(Current Year Revenue from Account - Previous Year Revenue from Account) / Previous Year Revenue from Account * 100",
    "calculation_formula": "(Current Year Revenue from Account - Previous Year Revenue from Account) / Previous Year Revenue from Account * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Year-over-Year Account Growth to be added.",
    "trend_analysis": """

    * Year-over-year account growth may show consistent upward trends, indicating successful customer retention and expansion strategies.
    * Fluctuating growth rates could signal changes in market conditions, customer behavior, or internal sales efforts.
    
    """,
    "diagnostic_questions": """

    * What specific factors contribute to the growth or decline of key accounts?
    * Are there any common characteristics among accounts that show significant growth versus those that stagnate or decline?
    
    """,
    "actionable_tips": """

    * Regularly review and update key account management strategies to align with changing customer needs and market dynamics.
    * Invest in customer relationship management (CRM) tools to better track account growth and identify opportunities for upselling or cross-selling.
    * Provide ongoing training and support for sales teams to enhance their ability to nurture and grow key accounts.
    
    """,
    "visualization_suggestions": """

    * Line charts to visualize the year-over-year growth trajectory for individual key accounts.
    * Pie charts to compare the contribution of different accounts to overall sales growth.
    
    """,
    "risk_warnings": """

    * Stagnant or declining account growth may lead to increased customer attrition and revenue loss.
    * Rapid growth in key accounts without proper support or resources may strain operational capabilities and lead to service quality issues.
    
    """,
    "tracking_tools": """

    * CRM systems with robust reporting and analytics capabilities to track account growth and customer interactions.
    * Data visualization tools to create clear and informative charts and graphs for presenting account growth trends.
    
    """,
    "integration_points": """

    * Integrate account growth data with sales forecasting and resource allocation systems to ensure adequate support for expanding accounts.
    * Link account growth metrics with customer satisfaction surveys and feedback mechanisms to gauge the impact of growth on customer experience.
    
    """,
    "change_impact_analysis": """

    * Positive account growth can lead to increased revenue, customer loyalty, and market share.
    * However, rapid growth may strain operational resources and require adjustments in service delivery and support processes.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:25.288217"},
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
                        138,
                        138,
                        113,
                        111,
                        136,
                        127,
                        129,
                        114,
                        128,
                        130,
                        110,
                        114
                ],
                "unit": "count"
        },
        "current": {
                "value": 114,
                "unit": "count",
                "change": 4,
                "change_percent": 3.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 124.0,
                "min": 110,
                "max": 138,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 27.16,
                        "percentage": 23.8
                },
                {
                        "category": "Category B",
                        "value": 26.18,
                        "percentage": 23.0
                },
                {
                        "category": "Category C",
                        "value": 20.98,
                        "percentage": 18.4
                },
                {
                        "category": "Category D",
                        "value": 10.1,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 29.58,
                        "percentage": 25.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.288217",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Year-over-Year Account Growth"
        }
    },
}
