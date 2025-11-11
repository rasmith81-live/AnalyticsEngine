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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Market Segment", "Product", "Product Adoption", "Product Usage", "Sales Quota", "Sales Team", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.261818"},
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
                        79.7,
                        67.56,
                        78.9,
                        69.72,
                        70.81,
                        64.44,
                        64.36,
                        66.25,
                        67.8,
                        67.89,
                        72.93,
                        66.98
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.98,
                "unit": "%",
                "change": -5.95,
                "change_percent": -8.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 69.78,
                "min": 64.36,
                "max": 79.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 17.52,
                        "percentage": 26.2
                },
                {
                        "category": "Existing Customers",
                        "value": 9.05,
                        "percentage": 13.5
                },
                {
                        "category": "VIP Customers",
                        "value": 11.67,
                        "percentage": 17.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.06,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 23.68,
                        "percentage": 35.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.620010",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Product Adoption Rate"
        }
    },
}
