"""
Partner Equity Score

A measure of the value channel partners perceive in their relationship with the company, factoring in financial, support, and strategic elements.
"""

PARTNER_EQUITY_SCORE = {
    "code": "PARTNER_EQUITY_SCORE",
    "name": "Partner Equity Score",
    "description": "A measure of the value channel partners perceive in their relationship with the company, factoring in financial, support, and strategic elements.",
    "formula": "Qualitative Assessment Score of Partner Equity",
    "calculation_formula": "Qualitative Assessment Score of Partner Equity",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Equity Score to be added.",
    "trend_analysis": """


    * Increasing partner equity score may indicate improved financial incentives, better support, or more strategic alignment with partners.
    * A decreasing score could signal dissatisfaction with the partnership, lack of support, or changes in the competitive landscape.
    
    
    """,
    "diagnostic_questions": """


    * What specific elements of the partnership are contributing to the perceived value for our channel partners?
    * Are there any recent changes in our support, financial incentives, or strategic direction that could be impacting partner equity score?
    
    
    """,
    "actionable_tips": """


    * Regularly engage with channel partners to understand their needs and challenges.
    * Provide additional training and resources to help partners maximize the value they receive from the partnership.
    * Align incentives and rewards with the desired behaviors and outcomes for channel partners.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of partner equity score over time.
    * Comparative bar charts to visualize partner equity score across different regions or partner types.
    
    
    """,
    "risk_warnings": """


    * Low partner equity score may lead to partners seeking out other, more valuable partnerships.
    * Perceived lack of value in the partnership can result in decreased sales and market share through the channel.
    
    
    """,
    "tracking_tools": """


    * Partner relationship management (PRM) software to track and analyze partner interactions and satisfaction.
    * Feedback and survey tools to gather input from channel partners on their perception of the partnership.
    
    
    """,
    "integration_points": """


    * Integrate partner equity score data with sales performance metrics to understand the impact on revenue and market share.
    * Link partner equity score with marketing efforts to ensure alignment in messaging and support for channel partners.
    
    
    """,
    "change_impact_analysis": """


    * Improving partner equity score can lead to increased sales, market share, and overall channel performance.
    * Conversely, a declining score may result in decreased sales and market share through the channel, impacting overall business performance.
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Partnership", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Strategic Initiative", "Strategic Review", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.194135"},
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
                        71.0,
                        64.6,
                        62.5,
                        65.8,
                        62.3,
                        63.6,
                        67.1,
                        59.3,
                        59.2,
                        61.6,
                        67.5,
                        62.4
                ],
                "unit": "score"
        },
        "current": {
                "value": 62.4,
                "unit": "score",
                "change": -5.1,
                "change_percent": -7.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.91,
                "min": 59.2,
                "max": 71.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.07,
                        "percentage": 24.2
                },
                {
                        "category": "Category B",
                        "value": 13.19,
                        "percentage": 21.1
                },
                {
                        "category": "Category C",
                        "value": 6.61,
                        "percentage": 10.6
                },
                {
                        "category": "Category D",
                        "value": 3.19,
                        "percentage": 5.1
                },
                {
                        "category": "Other",
                        "value": 24.34,
                        "percentage": 39.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.866575",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Partner Equity Score"
        }
    },
}
