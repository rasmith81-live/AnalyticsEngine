"""
Sales Playbook Adoption Rate

The rate at which the sales team adopts and utilizes the sales playbook in their processes.
"""

SALES_PLAYBOOK_ADOPTION_RATE = {
    "code": "SALES_PLAYBOOK_ADOPTION_RATE",
    "name": "Sales Playbook Adoption Rate",
    "description": "The rate at which the sales team adopts and utilizes the sales playbook in their processes.",
    "formula": "(Number of Reps Using Sales Playbook / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Reps Using Sales Playbook / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Playbook Adoption Rate to be added.",
    "trend_analysis": """


    * An increasing sales playbook adoption rate may indicate better alignment with sales processes and improved sales performance.
    * A decreasing rate could signal resistance to change, lack of understanding of the playbook's value, or ineffective training and communication.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sections or tools within the sales playbook that are being underutilized?
    * How does the adoption rate correlate with sales performance metrics such as win rates or deal size?
    
    
    """,
    "actionable_tips": """


    * Provide regular training and reinforcement of the playbook's value and usage.
    * Incorporate the playbook into the sales team's daily routines and processes to encourage adoption.
    * Solicit feedback from the sales team to continuously improve the playbook's relevance and effectiveness.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of adoption rate over time.
    * Comparison charts displaying adoption rates across different sales teams or regions.
    
    
    """,
    "risk_warnings": """


    * Low adoption rates may lead to inconsistent sales processes and missed opportunities.
    * Resistance to the playbook may indicate deeper issues with sales team culture or leadership buy-in.
    
    
    """,
    "tracking_tools": """


    * Sales enablement platforms like Seismic or Highspot for tracking and analyzing playbook usage.
    * CRM systems with integrated playbook features to seamlessly incorporate the playbook into sales workflows.
    
    
    """,
    "integration_points": """


    * Integrate the playbook adoption rate with sales performance metrics to understand its impact on overall sales effectiveness.
    * Link the adoption rate with training and development systems to identify areas for improvement and reinforcement.
    
    
    """,
    "change_impact_analysis": """


    * Improving the adoption rate can lead to more consistent sales processes and better customer interactions.
    * However, pushing for higher adoption may require changes in sales culture and processes, which could initially impact productivity.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Product Adoption", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.467746"},
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
                        48.31,
                        41.89,
                        39.94,
                        36.85,
                        49.06,
                        53.67,
                        50.95,
                        38.05,
                        42.6,
                        36.51,
                        39.53,
                        44.91
                ],
                "unit": "%"
        },
        "current": {
                "value": 44.91,
                "unit": "%",
                "change": 5.38,
                "change_percent": 13.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 43.52,
                "min": 36.51,
                "max": 53.67,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.57,
                        "percentage": 16.9
                },
                {
                        "category": "Category B",
                        "value": 8.66,
                        "percentage": 19.3
                },
                {
                        "category": "Category C",
                        "value": 5.63,
                        "percentage": 12.5
                },
                {
                        "category": "Category D",
                        "value": 3.2,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 19.85,
                        "percentage": 44.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.526263",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Playbook Adoption Rate"
        }
    },
}
