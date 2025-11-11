"""
Customer Downgrade Rate

The percentage of customers that move to a lower-tier service or product offering.
"""

CUSTOMER_DOWNGRADE_RATE = {
    "code": "CUSTOMER_DOWNGRADE_RATE",
    "name": "Customer Downgrade Rate",
    "description": "The percentage of customers that move to a lower-tier service or product offering.",
    "formula": "(Number of Customers Downgraded / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Downgraded / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Downgrade Rate to be added.",
    "trend_analysis": """


    * An increasing customer downgrade rate may indicate dissatisfaction with current service or product offerings.
    * A decreasing rate could signal successful upselling efforts or improved customer satisfaction.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific reasons why customers are downgrading their services or products?
    * How does our customer downgrade rate compare with industry benchmarks or competitors?
    
    
    """,
    "actionable_tips": """


    * Regularly survey customers to understand their needs and preferences.
    * Provide additional training or support for customers to maximize the value they receive from higher-tier offerings.
    * Review pricing strategies to ensure that the value proposition for higher-tier offerings is clear and compelling.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the customer downgrade rate over time.
    * Pie charts illustrating the distribution of downgrades by product or service category.
    
    
    """,
    "risk_warnings": """


    * High customer downgrade rates can lead to decreased revenue and market share.
    * Frequent downgrades may indicate that the organization is not meeting customer expectations or needs.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems to track customer interactions and feedback.
    * Survey and feedback tools to gather insights from customers about their experiences.
    
    
    """,
    "integration_points": """


    * Integrate customer downgrade rate data with sales and marketing systems to understand the impact on revenue and customer acquisition.
    * Link with customer support platforms to identify and address common reasons for downgrades.
    
    
    """,
    "change_impact_analysis": """


    * Decreasing the customer downgrade rate can lead to increased customer lifetime value and loyalty.
    * However, efforts to reduce downgrades may require additional resources and investment in customer satisfaction initiatives.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.812315"},
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
                        50.39,
                        46.04,
                        52.86,
                        44.22,
                        50.51,
                        43.55,
                        41.85,
                        54.85,
                        46.44,
                        50.3,
                        43.71,
                        39.1
                ],
                "unit": "%"
        },
        "current": {
                "value": 39.1,
                "unit": "%",
                "change": -4.61,
                "change_percent": -10.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 46.99,
                "min": 39.1,
                "max": 54.85,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.44,
                        "percentage": 24.1
                },
                {
                        "category": "Category B",
                        "value": 8.78,
                        "percentage": 22.5
                },
                {
                        "category": "Category C",
                        "value": 3.93,
                        "percentage": 10.1
                },
                {
                        "category": "Category D",
                        "value": 2.68,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 14.27,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.228823",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Downgrade Rate"
        }
    },
}
