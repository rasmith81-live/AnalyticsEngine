"""
Average Revenue Per User (ARPU)

The average revenue generated from each active customer or user.
"""

AVERAGE_REVENUE_PER_USER_ARPU = {
    "code": "AVERAGE_REVENUE_PER_USER_ARPU",
    "name": "Average Revenue Per User (ARPU)",
    "description": "The average revenue generated from each active customer or user.",
    "formula": "Total Revenue / Total Number of Users",
    "calculation_formula": "Total Revenue / Total Number of Users",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Revenue Per User (ARPU) to be added.",
    "trend_analysis": """



    * ARPU tends to increase as customers become more engaged with the product or service, indicating positive performance.
    * A declining ARPU may signal increased competition, customer dissatisfaction, or a shift in customer behavior.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors contribute to fluctuations in ARPU, such as pricing changes, product offerings, or customer segmentation?
    * How does ARPU vary across different customer segments, and what can be done to increase it for underperforming segments?
    
    
    
    """,
    "actionable_tips": """



    * Implement targeted upselling and cross-selling strategies to increase the average spend per customer.
    * Enhance the value proposition of the product or service to justify higher pricing and increase ARPU.
    * Focus on customer retention and loyalty programs to increase the lifetime value of each customer.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing ARPU trends over time to identify seasonal or cyclical patterns.
    * Comparison bar charts to visualize ARPU differences between customer segments or product categories.
    
    
    
    """,
    "risk_warnings": """



    * A declining ARPU can lead to reduced revenue and profitability if not addressed promptly.
    * High ARPU may indicate a reliance on a small number of high-value customers, posing a risk if they churn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify upsell opportunities.
    * Business intelligence tools for analyzing customer data and identifying opportunities to increase ARPU.
    
    
    
    """,
    "integration_points": """



    * Integrate ARPU data with marketing automation platforms to personalize offers and promotions based on customer spending habits.
    * Link ARPU with customer support systems to identify opportunities for upselling or cross-selling during customer interactions.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing ARPU may lead to higher revenue and profitability, but could also result in customer pushback if not managed carefully.
    * Decreasing ARPU may indicate a need for cost-cutting measures, but could also signal a decline in customer satisfaction and loyalty.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.655984"},
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
                        135,
                        95,
                        127,
                        93,
                        104,
                        95,
                        122,
                        132,
                        96,
                        99,
                        130,
                        93
                ],
                "unit": "count"
        },
        "current": {
                "value": 93,
                "unit": "count",
                "change": -37,
                "change_percent": -28.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 110.08,
                "min": 93,
                "max": 135,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 24.88,
                        "percentage": 26.8
                },
                {
                        "category": "Channel Sales",
                        "value": 16.31,
                        "percentage": 17.5
                },
                {
                        "category": "Online Sales",
                        "value": 10.82,
                        "percentage": 11.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 6.04,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 34.95,
                        "percentage": 37.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.381738",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Revenue Per User (ARPU)"
        }
    },
}
