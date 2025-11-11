"""
Product Adoption Rate

The percentage of customers who are using the product or service in the way it was intended. This KPI measures the effectiveness of the Customer Success Team in educating customers about the product or service.
"""

PRODUCT_ADOPTION_RATE = {
    "code": "PRODUCT_ADOPTION_RATE",
    "name": "Product Adoption Rate",
    "description": "The percentage of customers who are using the product or service in the way it was intended. This KPI measures the effectiveness of the Customer Success Team in educating customers about the product or service.",
    "formula": "(Number of Customers Using the Product or Feature / Total Target Market Customers) * 100",
    "calculation_formula": "(Number of Customers Using the Product or Feature / Total Target Market Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Adoption Rate to be added.",
    "trend_analysis": """

    * An increasing product adoption rate may indicate successful customer onboarding and education efforts.
    * A decreasing rate could signal issues with product usability, customer support, or changes in customer needs.
    
    """,
    "diagnostic_questions": """

    * Are there specific features or functionalities that customers struggle to adopt?
    * How does our product adoption rate compare with industry benchmarks or with different customer segments?
    
    """,
    "actionable_tips": """

    * Provide targeted training or resources to address common adoption barriers.
    * Collect and act on customer feedback to continuously improve product usability and customer support.
    * Segment customers based on their needs and provide personalized onboarding and education experiences.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the product adoption rate over time.
    * Pie charts to compare adoption rates across different customer segments or product features.
    
    """,
    "risk_warnings": """

    * Low product adoption rates may lead to customer churn and reduced lifetime value.
    * Failure to address adoption issues can result in negative reviews and damage to the brand's reputation.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) systems to track customer interactions and identify opportunities for education.
    * User behavior analytics tools to understand how customers engage with the product and identify adoption barriers.
    
    """,
    "integration_points": """

    * Integrate product adoption data with customer support systems to identify and address common issues.
    * Link adoption rates with sales data to understand the impact on revenue and customer retention.
    
    """,
    "change_impact_analysis": """

    * Improving product adoption can lead to increased customer satisfaction and loyalty.
    * However, changes in adoption rates may also impact revenue projections and customer retention metrics.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Market Segment", "Product", "Product Adoption", "Product Usage", "Sales Quota", "Sales Team", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.963205"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"],
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
                        76.32,
                        73.49,
                        68.81,
                        65.78,
                        62.26,
                        72.11,
                        66.39,
                        75.03,
                        61.92,
                        63.04,
                        78.91,
                        63.23
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.23,
                "unit": "%",
                "change": -15.68,
                "change_percent": -19.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 68.94,
                "min": 61.92,
                "max": 78.91,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.83,
                        "percentage": 18.7
                },
                {
                        "category": "Category B",
                        "value": 17.95,
                        "percentage": 28.4
                },
                {
                        "category": "Category C",
                        "value": 7.23,
                        "percentage": 11.4
                },
                {
                        "category": "Category D",
                        "value": 2.66,
                        "percentage": 4.2
                },
                {
                        "category": "Other",
                        "value": 23.56,
                        "percentage": 37.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.963205",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Product Adoption Rate"
        }
    },
}
