"""
Channel Partner Growth Rate

The rate at which individual channel partners grow in terms of their business with the company, which can be measured in sales or other metrics.
"""

CHANNEL_PARTNER_GROWTH_RATE = {
    "code": "CHANNEL_PARTNER_GROWTH_RATE",
    "name": "Channel Partner Growth Rate",
    "description": "The rate at which individual channel partners grow in terms of their business with the company, which can be measured in sales or other metrics.",
    "formula": "((Number of Active Partners at End of Period - Number at Beginning of Period) / Number at Beginning of Period) * 100",
    "calculation_formula": "((Number of Active Partners at End of Period - Number at Beginning of Period) / Number at Beginning of Period) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Channel Partner Growth Rate to be added.",
    "trend_analysis": """

    * Increasing channel partner growth rate may indicate successful onboarding and support programs for new partners.
    * A decreasing growth rate could signal dissatisfaction among existing partners or increased competition in the market.
    
    """,
    "diagnostic_questions": """

    * Are there specific regions or industries where channel partner growth is particularly strong or weak?
    * What factors contribute to the success of high-growth channel partners, and how can those strategies be replicated?
    
    """,
    "actionable_tips": """

    * Provide additional training and resources to underperforming channel partners to help them grow their business.
    * Regularly review and update the channel partner program to ensure it remains competitive and attractive.
    * Implement a referral program to incentivize existing partners to bring in new business.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the growth rate of individual channel partners over time.
    * Pie charts comparing the distribution of high-growth, moderate-growth, and low-growth partners.
    
    """,
    "risk_warnings": """

    * Rapid growth in a few partners may lead to overreliance on a small number of channels, increasing vulnerability to market changes.
    * Slow growth across the board may indicate a lack of competitiveness or support for the channel partner program.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track partner interactions and identify growth opportunities.
    * Partner Relationship Management (PRM) platforms to streamline partner onboarding, training, and support.
    
    """,
    "integration_points": """

    * Integrate channel partner growth data with sales performance metrics to understand the impact of partner growth on overall revenue.
    * Link growth rate analysis with marketing efforts to identify which campaigns or initiatives are driving partner success.
    
    """,
    "change_impact_analysis": """

    * Increasing channel partner growth can lead to expanded market reach and increased sales, but may also require additional resources for support and management.
    * A decline in partner growth may signal the need for strategic adjustments to the partner program or market approach.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.092218"},
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
                        63.4,
                        60.59,
                        53.47,
                        58.15,
                        52.13,
                        63.3,
                        61.26,
                        57.04,
                        50.57,
                        50.22,
                        51.25,
                        52.74
                ],
                "unit": "%"
        },
        "current": {
                "value": 52.74,
                "unit": "%",
                "change": 1.49,
                "change_percent": 2.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 56.18,
                "min": 50.22,
                "max": 63.4,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.82,
                        "percentage": 16.7
                },
                {
                        "category": "Category B",
                        "value": 14.93,
                        "percentage": 28.3
                },
                {
                        "category": "Category C",
                        "value": 5.11,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 6.0,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 17.88,
                        "percentage": 33.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.092218",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Channel Partner Growth Rate"
        }
    },
}
