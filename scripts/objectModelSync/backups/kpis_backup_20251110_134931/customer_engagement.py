"""
Customer Engagement

A metric that measures how frequently and deeply customers interact with a product or service. This KPI measures the effectiveness of the Customer Success Team in building strong relationships with customers.
"""

CUSTOMER_ENGAGEMENT = {
    "code": "CUSTOMER_ENGAGEMENT",
    "name": "Customer Engagement",
    "description": "A metric that measures how frequently and deeply customers interact with a product or service. This KPI measures the effectiveness of the Customer Success Team in building strong relationships with customers.",
    "formula": "Total Number of Customer Interactions / Total Number of Customers",
    "calculation_formula": "Total Number of Customer Interactions / Total Number of Customers",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Engagement to be added.",
    "trend_analysis": """

    * An increasing customer engagement may indicate a positive trend in customer satisfaction and loyalty.
    * A decreasing engagement could signal potential issues in product usage, customer support, or overall satisfaction.
    
    """,
    "diagnostic_questions": """

    * Are there specific features or aspects of the product/service that customers engage with more frequently?
    * How does the customer engagement compare with industry benchmarks or with competitors?
    
    """,
    "actionable_tips": """

    * Regularly solicit feedback from customers to understand their needs and preferences.
    * Provide targeted training or resources to help customers maximize the value they get from the product/service.
    * Personalize communication and engagement efforts based on individual customer behaviors and preferences.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of customer engagement over time.
    * Heat maps to identify patterns of engagement based on different customer segments or product features.
    
    """,
    "risk_warnings": """

    * Low customer engagement may lead to higher churn rates and decreased customer lifetime value.
    * Inconsistent or sporadic engagement could indicate a lack of perceived value in the product/service.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and analyze customer interactions.
    * Customer feedback and survey tools to gather insights on engagement levels and satisfaction.
    
    """,
    "integration_points": """

    * Integrate customer engagement data with sales and marketing systems to align efforts and messaging.
    * Link engagement metrics with product development and improvement processes to address customer needs.
    
    """,
    "change_impact_analysis": """

    * Improving customer engagement can lead to increased customer retention and advocacy.
    * However, a focus solely on engagement metrics may overlook other aspects of customer success, such as product quality and support.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Product", "Product Adoption", "Product Usage", "Prospect Engagement", "Sales Team", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.244155"},
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
                        99,
                        145,
                        129,
                        128,
                        123,
                        119,
                        113,
                        112,
                        116,
                        125,
                        128,
                        121
                ],
                "unit": "count"
        },
        "current": {
                "value": 121,
                "unit": "count",
                "change": -7,
                "change_percent": -5.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 121.5,
                "min": 99,
                "max": 145,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 28.75,
                        "percentage": 23.8
                },
                {
                        "category": "Category B",
                        "value": 27.1,
                        "percentage": 22.4
                },
                {
                        "category": "Category C",
                        "value": 21.43,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 8.53,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 35.19,
                        "percentage": 29.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.244155",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Engagement"
        }
    },
}
