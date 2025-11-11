"""
Peer-to-Peer Learning Engagement

The level of engagement in peer-to-peer learning activities within the sales team.
"""

PEER_TO_PEER_LEARNING_ENGAGEMENT = {
    "code": "PEER_TO_PEER_LEARNING_ENGAGEMENT",
    "name": "Peer-to-Peer Learning Engagement",
    "description": "The level of engagement in peer-to-peer learning activities within the sales team.",
    "formula": "Number of Peer-to-Peer Learning Activities Participated In / Total Number of Peer-to-Peer Learning Opportunities",
    "calculation_formula": "Number of Peer-to-Peer Learning Activities Participated In / Total Number of Peer-to-Peer Learning Opportunities",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Peer-to-Peer Learning Engagement to be added.",
    "trend_analysis": """

    * Increasing engagement in peer-to-peer learning may indicate a positive shift in team collaboration and knowledge sharing.
    * Decreasing engagement could signal a lack of interest or participation in learning activities, potentially impacting overall team performance.
    
    """,
    "diagnostic_questions": """

    * Are there specific topics or areas where peer-to-peer learning is more or less popular?
    * How does the level of engagement in peer-to-peer learning compare with other forms of training or coaching?
    
    """,
    "actionable_tips": """

    * Encourage team leaders to actively participate in peer-to-peer learning to set a positive example.
    * Provide incentives or recognition for individuals who contribute significantly to peer-to-peer learning activities.
    * Offer diverse and engaging learning opportunities to cater to different learning styles and preferences within the sales team.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of engagement in peer-to-peer learning over time.
    * Comparison bar charts displaying engagement levels across different teams or departments.
    
    """,
    "risk_warnings": """

    * Low engagement in peer-to-peer learning may lead to knowledge silos and reduced overall team performance.
    * Over-reliance on peer-to-peer learning without proper guidance or oversight may result in misinformation or inconsistent training.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) to track and analyze participation in peer-to-peer learning activities.
    * Collaboration tools such as Slack or Microsoft Teams to facilitate communication and knowledge sharing among team members.
    
    """,
    "integration_points": """

    * Integrate engagement data with performance management systems to assess the impact of peer-to-peer learning on sales outcomes.
    * Link peer-to-peer learning activities with individual development plans to align learning goals with career growth.
    
    """,
    "change_impact_analysis": """

    * Increased engagement in peer-to-peer learning can lead to a more knowledgeable and skilled sales team, potentially improving overall sales performance.
    * Conversely, low engagement may result in missed opportunities for skill development and knowledge transfer, impacting long-term team effectiveness.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.919391"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
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
                        452,
                        452,
                        429,
                        422,
                        472,
                        467,
                        456,
                        458,
                        432,
                        431,
                        432,
                        465
                ],
                "unit": "count"
        },
        "current": {
                "value": 465,
                "unit": "count",
                "change": 33,
                "change_percent": 7.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 447.33,
                "min": 422,
                "max": 472,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 142.02,
                        "percentage": 30.5
                },
                {
                        "category": "Category B",
                        "value": 67.78,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 47.64,
                        "percentage": 10.2
                },
                {
                        "category": "Category D",
                        "value": 60.38,
                        "percentage": 13.0
                },
                {
                        "category": "Other",
                        "value": 147.18,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.919391",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Peer-to-Peer Learning Engagement"
        }
    },
}
