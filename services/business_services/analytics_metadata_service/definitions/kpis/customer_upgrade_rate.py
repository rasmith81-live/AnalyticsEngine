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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.894322"},
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
                        64.27,
                        53.18,
                        62.75,
                        52.08,
                        62.39,
                        58.33,
                        56.0,
                        52.86,
                        63.33,
                        62.9,
                        58.14,
                        65.65
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.65,
                "unit": "%",
                "change": 7.51,
                "change_percent": 12.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 59.32,
                "min": 52.08,
                "max": 65.65,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 20.99,
                        "percentage": 32.0
                },
                {
                        "category": "Existing Customers",
                        "value": 9.53,
                        "percentage": 14.5
                },
                {
                        "category": "VIP Customers",
                        "value": 8.05,
                        "percentage": 12.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.69,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 21.39,
                        "percentage": 32.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.850641",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Upgrade Rate"
        }
    },
}
