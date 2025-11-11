"""
Channel Engagement Score

The level of active involvement and collaboration of channel partners in the sales process.
"""

CHANNEL_ENGAGEMENT_SCORE = {
    "code": "CHANNEL_ENGAGEMENT_SCORE",
    "name": "Channel Engagement Score",
    "description": "The level of active involvement and collaboration of channel partners in the sales process.",
    "formula": "Total Points Earned by Partners (based on interactions) / Total Possible Points",
    "calculation_formula": "Total Points Earned by Partners (based on interactions) / Total Possible Points",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Channel Engagement Score to be added.",
    "trend_analysis": """



    * An increasing channel engagement score may indicate stronger collaboration and support from channel partners, leading to improved sales performance.
    * A decreasing score could signal disengagement or dissatisfaction among channel partners, potentially impacting sales and market reach.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or regions where channel partners are more or less engaged?
    * How does our channel engagement score compare with industry benchmarks or with historical data?
    
    
    
    """,
    "actionable_tips": """



    * Provide regular training and support to channel partners to ensure they are equipped to effectively sell and promote the products.
    * Offer incentives and rewards for high-performing channel partners to encourage continued engagement and collaboration.
    * Regularly communicate with channel partners to gather feedback and address any issues or concerns they may have.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of channel engagement score over time.
    * Pie charts to compare the distribution of channel engagement scores across different partner segments or regions.
    
    
    
    """,
    "risk_warnings": """



    * Low channel engagement may lead to missed sales opportunities and reduced market penetration.
    * Disengaged channel partners may seek out alternative products or suppliers, impacting brand loyalty and market share.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) systems to track and manage interactions with channel partners.
    * Partner relationship management (PRM) software to streamline communication and collaboration with channel partners.
    
    
    
    """,
    "integration_points": """



    * Integrate channel engagement data with sales performance metrics to understand the impact of partner involvement on overall sales results.
    * Link channel engagement score with marketing and promotional activities to align partner efforts with strategic initiatives.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving channel engagement can lead to increased sales and market share, but may require additional resources and support.
    * Decreasing channel engagement may result in decreased sales and market reach, impacting overall business performance.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Lead", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.681123"},
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
                        76.3,
                        74.3,
                        69.1,
                        66.6,
                        78.2,
                        67.2,
                        70.0,
                        67.1,
                        73.0,
                        70.9,
                        71.5,
                        75.2
                ],
                "unit": "score"
        },
        "current": {
                "value": 75.2,
                "unit": "score",
                "change": 3.7,
                "change_percent": 5.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.62,
                "min": 66.6,
                "max": 78.2,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 21.34,
                        "percentage": 28.4
                },
                {
                        "category": "Segment B",
                        "value": 15.73,
                        "percentage": 20.9
                },
                {
                        "category": "Segment C",
                        "value": 11.92,
                        "percentage": 15.9
                },
                {
                        "category": "Segment D",
                        "value": 2.8,
                        "percentage": 3.7
                },
                {
                        "category": "Other",
                        "value": 23.41,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.437191",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Channel Engagement Score"
        }
    },
}
