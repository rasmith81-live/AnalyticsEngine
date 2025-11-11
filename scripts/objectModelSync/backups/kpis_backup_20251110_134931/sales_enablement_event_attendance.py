"""
Sales Enablement Event Attendance

The number or percentage of sales team members attending sales enablement events, such as workshops or webinars.
"""

SALES_ENABLEMENT_EVENT_ATTENDANCE = {
    "code": "SALES_ENABLEMENT_EVENT_ATTENDANCE",
    "name": "Sales Enablement Event Attendance",
    "description": "The number or percentage of sales team members attending sales enablement events, such as workshops or webinars.",
    "formula": "(Number of Attendees / Total Number of Sales Team Members) * 100",
    "calculation_formula": "(Number of Attendees / Total Number of Sales Team Members) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Enablement Event Attendance to be added.",
    "trend_analysis": """

    * An increasing attendance rate at sales enablement events may indicate a growing interest in professional development and a proactive sales team.
    * A decreasing attendance rate could signal disengagement, lack of perceived value in the events, or competing priorities that need to be addressed.
    
    """,
    "diagnostic_questions": """

    * Are there specific events or topics that consistently attract higher attendance?
    * How does the attendance rate compare with the overall sales team performance and individual sales targets?
    
    """,
    "actionable_tips": """

    * Offer incentives or recognition for active participation in sales enablement events to boost attendance.
    * Customize event topics and formats based on feedback and preferences from the sales team to increase relevance and engagement.
    * Provide easy access to event recordings or materials for team members who may have scheduling conflicts.
    
    """,
    "visualization_suggestions": """

    * Line charts showing attendance rates over time for different events or types of events.
    * Pie charts comparing attendance rates by sales team members or departments.
    
    """,
    "risk_warnings": """

    * Low attendance rates may lead to missed opportunities for skill development and knowledge sharing among the sales team.
    * Inconsistent attendance could indicate a lack of alignment between the content of the events and the needs of the sales team.
    
    """,
    "tracking_tools": """

    * Event management platforms like Eventbrite or Cvent to streamline event planning and registration processes.
    * Sales performance management software that includes modules for tracking event attendance and correlating it with sales outcomes.
    
    """,
    "integration_points": """

    * Integrate attendance data with individual performance metrics to identify correlations between event participation and sales results.
    * Link event attendance with learning and development systems to track the impact of sales enablement events on skill enhancement and knowledge retention.
    
    """,
    "change_impact_analysis": """

    * Improving attendance rates can lead to a more knowledgeable and motivated sales team, potentially impacting overall sales performance and customer satisfaction.
    * Conversely, low attendance rates may indicate a need for reevaluation of the content and delivery of sales enablement events, impacting the effectiveness of the sales enablement program.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Churn Event", "Enablement Feedback", "Enablement Platform", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.376758"},
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
                        285,
                        273,
                        297,
                        307,
                        285,
                        276,
                        303,
                        286,
                        283,
                        308,
                        263,
                        289
                ],
                "unit": "count"
        },
        "current": {
                "value": 289,
                "unit": "count",
                "change": 26,
                "change_percent": 9.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 287.92,
                "min": 263,
                "max": 308,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 67.88,
                        "percentage": 23.5
                },
                {
                        "category": "Category B",
                        "value": 63.96,
                        "percentage": 22.1
                },
                {
                        "category": "Category C",
                        "value": 47.18,
                        "percentage": 16.3
                },
                {
                        "category": "Category D",
                        "value": 13.11,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 96.87,
                        "percentage": 33.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.376758",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Enablement Event Attendance"
        }
    },
}
