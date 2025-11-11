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
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Email", "Meeting", "Partner Performance Scorecard", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.004992"},
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
                        119,
                        107,
                        120,
                        96,
                        118,
                        97,
                        133,
                        107,
                        136,
                        108,
                        122,
                        100
                ],
                "unit": "count"
        },
        "current": {
                "value": 100,
                "unit": "count",
                "change": -22,
                "change_percent": -18.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 113.58,
                "min": 96,
                "max": 136,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.51,
                        "percentage": 20.5
                },
                {
                        "category": "Category B",
                        "value": 15.09,
                        "percentage": 15.1
                },
                {
                        "category": "Category C",
                        "value": 13.32,
                        "percentage": 13.3
                },
                {
                        "category": "Category D",
                        "value": 6.7,
                        "percentage": 6.7
                },
                {
                        "category": "Other",
                        "value": 44.38,
                        "percentage": 44.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.004992",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Activity Scorecard"
        }
    },
}
