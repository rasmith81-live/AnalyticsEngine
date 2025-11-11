"""
Number of Active Prospects

The total number of prospects that are currently being engaged by the sales team.
"""

NUMBER_OF_ACTIVE_PROSPECTS = {
    "code": "NUMBER_OF_ACTIVE_PROSPECTS",
    "name": "Number of Active Prospects",
    "description": "The total number of prospects that are currently being engaged by the sales team.",
    "formula": "Count of Prospects Currently in the Sales Pipeline",
    "calculation_formula": "Count of Prospects Currently in the Sales Pipeline",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Active Prospects to be added.",
    "trend_analysis": """

    * An increasing number of active prospects may indicate a growing market or improved lead generation efforts.
    * A decreasing number could signal a lack of new leads or a shift in the target market's interest.
    
    """,
    "diagnostic_questions": """

    * Are there specific industries or regions where the number of active prospects is consistently higher or lower?
    * What strategies or channels have been most effective in generating new prospects?
    
    """,
    "actionable_tips": """

    * Implement targeted marketing campaigns to reach new prospects in untapped industries or regions.
    * Regularly review and update the sales team's prospecting techniques to adapt to changing market dynamics.
    * Utilize customer relationship management (CRM) software to track and manage prospect engagement more effectively.
    
    """,
    "visualization_suggestions": """

    * Line charts to visualize the trend in the number of active prospects over time.
    * Pie charts to compare the distribution of active prospects across different industries or regions.
    
    """,
    "risk_warnings": """

    * A consistently low number of active prospects may lead to a stagnant sales pipeline and reduced revenue opportunities.
    * An excessively high number of prospects without proper qualification may strain the sales team's resources and lead to inefficiencies.
    
    """,
    "tracking_tools": """

    * Lead management software such as HubSpot or Salesforce to track and manage prospect interactions.
    * Data analytics tools to identify patterns and trends in prospect engagement for targeted outreach.
    
    """,
    "integration_points": """

    * Integrate prospect data with marketing automation platforms to align sales and marketing efforts for better lead nurturing.
    * Link prospect information with customer relationship management systems to provide a comprehensive view of the sales pipeline.
    
    """,
    "change_impact_analysis": """

    * An increase in the number of active prospects can lead to higher sales volume but may also require additional resources for effective management.
    * A decrease in prospects may prompt a need for strategic shifts in marketing and sales tactics to reinvigorate lead generation efforts.
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.698541"},
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
                        202,
                        231,
                        215,
                        189,
                        186,
                        186,
                        205,
                        203,
                        210,
                        230,
                        199,
                        205
                ],
                "unit": "count"
        },
        "current": {
                "value": 205,
                "unit": "count",
                "change": 6,
                "change_percent": 3.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 205.08,
                "min": 186,
                "max": 231,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 31.29,
                        "percentage": 15.3
                },
                {
                        "category": "Category B",
                        "value": 49.37,
                        "percentage": 24.1
                },
                {
                        "category": "Category C",
                        "value": 42.56,
                        "percentage": 20.8
                },
                {
                        "category": "Category D",
                        "value": 8.82,
                        "percentage": 4.3
                },
                {
                        "category": "Other",
                        "value": 72.96,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.698541",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Number of Active Prospects"
        }
    },
}
