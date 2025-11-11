"""
Expansion Revenue Rate

The rate at which existing customers increase spending through upsells or cross-sells.
"""

EXPANSION_REVENUE_RATE = {
    "code": "EXPANSION_REVENUE_RATE",
    "name": "Expansion Revenue Rate",
    "description": "The rate at which existing customers increase spending through upsells or cross-sells.",
    "formula": "(New Revenue from Existing Customers / Total Revenue from Existing Customers) * 100",
    "calculation_formula": "(New Revenue from Existing Customers / Total Revenue from Existing Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Expansion Revenue Rate to be added.",
    "trend_analysis": """



    * Expansion revenue rate tends to increase as customers become more familiar with the product or service and see the value in additional offerings.
    * A decreasing expansion revenue rate could indicate a lack of effective upselling or cross-selling strategies, or a disconnect between customer needs and available offerings.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments or industries that are more receptive to upsells or cross-sells?
    * How does our expansion revenue rate compare to industry benchmarks or to our own historical performance?
    
    
    
    """,
    "actionable_tips": """



    * Train sales teams to identify upsell and cross-sell opportunities during customer interactions.
    * Personalize upsell and cross-sell recommendations based on customer behavior and preferences.
    * Regularly review and update the product or service portfolio to ensure relevant and attractive offerings for existing customers.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of expansion revenue rate over time.
    * Pie charts illustrating the proportion of revenue coming from upsells versus cross-sells.
    
    
    
    """,
    "risk_warnings": """



    * A stagnant or declining expansion revenue rate may lead to missed revenue opportunities and reduced customer lifetime value.
    * Overly aggressive upselling or cross-selling tactics can result in customer dissatisfaction and potential churn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems with built-in upsell and cross-sell tracking capabilities.
    * Marketing automation platforms for targeted upsell and cross-sell campaigns.
    
    
    
    """,
    "integration_points": """



    * Integrate expansion revenue rate data with customer feedback and satisfaction scores to understand the impact of upselling and cross-selling on customer experience.
    * Link with inventory and supply chain systems to ensure the availability of products or services being upsold or cross-sold.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the expansion revenue rate can lead to increased customer lifetime value and overall revenue growth.
    * However, overly aggressive upselling or cross-selling can strain customer relationships and impact brand reputation.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Expansion Opportunity", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.950662"},
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
                        73.18,
                        64.57,
                        59.69,
                        68.22,
                        65.83,
                        71.04,
                        65.15,
                        66.91,
                        72.61,
                        62.66,
                        65.78,
                        72.97
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.97,
                "unit": "%",
                "change": 7.19,
                "change_percent": 10.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.38,
                "min": 59.69,
                "max": 73.18,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 12.99,
                        "percentage": 17.8
                },
                {
                        "category": "Existing Customers",
                        "value": 13.07,
                        "percentage": 17.9
                },
                {
                        "category": "VIP Customers",
                        "value": 13.36,
                        "percentage": 18.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 7.69,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 25.86,
                        "percentage": 35.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.980664",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Expansion Revenue Rate"
        }
    },
}
