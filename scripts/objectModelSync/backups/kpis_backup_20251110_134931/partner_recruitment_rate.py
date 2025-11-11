"""
Partner Recruitment Rate

The rate at which new channel partners are recruited over a specific period, which indicates the expansion of the channel network.
"""

PARTNER_RECRUITMENT_RATE = {
    "code": "PARTNER_RECRUITMENT_RATE",
    "name": "Partner Recruitment Rate",
    "description": "The rate at which new channel partners are recruited over a specific period, which indicates the expansion of the channel network.",
    "formula": "(Number of New Partners Acquired / Number of Partners Targeted) * 100",
    "calculation_formula": "(Number of New Partners Acquired / Number of Partners Targeted) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Recruitment Rate to be added.",
    "trend_analysis": """

    * An increasing partner recruitment rate may indicate successful marketing and sales efforts to attract new partners.
    * A decreasing rate could signal market saturation or ineffective partner onboarding processes.
    
    """,
    "diagnostic_questions": """

    * What specific strategies or channels have been most effective in recruiting new partners?
    * Are there any common barriers or challenges that potential partners face during the recruitment process?
    
    """,
    "actionable_tips": """

    * Offer comprehensive training and support to new partners to ensure their success and commitment.
    * Regularly review and update the partner recruitment process to streamline and improve efficiency.
    * Implement referral programs or incentives to encourage existing partners to refer new potential partners.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the monthly or quarterly trend of partner recruitment rate.
    * Pie charts to compare the contribution of different channels or strategies to partner recruitment.
    
    """,
    "risk_warnings": """

    * Rapid partner recruitment without proper vetting can lead to poor-quality partnerships and negative impact on brand reputation.
    * A declining partner recruitment rate may indicate a need for reevaluation of the overall channel strategy and approach.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and manage partner leads and conversions.
    * Partner Relationship Management (PRM) platforms to streamline partner onboarding and management processes.
    
    """,
    "integration_points": """

    * Integrate partner recruitment data with sales performance metrics to understand the impact of new partners on overall sales.
    * Link partner recruitment with marketing analytics to assess the effectiveness of different marketing channels in attracting potential partners.
    
    """,
    "change_impact_analysis": """

    * An increase in partner recruitment rate can lead to expanded market reach and potentially higher sales volume.
    * However, rapid expansion without proper support and resources can strain internal operations and customer service capabilities.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Advocacy Program", "Customer Success Manager", "Expansion Opportunity", "Loyalty Program", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.897206"},
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
                        58.57,
                        75.18,
                        70.53,
                        59.66,
                        70.62,
                        74.45,
                        73.05,
                        69.84,
                        64.4,
                        63.13,
                        59.42,
                        76.53
                ],
                "unit": "%"
        },
        "current": {
                "value": 76.53,
                "unit": "%",
                "change": 17.11,
                "change_percent": 28.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.95,
                "min": 58.57,
                "max": 76.53,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.01,
                        "percentage": 19.6
                },
                {
                        "category": "Category B",
                        "value": 18.44,
                        "percentage": 24.1
                },
                {
                        "category": "Category C",
                        "value": 14.32,
                        "percentage": 18.7
                },
                {
                        "category": "Category D",
                        "value": 6.35,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 22.41,
                        "percentage": 29.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.897206",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Recruitment Rate"
        }
    },
}
