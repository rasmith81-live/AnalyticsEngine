"""
Deal Registration Rate

The rate at which channel partners register deals, which helps in tracking partner engagement and potential sales.
"""

DEAL_REGISTRATION_RATE = {
    "code": "DEAL_REGISTRATION_RATE",
    "name": "Deal Registration Rate",
    "description": "The rate at which channel partners register deals, which helps in tracking partner engagement and potential sales.",
    "formula": "(Number of Deals Registered by Partners / Total Number of Deals) * 100",
    "calculation_formula": "(Number of Deals Registered by Partners / Total Number of Deals) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Registration Rate to be added.",
    "trend_analysis": """



    * An increasing deal registration rate may indicate improved partner engagement and potential sales growth.
    * A decreasing rate could signal disengagement or dissatisfaction among channel partners, leading to missed sales opportunities.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that are frequently registered by channel partners?
    * How does our deal registration rate compare with industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Provide incentives for channel partners to register deals, such as discounts or priority support.
    * Offer training and resources to help partners understand the benefits of deal registration and how to effectively utilize the process.
    * Regularly communicate with partners to gather feedback and address any concerns or barriers to deal registration.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of deal registration rate over time.
    * Pie charts to visualize the distribution of registered deals by product or partner.
    
    
    
    """,
    "risk_warnings": """



    * A low deal registration rate may lead to missed sales opportunities and underperformance in the channel sales channel.
    * Disengaged partners may seek alternative vendors or suppliers, impacting long-term relationships and revenue.
    
    
    
    """,
    "tracking_tools": """



    * Partner relationship management (PRM) software to streamline deal registration processes and provide visibility into partner activities.
    * Customer relationship management (CRM) systems to track and manage registered deals and associated sales activities.
    
    
    
    """,
    "integration_points": """



    * Integrate deal registration data with sales forecasting and pipeline management to align channel sales efforts with overall sales strategies.
    * Link deal registration with incentive and reward programs to recognize and incentivize high-performing partners.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the deal registration rate can lead to increased sales efficiency and revenue growth, but may require additional resources for partner support and engagement.
    * A low deal registration rate can impact the overall sales performance and market competitiveness, affecting the organization's bottom line and market position.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Deal", "Lead", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.911021"},
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
                        57.56,
                        46.05,
                        53.11,
                        60.91,
                        58.74,
                        55.27,
                        60.43,
                        47.98,
                        57.18,
                        52.96,
                        51.43,
                        57.01
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.01,
                "unit": "%",
                "change": 5.58,
                "change_percent": 10.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 54.89,
                "min": 46.05,
                "max": 60.91,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12.14,
                        "percentage": 21.3
                },
                {
                        "category": "Segment B",
                        "value": 13.86,
                        "percentage": 24.3
                },
                {
                        "category": "Segment C",
                        "value": 5.73,
                        "percentage": 10.1
                },
                {
                        "category": "Segment D",
                        "value": 3.24,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 22.04,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.880758",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Deal Registration Rate"
        }
    },
}
