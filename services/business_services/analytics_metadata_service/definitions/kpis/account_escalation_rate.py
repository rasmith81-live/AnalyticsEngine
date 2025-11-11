"""
Account Escalation Rate

The frequency at which customer issues are escalated to higher levels of customer service or management.
"""

ACCOUNT_ESCALATION_RATE = {
    "code": "ACCOUNT_ESCALATION_RATE",
    "name": "Account Escalation Rate",
    "description": "The frequency at which customer issues are escalated to higher levels of customer service or management.",
    "formula": "(Number of Escalated Cases / Total Number of Cases) * 100",
    "calculation_formula": "(Number of Escalated Cases / Total Number of Cases) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Account Escalation Rate to be added.",
    "trend_analysis": """



    * An increasing account escalation rate may indicate systemic issues with customer service or product quality that need to be addressed.
    * A decreasing rate could signal improvements in frontline customer support or better product reliability.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common reasons why customer issues are being escalated, and can these be addressed at the root cause?
    * How does our account escalation rate compare with industry benchmarks or with our competitors?
    
    
    
    """,
    "actionable_tips": """



    * Invest in ongoing training for customer service representatives to handle a wider range of issues without escalation.
    * Implement a feedback loop from escalated cases to identify recurring problems and address them systematically.
    * Consider implementing self-service options or improved documentation to empower customers to resolve issues without escalation.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of account escalation rates over time.
    * Pareto charts to identify the most common reasons for escalation.
    
    
    
    """,
    "risk_warnings": """



    * High account escalation rates can lead to customer churn and damage to the brand's reputation.
    * Chronic escalations may indicate deeper issues in product quality or customer service that need immediate attention.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and analyze escalation patterns.
    * Quality management software to identify and address recurring product issues.
    
    
    
    """,
    "integration_points": """



    * Integrate account escalation data with customer satisfaction surveys to understand the impact of escalations on overall customer experience.
    * Link escalation data with product development and quality assurance processes to address root causes of customer issues.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing account escalation rates can lead to higher customer satisfaction and loyalty, positively impacting long-term revenue.
    * However, addressing escalation issues may require investments in training, technology, or product improvements.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Product", "Renewal Management", "Service Level Agreement", "Support Ticket"], "last_validated": "2025-11-10T13:49:32.626759"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
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
                        73.29,
                        72.69,
                        66.13,
                        62.72,
                        69.6,
                        59.93,
                        59.9,
                        57.61,
                        71.04,
                        74.75,
                        65.99,
                        70.87
                ],
                "unit": "%"
        },
        "current": {
                "value": 70.87,
                "unit": "%",
                "change": 4.88,
                "change_percent": 7.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.04,
                "min": 57.61,
                "max": 74.75,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 14.81,
                        "percentage": 20.9
                },
                {
                        "category": "Mid-Market",
                        "value": 19.4,
                        "percentage": 27.4
                },
                {
                        "category": "Small Business",
                        "value": 8.76,
                        "percentage": 12.4
                },
                {
                        "category": "Strategic Partners",
                        "value": 6.16,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 21.74,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.331473",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Escalation Rate"
        }
    },
}
