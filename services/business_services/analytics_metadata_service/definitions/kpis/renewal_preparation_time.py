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
                        50.89,
                        48.33,
                        55.24,
                        52.62,
                        49.34,
                        43.4,
                        53.56,
                        49.7,
                        46.55,
                        45.67,
                        46.11,
                        46.04
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.04,
                "unit": "%",
                "change": -0.07,
                "change_percent": -0.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 48.95,
                "min": 43.4,
                "max": 55.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.19,
                        "percentage": 33.0
                },
                {
                        "category": "Segment B",
                        "value": 8.24,
                        "percentage": 17.9
                },
                {
                        "category": "Segment C",
                        "value": 6.98,
                        "percentage": 15.2
                },
                {
                        "category": "Segment D",
                        "value": 3.23,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 12.4,
                        "percentage": 26.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.775332",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Renewal Preparation Time"
        }
    },
}
