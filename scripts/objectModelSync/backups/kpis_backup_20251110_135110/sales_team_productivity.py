"""
Sales Team Productivity

The revenue generated per sales team member or the number of deals closed per sales team member.
"""

SALES_TEAM_PRODUCTIVITY = {
    "code": "SALES_TEAM_PRODUCTIVITY",
    "name": "Sales Team Productivity",
    "description": "The revenue generated per sales team member or the number of deals closed per sales team member.",
    "formula": "Total Sales Revenue / (Number of Sales Reps * Hours Worked)",
    "calculation_formula": "Total Sales Revenue / (Number of Sales Reps * Hours Worked)",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Team Productivity to be added.",
    "trend_analysis": """


    * An increasing sales team productivity may indicate improved sales processes, better lead generation, or enhanced product knowledge among the team members.
    * A decreasing productivity could signal issues such as lack of motivation, poor training, or ineffective sales strategies.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific products or services that are consistently generating higher revenue or closing more deals?
    * How does the sales team productivity compare with industry benchmarks or historical performance?
    
    
    """,
    "actionable_tips": """


    * Invest in ongoing sales training and development programs to enhance the skills and knowledge of the sales team.
    * Implement a clear and motivating sales incentive program to drive performance and productivity.
    * Regularly review and optimize the sales process to identify and eliminate any bottlenecks or inefficiencies.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of revenue generated per sales team member over time.
    * Pie charts illustrating the distribution of closed deals among sales team members.
    
    
    """,
    "risk_warnings": """


    * Low sales team productivity can lead to missed revenue targets and decreased overall sales performance.
    * High sales team productivity without proper support or resources can result in burnout and decreased quality of customer interactions.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track individual sales team member performance and customer interactions.
    * Sales enablement platforms to provide the sales team with the necessary tools, content, and information to effectively engage with prospects and close deals.
    
    
    """,
    "integration_points": """


    * Integrate sales team productivity data with marketing analytics to understand the impact of marketing efforts on sales performance.
    * Link sales team productivity with customer feedback systems to identify areas for improvement and training needs.
    
    
    """,
    "change_impact_analysis": """


    * Increasing sales team productivity may lead to higher revenue and improved customer satisfaction, but it could also strain resources and increase workload for the team.
    * Conversely, a decrease in sales team productivity may result in missed opportunities and decreased customer retention, impacting long-term business growth.
    
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Deal", "Opportunity", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.512014"},
    "required_objects": [],
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
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
                        476,
                        496,
                        494,
                        464,
                        475,
                        471,
                        456,
                        479,
                        469,
                        465,
                        496,
                        484
                ],
                "unit": "count"
        },
        "current": {
                "value": 484,
                "unit": "count",
                "change": -12,
                "change_percent": -2.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 477.08,
                "min": 456,
                "max": 496,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 87.27,
                        "percentage": 18.0
                },
                {
                        "category": "Category B",
                        "value": 113.46,
                        "percentage": 23.4
                },
                {
                        "category": "Category C",
                        "value": 85.21,
                        "percentage": 17.6
                },
                {
                        "category": "Category D",
                        "value": 55.41,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 142.65,
                        "percentage": 29.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.639940",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Team Productivity"
        }
    },
}
