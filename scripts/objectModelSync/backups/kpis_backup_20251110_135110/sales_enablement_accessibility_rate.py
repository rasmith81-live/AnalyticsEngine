"""
Sales Enablement Accessibility Rate

The rate at which sales enablement resources are accessible to the sales team, including mobile and remote accessibility.
"""

SALES_ENABLEMENT_ACCESSIBILITY_RATE = {
    "code": "SALES_ENABLEMENT_ACCESSIBILITY_RATE",
    "name": "Sales Enablement Accessibility Rate",
    "description": "The rate at which sales enablement resources are accessible to the sales team, including mobile and remote accessibility.",
    "formula": "(Number of Accessible Resources / Total Number of Resources) * 100",
    "calculation_formula": "(Number of Accessible Resources / Total Number of Resources) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Enablement Accessibility Rate to be added.",
    "trend_analysis": """


    * An increasing accessibility rate may indicate improved sales enablement processes or better technology adoption within the sales team.
    * A decreasing rate could signal issues with resource availability, technological barriers, or lack of training on new tools.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sales enablement resources that are consistently underutilized or inaccessible to the sales team?
    * How does our accessibility rate compare with industry benchmarks or with the accessibility rates of top-performing sales teams?
    
    
    """,
    "actionable_tips": """


    * Invest in user-friendly, mobile-friendly sales enablement platforms and tools.
    * Provide regular training and support for the sales team to ensure they are proficient in using all available sales enablement resources.
    * Implement a feedback mechanism to gather insights from the sales team on the accessibility and effectiveness of sales enablement resources.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of accessibility rates over time.
    * Pie charts to visualize the distribution of accessible resources across different categories or types.
    
    
    """,
    "risk_warnings": """


    * Low accessibility rates can lead to missed sales opportunities and decreased productivity for the sales team.
    * Inaccessible resources may result in frustration and disengagement among the sales team, impacting overall morale and performance.
    
    
    """,
    "tracking_tools": """


    * Sales enablement platforms like Seismic or Highspot that offer mobile and remote accessibility features.
    * Collaboration tools such as Microsoft Teams or Slack to facilitate communication and access to resources for remote sales teams.
    
    
    """,
    "integration_points": """


    * Integrate accessibility rate tracking with CRM systems to understand the impact of resource accessibility on sales performance.
    * Link accessibility data with training and development platforms to identify areas for improvement in sales enablement training.
    
    
    """,
    "change_impact_analysis": """


    * Improving accessibility rates can lead to increased sales efficiency and effectiveness, potentially impacting revenue and customer satisfaction positively.
    * Conversely, low accessibility rates may result in decreased sales performance and hinder the achievement of sales targets.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.410393"},
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
                        58.58,
                        63.93,
                        67.78,
                        70.84,
                        61.67,
                        58.61,
                        76.64,
                        74.39,
                        68.9,
                        70.89,
                        57.42,
                        72.32
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.32,
                "unit": "%",
                "change": 14.9,
                "change_percent": 25.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 66.83,
                "min": 57.42,
                "max": 76.64,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.95,
                        "percentage": 31.7
                },
                {
                        "category": "Category B",
                        "value": 13.11,
                        "percentage": 18.1
                },
                {
                        "category": "Category C",
                        "value": 7.02,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 5.12,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 24.12,
                        "percentage": 33.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.366854",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Enablement Accessibility Rate"
        }
    },
}
