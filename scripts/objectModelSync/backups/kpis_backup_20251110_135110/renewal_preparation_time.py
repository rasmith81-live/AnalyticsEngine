"""
Renewal Preparation Time

The time needed to prepare for renewals with key accounts, impacting customer retention.
"""

RENEWAL_PREPARATION_TIME = {
    "code": "RENEWAL_PREPARATION_TIME",
    "name": "Renewal Preparation Time",
    "description": "The time needed to prepare for renewals with key accounts, impacting customer retention.",
    "formula": "Total Time Spent on Renewal Preparation / Number of Renewals Prepared",
    "calculation_formula": "Total Time Spent on Renewal Preparation / Number of Renewals Prepared",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Renewal Preparation Time to be added.",
    "trend_analysis": """


    * An increasing renewal preparation time may indicate growing complexity in customer needs or a lack of streamlined processes.
    * A decreasing time could signal improved account management efficiency or better alignment of customer expectations.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific accounts that consistently require more time to prepare for renewals?
    * How does our renewal preparation time compare with industry benchmarks or customer feedback?
    
    
    """,
    "actionable_tips": """


    * Implement customer success management strategies to proactively address account needs and minimize renewal preparation time.
    * Leverage automation and CRM tools to streamline renewal processes and reduce manual administrative tasks.
    * Regularly review and update account management practices to ensure they align with evolving customer requirements.
    
    
    """,
    "visualization_suggestions": """


    * Line charts tracking renewal preparation time over time to identify long-term trends and seasonal variations.
    * Stacked bar graphs comparing renewal preparation time across different key accounts to identify outliers and areas for improvement.
    
    
    """,
    "risk_warnings": """


    * Extended renewal preparation time may lead to customer dissatisfaction and potential loss of key accounts.
    * Inefficient renewal processes can strain internal resources and impact the ability to focus on new business opportunities.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track and manage key account interactions and renewal timelines.
    * Project management tools to streamline and coordinate cross-functional efforts related to key account renewals.
    
    
    """,
    "integration_points": """


    * Integrate renewal preparation time tracking with customer feedback systems to identify areas for improvement and align with customer expectations.
    * Link with sales forecasting and pipeline management to ensure adequate resources are allocated for key account renewal activities.
    
    
    """,
    "change_impact_analysis": """


    * Reducing renewal preparation time can free up resources for proactive account management and new business development.
    * However, overly aggressive time reduction efforts may compromise the quality of account management and customer relationships.
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Sales Representative"], "last_validated": "2025-11-10T13:49:33.329883"},
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
                        57.03,
                        51.33,
                        67.37,
                        59.74,
                        62.33,
                        62.23,
                        50.32,
                        59.6,
                        52.98,
                        48.24,
                        62.98,
                        57.25
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.25,
                "unit": "%",
                "change": -5.73,
                "change_percent": -9.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 57.62,
                "min": 48.24,
                "max": 67.37,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.22,
                        "percentage": 31.8
                },
                {
                        "category": "Category B",
                        "value": 7.64,
                        "percentage": 13.3
                },
                {
                        "category": "Category C",
                        "value": 9.89,
                        "percentage": 17.3
                },
                {
                        "category": "Category D",
                        "value": 3.53,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 17.97,
                        "percentage": 31.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.060533",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Renewal Preparation Time"
        }
    },
}
