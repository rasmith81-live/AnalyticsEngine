"""
Customer Self-Service Success Rate

The percentage of issues that customers resolve on their own, without direct intervention from customer support.
"""

CUSTOMER_SELF_SERVICE_SUCCESS_RATE = {
    "code": "CUSTOMER_SELF_SERVICE_SUCCESS_RATE",
    "name": "Customer Self-Service Success Rate",
    "description": "The percentage of issues that customers resolve on their own, without direct intervention from customer support.",
    "formula": "(Number of Self-Service Resolutions / Total Number of Self-Service Attempts) * 100",
    "calculation_formula": "(Number of Self-Service Resolutions / Total Number of Self-Service Attempts) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Self-Service Success Rate to be added.",
    "trend_analysis": """



    * An increasing self-service success rate may indicate improved user experience and more intuitive product design.
    * A decreasing rate could signal complex or confusing product features that require additional support or a lack of easily accessible self-service resources.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common types of issues that customers struggle to resolve on their own?
    * How does our self-service success rate compare with industry benchmarks or with similar products in the market?
    
    
    
    """,
    "actionable_tips": """



    * Regularly update and improve self-service resources such as FAQs, tutorials, and knowledge bases.
    * Collect and analyze customer feedback to identify pain points in the self-service process and make necessary improvements.
    * Provide incentives for customers to utilize self-service options, such as exclusive content or discounts.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of self-service success rate over time.
    * Pie charts comparing the distribution of resolved issues between self-service and customer support.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low self-service success rate may indicate a need for better user education or product simplification.
    * High reliance on customer support for issue resolution can lead to increased support costs and longer resolution times.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems with self-service analytics capabilities.
    * Customer feedback and survey tools to gather insights on self-service effectiveness.
    
    
    
    """,
    "integration_points": """



    * Integrate self-service success rate data with product development processes to prioritize features that improve user autonomy.
    * Link self-service analytics with customer relationship management systems to identify opportunities for proactive customer support.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the self-service success rate can lead to higher customer satisfaction and loyalty, positively impacting customer retention and lifetime value.
    * Conversely, a low self-service success rate may result in increased customer churn and negative word-of-mouth, affecting brand reputation.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Service Level Agreement", "Support Ticket"], "last_validated": "2025-11-10T13:49:32.883421"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
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
                        53.65,
                        53.55,
                        62.27,
                        63.96,
                        53.63,
                        56.24,
                        51.01,
                        54.39,
                        49.41,
                        61.9,
                        62.73,
                        67.08
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.08,
                "unit": "%",
                "change": 4.35,
                "change_percent": 6.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 57.49,
                "min": 49.41,
                "max": 67.08,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 21.11,
                        "percentage": 31.5
                },
                {
                        "category": "Existing Customers",
                        "value": 14.78,
                        "percentage": 22.0
                },
                {
                        "category": "VIP Customers",
                        "value": 9.28,
                        "percentage": 13.8
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.64,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 16.27,
                        "percentage": 24.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.813448",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Self-Service Success Rate"
        }
    },
}
