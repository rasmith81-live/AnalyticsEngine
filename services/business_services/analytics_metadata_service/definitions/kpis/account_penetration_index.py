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
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer Success Manager", "Key Account", "Key Account Manager", "Product", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.627800"},
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
                        62.36,
                        57.91,
                        66.43,
                        56.03,
                        61.02,
                        69.23,
                        58.55,
                        63.22,
                        70.14,
                        64.77,
                        71.66,
                        68.03
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.03,
                "unit": "%",
                "change": -3.63,
                "change_percent": -5.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 64.11,
                "min": 56.03,
                "max": 71.66,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 21.76,
                        "percentage": 32.0
                },
                {
                        "category": "Mid-Market",
                        "value": 8.6,
                        "percentage": 12.6
                },
                {
                        "category": "Small Business",
                        "value": 12.11,
                        "percentage": 17.8
                },
                {
                        "category": "Strategic Partners",
                        "value": 5.02,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 20.54,
                        "percentage": 30.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.333478",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Penetration Index"
        }
    },
}
