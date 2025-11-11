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
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Churn Event", "Enablement Feedback", "Enablement Platform", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.414451"},
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
                        60.31,
                        55.25,
                        60.5,
                        65.54,
                        63.53,
                        58.45,
                        58.39,
                        72.37,
                        55.6,
                        57.55,
                        62.17,
                        54.9
                ],
                "unit": "%"
        },
        "current": {
                "value": 54.9,
                "unit": "%",
                "change": -7.27,
                "change_percent": -11.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 60.38,
                "min": 54.9,
                "max": 72.37,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 15.25,
                        "percentage": 27.8
                },
                {
                        "category": "Channel Sales",
                        "value": 13.14,
                        "percentage": 23.9
                },
                {
                        "category": "Online Sales",
                        "value": 5.72,
                        "percentage": 10.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.05,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 16.74,
                        "percentage": 30.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.960817",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Enablement Event Attendance"
        }
    },
}
