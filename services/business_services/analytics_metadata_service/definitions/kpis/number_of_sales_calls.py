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
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.097402"},
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
                        638.35,
                        586.62,
                        630.88,
                        625.27,
                        527.85,
                        549.17,
                        578.97,
                        614.21,
                        628.04,
                        624.4,
                        564.42,
                        574.95
                ],
                "unit": "units"
        },
        "current": {
                "value": 574.95,
                "unit": "units",
                "change": 10.53,
                "change_percent": 1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 595.26,
                "min": 527.85,
                "max": 638.35,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 146.79,
                        "percentage": 25.5
                },
                {
                        "category": "Channel Sales",
                        "value": 118.18,
                        "percentage": 20.6
                },
                {
                        "category": "Online Sales",
                        "value": 85.81,
                        "percentage": 14.9
                },
                {
                        "category": "Enterprise Sales",
                        "value": 32.75,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 191.42,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.277943",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Number of Sales Calls"
        }
    },
}
