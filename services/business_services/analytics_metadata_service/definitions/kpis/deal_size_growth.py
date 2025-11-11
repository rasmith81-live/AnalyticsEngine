"""
Deal Size Growth

The change in average size or value of sales deals over time.
"""

DEAL_SIZE_GROWTH = {
    "code": "DEAL_SIZE_GROWTH",
    "name": "Deal Size Growth",
    "description": "The change in average size or value of sales deals over time.",
    "formula": "(Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size * 100",
    "calculation_formula": "(Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Size Growth to be added.",
    "trend_analysis": """



    * Increasing deal size growth may indicate successful upselling or cross-selling strategies.
    * Decreasing deal size growth could signal increased competition or pricing pressure.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors have contributed to the recent changes in deal size growth?
    * Are there specific customer segments or product lines driving the fluctuations in deal size?
    
    
    
    """,
    "actionable_tips": """



    * Implement targeted sales training to improve upselling and cross-selling techniques.
    * Conduct pricing analysis to ensure competitiveness without sacrificing profitability.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing deal size growth over time.
    * Comparison bar charts to visualize deal size growth by customer segment or product category.
    
    
    
    """,
    "risk_warnings": """



    * Significant fluctuations in deal size growth may impact revenue forecasts and financial planning.
    * Consistently declining deal size growth could indicate a need for strategic reevaluation of sales tactics.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze customer purchasing patterns.
    * Business intelligence tools for in-depth sales performance analysis and trend identification.
    
    
    
    """,
    "integration_points": """



    * Integrate deal size growth data with sales pipeline management to align sales strategies with changing deal sizes.
    * Link deal size growth with customer feedback systems to understand the impact of sales strategies on customer satisfaction.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing deal size growth may lead to higher revenue and improved sales team motivation.
    * Decreasing deal size growth could impact sales team morale and require adjustments to sales targets and incentives.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Deal", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.913454"},
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
                        66.14,
                        61.19,
                        66.11,
                        77.95,
                        65.11,
                        64.99,
                        68.67,
                        72.45,
                        72.69,
                        62.7,
                        73.81,
                        74.03
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.03,
                "unit": "%",
                "change": 0.22,
                "change_percent": 0.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 68.82,
                "min": 61.19,
                "max": 77.95,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.72,
                        "percentage": 19.9
                },
                {
                        "category": "Segment B",
                        "value": 16.45,
                        "percentage": 22.2
                },
                {
                        "category": "Segment C",
                        "value": 9.11,
                        "percentage": 12.3
                },
                {
                        "category": "Segment D",
                        "value": 6.43,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 27.32,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.887574",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Deal Size Growth"
        }
    },
}
