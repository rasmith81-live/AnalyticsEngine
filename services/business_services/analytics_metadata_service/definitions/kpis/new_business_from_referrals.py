"""
New Business from Referrals

The amount of new business generated through referrals from existing key accounts.
"""

NEW_BUSINESS_FROM_REFERRALS = {
    "code": "NEW_BUSINESS_FROM_REFERRALS",
    "name": "New Business from Referrals",
    "description": "The amount of new business generated through referrals from existing key accounts.",
    "formula": "Revenue from Referred Customers / Total Revenue",
    "calculation_formula": "Revenue from Referred Customers / Total Revenue",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for New Business from Referrals to be added.",
    "trend_analysis": """



    * Increasing new business from referrals may indicate a strong relationship with existing key accounts and a high level of customer satisfaction.
    * A decreasing trend could signal a need to improve the quality of service or products offered to existing key accounts, leading to fewer referrals.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific key accounts that consistently provide more referrals than others?
    * How does the conversion rate of referrals compare to other lead generation sources?
    
    
    
    """,
    "actionable_tips": """



    * Implement a formal referral program to incentivize existing key accounts to refer new business.
    * Regularly communicate with key accounts to ensure their needs are being met and to encourage them to refer others.
    * Provide exceptional service and value to existing key accounts to naturally generate more referrals.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of new business from referrals over time.
    * Pie charts comparing the percentage of new business from referrals versus other sources.
    
    
    
    """,
    "risk_warnings": """



    * Low levels of new business from referrals may indicate a lack of satisfaction or loyalty among existing key accounts.
    * Relying too heavily on referrals may limit the diversity of the customer base and increase vulnerability to changes in the referral network.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and manage referral activities from key accounts.
    * Referral tracking tools to identify which key accounts are providing the most referrals and which ones need more attention.
    
    
    
    """,
    "integration_points": """



    * Integrate referral tracking with sales performance metrics to understand the impact of referrals on overall sales results.
    * Link referral data with customer satisfaction surveys to correlate referral activity with customer loyalty and satisfaction levels.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing new business from referrals can lead to a more predictable and sustainable sales pipeline, reducing the reliance on other lead generation methods.
    * However, a decrease in new business from referrals may require additional investment in other lead generation strategies to maintain sales growth.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Quarterly Business Review", "Renewal Management", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:33.071860"},
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
                        508.59,
                        580.34,
                        459.79,
                        577.55,
                        531.04,
                        513.16,
                        540.83,
                        559.91,
                        605.48,
                        566.17,
                        568.77,
                        568.67
                ],
                "unit": "units"
        },
        "current": {
                "value": 568.67,
                "unit": "units",
                "change": -0.1,
                "change_percent": -0.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 548.36,
                "min": 459.79,
                "max": 605.48,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 165.69,
                        "percentage": 29.1
                },
                {
                        "category": "Existing Customers",
                        "value": 93.18,
                        "percentage": 16.4
                },
                {
                        "category": "VIP Customers",
                        "value": 104.21,
                        "percentage": 18.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 58.45,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 147.14,
                        "percentage": 25.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.235177",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "New Business from Referrals"
        }
    },
}
