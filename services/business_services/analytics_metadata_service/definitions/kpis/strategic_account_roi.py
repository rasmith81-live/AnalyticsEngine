"""
Strategic Account ROI

Return on investment for each strategic account, factoring in the costs of sales and support.
"""

STRATEGIC_ACCOUNT_ROI = {
    "code": "STRATEGIC_ACCOUNT_ROI",
    "name": "Strategic Account ROI",
    "description": "Return on investment for each strategic account, factoring in the costs of sales and support.",
    "formula": "(Net Profit from Strategic Account / Cost of Investment in Strategic Account) * 100",
    "calculation_formula": "(Net Profit from Strategic Account / Cost of Investment in Strategic Account) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Account ROI to be added.",
    "trend_analysis": """



    * Increasing ROI for strategic accounts may indicate successful sales and support efforts, leading to higher customer satisfaction and loyalty.
    * Decreasing ROI could signal inefficiencies in sales and support processes, potential dissatisfaction among strategic accounts, or increased competition.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific strategic accounts that consistently show higher or lower ROI, and what factors contribute to this trend?
    * How does the ROI of strategic accounts compare with industry benchmarks or with the ROI of non-strategic accounts?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and adjust sales and support strategies for each strategic account based on their unique needs and potential for growth.
    * Invest in training and development for sales and support teams to ensure they are equipped to effectively manage strategic accounts.
    * Implement customer relationship management (CRM) systems to better track interactions and identify opportunities for improving ROI.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the ROI of each strategic account over time to identify trends and patterns.
    * Pareto charts to visualize the distribution of ROI across strategic accounts and prioritize efforts accordingly.
    
    
    
    """,
    "risk_warnings": """



    * Low ROI for strategic accounts may lead to loss of key customers and revenue.
    * High ROI for certain strategic accounts may create over-reliance on a few customers, increasing vulnerability to market changes.
    
    
    
    """,
    "tracking_tools": """



    * CRM software like Salesforce or HubSpot for tracking and managing interactions with strategic accounts.
    * Business intelligence tools such as Tableau or Power BI for analyzing ROI data and identifying opportunities for improvement.
    
    
    
    """,
    "integration_points": """



    * Integrate ROI data with sales and marketing systems to align efforts and resources towards high-potential strategic accounts.
    * Link ROI tracking with customer feedback and satisfaction metrics to gain a comprehensive view of strategic account performance.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving ROI for strategic accounts can lead to increased revenue and customer lifetime value, but may require additional resources and investments.
    * Conversely, declining ROI may indicate the need for strategic shifts in sales and support strategies to prevent further losses.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Strategic Initiative", "Strategic Review", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.603116"},
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
                        63.26,
                        55.3,
                        54.98,
                        60.51,
                        65.2,
                        53.07,
                        56.37,
                        66.92,
                        55.76,
                        64.74,
                        56.87,
                        61.7
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.7,
                "unit": "%",
                "change": 4.83,
                "change_percent": 8.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 59.56,
                "min": 53.07,
                "max": 66.92,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 13.81,
                        "percentage": 22.4
                },
                {
                        "category": "Mid-Market",
                        "value": 10.82,
                        "percentage": 17.5
                },
                {
                        "category": "Small Business",
                        "value": 6.4,
                        "percentage": 10.4
                },
                {
                        "category": "Strategic Partners",
                        "value": 6.13,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 24.54,
                        "percentage": 39.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.470658",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Account ROI"
        }
    },
}
