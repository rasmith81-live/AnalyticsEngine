"""
Sales Team Collaboration Index

A measure of the effectiveness of collaboration within the sales team, which could include cross-functional initiatives.
"""

SALES_TEAM_COLLABORATION_INDEX = {
    "code": "SALES_TEAM_COLLABORATION_INDEX",
    "name": "Sales Team Collaboration Index",
    "description": "A measure of the effectiveness of collaboration within the sales team, which could include cross-functional initiatives.",
    "formula": "Collaborative Activities Score / Total Number of Opportunities for Collaboration",
    "calculation_formula": "Collaborative Activities Score / Total Number of Opportunities for Collaboration",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Team Collaboration Index to be added.",
    "trend_analysis": """


    * An increasing Sales Team Collaboration Index may indicate improved cross-functional initiatives and better alignment within the sales team.
    * A decreasing index could signal breakdowns in communication, lack of teamwork, or siloed behavior within the sales team.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sales projects or initiatives where collaboration has been particularly effective or ineffective?
    * How does our Sales Team Collaboration Index compare with industry benchmarks or best practices?
    
    
    """,
    "actionable_tips": """


    * Implement regular cross-functional meetings to align on goals and strategies.
    * Encourage open communication and knowledge sharing within the sales team.
    * Utilize collaboration tools and technologies to facilitate teamwork and information exchange.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of the Sales Team Collaboration Index over time.
    * Stacked bar charts comparing collaboration levels across different sales projects or teams.
    
    
    """,
    "risk_warnings": """


    * Low Sales Team Collaboration Index can lead to missed opportunities, duplicated efforts, and internal conflicts.
    * Ineffective collaboration may result in poor customer experience and lost sales.
    
    
    """,
    "tracking_tools": """


    * Collaboration platforms like Microsoft Teams or Slack for seamless communication and file sharing.
    * Project management tools such as Asana or Trello to track and manage cross-functional initiatives.
    
    
    """,
    "integration_points": """


    * Integrate the Sales Team Collaboration Index with performance management systems to align individual goals with team collaboration efforts.
    * Link collaboration metrics with customer relationship management (CRM) systems to understand the impact on customer interactions and sales outcomes.
    
    
    """,
    "change_impact_analysis": """


    * Improving the Sales Team Collaboration Index can lead to better customer engagement, increased sales productivity, and higher overall team morale.
    * Conversely, a low index may result in missed sales opportunities, decreased employee satisfaction, and potential turnover.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.507064"},
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
                        50.25,
                        51.97,
                        59.28,
                        48.38,
                        54.69,
                        42.8,
                        59.62,
                        61.09,
                        55.57,
                        58.37,
                        42.62,
                        58.37
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.37,
                "unit": "%",
                "change": 15.75,
                "change_percent": 37.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 53.58,
                "min": 42.62,
                "max": 61.09,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.88,
                        "percentage": 34.1
                },
                {
                        "category": "Category B",
                        "value": 8.1,
                        "percentage": 13.9
                },
                {
                        "category": "Category C",
                        "value": 6.55,
                        "percentage": 11.2
                },
                {
                        "category": "Category D",
                        "value": 4.59,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 19.25,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.629378",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Team Collaboration Index"
        }
    },
}
