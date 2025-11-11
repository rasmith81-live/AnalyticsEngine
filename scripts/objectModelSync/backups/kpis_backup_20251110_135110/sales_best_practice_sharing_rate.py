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
                        68.06,
                        81.9,
                        63.87,
                        74.6,
                        73.79,
                        82.51,
                        65.37,
                        71.66,
                        70.13,
                        70.12,
                        81.31,
                        68.62
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.62,
                "unit": "%",
                "change": -12.69,
                "change_percent": -15.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 72.66,
                "min": 63.87,
                "max": 82.51,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.3,
                        "percentage": 23.8
                },
                {
                        "category": "Category B",
                        "value": 9.57,
                        "percentage": 13.9
                },
                {
                        "category": "Category C",
                        "value": 9.7,
                        "percentage": 14.1
                },
                {
                        "category": "Category D",
                        "value": 4.41,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 28.64,
                        "percentage": 41.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.134786",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Best Practice Sharing Rate"
        }
    },
}
