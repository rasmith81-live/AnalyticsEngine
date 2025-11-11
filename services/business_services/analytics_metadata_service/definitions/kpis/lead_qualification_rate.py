"""
Lead Qualification Rate

The percentage of leads that are qualified and accepted as potential opportunities.
"""

LEAD_QUALIFICATION_RATE = {
    "code": "LEAD_QUALIFICATION_RATE",
    "name": "Lead Qualification Rate",
    "description": "The percentage of leads that are qualified and accepted as potential opportunities.",
    "formula": "(Number of Qualified Leads / Total Number of Leads) * 100",
    "calculation_formula": "(Number of Qualified Leads / Total Number of Leads) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Qualification Rate to be added.",
    "trend_analysis": """



    * An increasing lead qualification rate may indicate improved lead generation strategies or better alignment between marketing and sales teams.
    * A decreasing rate could signal issues with lead quality, ineffective qualification criteria, or misalignment between sales and marketing efforts.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific lead sources or channels that consistently produce higher quality leads?
    * How does our lead qualification rate compare with industry benchmarks or historical performance?
    
    
    
    """,
    "actionable_tips": """



    * Refine lead qualification criteria to ensure only the most promising leads are accepted.
    * Implement lead nurturing strategies to improve the quality of leads before they enter the sales pipeline.
    * Provide ongoing training and support for sales representatives to enhance their lead qualification skills.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing lead qualification rates over time to identify trends and seasonality.
    * Pie charts comparing the distribution of qualified and unqualified leads by source or channel.
    
    
    
    """,
    "risk_warnings": """



    * A high lead qualification rate may lead to a smaller pool of potential opportunities, impacting overall sales performance.
    * An excessively low qualification rate can result in wasted resources and decreased sales productivity.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) systems like Salesforce or HubSpot for tracking and managing lead qualification processes.
    * Marketing automation platforms to score and prioritize leads based on their engagement and behavior.
    
    
    
    """,
    "integration_points": """



    * Integrate lead qualification data with marketing analytics to understand the quality of leads generated from different campaigns and channels.
    * Link lead qualification with sales forecasting to assess the impact of qualified leads on future revenue projections.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving lead qualification can lead to higher conversion rates and sales efficiency, but may also require adjustments in marketing strategies and resource allocation.
    * A declining lead qualification rate can negatively impact sales performance and revenue generation, affecting overall business growth.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Lead Qualification", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.008402"},
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
                        60.85,
                        57.74,
                        56.41,
                        51.52,
                        59.16,
                        57.9,
                        52.41,
                        60.32,
                        56.59,
                        48.14,
                        52.43,
                        47.75
                ],
                "unit": "%"
        },
        "current": {
                "value": 47.75,
                "unit": "%",
                "change": -4.68,
                "change_percent": -8.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 55.1,
                "min": 47.75,
                "max": 60.85,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.22,
                        "percentage": 29.8
                },
                {
                        "category": "Segment B",
                        "value": 7.87,
                        "percentage": 16.5
                },
                {
                        "category": "Segment C",
                        "value": 7.78,
                        "percentage": 16.3
                },
                {
                        "category": "Segment D",
                        "value": 4.88,
                        "percentage": 10.2
                },
                {
                        "category": "Other",
                        "value": 13.0,
                        "percentage": 27.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.113948",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Lead Qualification Rate"
        }
    },
}
