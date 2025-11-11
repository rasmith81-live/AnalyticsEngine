"""
Average Revenue Per Account (ARPA)

The average revenue generated per account over a given time period, typically monthly or annually.
"""

AVERAGE_REVENUE_PER_ACCOUNT_ARPA = {
    "code": "AVERAGE_REVENUE_PER_ACCOUNT_ARPA",
    "name": "Average Revenue Per Account (ARPA)",
    "description": "The average revenue generated per account over a given time period, typically monthly or annually.",
    "formula": "Total Revenue / Total Number of Accounts",
    "calculation_formula": "Total Revenue / Total Number of Accounts",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Revenue Per Account (ARPA) to be added.",
    "trend_analysis": """


    * ARPA tends to increase over time as customer accounts grow and more revenue is generated.
    * A sudden decrease in ARPA could indicate customer churn or a shift towards lower-value accounts.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific customer segments or industries that contribute more to ARPA?
    * How does our ARPA compare with industry benchmarks or changes in our product/service offerings?
    
    
    """,
    "actionable_tips": """


    * Upsell and cross-sell strategies to increase revenue from existing accounts.
    * Target higher-value customer segments and tailor offerings to maximize revenue potential.
    * Implement pricing strategies to capture more value from each account without sacrificing customer satisfaction.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing ARPA trends over time.
    * Pie charts to visualize the distribution of revenue across different customer segments.
    
    
    """,
    "risk_warnings": """


    * Average Revenue Per Account may not reflect profitability if acquisition or servicing costs are high.
    * Over-reliance on a few high-value accounts can pose a risk if they are lost or reduce spending.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) systems to track account revenue and interactions.
    * Business Intelligence (BI) tools for analyzing customer data and identifying opportunities for revenue growth.
    
    
    """,
    "integration_points": """


    * Integrate ARPA tracking with sales and marketing systems to align efforts towards higher-value accounts.
    * Link ARPA with customer support systems to ensure consistent service for high-value accounts.
    
    
    """,
    "change_impact_analysis": """


    * Increasing ARPA may lead to higher overall revenue but could also strain resources if not managed effectively.
    * Decreasing ARPA may indicate a need to reevaluate customer targeting and product/service offerings to maintain overall revenue levels.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.653858"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"],
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
                        467,
                        478,
                        474,
                        462,
                        498,
                        496,
                        493,
                        463,
                        486,
                        465,
                        454,
                        472
                ],
                "unit": "count"
        },
        "current": {
                "value": 472,
                "unit": "count",
                "change": 18,
                "change_percent": 4.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 475.67,
                "min": 454,
                "max": 498,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 137.23,
                        "percentage": 29.1
                },
                {
                        "category": "Category B",
                        "value": 101.55,
                        "percentage": 21.5
                },
                {
                        "category": "Category C",
                        "value": 68.64,
                        "percentage": 14.5
                },
                {
                        "category": "Category D",
                        "value": 31.96,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 132.62,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.031835",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Revenue Per Account (ARPA)"
        }
    },
}
