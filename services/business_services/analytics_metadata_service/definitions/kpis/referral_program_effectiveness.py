"""
Referral Program Effectiveness

The effectiveness of a referral program in generating new business through existing key accounts.
"""

REFERRAL_PROGRAM_EFFECTIVENESS = {
    "code": "REFERRAL_PROGRAM_EFFECTIVENESS",
    "name": "Referral Program Effectiveness",
    "description": "The effectiveness of a referral program in generating new business through existing key accounts.",
    "formula": "(New Customers Acquired Through Referrals / Total Number of Referrals) * 100",
    "calculation_formula": "(New Customers Acquired Through Referrals / Total Number of Referrals) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Referral Program Effectiveness to be added.",
    "trend_analysis": """



    * An increasing number of referrals from existing key accounts may indicate a growing satisfaction and loyalty among customers.
    * A decreasing number of referrals could signal dissatisfaction or a need for improvement in the referral program's incentives or processes.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the specific reasons why key accounts are or are not referring new business to us?
    * How does the referral program's performance compare to industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Regularly solicit feedback from key accounts to understand their satisfaction and identify areas for improvement in the referral program.
    * Offer incentives or rewards for key accounts to encourage and recognize successful referrals.
    * Continuously evaluate and update the referral program to ensure it remains relevant and appealing to key accounts.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the number of referrals over time to identify any trends or patterns.
    * Pie charts to visualize the distribution of referrals by key account or industry.
    
    
    
    """,
    "risk_warnings": """



    * A lack of referrals may indicate a weakened relationship with key accounts and potential loss of business in the future.
    * Over-reliance on referrals from key accounts may lead to vulnerability if those accounts reduce their business with the organization.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and manage interactions with key accounts and monitor referral activity.
    * Referral management platforms to streamline the process of tracking and rewarding successful referrals.
    
    
    
    """,
    "integration_points": """



    * Integrate referral program data with sales and marketing systems to better understand the impact of referrals on overall business performance.
    * Link referral program performance with customer satisfaction metrics to assess the correlation between referrals and customer loyalty.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the referral program can lead to increased sales and revenue from new business generated through key accounts.
    * However, a decline in referral effectiveness may require additional resources to address underlying issues and maintain strong relationships with key accounts.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Success Manager", "Key Account", "Key Account Manager", "Loyalty Program", "Quarterly Business Review", "Referral", "Renewal Management", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.322660"},
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
                        49.69,
                        63.46,
                        48.14,
                        52.65,
                        51.52,
                        50.31,
                        48.92,
                        52.87,
                        65.95,
                        53.77,
                        62.07,
                        65.54
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.54,
                "unit": "%",
                "change": 3.47,
                "change_percent": 5.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 55.41,
                "min": 48.14,
                "max": 65.95,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 13.61,
                        "percentage": 20.8
                },
                {
                        "category": "Existing Customers",
                        "value": 12.05,
                        "percentage": 18.4
                },
                {
                        "category": "VIP Customers",
                        "value": 9.12,
                        "percentage": 13.9
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.12,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 25.64,
                        "percentage": 39.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.761493",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Referral Program Effectiveness"
        }
    },
}
