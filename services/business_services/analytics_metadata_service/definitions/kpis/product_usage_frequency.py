"""
Product Usage Frequency

The frequency at which customers use a product or service.
"""

PRODUCT_USAGE_FREQUENCY = {
    "code": "PRODUCT_USAGE_FREQUENCY",
    "name": "Product Usage Frequency",
    "description": "The frequency at which customers use a product or service.",
    "formula": "Total Number of Product Uses / Total Number of Users",
    "calculation_formula": "Total Number of Product Uses / Total Number of Users",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Usage Frequency to be added.",
    "trend_analysis": """



    * Increasing product usage frequency may indicate higher customer satisfaction and engagement with the product or service.
    * Decreasing usage frequency could signal a decline in customer interest or the emergence of competing products in the market.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific features or aspects of the product that are driving higher or lower usage frequency?
    * How does the product usage frequency compare with industry benchmarks or with customer feedback and satisfaction metrics?
    
    
    
    """,
    "actionable_tips": """



    * Regularly gather customer feedback to understand their usage patterns and identify areas for improvement.
    * Offer incentives or promotions to encourage increased usage frequency, such as loyalty programs or exclusive content.
    * Continuously innovate and update the product to maintain customer interest and usage frequency.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend in product usage frequency over time.
    * Stacked bar charts comparing usage frequency across different customer segments or product versions.
    
    
    
    """,
    "risk_warnings": """



    * Low product usage frequency may lead to customer churn and decreased revenue.
    * High usage frequency without corresponding customer satisfaction may indicate potential burnout or dissatisfaction in the long run.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and analyze customer usage patterns.
    * Analytics tools to monitor and analyze customer behavior and engagement with the product or service.
    
    
    
    """,
    "integration_points": """



    * Integrate product usage frequency data with customer support systems to identify and address usage-related issues proactively.
    * Link usage frequency with marketing automation platforms to tailor targeted campaigns and communications based on usage patterns.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing product usage frequency can lead to higher customer lifetime value and overall revenue growth.
    * However, pushing for higher usage frequency without considering customer satisfaction may lead to negative brand perception and reduced customer loyalty.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.276741"},
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
                        103,
                        110,
                        106,
                        135,
                        115,
                        142,
                        143,
                        148,
                        104,
                        136,
                        142,
                        117
                ],
                "unit": "count"
        },
        "current": {
                "value": 117,
                "unit": "count",
                "change": -25,
                "change_percent": -17.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 125.08,
                "min": 103,
                "max": 148,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 24.71,
                        "percentage": 21.1
                },
                {
                        "category": "Product Line B",
                        "value": 19.75,
                        "percentage": 16.9
                },
                {
                        "category": "Product Line C",
                        "value": 19.06,
                        "percentage": 16.3
                },
                {
                        "category": "Services",
                        "value": 5.82,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 47.66,
                        "percentage": 40.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.655905",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Product Usage Frequency"
        }
    },
}
