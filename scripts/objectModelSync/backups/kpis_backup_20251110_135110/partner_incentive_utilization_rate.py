"""
Partner Incentive Utilization Rate

The rate at which channel partners make use of available incentives, which can indicate the effectiveness of incentive programs.
"""

PARTNER_INCENTIVE_UTILIZATION_RATE = {
    "code": "PARTNER_INCENTIVE_UTILIZATION_RATE",
    "name": "Partner Incentive Utilization Rate",
    "description": "The rate at which channel partners make use of available incentives, which can indicate the effectiveness of incentive programs.",
    "formula": "(Value of Incentives Claimed by Partners / Total Value of Incentives Offered) * 100",
    "calculation_formula": "(Value of Incentives Claimed by Partners / Total Value of Incentives Offered) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Incentive Utilization Rate to be added.",
    "trend_analysis": """


    * Increasing partner incentive utilization rate may indicate the effectiveness of incentive programs or improved partner engagement.
    * Decreasing utilization could signal a need to reevaluate the incentive structure or communication of available incentives to partners.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific types of incentives that are consistently underutilized?
    * How does our partner incentive utilization rate compare with industry benchmarks or with historical data?
    
    
    """,
    "actionable_tips": """


    * Regularly communicate available incentives to partners and provide clear guidelines on how to utilize them.
    * Collect feedback from partners on the effectiveness of current incentives and make adjustments accordingly.
    * Offer training and support to help partners take full advantage of available incentives.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of partner incentive utilization rate over time.
    * Pie charts to compare the utilization rates of different types of incentives.
    
    
    """,
    "risk_warnings": """


    * Low partner incentive utilization rates may indicate a lack of partner engagement or dissatisfaction with the current incentive offerings.
    * High utilization rates for certain incentives may suggest an over-reliance on those incentives or a lack of diversity in the incentive programs.
    
    
    """,
    "tracking_tools": """


    * Partner relationship management (PRM) software to track and analyze partner engagement and incentive utilization.
    * Data analytics tools to identify patterns and correlations between incentive utilization and partner performance.
    
    
    """,
    "integration_points": """


    * Integrate partner incentive utilization data with sales performance metrics to understand the impact of incentives on overall sales results.
    * Link incentive utilization with partner feedback and satisfaction data to gain a comprehensive view of partner engagement.
    
    
    """,
    "change_impact_analysis": """


    * Increasing partner incentive utilization can lead to higher sales and improved partner loyalty, but may also increase incentive costs.
    * Conversely, low utilization rates may result in missed sales opportunities and strained partner relationships.
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.197854"},
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
                        67.24,
                        56.85,
                        54.82,
                        68.89,
                        50.69,
                        54.49,
                        66.9,
                        53.35,
                        54.86,
                        67.56,
                        55.32,
                        51.29
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.29,
                "unit": "%",
                "change": -4.03,
                "change_percent": -7.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 58.52,
                "min": 50.69,
                "max": 68.89,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.02,
                        "percentage": 15.6
                },
                {
                        "category": "Category B",
                        "value": 9.56,
                        "percentage": 18.6
                },
                {
                        "category": "Category C",
                        "value": 11.37,
                        "percentage": 22.2
                },
                {
                        "category": "Category D",
                        "value": 4.73,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 17.61,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.871239",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Incentive Utilization Rate"
        }
    },
}
