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
                        76.2,
                        76.08,
                        57.14,
                        69.37,
                        74.18,
                        68.38,
                        58.76,
                        71.63,
                        75.96,
                        58.85,
                        62.09,
                        57.5
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.5,
                "unit": "%",
                "change": -4.59,
                "change_percent": -7.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.18,
                "min": 57.14,
                "max": 76.2,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.22,
                        "percentage": 21.3
                },
                {
                        "category": "Category B",
                        "value": 15.8,
                        "percentage": 27.5
                },
                {
                        "category": "Category C",
                        "value": 6.41,
                        "percentage": 11.1
                },
                {
                        "category": "Category D",
                        "value": 6.1,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 16.97,
                        "percentage": 29.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:22.997011",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Saturation Index"
        }
    },
}
