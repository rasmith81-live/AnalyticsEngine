"""
Account Saturation Index

A measure of how deeply a company has penetrated a key account with its products or services.
"""

ACCOUNT_SATURATION_INDEX = {
    "code": "ACCOUNT_SATURATION_INDEX",
    "name": "Account Saturation Index",
    "description": "A measure of how deeply a company has penetrated a key account with its products or services.",
    "formula": "(Number of Products/Services Purchased by Account / Total Number of Relevant Products/Services) * 100",
    "calculation_formula": "(Number of Products/Services Purchased by Account / Total Number of Relevant Products/Services) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Account Saturation Index to be added.",
    "trend_analysis": """



    * An increasing account saturation index may indicate successful cross-selling or upselling efforts within the key account.
    * A decreasing index could signal a loss of market share within the key account or increased competition.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific products or services have contributed to the increase or decrease in the account saturation index?
    * How does the account saturation index compare with industry benchmarks or with the performance of other key accounts?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and update the key account strategy to ensure alignment with the account's evolving needs and goals.
    * Invest in training and development for the sales team to enhance their ability to identify and capitalize on cross-selling or upselling opportunities.
    * Implement a customer relationship management (CRM) system to track interactions and identify potential areas for deeper penetration within the key account.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the account saturation index over time to identify trends and patterns.
    * Pie charts to visualize the distribution of products or services contributing to the account saturation index.
    
    
    
    """,
    "risk_warnings": """



    * A declining account saturation index may lead to decreased revenue and market share within the key account.
    * Overreliance on a single key account for a high account saturation index may pose a risk if the account experiences changes or challenges.
    
    
    
    """,
    "tracking_tools": """



    * CRM software such as Salesforce or HubSpot to track and manage key account relationships and opportunities.
    * Data analytics tools to identify patterns and opportunities for deeper penetration within the key account.
    
    
    
    """,
    "integration_points": """



    * Integrate the account saturation index with sales forecasting systems to align resource allocation and strategic planning.
    * Link the index with customer satisfaction metrics to ensure that deeper penetration efforts do not compromise overall satisfaction.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the account saturation index can lead to increased customer lifetime value and long-term loyalty.
    * However, overly aggressive tactics to increase the index may strain the relationship with the key account and impact overall customer satisfaction.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Product", "Renewal Management"], "last_validated": "2025-11-10T13:49:32.632994"},
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
                        56.15,
                        48.03,
                        53.72,
                        56.29,
                        54.84,
                        59.6,
                        45.45,
                        43.66,
                        53.96,
                        48.97,
                        50.08,
                        62.23
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.23,
                "unit": "%",
                "change": 12.15,
                "change_percent": 24.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 52.75,
                "min": 43.66,
                "max": 62.23,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 15.9,
                        "percentage": 25.6
                },
                {
                        "category": "Mid-Market",
                        "value": 11.44,
                        "percentage": 18.4
                },
                {
                        "category": "Small Business",
                        "value": 9.96,
                        "percentage": 16.0
                },
                {
                        "category": "Strategic Partners",
                        "value": 4.74,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 20.19,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.339391",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Saturation Index"
        }
    },
}
