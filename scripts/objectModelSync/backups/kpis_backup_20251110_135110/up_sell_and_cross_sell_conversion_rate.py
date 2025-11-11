"""
Up-sell and Cross-sell Conversion Rate

The success rate of sales strategies aimed at selling additional or complementary products to existing customers.
"""

UP_SELL_AND_CROSS_SELL_CONVERSION_RATE = {
    "code": "UP_SELL_AND_CROSS_SELL_CONVERSION_RATE",
    "name": "Up-sell and Cross-sell Conversion Rate",
    "description": "The success rate of sales strategies aimed at selling additional or complementary products to existing customers.",
    "formula": "(Number of Successful Up-sell/Cross-sell Deals / Total Number of Opportunities) * 100",
    "calculation_formula": "(Number of Successful Up-sell/Cross-sell Deals / Total Number of Opportunities) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Up-sell and Cross-sell Conversion Rate to be added.",
    "trend_analysis": """


    * An increasing up-sell and cross-sell conversion rate may indicate successful sales strategies or a growing understanding of customer needs.
    * A decreasing rate could signal ineffective sales approaches, lack of product knowledge among sales teams, or changing customer preferences.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific products or services that have higher conversion rates for up-sell and cross-sell opportunities?
    * How does our conversion rate compare with industry benchmarks or with historical data?
    
    
    """,
    "actionable_tips": """


    * Provide regular training and product knowledge sessions for sales teams to better understand the full range of offerings.
    * Implement targeted marketing campaigns to educate existing customers about complementary products or services.
    * Offer incentives or rewards for sales representatives who successfully execute up-sell and cross-sell strategies.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of conversion rates over time.
    * Pie charts to visualize the distribution of up-sell and cross-sell opportunities across different product categories.
    
    
    """,
    "risk_warnings": """


    * A low conversion rate may lead to missed revenue opportunities and underutilization of the existing customer base.
    * Pushing too aggressively for up-sell and cross-sell opportunities could result in customer dissatisfaction and potential churn.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) systems with built-in analytics to track customer behavior and preferences.
    * Sales enablement platforms that provide insights into customer interactions and buying patterns.
    
    
    """,
    "integration_points": """


    * Integrate up-sell and cross-sell data with customer relationship management systems to create personalized recommendations for each customer.
    * Link sales performance data with inventory management systems to ensure the availability of complementary products.
    
    
    """,
    "change_impact_analysis": """


    * Improving up-sell and cross-sell conversion rates can lead to increased revenue and customer lifetime value.
    * However, overly aggressive tactics may impact customer satisfaction and long-term loyalty.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Success Manager", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.761190"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        62.96,
                        64.66,
                        57.05,
                        73.51,
                        60.24,
                        73.17,
                        57.69,
                        62.47,
                        64.11,
                        62.26,
                        63.69,
                        63.08
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.08,
                "unit": "%",
                "change": -0.61,
                "change_percent": -1.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.74,
                "min": 57.05,
                "max": 73.51,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.83,
                        "percentage": 15.6
                },
                {
                        "category": "Category B",
                        "value": 8.25,
                        "percentage": 13.1
                },
                {
                        "category": "Category C",
                        "value": 14.88,
                        "percentage": 23.6
                },
                {
                        "category": "Category D",
                        "value": 4.52,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 25.6,
                        "percentage": 40.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.163181",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Up-sell and Cross-sell Conversion Rate"
        }
    },
}
