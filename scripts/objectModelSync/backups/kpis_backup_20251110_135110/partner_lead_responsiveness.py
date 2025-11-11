"""
Partner Lead Responsiveness

The speed with which channel partners follow up on leads provided by the company.
"""

PARTNER_LEAD_RESPONSIVENESS = {
    "code": "PARTNER_LEAD_RESPONSIVENESS",
    "name": "Partner Lead Responsiveness",
    "description": "The speed with which channel partners follow up on leads provided by the company.",
    "formula": "Average Time Taken by Partners to Follow Up on Leads",
    "calculation_formula": "Average Time Taken by Partners to Follow Up on Leads",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Lead Responsiveness to be added.",
    "trend_analysis": """


    * Increasing partner lead responsiveness may indicate better alignment between partners and the company's sales goals.
    * Decreasing responsiveness could signal a lack of motivation or engagement from channel partners.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific regions or partners that consistently show higher or lower lead responsiveness?
    * How does the lead responsiveness compare with industry benchmarks or competitors' performance?
    
    
    """,
    "actionable_tips": """


    * Provide regular training and support to channel partners on lead management and follow-up best practices.
    * Implement lead tracking systems to monitor partner responsiveness and provide timely feedback and incentives.
    * Establish clear communication channels and expectations with partners regarding lead follow-up.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing lead responsiveness over time for different partners or regions.
    * Pie charts to compare the distribution of leads and the corresponding follow-up rates among partners.
    
    
    """,
    "risk_warnings": """


    * Low partner lead responsiveness can result in missed sales opportunities and revenue loss.
    * Consistently high responsiveness from a few partners may indicate an over-reliance on a small group, posing a risk to overall sales performance.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track and manage leads provided to partners.
    * Lead management platforms to automate lead distribution and follow-up tracking.
    
    
    """,
    "integration_points": """


    * Integrate lead responsiveness data with sales performance metrics to understand the impact on overall revenue generation.
    * Link lead management systems with marketing automation tools to ensure seamless lead handoff and follow-up.
    
    
    """,
    "change_impact_analysis": """


    * Improving partner lead responsiveness can lead to increased sales efficiency and revenue growth.
    * However, a sudden change in responsiveness may also impact the quality of leads and the overall sales pipeline.
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Lead Qualification", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.202164"},
    "required_objects": [],
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
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
                        836.6,
                        887.52,
                        913.43,
                        929.74,
                        906.37,
                        852.25,
                        903.98,
                        877.91,
                        950.18,
                        852.49,
                        917.7,
                        967.7
                ],
                "unit": "units"
        },
        "current": {
                "value": 967.7,
                "unit": "units",
                "change": 50.0,
                "change_percent": 5.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 899.66,
                "min": 836.6,
                "max": 967.7,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 242.72,
                        "percentage": 25.1
                },
                {
                        "category": "Category B",
                        "value": 183.86,
                        "percentage": 19.0
                },
                {
                        "category": "Category C",
                        "value": 122.23,
                        "percentage": 12.6
                },
                {
                        "category": "Category D",
                        "value": 45.1,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 373.79,
                        "percentage": 38.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.875402",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Partner Lead Responsiveness"
        }
    },
}
