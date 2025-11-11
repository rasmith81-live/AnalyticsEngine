"""
Sales Best Practice Sharing Rate

The rate at which best practices are shared and adopted within the sales team, facilitated by the Sales Enablement Team.
"""

SALES_BEST_PRACTICE_SHARING_RATE = {
    "code": "SALES_BEST_PRACTICE_SHARING_RATE",
    "name": "Sales Best Practice Sharing Rate",
    "description": "The rate at which best practices are shared and adopted within the sales team, facilitated by the Sales Enablement Team.",
    "formula": "(Number of Best Practice Documents Shared / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Best Practice Documents Shared / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Best Practice Sharing Rate to be added.",
    "trend_analysis": """



    * Increasing sales best practice sharing rate may indicate a growing culture of collaboration and knowledge sharing within the sales team.
    * A decreasing rate could signal a lack of engagement or adoption of best practices, potentially leading to missed sales opportunities or inefficiencies.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific best practices that are consistently underutilized or overlooked by the sales team?
    * How does the sales best practice sharing rate correlate with sales performance metrics such as conversion rates or average deal size?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular knowledge sharing sessions or workshops to encourage best practice sharing.
    * Utilize technology platforms or tools that make it easy for sales team members to contribute and access best practices.
    * Recognize and reward individuals who actively contribute to the sharing and adoption of best practices within the sales team.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of best practice sharing rate over time.
    * Comparison charts to highlight the adoption rates of specific best practices across different sales team members or regions.
    
    
    
    """,
    "risk_warnings": """



    * A low sales best practice sharing rate may lead to inconsistent sales approaches and missed opportunities for improvement.
    * Resistance to change or a lack of buy-in from sales team members could hinder the adoption of best practices.
    
    
    
    """,
    "tracking_tools": """



    * Collaboration and communication platforms such as Slack or Microsoft Teams to facilitate ongoing sharing and discussion of best practices.
    * Sales enablement software that includes features for documenting, organizing, and distributing best practices to the sales team.
    
    
    
    """,
    "integration_points": """



    * Integrate the sales best practice sharing rate with performance management systems to align recognition and incentives with active participation in sharing best practices.
    * Link the sharing rate with customer relationship management (CRM) systems to track the impact of adopted best practices on customer interactions and outcomes.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the sales best practice sharing rate can lead to more consistent and effective sales approaches, potentially increasing overall sales performance.
    * Conversely, a decline in the sharing rate may result in missed opportunities for process improvement and innovation within the sales team.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.369922"},
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
                        57.53,
                        44.47,
                        42.34,
                        51.19,
                        41.18,
                        58.48,
                        47.23,
                        52.35,
                        43.97,
                        42.6,
                        53.42,
                        41.68
                ],
                "unit": "%"
        },
        "current": {
                "value": 41.68,
                "unit": "%",
                "change": -11.74,
                "change_percent": -22.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 48.04,
                "min": 41.18,
                "max": 58.48,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 6.39,
                        "percentage": 15.3
                },
                {
                        "category": "Channel Sales",
                        "value": 11.44,
                        "percentage": 27.4
                },
                {
                        "category": "Online Sales",
                        "value": 5.14,
                        "percentage": 12.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.47,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 15.24,
                        "percentage": 36.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.858192",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Best Practice Sharing Rate"
        }
    },
}
