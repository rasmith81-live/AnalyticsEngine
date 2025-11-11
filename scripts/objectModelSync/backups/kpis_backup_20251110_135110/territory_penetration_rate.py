"""
Territory Penetration Rate

The rate at which the outside sales team is able to penetrate or cover the allocated sales territory.
"""

TERRITORY_PENETRATION_RATE = {
    "code": "TERRITORY_PENETRATION_RATE",
    "name": "Territory Penetration Rate",
    "description": "The rate at which the outside sales team is able to penetrate or cover the allocated sales territory.",
    "formula": "(Number of Customers in Territory / Total Market Potential in Territory) * 100",
    "calculation_formula": "(Number of Customers in Territory / Total Market Potential in Territory) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Territory Penetration Rate to be added.",
    "trend_analysis": """


    * Increasing territory penetration rate may indicate successful expansion into new markets or improved sales strategies.
    * Decreasing rate could signal increased competition or ineffective territory management.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific regions within the territory that are consistently underperforming?
    * How does our territory penetration rate compare with industry benchmarks or with previous performance?
    
    
    """,
    "actionable_tips": """


    * Provide additional training and resources to the sales team to better understand and address the needs of different regions within the territory.
    * Regularly review and adjust territory boundaries based on market changes and sales performance.
    * Implement a customer relationship management (CRM) system to track and manage sales activities within the territory.
    
    
    """,
    "visualization_suggestions": """


    * Heat maps to visually represent the coverage and performance within the sales territory.
    * Line charts showing the territory penetration rate over time to identify trends and patterns.
    
    
    """,
    "risk_warnings": """


    * Low territory penetration rate may result in missed sales opportunities and reduced market share.
    * High turnover or dissatisfaction among the sales team can negatively impact territory coverage and penetration.
    
    
    """,
    "tracking_tools": """


    * Geographic information system (GIS) software to analyze and visualize territory data.
    * CRM platforms with territory management features to track and optimize sales activities within the territory.
    
    
    """,
    "integration_points": """


    * Integrate territory penetration rate with sales performance metrics to understand the relationship between coverage and actual sales results.
    * Link territory data with marketing and lead generation systems to align sales efforts with potential opportunities.
    
    
    """,
    "change_impact_analysis": """


    * Improving territory penetration rate can lead to increased sales and market share, but may require additional resources and investment in sales activities.
    * Conversely, a declining territory penetration rate can impact overall revenue and market presence, affecting the organization's growth and competitiveness.
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Penetration", "Channel Market", "Customer", "Market Segment", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Territory Assignment"], "last_validated": "2025-11-10T13:49:33.701225"},
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
                        60.98,
                        62.14,
                        55.57,
                        61.22,
                        54.67,
                        55.65,
                        56.92,
                        62.94,
                        56.51,
                        55.17,
                        60.38,
                        61.43
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.43,
                "unit": "%",
                "change": 1.05,
                "change_percent": 1.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 58.63,
                "min": 54.67,
                "max": 62.94,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.38,
                        "percentage": 23.4
                },
                {
                        "category": "Category B",
                        "value": 7.09,
                        "percentage": 11.5
                },
                {
                        "category": "Category C",
                        "value": 7.6,
                        "percentage": 12.4
                },
                {
                        "category": "Category D",
                        "value": 6.66,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 25.7,
                        "percentage": 41.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.982602",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Territory Penetration Rate"
        }
    },
}
