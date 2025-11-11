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
                        317,
                        316,
                        300,
                        312,
                        296,
                        327,
                        278,
                        310,
                        292,
                        294,
                        297,
                        316
                ],
                "unit": "count"
        },
        "current": {
                "value": 316,
                "unit": "count",
                "change": 19,
                "change_percent": 6.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 304.58,
                "min": 278,
                "max": 327,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 70.64,
                        "percentage": 22.4
                },
                {
                        "category": "Category B",
                        "value": 59.64,
                        "percentage": 18.9
                },
                {
                        "category": "Category C",
                        "value": 43.24,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 14.84,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 127.64,
                        "percentage": 40.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.050392",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Referral Program Effectiveness"
        }
    },
}
