"""
Revenue Retention Rate

The amount of revenue retained from existing customers over a given period, often excluding upsell and cross-sell revenues.
"""

REVENUE_RETENTION_RATE = {
    "code": "REVENUE_RETENTION_RATE",
    "name": "Revenue Retention Rate",
    "description": "The amount of revenue retained from existing customers over a given period, often excluding upsell and cross-sell revenues.",
    "formula": "((Starting Revenue - Revenue from Churned Customers) / Starting Revenue) * 100",
    "calculation_formula": "((Starting Revenue - Revenue from Churned Customers) / Starting Revenue) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Revenue Retention Rate to be added.",
    "trend_analysis": """


    * An increasing revenue retention rate may indicate successful customer loyalty programs or improved customer satisfaction.
    * A decreasing rate could signal increased competition, declining product quality, or poor customer service.
    
    
    """,
    "diagnostic_questions": """


    * What factors have contributed to the changes in our revenue retention rate?
    * Are there specific customer segments or product lines that are experiencing lower retention?
    
    
    """,
    "actionable_tips": """


    * Enhance customer support and after-sales services to improve overall customer experience.
    * Implement targeted marketing campaigns to re-engage existing customers and encourage repeat purchases.
    * Regularly gather feedback from customers to identify areas for improvement and address any concerns promptly.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of revenue retention rate over time.
    * Pie charts to visualize the distribution of retained revenue by customer segments or product categories.
    
    
    """,
    "risk_warnings": """


    * A declining revenue retention rate may lead to reduced overall revenue and market share.
    * High retention rates without corresponding revenue growth could indicate a lack of focus on acquiring new customers.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track customer interactions and identify opportunities for retention.
    * Data analytics tools to analyze customer behavior and preferences for targeted retention strategies.
    
    
    """,
    "integration_points": """


    * Integrate revenue retention rate analysis with sales and marketing systems to align efforts towards customer retention.
    * Link retention rate data with financial systems to understand the impact on overall revenue and profitability.
    
    
    """,
    "change_impact_analysis": """


    * Improving revenue retention can lead to increased customer lifetime value and overall business sustainability.
    * However, focusing solely on retention may lead to missed opportunities for growth through new customer acquisition.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale", "Subscription"], "last_validated": "2025-11-10T13:49:33.366721"},
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
                        71.34,
                        86.91,
                        76.48,
                        86.19,
                        72.12,
                        71.74,
                        87.54,
                        85.77,
                        78.74,
                        81.09,
                        69.38,
                        69.55
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.55,
                "unit": "%",
                "change": 0.17,
                "change_percent": 0.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 78.07,
                "min": 69.38,
                "max": 87.54,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.85,
                        "percentage": 28.5
                },
                {
                        "category": "Category B",
                        "value": 11.94,
                        "percentage": 17.2
                },
                {
                        "category": "Category C",
                        "value": 8.37,
                        "percentage": 12.0
                },
                {
                        "category": "Category D",
                        "value": 6.42,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 22.97,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.127994",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Revenue Retention Rate"
        }
    },
}
