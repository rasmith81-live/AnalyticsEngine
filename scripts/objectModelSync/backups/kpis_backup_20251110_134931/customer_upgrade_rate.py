"""
Customer Upgrade Rate

The percentage of customers that move to a higher-tier service or product offering.
"""

CUSTOMER_UPGRADE_RATE = {
    "code": "CUSTOMER_UPGRADE_RATE",
    "name": "Customer Upgrade Rate",
    "description": "The percentage of customers that move to a higher-tier service or product offering.",
    "formula": "(Number of Customers Upgraded / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Upgraded / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Upgrade Rate to be added.",
    "trend_analysis": """

    * An increasing customer upgrade rate may indicate successful upselling strategies or a growing demand for higher-tier offerings.
    * A decreasing rate could signal customer dissatisfaction with higher-tier products or a lack of effective upselling techniques.
    
    """,
    "diagnostic_questions": """

    * Are there specific customer segments or industries that are more likely to upgrade?
    * What are the main reasons customers give for upgrading, and are there any common objections that prevent them from doing so?
    
    """,
    "actionable_tips": """

    * Train sales teams to effectively communicate the value of higher-tier offerings and identify upselling opportunities.
    * Personalize upselling strategies based on customer behavior and preferences to increase the likelihood of upgrades.
    * Offer incentives or promotions to encourage customers to move to higher-tier products or services.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the customer upgrade rate over time to identify trends and seasonality.
    * Pie charts to visualize the distribution of upgrades across different product or service categories.
    
    """,
    "risk_warnings": """

    * A low upgrade rate may indicate a lack of customer satisfaction with higher-tier offerings, leading to potential churn.
    * Overemphasis on upselling may lead to customer fatigue and resistance, impacting overall customer experience.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track customer interactions and identify upselling opportunities.
    * Analytics tools to segment customers and understand their behavior to tailor upselling strategies.
    
    """,
    "integration_points": """

    * Integrate customer upgrade rate data with customer feedback and satisfaction metrics to understand the impact of upgrades on overall customer experience.
    * Link with sales performance metrics to evaluate the effectiveness of upselling techniques and strategies.
    
    """,
    "change_impact_analysis": """

    * An increase in the customer upgrade rate can positively impact revenue and customer lifetime value.
    * However, aggressive upselling tactics may negatively impact customer trust and brand reputation, affecting long-term customer relationships.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.386816"},
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
                        65.25,
                        82.39,
                        74.56,
                        75.69,
                        74.84,
                        81.6,
                        77.21,
                        73.68,
                        71.53,
                        70.0,
                        83.24,
                        69.74
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.74,
                "unit": "%",
                "change": -13.5,
                "change_percent": -16.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.98,
                "min": 65.25,
                "max": 83.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.4,
                        "percentage": 32.1
                },
                {
                        "category": "Category B",
                        "value": 7.7,
                        "percentage": 11.0
                },
                {
                        "category": "Category C",
                        "value": 8.01,
                        "percentage": 11.5
                },
                {
                        "category": "Category D",
                        "value": 9.1,
                        "percentage": 13.0
                },
                {
                        "category": "Other",
                        "value": 22.53,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.386816",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Upgrade Rate"
        }
    },
}
