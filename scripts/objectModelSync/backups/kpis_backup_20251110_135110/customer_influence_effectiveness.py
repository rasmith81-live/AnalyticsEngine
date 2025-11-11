"""
Customer Influence Effectiveness

The effectiveness of key accounts in influencing the market and bringing in additional business.
"""

CUSTOMER_INFLUENCE_EFFECTIVENESS = {
    "code": "CUSTOMER_INFLUENCE_EFFECTIVENESS",
    "name": "Customer Influence Effectiveness",
    "description": "The effectiveness of key accounts in influencing the market and bringing in additional business.",
    "formula": "Revenue from Influenced Leads / Total Number of Influenced Leads",
    "calculation_formula": "Revenue from Influenced Leads / Total Number of Influenced Leads",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Influence Effectiveness to be added.",
    "trend_analysis": """


    * Increasing customer influence effectiveness may indicate a growing market presence and strong relationships with key accounts.
    * Decreasing influence effectiveness could signal a loss of key accounts or a shift in market dynamics that diminishes the impact of existing relationships.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific key accounts that have shown a significant increase or decrease in their influence on the market?
    * How do our key accounts compare in terms of their ability to bring in additional business and influence market trends?
    
    
    """,
    "actionable_tips": """


    * Regularly assess the needs and expectations of key accounts to ensure their influence remains strong.
    * Invest in building deeper, more strategic partnerships with key accounts to enhance their ability to influence the market.
    * Provide key accounts with exclusive access to new products or services to further leverage their influence.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer influence effectiveness over time.
    * Comparison bar charts displaying the influence effectiveness of different key accounts.
    
    
    """,
    "risk_warnings": """


    * A decline in customer influence effectiveness could lead to a loss of market share and missed business opportunities.
    * Over-reliance on a small number of key accounts for market influence may pose a risk if those relationships deteriorate.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track and analyze the impact of key accounts on the market.
    * Social listening tools to monitor the online influence of key accounts and identify potential opportunities for business growth.
    
    
    """,
    "integration_points": """


    * Integrate customer influence effectiveness data with sales and marketing systems to align strategies with the most influential accounts.
    * Link customer influence metrics with product development and innovation processes to leverage key accounts for market insights.
    
    
    """,
    "change_impact_analysis": """


    * Improving customer influence effectiveness can lead to increased market share and revenue growth.
    * Declining influence effectiveness may require a shift in sales and marketing strategies to identify new influential accounts or re-engage existing ones.
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Lead", "Market Segment", "Quarterly Business Review", "Renewal Management", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.839338"},
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
                        357,
                        369,
                        339,
                        349,
                        376,
                        370,
                        344,
                        387,
                        366,
                        352,
                        353,
                        389
                ],
                "unit": "count"
        },
        "current": {
                "value": 389,
                "unit": "count",
                "change": 36,
                "change_percent": 10.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 362.58,
                "min": 339,
                "max": 389,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 83.06,
                        "percentage": 21.4
                },
                {
                        "category": "Category B",
                        "value": 46.81,
                        "percentage": 12.0
                },
                {
                        "category": "Category C",
                        "value": 68.96,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 22.87,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 167.3,
                        "percentage": 43.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.284458",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Influence Effectiveness"
        }
    },
}
