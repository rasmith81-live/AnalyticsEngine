"""
Customer Feedback Score

The score given by key customers based on their feedback regarding products or services.
"""

CUSTOMER_FEEDBACK_SCORE = {
    "code": "CUSTOMER_FEEDBACK_SCORE",
    "name": "Customer Feedback Score",
    "description": "The score given by key customers based on their feedback regarding products or services.",
    "formula": "Sum of Customer Ratings / Total Number of Ratings",
    "calculation_formula": "Sum of Customer Ratings / Total Number of Ratings",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Feedback Score to be added.",
    "trend_analysis": """



    * Increasing customer feedback scores may indicate improved product quality or customer service.
    * Decreasing scores could signal declining satisfaction with products or services.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific aspects of our products or services are contributing to higher or lower feedback scores?
    * How do our feedback scores compare with industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular customer feedback surveys to gather actionable insights for improvement.
    * Invest in training and development for sales and customer service teams to enhance customer experience.
    * Use feedback scores as a basis for continuous improvement initiatives across the organization.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of feedback scores over time.
    * Pie charts to visualize the distribution of feedback scores across different customer segments.
    
    
    
    """,
    "risk_warnings": """



    * Consistently low feedback scores can lead to customer churn and negative word-of-mouth.
    * Ignoring feedback scores may result in missed opportunities for improvement and innovation.
    
    
    
    """,
    "tracking_tools": """



    * Customer feedback management platforms like Medallia or Qualtrics for systematic collection and analysis of feedback.
    * CRM systems with built-in feedback tracking capabilities to integrate customer feedback data with sales management processes.
    
    
    
    """,
    "integration_points": """



    * Integrate customer feedback scores with performance management systems to align sales and service goals with customer satisfaction metrics.
    * Link feedback scores with product development and innovation processes to drive customer-centric improvements.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving feedback scores can lead to increased customer retention and lifetime value.
    * However, changes in feedback scores may also require adjustments in product offerings or service delivery, impacting operational processes.
    
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Key Account", "Key Account Manager", "Product", "Renewal Management"], "last_validated": "2025-11-10T13:49:32.833584"},
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
                        132,
                        115,
                        123,
                        101,
                        145,
                        111,
                        128,
                        119,
                        141,
                        128,
                        108,
                        121
                ],
                "unit": "count"
        },
        "current": {
                "value": 121,
                "unit": "count",
                "change": 13,
                "change_percent": 12.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 122.67,
                "min": 101,
                "max": 145,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 42.19,
                        "percentage": 34.9
                },
                {
                        "category": "Existing Customers",
                        "value": 23.64,
                        "percentage": 19.5
                },
                {
                        "category": "VIP Customers",
                        "value": 19.02,
                        "percentage": 15.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.99,
                        "percentage": 3.3
                },
                {
                        "category": "Other",
                        "value": 32.16,
                        "percentage": 26.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.674108",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Feedback Score"
        }
    },
}
