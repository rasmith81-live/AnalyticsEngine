"""
Win/Loss Ratio

The ratio of won sales to lost opportunities, helping to assess the competitiveness and effectiveness of the sales process.
"""

WINLOSS_RATIO = {
    "code": "WINLOSS_RATIO",
    "name": "Win/Loss Ratio",
    "description": "The ratio of won sales to lost opportunities, helping to assess the competitiveness and effectiveness of the sales process.",
    "formula": "Number of Sales Won / Number of Sales Lost",
    "calculation_formula": "Number of Sales Won / Number of Sales Lost",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Win/Loss Ratio to be added.",
    "trend_analysis": """



    * An increasing win-loss ratio may indicate improved sales strategies or a stronger market position.
    * A decreasing ratio could signal increased competition or inefficiencies in the sales process.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales tactics or approaches that have contributed to recent wins or losses?
    * How does our win-loss ratio compare with industry benchmarks or with our competitors?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional sales training and resources to improve the effectiveness of the sales team.
    * Regularly review and update the sales process to adapt to changing market conditions and customer needs.
    * Implement a robust customer relationship management (CRM) system to better track and manage sales opportunities.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of win-loss ratio over time.
    * Stacked bar charts comparing win and loss percentages across different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low win-loss ratio may indicate a need for significant changes in sales strategies or team composition.
    * High fluctuations in the win-loss ratio could point to instability in the sales process or market conditions.
    
    
    
    """,
    "tracking_tools": """



    * CRM software such as Salesforce or HubSpot for tracking and managing sales opportunities.
    * Sales performance analytics tools like InsightSquared or Clari for deeper insights into win-loss patterns.
    
    
    
    """,
    "integration_points": """



    * Integrate win-loss ratio data with sales forecasting systems to better predict future performance and resource needs.
    * Link with customer feedback platforms to understand the impact of wins and losses on overall customer satisfaction.
    
    
    
    """,
    "change_impact_analysis": """



    * An improved win-loss ratio can lead to increased revenue and market share, but may also require adjustments in sales strategies and resource allocation.
    * Conversely, a declining ratio may lead to decreased confidence from stakeholders and potential shifts in investment priorities.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lost Sale", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.817974"},
    "required_objects": [],
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
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
                        60.68,
                        66.67,
                        61.35,
                        62.4,
                        54.64,
                        65.88,
                        72.2,
                        60.49,
                        70.36,
                        66.17,
                        60.29,
                        59.09
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.09,
                "unit": "%",
                "change": -1.2,
                "change_percent": -2.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.35,
                "min": 54.64,
                "max": 72.2,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 12.95,
                        "percentage": 21.9
                },
                {
                        "category": "Channel Sales",
                        "value": 14.45,
                        "percentage": 24.5
                },
                {
                        "category": "Online Sales",
                        "value": 7.85,
                        "percentage": 13.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 6.71,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 17.13,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:14.004656",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Win/Loss Ratio"
        }
    },
}
