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
                        252,
                        244,
                        273,
                        260,
                        258,
                        273,
                        242,
                        248,
                        247,
                        263,
                        238,
                        234
                ],
                "unit": "count"
        },
        "current": {
                "value": 234,
                "unit": "count",
                "change": -4,
                "change_percent": -1.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 252.67,
                "min": 234,
                "max": 273,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 57.89,
                        "percentage": 24.7
                },
                {
                        "category": "Category B",
                        "value": 44.36,
                        "percentage": 19.0
                },
                {
                        "category": "Category C",
                        "value": 23.51,
                        "percentage": 10.0
                },
                {
                        "category": "Category D",
                        "value": 28.54,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 79.7,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.036045",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Revenue Per User (ARPU)"
        }
    },
}
