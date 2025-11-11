"""
Sales Collateral Development Time

The average time taken to develop new sales collateral or tools for the sales team.
"""

SALES_COLLATERAL_DEVELOPMENT_TIME = {
    "code": "SALES_COLLATERAL_DEVELOPMENT_TIME",
    "name": "Sales Collateral Development Time",
    "description": "The average time taken to develop new sales collateral or tools for the sales team.",
    "formula": "Average Time to Produce New Sales Material",
    "calculation_formula": "Average Time to Produce New Sales Material",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Collateral Development Time to be added.",
    "trend_analysis": """



    * Development time may decrease as sales teams become more familiar with the collateral creation process and tools.
    * An increasing development time could indicate a need for more resources or a lack of efficiency in the creation process.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific types of collateral that consistently take longer to develop?
    * How does the development time for new collateral compare to the impact it has on sales performance?
    
    
    
    """,
    "actionable_tips": """



    * Invest in training and tools that can streamline the collateral development process.
    * Regularly gather feedback from the sales team to understand their specific needs for collateral and how it can be improved.
    * Consider outsourcing certain collateral development tasks to specialized agencies or freelancers to speed up the process.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average development time over different quarters or years to identify long-term trends.
    * Stacked bar charts comparing development time for different types of collateral to pinpoint areas that require more attention.
    
    
    
    """,
    "risk_warnings": """



    * Extended development time may lead to sales teams using outdated or ineffective collateral, impacting their performance.
    * Rapidly increasing development time could indicate a bottleneck in the creation process that needs to be addressed to avoid delays.
    
    
    
    """,
    "tracking_tools": """



    * Project management software like Asana or Trello to track and manage the development of sales collateral.
    * Content creation tools such as Canva or Adobe Creative Cloud to streamline the design and creation process.
    
    
    
    """,
    "integration_points": """



    * Integrate development time tracking with CRM systems to understand the impact of new collateral on sales activities and performance.
    * Link collateral development with marketing automation platforms to ensure alignment in messaging and branding.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing development time can lead to more agile and responsive sales teams, potentially improving overall sales performance.
    * However, rushing the development process may compromise the quality and effectiveness of the collateral, impacting its impact on potential customers.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.390035"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        20.5,
                        22.4,
                        19.2,
                        14.9,
                        17.6,
                        14.5,
                        19.8,
                        18.9,
                        21.1,
                        22.2,
                        22.0,
                        19.4
                ],
                "unit": "days"
        },
        "current": {
                "value": 19.4,
                "unit": "days",
                "change": -2.6,
                "change_percent": -11.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 19.38,
                "min": 14.5,
                "max": 22.4,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 5.2,
                        "percentage": 26.8
                },
                {
                        "category": "Channel Sales",
                        "value": 4.04,
                        "percentage": 20.8
                },
                {
                        "category": "Online Sales",
                        "value": 2.87,
                        "percentage": 14.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 2.05,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 5.24,
                        "percentage": 27.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.903771",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Sales Collateral Development Time"
        }
    },
}
