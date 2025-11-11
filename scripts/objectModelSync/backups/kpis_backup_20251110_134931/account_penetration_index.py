"""
Account Penetration Index

The number of products or services sold to key accounts relative to the potential number of products or services, indicating cross-selling success.
"""

ACCOUNT_PENETRATION_INDEX = {
    "code": "ACCOUNT_PENETRATION_INDEX",
    "name": "Account Penetration Index",
    "description": "The number of products or services sold to key accounts relative to the potential number of products or services, indicating cross-selling success.",
    "formula": "(Number of Products/Services Sold to Account / Total Sales Opportunities for Account) * 100",
    "calculation_formula": "(Number of Products/Services Sold to Account / Total Sales Opportunities for Account) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Account Penetration Index to be added.",
    "trend_analysis": """

    * An increasing Account Penetration Index may indicate successful cross-selling efforts and a strong relationship with key accounts.
    * A decreasing index could signal missed opportunities for cross-selling or a decline in the value of the products or services offered.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or services that key accounts consistently show interest in?
    * How does our Account Penetration Index compare with industry benchmarks or with historical data?
    
    """,
    "actionable_tips": """

    * Train sales teams to identify cross-selling opportunities and effectively communicate the value of additional products or services.
    * Regularly review and update the product or service offerings to ensure they align with the evolving needs of key accounts.
    * Implement a customer relationship management (CRM) system to track interactions and identify potential cross-selling opportunities.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of Account Penetration Index over time.
    * Pie charts to visualize the distribution of products or services sold to key accounts.
    
    """,
    "risk_warnings": """

    * A low Account Penetration Index may lead to missed revenue opportunities and reduced customer loyalty.
    * A high index without corresponding customer satisfaction may indicate aggressive selling tactics that could harm long-term relationships.
    
    """,
    "tracking_tools": """

    * CRM systems with sales tracking capabilities to monitor cross-selling efforts and track customer preferences.
    * Data analytics tools to identify patterns and opportunities for cross-selling based on key account behavior.
    
    """,
    "integration_points": """

    * Integrate the Account Penetration Index with customer feedback systems to understand the impact of cross-selling on customer satisfaction.
    * Link the index with inventory management systems to ensure the availability of cross-sellable products or services.
    
    """,
    "change_impact_analysis": """

    * Improving the Account Penetration Index can lead to increased revenue and stronger customer relationships.
    * However, aggressive cross-selling tactics may negatively impact customer trust and loyalty, affecting long-term business performance.
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer Success Manager", "Key Account", "Key Account Manager", "Product", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:22.992511"},
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
                        82.17,
                        71.06,
                        84.93,
                        69.06,
                        76.69,
                        82.82,
                        78.28,
                        82.75,
                        83.21,
                        84.78,
                        83.28,
                        69.01
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.01,
                "unit": "%",
                "change": -14.27,
                "change_percent": -17.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 79.0,
                "min": 69.01,
                "max": 84.93,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 24.04,
                        "percentage": 34.8
                },
                {
                        "category": "Category B",
                        "value": 8.0,
                        "percentage": 11.6
                },
                {
                        "category": "Category C",
                        "value": 6.17,
                        "percentage": 8.9
                },
                {
                        "category": "Category D",
                        "value": 8.44,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 22.36,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:22.992511",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Penetration Index"
        }
    },
}
