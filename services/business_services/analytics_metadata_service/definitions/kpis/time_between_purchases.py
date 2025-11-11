"""
Time Between Purchases

The average time interval between purchases made by a repeat customer.
"""

TIME_BETWEEN_PURCHASES = {
    "code": "TIME_BETWEEN_PURCHASES",
    "name": "Time Between Purchases",
    "description": "The average time interval between purchases made by a repeat customer.",
    "formula": "Average Time Span Between Customer Purchases",
    "calculation_formula": "Average Time Span Between Customer Purchases",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time Between Purchases to be added.",
    "trend_analysis": """



    * Shortening time between purchases may indicate improved customer satisfaction and loyalty.
    * An increasing time interval could signal declining interest in products or services.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that are driving longer intervals between purchases?
    * How does our time between purchases compare with industry averages or benchmarks?
    
    
    
    """,
    "actionable_tips": """



    * Enhance customer engagement and communication to maintain interest and encourage repeat purchases.
    * Offer loyalty programs or incentives to incentivize more frequent purchases.
    * Regularly analyze customer feedback and adjust product or service offerings to meet changing needs and preferences.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average time between purchases over time.
    * Cohort analysis to compare the purchasing behavior of different customer segments.
    
    
    
    """,
    "risk_warnings": """



    * Longer time between purchases may lead to decreased customer lifetime value and revenue.
    * It could indicate a need to reevaluate the product or service offering to maintain relevance in the market.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze customer behavior and preferences.
    * Data analytics tools to identify patterns and trends in customer purchasing behavior.
    
    
    
    """,
    "integration_points": """



    * Integrate with marketing automation platforms to personalize and target communications based on customer purchasing patterns.
    * Link with inventory management systems to ensure product availability and timely delivery for repeat purchases.
    
    
    
    """,
    "change_impact_analysis": """



    * Shortening the time between purchases can increase revenue and customer lifetime value.
    * However, it may also require increased marketing and operational costs to maintain customer engagement.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Representative"], "last_validated": "2025-11-10T13:49:33.705649"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "SALES_OPERATIONS"],
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
                        11.3,
                        9.5,
                        8.0,
                        8.3,
                        9.0,
                        9.7,
                        8.1,
                        6.2,
                        10.4,
                        5.8,
                        10.4,
                        8.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 8.1,
                "unit": "days",
                "change": -2.3,
                "change_percent": -22.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 8.73,
                "min": 5.8,
                "max": 11.3,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 2.13,
                        "percentage": 26.3
                },
                {
                        "category": "Existing Customers",
                        "value": 1.24,
                        "percentage": 15.3
                },
                {
                        "category": "VIP Customers",
                        "value": 1.48,
                        "percentage": 18.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 0.72,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 2.53,
                        "percentage": 31.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.742248",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time Between Purchases"
        }
    },
}
