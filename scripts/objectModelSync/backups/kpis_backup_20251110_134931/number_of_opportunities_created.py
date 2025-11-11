"""
Number of Opportunities Created

The total number of sales opportunities created by the sales development team.
"""

NUMBER_OF_OPPORTUNITIES_CREATED = {
    "code": "NUMBER_OF_OPPORTUNITIES_CREATED",
    "name": "Number of Opportunities Created",
    "description": "The total number of sales opportunities created by the sales development team.",
    "formula": "Count of Leads Converted to Opportunities",
    "calculation_formula": "Count of Leads Converted to Opportunities",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Opportunities Created to be added.",
    "trend_analysis": """

    * An increasing number of opportunities created may indicate a more effective sales development team or increased market demand.
    * A decreasing number of opportunities could signal issues with lead generation, sales outreach, or market saturation.
    
    """,
    "diagnostic_questions": """

    * Are there specific industries or segments where opportunities are consistently being created?
    * How does the number of opportunities created compare to the overall sales pipeline and conversion rates?
    
    """,
    "actionable_tips": """

    * Implement targeted marketing campaigns to generate more qualified leads for the sales development team.
    * Provide ongoing training and support for the sales development team to improve their lead generation and outreach strategies.
    * Regularly review and optimize the sales development process to identify and address any bottlenecks or inefficiencies.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of opportunities created over time.
    * Pie charts to visualize the distribution of opportunities by industry or segment.
    
    """,
    "risk_warnings": """

    * A low number of opportunities created may lead to a limited sales pipeline and reduced revenue potential.
    * An excessively high number of opportunities without proper qualification may strain the sales team and lead to inefficiencies.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and manage sales opportunities effectively.
    * Sales engagement platforms to automate and streamline the outreach process for the sales development team.
    
    """,
    "integration_points": """

    * Integrate with marketing automation systems to ensure a seamless handoff of leads from marketing to the sales development team.
    * Connect with the sales team's CRM to provide visibility into the opportunities created and their progression through the sales pipeline.
    
    """,
    "change_impact_analysis": """

    * An increase in opportunities created can positively impact the overall sales performance and revenue generation.
    * However, a high number of unqualified opportunities may lead to wasted resources and decreased conversion rates.
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.710786"},
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
                        233,
                        204,
                        202,
                        224,
                        199,
                        198,
                        195,
                        200,
                        222,
                        211,
                        205,
                        195
                ],
                "unit": "count"
        },
        "current": {
                "value": 195,
                "unit": "count",
                "change": -10,
                "change_percent": -4.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 207.33,
                "min": 195,
                "max": 233,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 51.9,
                        "percentage": 26.6
                },
                {
                        "category": "Category B",
                        "value": 38.54,
                        "percentage": 19.8
                },
                {
                        "category": "Category C",
                        "value": 34.93,
                        "percentage": 17.9
                },
                {
                        "category": "Category D",
                        "value": 11.15,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 58.48,
                        "percentage": 30.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.710786",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Number of Opportunities Created"
        }
    },
}
