"""
Customer Health Score

A composite metric that combines various customer data points to indicate the overall health and long-term prospects of a customer relationship.
"""

CUSTOMER_HEALTH_SCORE = {
    "code": "CUSTOMER_HEALTH_SCORE",
    "name": "Customer Health Score",
    "description": "A composite metric that combines various customer data points to indicate the overall health and long-term prospects of a customer relationship.",
    "formula": "Sum of Weighted Customer Metrics (such as product usage, satisfaction, etc.)",
    "calculation_formula": "Sum of Weighted Customer Metrics (such as product usage, satisfaction, etc.)",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Health Score to be added.",
    "trend_analysis": """



    * Increasing customer health score may indicate stronger engagement and satisfaction with the product or service.
    * Decreasing score could signal potential issues with customer retention and loyalty.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments or demographics that consistently show lower health scores?
    * How does the customer health score align with customer feedback and support interactions?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular customer feedback surveys to gauge satisfaction and identify areas for improvement.
    * Provide targeted resources or support to customers with lower health scores to improve their experience.
    * Develop personalized retention strategies based on individual customer health scores.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of customer health scores over time.
    * Pie charts to visualize the distribution of customer health scores across different segments.
    
    
    
    """,
    "risk_warnings": """



    * Low customer health scores may lead to increased churn and reduced lifetime value.
    * Inaccurate or outdated data inputs can skew the customer health score and lead to misinformed decisions.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze customer interactions and feedback.
    * Customer health score calculators or algorithms to automate the process of determining scores.
    
    
    
    """,
    "integration_points": """



    * Integrate customer health scores with sales and marketing systems to tailor outreach and messaging based on customer health.
    * Link customer health scores with customer success platforms to proactively address potential issues and improve retention.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving customer health scores can lead to increased customer lifetime value and overall revenue.
    * However, focusing solely on the score without addressing underlying customer issues may lead to short-term improvements but long-term dissatisfaction.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.835106"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"],
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
                        66.2,
                        63.4,
                        63.9,
                        66.3,
                        66.5,
                        64.0,
                        63.6,
                        60.8,
                        64.5,
                        67.3,
                        69.4,
                        57.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 57.6,
                "unit": "score",
                "change": -11.8,
                "change_percent": -17.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 64.46,
                "min": 57.6,
                "max": 69.4,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 9.71,
                        "percentage": 16.9
                },
                {
                        "category": "Existing Customers",
                        "value": 7.53,
                        "percentage": 13.1
                },
                {
                        "category": "VIP Customers",
                        "value": 6.74,
                        "percentage": 11.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 9.22,
                        "percentage": 16.0
                },
                {
                        "category": "Other",
                        "value": 24.4,
                        "percentage": 42.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.683966",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Customer Health Score"
        }
    },
}
