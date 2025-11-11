"""
Outbound Calls per Day

The number of outbound calls made by the Sales Development team per day. It provides insight into how active the team is in generating new leads and opportunities.
"""

OUTBOUND_CALLS_PER_DAY = {
    "code": "OUTBOUND_CALLS_PER_DAY",
    "name": "Outbound Calls per Day",
    "description": "The number of outbound calls made by the Sales Development team per day. It provides insight into how active the team is in generating new leads and opportunities.",
    "formula": "Total Outbound Calls / Number of Working Days",
    "calculation_formula": "Total Outbound Calls / Number of Working Days",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Outbound Calls per Day to be added.",
    "trend_analysis": """



    * An increasing number of outbound calls per day may indicate a proactive and engaged sales development team actively pursuing new leads.
    * A decreasing trend in outbound calls could signal potential issues with team motivation, lead generation strategies, or resource allocation.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific time periods or days of the week when outbound call volume tends to be higher or lower?
    * What is the average conversion rate of outbound calls to qualified leads, and how does it correlate with the number of calls made?
    
    
    
    """,
    "actionable_tips": """



    * Implement call cadences and schedules to ensure consistent outbound call activity throughout the day and week.
    * Provide ongoing training and coaching to the sales development team to improve call quality and effectiveness.
    * Regularly review and update the lead generation strategy to ensure a steady flow of new prospects to call.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the daily outbound call volume over time to identify patterns and fluctuations.
    * Comparison bar charts to visualize the outbound call performance of individual team members or regions.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low number of outbound calls per day may lead to a lack of new leads and opportunities, impacting overall sales performance.
    * An excessively high number of calls without corresponding results could indicate inefficiencies in the lead generation or qualification process.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems like Salesforce or HubSpot to track and analyze outbound call activity, lead status, and conversion rates.
    * Call tracking and analytics tools such as CallRail or Gong to monitor call quality and effectiveness.
    
    
    
    """,
    "integration_points": """



    * Integrate outbound call data with sales performance metrics to understand the impact of call activity on revenue generation.
    * Link outbound call activity with marketing campaign data to assess the effectiveness of lead generation efforts.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing outbound calls may lead to higher lead volume and potential revenue growth, but it could also impact the workload and stress levels of the sales development team.
    * Conversely, a decrease in outbound calls may result in a decline in new opportunities and sales, affecting overall business performance.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Lead", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.136773"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        520,
                        494,
                        502,
                        472,
                        497,
                        473,
                        474,
                        522,
                        486,
                        480,
                        502,
                        521
                ],
                "unit": "count"
        },
        "current": {
                "value": 521,
                "unit": "count",
                "change": 19,
                "change_percent": 3.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 495.25,
                "min": 472,
                "max": 522,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 132.07,
                        "percentage": 25.3
                },
                {
                        "category": "Segment B",
                        "value": 73.73,
                        "percentage": 14.2
                },
                {
                        "category": "Segment C",
                        "value": 70.33,
                        "percentage": 13.5
                },
                {
                        "category": "Segment D",
                        "value": 24.57,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 220.3,
                        "percentage": 42.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.352393",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Outbound Calls per Day"
        }
    },
}
