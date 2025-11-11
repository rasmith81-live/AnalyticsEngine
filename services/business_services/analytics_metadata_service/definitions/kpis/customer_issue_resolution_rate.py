"""
Customer Issue Resolution Rate

The percentage of all customer issues that are resolved satisfactorily.
"""

CUSTOMER_ISSUE_RESOLUTION_RATE = {
    "code": "CUSTOMER_ISSUE_RESOLUTION_RATE",
    "name": "Customer Issue Resolution Rate",
    "description": "The percentage of all customer issues that are resolved satisfactorily.",
    "formula": "(Number of Issues Resolved on First Interaction / Total Number of Issues) * 100",
    "calculation_formula": "(Number of Issues Resolved on First Interaction / Total Number of Issues) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Issue Resolution Rate to be added.",
    "trend_analysis": """



    * An increasing customer issue resolution rate may indicate improved customer service processes or better product quality.
    * A decreasing rate could signal a decline in customer satisfaction or an increase in product issues.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific product lines or services that consistently have higher issue resolution rates?
    * How does our issue resolution rate compare with industry benchmarks or customer feedback?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular customer feedback surveys to identify areas for improvement.
    * Provide additional training for customer service teams to handle complex issues more effectively.
    * Invest in product quality control measures to reduce the occurrence of customer issues.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of issue resolution rates over time.
    * Pie charts to compare the distribution of resolved and unresolved issues by category.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low issue resolution rate can lead to customer churn and negative word-of-mouth.
    * High issue resolution rates may also indicate a lack of thorough problem-solving, leading to recurring issues.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and manage customer issues and resolutions.
    * Quality management systems to identify and address recurring product issues.
    
    
    
    """,
    "integration_points": """



    * Integrate issue resolution rate data with customer feedback systems to gain a comprehensive view of customer satisfaction.
    * Link with product development processes to address recurring issues and improve product quality.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the issue resolution rate can lead to higher customer retention and loyalty.
    * However, a focus solely on increasing the rate may lead to rushed or inadequate resolutions, impacting overall customer satisfaction.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Support Ticket"], "replaces": ["CUSTOMER_PROBLEM_RESOLUTION_RATE"], "last_validated": "2025-11-10T13:49:32.840347"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"],
    "module_code": "CUSTOMER_SUCCESS",
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
                        69.15,
                        59.34,
                        52.06,
                        57.04,
                        66.54,
                        58.58,
                        57.45,
                        69.34,
                        53.05,
                        53.53,
                        55.8,
                        64.35
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.35,
                "unit": "%",
                "change": 8.55,
                "change_percent": 15.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 59.69,
                "min": 52.06,
                "max": 69.34,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 10.13,
                        "percentage": 15.7
                },
                {
                        "category": "Existing Customers",
                        "value": 9.01,
                        "percentage": 14.0
                },
                {
                        "category": "VIP Customers",
                        "value": 15.68,
                        "percentage": 24.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 6.99,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 22.54,
                        "percentage": 35.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.700471",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Issue Resolution Rate"
        }
    },
}
