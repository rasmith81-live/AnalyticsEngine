"""
Time Spent Selling

The average amount of time a sales representative spends directly on selling activities.
"""

TIME_SPENT_SELLING = {
    "code": "TIME_SPENT_SELLING",
    "name": "Time Spent Selling",
    "description": "The average amount of time a sales representative spends directly on selling activities.",
    "formula": "Total Hours Spent on Selling Activities / Total Hours Worked",
    "calculation_formula": "Total Hours Spent on Selling Activities / Total Hours Worked",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time Spent Selling to be added.",
    "trend_analysis": """



    * An increasing average time spent selling may indicate a need for more efficient sales processes or increased customer engagement.
    * A decreasing time spent selling could signal improved sales strategies, better lead generation, or increased administrative burdens on sales reps.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific activities are consuming the most time for our sales representatives?
    * Are there any common obstacles or inefficiencies that hinder the sales team's ability to spend more time on direct selling activities?
    
    
    
    """,
    "actionable_tips": """



    * Implement sales automation tools to streamline administrative tasks and free up more time for selling.
    * Provide targeted training and coaching to improve sales efficiency and time management skills.
    * Regularly review and optimize sales processes to eliminate unnecessary steps and focus on high-value activities.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average time spent selling over time to identify trends and patterns.
    * Pie charts to visualize the breakdown of time spent on different sales activities.
    
    
    
    """,
    "risk_warnings": """



    * Low average time spent selling may lead to missed sales opportunities and reduced revenue.
    * High average time spent selling may result in burnout and decreased job satisfaction for sales representatives.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and analyze sales activities and customer interactions.
    * Sales performance management tools to monitor and optimize sales rep productivity.
    
    
    
    """,
    "integration_points": """



    * Integrate time spent selling data with customer feedback and satisfaction metrics to understand the impact of sales activities on customer relationships.
    * Link time spent selling with lead generation and conversion data to assess the effectiveness of sales efforts.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing the average time spent selling may lead to higher sales volumes and improved customer relationships.
    * However, excessive focus on selling activities could neglect important administrative and support tasks, impacting overall sales effectiveness.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.707266"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"],
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
                        21.9,
                        26.3,
                        24.6,
                        20.4,
                        22.3,
                        20.5,
                        26.0,
                        23.1,
                        27.1,
                        26.2,
                        20.3,
                        21.8
                ],
                "unit": "days"
        },
        "current": {
                "value": 21.8,
                "unit": "days",
                "change": 1.5,
                "change_percent": 7.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 23.38,
                "min": 20.3,
                "max": 27.1,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 6.36,
                        "percentage": 29.2
                },
                {
                        "category": "Segment B",
                        "value": 3.07,
                        "percentage": 14.1
                },
                {
                        "category": "Segment C",
                        "value": 3.33,
                        "percentage": 15.3
                },
                {
                        "category": "Segment D",
                        "value": 2.64,
                        "percentage": 12.1
                },
                {
                        "category": "Other",
                        "value": 6.4,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.747887",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time Spent Selling"
        }
    },
}
