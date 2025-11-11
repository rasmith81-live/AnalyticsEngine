"""
Strategic Account Contact Frequency

The frequency of contact or touchpoints with strategic accounts over a given time period.
"""

STRATEGIC_ACCOUNT_CONTACT_FREQUENCY = {
    "code": "STRATEGIC_ACCOUNT_CONTACT_FREQUENCY",
    "name": "Strategic Account Contact Frequency",
    "description": "The frequency of contact or touchpoints with strategic accounts over a given time period.",
    "formula": "Total Number of Contacts with Account / Specified Time Period",
    "calculation_formula": "Total Number of Contacts with Account / Specified Time Period",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Account Contact Frequency to be added.",
    "trend_analysis": """



    * An increasing contact frequency may indicate a proactive approach to account management and stronger relationships with key accounts.
    * A decreasing contact frequency could signal potential disengagement or neglect of strategic accounts, leading to missed opportunities or customer dissatisfaction.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific strategic accounts that receive significantly more or less contact than others?
    * How does our contact frequency compare with industry standards or best practices in key account management?
    
    
    
    """,
    "actionable_tips": """



    * Implement a structured account management plan with defined touchpoints and communication schedules for each strategic account.
    * Leverage customer relationship management (CRM) software to track and schedule interactions with key accounts.
    * Regularly review and adjust contact frequency based on the evolving needs and priorities of strategic accounts.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of contact frequency over time for each strategic account.
    * Comparison bar charts displaying the average contact frequency across different segments or regions.
    
    
    
    """,
    "risk_warnings": """



    * Low contact frequency may result in missed sales opportunities or reduced customer loyalty.
    * Excessive contact without adding value can lead to customer fatigue and potential disengagement.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems like Salesforce or HubSpot for tracking and managing interactions with strategic accounts.
    * Marketing automation platforms to personalize and automate communication with key accounts based on their preferences and behavior.
    
    
    
    """,
    "integration_points": """



    * Integrate contact frequency data with sales performance metrics to understand the impact of account management on revenue generation.
    * Link contact frequency with customer feedback and satisfaction scores to gauge the effectiveness of key account management efforts.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing contact frequency may lead to better customer retention and increased sales, but it could also require additional resources and time from the sales team.
    * Conversely, reducing contact frequency to focus on more profitable accounts may result in short-term gains but could harm long-term relationships and customer lifetime value.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Strategic Initiative", "Strategic Review"], "last_validated": "2025-11-10T13:49:33.596460"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        64.65,
                        63.11,
                        73.41,
                        60.03,
                        72.2,
                        65.22,
                        69.87,
                        70.01,
                        69.28,
                        69.93,
                        62.43,
                        67.86
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.86,
                "unit": "%",
                "change": 5.43,
                "change_percent": 8.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.33,
                "min": 60.03,
                "max": 73.41,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 20.51,
                        "percentage": 30.2
                },
                {
                        "category": "Mid-Market",
                        "value": 12.31,
                        "percentage": 18.1
                },
                {
                        "category": "Small Business",
                        "value": 10.37,
                        "percentage": 15.3
                },
                {
                        "category": "Strategic Partners",
                        "value": 4.71,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 19.96,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.452226",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Account Contact Frequency"
        }
    },
}
