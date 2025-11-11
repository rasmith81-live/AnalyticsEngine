"""
Peer-to-Peer Coaching Participation Rate

The percentage of sales team members who participate in peer-to-peer coaching sessions.
"""

PEER_TO_PEER_COACHING_PARTICIPATION_RATE = {
    "code": "PEER_TO_PEER_COACHING_PARTICIPATION_RATE",
    "name": "Peer-to-Peer Coaching Participation Rate",
    "description": "The percentage of sales team members who participate in peer-to-peer coaching sessions.",
    "formula": "(Number of Sales Reps Participating in Coaching / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Sales Reps Participating in Coaching / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Peer-to-Peer Coaching Participation Rate to be added.",
    "trend_analysis": """



    * Increasing participation rate may indicate a positive shift in team collaboration and knowledge sharing.
    * Decreasing participation could signal disengagement or lack of buy-in from the sales team.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific topics or areas where peer-to-peer coaching sessions are more popular or less popular?
    * How does the participation rate correlate with sales performance or team satisfaction?
    
    
    
    """,
    "actionable_tips": """



    * Encourage senior or high-performing team members to lead coaching sessions to increase interest and engagement.
    * Provide incentives or recognition for active participation in coaching sessions.
    * Regularly solicit feedback from sales team members to understand their preferences and needs for coaching topics.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of participation rate over time.
    * Pie charts to compare participation rates across different coaching topics or leaders.
    
    
    
    """,
    "risk_warnings": """



    * Low participation rates may lead to missed opportunities for knowledge sharing and skill development.
    * Consistently low participation could indicate deeper issues with team dynamics or coaching effectiveness.
    
    
    
    """,
    "tracking_tools": """



    * Collaboration platforms like Slack or Microsoft Teams to facilitate communication and scheduling for coaching sessions.
    * Survey tools to gather feedback and preferences from sales team members regarding coaching topics and formats.
    
    
    
    """,
    "integration_points": """



    * Integrate participation rate data with individual sales performance metrics to identify correlations and opportunities for improvement.
    * Link coaching participation with employee development plans and performance reviews to align coaching with career growth.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing participation can lead to improved sales performance and team cohesion, but may require additional resources for coaching support.
    * Low participation rates can impact overall team morale and knowledge sharing, potentially affecting the entire sales organization's performance.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.226541"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        75.7,
                        65.14,
                        75.01,
                        76.87,
                        79.98,
                        61.84,
                        74.32,
                        66.17,
                        79.1,
                        62.2,
                        67.56,
                        64.8
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.8,
                "unit": "%",
                "change": -2.76,
                "change_percent": -4.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 70.72,
                "min": 61.84,
                "max": 79.98,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 9.89,
                        "percentage": 15.3
                },
                {
                        "category": "Channel Sales",
                        "value": 11.64,
                        "percentage": 18.0
                },
                {
                        "category": "Online Sales",
                        "value": 11.87,
                        "percentage": 18.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.38,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 28.02,
                        "percentage": 43.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.537629",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Peer-to-Peer Coaching Participation Rate"
        }
    },
}
