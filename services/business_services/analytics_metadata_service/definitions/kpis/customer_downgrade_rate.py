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
                        61.24,
                        69.85,
                        63.89,
                        66.17,
                        51.07,
                        57.14,
                        56.99,
                        52.6,
                        56.15,
                        69.17,
                        60.05,
                        65.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.71,
                "unit": "%",
                "change": 5.66,
                "change_percent": 9.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 60.84,
                "min": 51.07,
                "max": 69.85,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 17.85,
                        "percentage": 27.2
                },
                {
                        "category": "Existing Customers",
                        "value": 11.61,
                        "percentage": 17.7
                },
                {
                        "category": "VIP Customers",
                        "value": 5.53,
                        "percentage": 8.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.08,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 27.64,
                        "percentage": 42.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.626130",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Downgrade Rate"
        }
    },
}
