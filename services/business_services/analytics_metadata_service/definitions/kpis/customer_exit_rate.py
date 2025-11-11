"""
Customer Exit Rate

The rate at which customers cease to do business with a company.
"""

CUSTOMER_EXIT_RATE = {
    "code": "CUSTOMER_EXIT_RATE",
    "name": "Customer Exit Rate",
    "description": "The rate at which customers cease to do business with a company.",
    "formula": "(Number of Customers Who Left / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Who Left / Total Number of Customers) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Exit Rate to be added.",
    "trend_analysis": """



    * An increasing customer exit rate may indicate issues with product quality, customer service, or pricing.
    * A decreasing rate could signal improved customer satisfaction, loyalty programs, or targeted marketing efforts.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common reasons cited by customers for ending their business relationship with us?
    * How does our customer exit rate compare with industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Implement customer feedback mechanisms to understand the reasons for customer exits and address them proactively.
    * Invest in customer service training and resources to improve overall customer experience and retention.
    * Develop loyalty programs or incentives to encourage repeat business and reduce customer churn.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of customer exit rates over time.
    * Pie charts to visualize the distribution of customer exits by reason or customer segment.
    
    
    
    """,
    "risk_warnings": """



    * High customer exit rates can lead to loss of revenue and market share.
    * Consistently high exit rates may indicate systemic issues that require immediate attention to prevent further loss.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify potential churn risks.
    * Social listening tools to monitor online conversations and sentiment about the brand.
    
    
    
    """,
    "integration_points": """



    * Integrate customer exit rate data with sales and marketing systems to identify patterns and triggers for customer exits.
    * Link customer exit rate with customer feedback systems to gain deeper insights into the reasons behind exits.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing customer exit rates can lead to increased customer lifetime value and higher overall revenue.
    * However, efforts to reduce exit rates may require increased investment in customer retention strategies and resources.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review"], "last_validated": "2025-11-10T13:49:32.827215"},
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
                        65.56,
                        63.2,
                        52.74,
                        66.97,
                        50.78,
                        49.03,
                        50.89,
                        56.63,
                        63.04,
                        48.14,
                        61.29,
                        49.13
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.13,
                "unit": "%",
                "change": -12.16,
                "change_percent": -19.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 56.45,
                "min": 48.14,
                "max": 66.97,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 13.99,
                        "percentage": 28.5
                },
                {
                        "category": "Existing Customers",
                        "value": 6.33,
                        "percentage": 12.9
                },
                {
                        "category": "VIP Customers",
                        "value": 7.14,
                        "percentage": 14.5
                },
                {
                        "category": "At-Risk Customers",
                        "value": 2.6,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 19.07,
                        "percentage": 38.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.653555",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Exit Rate"
        }
    },
}
