"""
Partner Training Completion Rate

The percentage of channel partners who complete mandatory training programs, ensuring they are well-equipped to sell and support the products.
"""

PARTNER_TRAINING_COMPLETION_RATE = {
    "code": "PARTNER_TRAINING_COMPLETION_RATE",
    "name": "Partner Training Completion Rate",
    "description": "The percentage of channel partners who complete mandatory training programs, ensuring they are well-equipped to sell and support the products.",
    "formula": "(Number of Partners Completing Training / Total Number of Partners Enrolled) * 100",
    "calculation_formula": "(Number of Partners Completing Training / Total Number of Partners Enrolled) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Training Completion Rate to be added.",
    "trend_analysis": """



    * Increasing partner training completion rate may indicate a more engaged and committed channel partner network.
    * A decreasing rate could signal a lack of interest in the training programs or a need for more engaging and relevant content.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific training modules that have consistently low completion rates?
    * How does our partner training completion rate compare with industry benchmarks or with the completion rates of similar programs?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and update training content to ensure it remains relevant and valuable to channel partners.
    * Implement incentives or rewards for completing training programs to increase motivation and engagement.
    * Provide additional support and resources to channel partners who may struggle with completing the training.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the completion rate over time to identify any trends or patterns.
    * Pie charts to compare completion rates across different training modules or partner groups.
    
    
    
    """,
    "risk_warnings": """



    * Low completion rates may lead to decreased product knowledge and ultimately impact sales performance.
    * Consistently low completion rates could indicate a need for a complete overhaul of the training program or content.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track and manage partner training progress and completion.
    * Survey tools to gather feedback from channel partners on the effectiveness and relevance of the training programs.
    
    
    
    """,
    "integration_points": """



    * Integrate partner training completion data with sales performance metrics to understand the impact of training on sales outcomes.
    * Link completion rates with partner relationship management systems to tailor support and resources based on training progress.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving partner training completion rates can lead to better product knowledge, increased sales, and stronger partner relationships.
    * However, investing in more comprehensive training programs may require additional resources and budget allocation.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Product", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket", "Training Program"], "last_validated": "2025-11-10T13:49:33.222642"},
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
                        69.31,
                        79.15,
                        75.02,
                        67.93,
                        73.52,
                        80.07,
                        68.23,
                        64.29,
                        71.29,
                        79.58,
                        74.81,
                        75.39
                ],
                "unit": "%"
        },
        "current": {
                "value": 75.39,
                "unit": "%",
                "change": 0.58,
                "change_percent": 0.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.22,
                "min": 64.29,
                "max": 80.07,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12.43,
                        "percentage": 16.5
                },
                {
                        "category": "Segment B",
                        "value": 11.99,
                        "percentage": 15.9
                },
                {
                        "category": "Segment C",
                        "value": 17.57,
                        "percentage": 23.3
                },
                {
                        "category": "Segment D",
                        "value": 8.31,
                        "percentage": 11.0
                },
                {
                        "category": "Other",
                        "value": 25.09,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.531598",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Training Completion Rate"
        }
    },
}
