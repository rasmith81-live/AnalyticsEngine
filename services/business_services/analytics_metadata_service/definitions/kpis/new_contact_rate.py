"""
New Contact Rate

The rate at which the sales team is generating new contacts or leads.
"""

NEW_CONTACT_RATE = {
    "code": "NEW_CONTACT_RATE",
    "name": "New Contact Rate",
    "description": "The rate at which the sales team is generating new contacts or leads.",
    "formula": "(Number of New Contacts / Total Sales Efforts) * 100",
    "calculation_formula": "(Number of New Contacts / Total Sales Efforts) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for New Contact Rate to be added.",
    "trend_analysis": """



    * An increasing new contact rate may indicate successful marketing efforts or a growing market.
    * A decreasing rate could signal a need for revamped lead generation strategies or a shrinking target audience.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific demographics or industries that are responding more positively to our outreach efforts?
    * How does our new contact rate compare with industry benchmarks or seasonal fluctuations?
    
    
    
    """,
    "actionable_tips": """



    * Utilize targeted advertising and content marketing to reach new audiences.
    * Implement lead scoring to prioritize high-quality leads and focus efforts on the most promising contacts.
    * Regularly update and optimize the sales team's outreach scripts and messaging to improve response rates.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of new contact rates over time.
    * Pie charts to visualize the distribution of new contacts by source or demographic.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low new contact rate can lead to stagnation in sales growth and missed opportunities.
    * Relying on a single source for new contacts may pose a risk if that source becomes less effective or unavailable.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and manage new leads and contacts.
    * Sales engagement platforms to automate and streamline outreach efforts.
    
    
    
    """,
    "integration_points": """



    * Integrate new contact rate tracking with marketing automation systems to align sales and marketing efforts.
    * Link new contact data with customer relationship management systems to ensure seamless lead nurturing and follow-up.
    
    
    
    """,
    "change_impact_analysis": """



    * An increased new contact rate can lead to higher sales volume and revenue, but may also require additional resources for lead management and follow-up.
    * Conversely, a declining new contact rate can impact overall sales performance and market share, potentially leading to decreased revenue and growth.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.075707"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
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
                        77.89,
                        77.11,
                        65.71,
                        61.07,
                        73.18,
                        79.56,
                        65.61,
                        77.78,
                        69.43,
                        65.97,
                        76.74,
                        59.84
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.84,
                "unit": "%",
                "change": -16.9,
                "change_percent": -22.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 70.82,
                "min": 59.84,
                "max": 79.56,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 9.85,
                        "percentage": 16.5
                },
                {
                        "category": "Channel Sales",
                        "value": 15.72,
                        "percentage": 26.3
                },
                {
                        "category": "Online Sales",
                        "value": 8.98,
                        "percentage": 15.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 6.35,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 18.94,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.241772",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "New Contact Rate"
        }
    },
}
