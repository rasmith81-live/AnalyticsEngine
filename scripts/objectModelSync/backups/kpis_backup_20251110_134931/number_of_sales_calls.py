"""
Number of Sales Calls

The total number of sales-related calls made by the outside sales team.
"""

NUMBER_OF_SALES_CALLS = {
    "code": "NUMBER_OF_SALES_CALLS",
    "name": "Number of Sales Calls",
    "description": "The total number of sales-related calls made by the outside sales team.",
    "formula": "Sum of all Sales Calls Made",
    "calculation_formula": "Sum of all Sales Calls Made",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Sales Calls to be added.",
    "trend_analysis": """

    * An increasing number of sales calls may indicate a proactive sales team or a push to meet higher sales targets.
    * A decreasing number of sales calls could signal a lack of engagement or challenges in reaching potential clients.
    
    """,
    "diagnostic_questions": """

    * Are the sales calls evenly distributed across the sales team, or are there individuals who are making significantly more or fewer calls?
    * How do the number of sales calls correlate with actual sales performance and conversion rates?
    
    """,
    "actionable_tips": """

    * Implement a CRM system to track and manage sales calls more effectively.
    * Provide regular training and coaching to the sales team on effective sales call techniques and strategies.
    * Encourage the use of technology such as automated dialing systems to increase the volume of sales calls without sacrificing quality.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of sales calls over time.
    * Pie charts to compare the distribution of sales calls among different team members or territories.
    
    """,
    "risk_warnings": """

    * A high number of sales calls without corresponding sales may indicate inefficiencies in the sales process or poor lead quality.
    * A low number of sales calls may result in missed opportunities and reduced sales performance.
    
    """,
    "tracking_tools": """

    * Utilize sales engagement platforms like Outreach or SalesLoft to streamline and track sales call activities.
    * Integrate with communication tools such as Zoom or Microsoft Teams for virtual sales calls and meetings.
    
    """,
    "integration_points": """

    * Integrate sales call data with customer relationship management (CRM) systems to better understand the impact of calls on the sales pipeline.
    * Link sales call metrics with marketing automation platforms to align sales efforts with marketing campaigns and lead generation activities.
    
    """,
    "change_impact_analysis": """

    * An increase in the number of sales calls may lead to higher sales volume but could also result in increased pressure on the sales team.
    * A decrease in sales calls may free up time for more personalized and effective sales interactions but could also reduce the overall outreach and lead generation.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.718033"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        305.48,
                        297.91,
                        268.6,
                        338.99,
                        394.6,
                        271.92,
                        349.54,
                        295.67,
                        279.12,
                        273.53,
                        389.02,
                        333.71
                ],
                "unit": "units"
        },
        "current": {
                "value": 333.71,
                "unit": "units",
                "change": -55.31,
                "change_percent": -14.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 316.51,
                "min": 268.6,
                "max": 394.6,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 75.76,
                        "percentage": 22.7
                },
                {
                        "category": "Category B",
                        "value": 53.21,
                        "percentage": 15.9
                },
                {
                        "category": "Category C",
                        "value": 59.15,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 39.58,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 106.01,
                        "percentage": 31.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.718033",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Number of Sales Calls"
        }
    },
}
