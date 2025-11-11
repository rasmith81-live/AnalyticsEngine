"""
Partner Deal Size Growth

The change in the average deal size closed by channel partners over time, indicating the partners' growing sales capability.
"""

PARTNER_DEAL_SIZE_GROWTH = {
    "code": "PARTNER_DEAL_SIZE_GROWTH",
    "name": "Partner Deal Size Growth",
    "description": "The change in the average deal size closed by channel partners over time, indicating the partners' growing sales capability.",
    "formula": "((Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size) * 100",
    "calculation_formula": "((Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Deal Size Growth to be added.",
    "trend_analysis": """


    * Increasing partner deal size growth may indicate improved sales training and enablement for partners.
    * Decreasing growth could signal market saturation or a lack of new opportunities being pursued by partners.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific product lines or customer segments where partners are seeing the most significant deal size growth?
    * How does the partner deal size growth compare with industry benchmarks or competitors' performance?
    
    
    """,
    "actionable_tips": """


    * Provide additional sales training and resources to help partners target higher-value opportunities.
    * Encourage partners to focus on cross-selling and upselling to increase deal sizes.
    * Explore new market segments or industries where partners can pursue larger deals.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend in average deal size over time for each partner.
    * Bar graphs comparing average deal sizes across different partner groups or regions.
    
    
    """,
    "risk_warnings": """


    * Rapid partner deal size growth may lead to increased competition and potential margin erosion.
    * Stagnant or declining deal size growth could indicate a need for reevaluation of the partner ecosystem and sales strategies.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) systems to track and analyze partner deal sizes and trends.
    * Business Intelligence (BI) tools to identify patterns and opportunities for deal size growth.
    
    
    """,
    "integration_points": """


    * Integrate partner deal size data with sales performance metrics to understand the impact on overall revenue and profitability.
    * Link deal size growth with partner incentive and reward programs to align incentives with desired outcomes.
    
    
    """,
    "change_impact_analysis": """


    * Increasing partner deal size growth can positively impact overall revenue and profitability.
    * However, it may also require adjustments in sales strategies and resource allocation to support larger deals.
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.188690"},
    "required_objects": [],
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
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
                        642.86,
                        772.25,
                        653.51,
                        748.08,
                        649.76,
                        641.09,
                        780.0,
                        754.73,
                        743.88,
                        683.39,
                        741.51,
                        683.46
                ],
                "unit": "units"
        },
        "current": {
                "value": 683.46,
                "unit": "units",
                "change": -58.05,
                "change_percent": -7.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 707.88,
                "min": 641.09,
                "max": 780.0,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 182.31,
                        "percentage": 26.7
                },
                {
                        "category": "Category B",
                        "value": 164.35,
                        "percentage": 24.0
                },
                {
                        "category": "Category C",
                        "value": 117.75,
                        "percentage": 17.2
                },
                {
                        "category": "Category D",
                        "value": 64.3,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 154.75,
                        "percentage": 22.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.860732",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Partner Deal Size Growth"
        }
    },
}
