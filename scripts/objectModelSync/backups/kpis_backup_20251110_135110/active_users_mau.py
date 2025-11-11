"""
Active Users (MAU)

The number of unique users who engage with a service or product within a selected period.
"""

ACTIVE_USERS_MAU = {
    "code": "ACTIVE_USERS_MAU",
    "name": "Active Users (MAU)",
    "description": "The number of unique users who engage with a service or product within a selected period.",
    "formula": "Total Number of Unique Active Users in a selected period",
    "calculation_formula": "Total Number of Unique Active Users in a selected period",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Active Users (MAU) to be added.",
    "trend_analysis": """


    * An increasing MAU may indicate growing user engagement and interest in the product or service.
    * A decreasing MAU could signal declining interest, potential issues with the product, or increased competition in the market.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific features or content that are driving user engagement?
    * How does our MAU compare with industry benchmarks or seasonal trends?
    
    
    """,
    "actionable_tips": """


    * Regularly update and refresh content or features to maintain user interest and engagement.
    * Invest in targeted marketing or promotional campaigns to attract and retain users.
    * Collect and analyze user feedback to identify areas for improvement and innovation.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing monthly trends in MAU over time.
    * Cohort analysis to track the retention of users who joined in specific time periods.
    
    
    """,
    "risk_warnings": """


    * Declining MAU may lead to reduced revenue and market share.
    * High MAU with low conversion rates may indicate issues with the product or service that need to be addressed.
    
    
    """,
    "tracking_tools": """


    * Analytics platforms like Google Analytics or Mixpanel to track user engagement and behavior.
    * Customer relationship management (CRM) systems to manage and nurture customer relationships for improved retention.
    
    
    """,
    "integration_points": """


    * Integrate MAU data with marketing automation systems to personalize user experiences and communications.
    * Link MAU with customer support systems to identify and address user concerns or issues proactively.
    
    
    """,
    "change_impact_analysis": """


    * Increasing MAU can lead to higher revenue and market growth, but may also require scaling up infrastructure and support resources.
    * Decreasing MAU can impact overall business performance and may require strategic shifts in product development or marketing strategies.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.636087"},
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
                        98,
                        137,
                        144,
                        101,
                        142,
                        140,
                        141,
                        118,
                        135,
                        127,
                        104,
                        102
                ],
                "unit": "count"
        },
        "current": {
                "value": 102,
                "unit": "count",
                "change": -2,
                "change_percent": -1.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 124.08,
                "min": 98,
                "max": 144,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.1,
                        "percentage": 16.8
                },
                {
                        "category": "Category B",
                        "value": 19.82,
                        "percentage": 19.4
                },
                {
                        "category": "Category C",
                        "value": 14.45,
                        "percentage": 14.2
                },
                {
                        "category": "Category D",
                        "value": 12.98,
                        "percentage": 12.7
                },
                {
                        "category": "Other",
                        "value": 37.65,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.001609",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Active Users (MAU)"
        }
    },
}
