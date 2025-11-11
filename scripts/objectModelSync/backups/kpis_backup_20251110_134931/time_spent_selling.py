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
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.993390"},
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
                        27.3,
                        28.0,
                        26.2,
                        28.3,
                        28.9,
                        32.4,
                        30.1,
                        32.1,
                        29.8,
                        32.9,
                        32.7,
                        27.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 27.0,
                "unit": "days",
                "change": -5.7,
                "change_percent": -17.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 29.64,
                "min": 26.2,
                "max": 32.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 4.47,
                        "percentage": 16.6
                },
                {
                        "category": "Category B",
                        "value": 4.21,
                        "percentage": 15.6
                },
                {
                        "category": "Category C",
                        "value": 4.64,
                        "percentage": 17.2
                },
                {
                        "category": "Category D",
                        "value": 3.16,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 10.52,
                        "percentage": 39.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.993390",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time Spent Selling"
        }
    },
}
