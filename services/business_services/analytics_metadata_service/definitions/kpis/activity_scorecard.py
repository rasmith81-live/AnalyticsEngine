"""
Activity Scorecard

A comprehensive measure of sales activities, including calls, emails, meetings, and tasks completed.
"""

ACTIVITY_SCORECARD = {
    "code": "ACTIVITY_SCORECARD",
    "name": "Activity Scorecard",
    "description": "A comprehensive measure of sales activities, including calls, emails, meetings, and tasks completed.",
    "formula": "Sum of all sales activities completed / Total number of sales reps",
    "calculation_formula": "Sum of all sales activities completed / Total number of sales reps",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Activity Scorecard to be added.",
    "trend_analysis": """



    * An increasing activity scorecard may indicate a proactive sales team or increased outreach efforts.
    * A decreasing scorecard could signal issues with sales team productivity or engagement.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales activities that are consistently underperforming?
    * How does our activity scorecard compare with industry benchmarks or seasonal fluctuations?
    
    
    
    """,
    "actionable_tips": """



    * Implement sales activity tracking software to monitor and analyze individual and team performance.
    * Provide regular training and coaching to improve sales skills and increase activity effectiveness.
    * Establish clear activity goals and incentives to motivate the sales team.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of different sales activities over time.
    * Pie charts to compare the distribution of various sales activities within the team.
    
    
    
    """,
    "risk_warnings": """



    * Low activity scorecard may lead to missed sales opportunities and revenue loss.
    * High activity scorecard without corresponding results may indicate inefficiencies or ineffective sales strategies.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems like Salesforce or HubSpot for tracking and managing sales activities.
    * Sales engagement platforms to automate and optimize outreach efforts.
    
    
    
    """,
    "integration_points": """



    * Integrate activity scorecard data with performance management systems to align individual goals with overall sales objectives.
    * Link sales activity data with customer relationship management systems to track the impact on customer interactions and conversions.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing sales activities may lead to higher customer acquisition but could also strain resources and increase costs.
    * Decreasing activities may improve efficiency but could also result in missed opportunities and reduced revenue.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Email", "Meeting", "Partner Performance Scorecard", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.637698"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
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
                        198,
                        162,
                        174,
                        185,
                        160,
                        182,
                        151,
                        194,
                        179,
                        199,
                        157,
                        173
                ],
                "unit": "count"
        },
        "current": {
                "value": 173,
                "unit": "count",
                "change": 16,
                "change_percent": 10.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 176.17,
                "min": 151,
                "max": 199,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 45.4,
                        "percentage": 26.2
                },
                {
                        "category": "Channel Sales",
                        "value": 24.91,
                        "percentage": 14.4
                },
                {
                        "category": "Online Sales",
                        "value": 20.64,
                        "percentage": 11.9
                },
                {
                        "category": "Enterprise Sales",
                        "value": 9.73,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 72.32,
                        "percentage": 41.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.347439",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Activity Scorecard"
        }
    },
}
