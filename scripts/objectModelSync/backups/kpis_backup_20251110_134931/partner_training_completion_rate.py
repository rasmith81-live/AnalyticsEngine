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
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Product", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket", "Training Program"], "last_validated": "2025-11-10T13:43:23.911607"},
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
                        79.34,
                        66.62,
                        80.43,
                        78.45,
                        80.15,
                        79.13,
                        71.59,
                        62.26,
                        65.93,
                        74.41,
                        61.62,
                        66.36
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.36,
                "unit": "%",
                "change": 4.74,
                "change_percent": 7.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 72.19,
                "min": 61.62,
                "max": 80.43,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.34,
                        "percentage": 30.7
                },
                {
                        "category": "Category B",
                        "value": 14.14,
                        "percentage": 21.3
                },
                {
                        "category": "Category C",
                        "value": 9.21,
                        "percentage": 13.9
                },
                {
                        "category": "Category D",
                        "value": 4.08,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 18.59,
                        "percentage": 28.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.911607",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Training Completion Rate"
        }
    },
}
