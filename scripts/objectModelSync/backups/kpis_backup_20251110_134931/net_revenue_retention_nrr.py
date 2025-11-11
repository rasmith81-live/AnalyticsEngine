"""
Net Revenue Retention (NRR)

The percentage of revenue retained from existing customers after accounting for churned and downgraded customers.
"""

NET_REVENUE_RETENTION_NRR = {
    "code": "NET_REVENUE_RETENTION_NRR",
    "name": "Net Revenue Retention (NRR)",
    "description": "The percentage of revenue retained from existing customers after accounting for churned and downgraded customers.",
    "formula": "((Starting MRR + Expansion Revenue - Churned Revenue) / Starting MRR) * 100",
    "calculation_formula": "((Starting MRR + Expansion Revenue - Churned Revenue) / Starting MRR) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Net Revenue Retention (NRR) to be added.",
    "trend_analysis": """

    * An increasing NRR may indicate successful upselling or cross-selling efforts with existing customers.
    * A decreasing NRR could signal increased competition or dissatisfaction among the customer base.
    
    """,
    "diagnostic_questions": """

    * Are there specific customer segments or product lines that are driving the changes in NRR?
    * How does our NRR compare with industry benchmarks or with our historical performance?
    
    """,
    "actionable_tips": """

    * Focus on delivering exceptional customer service to retain existing customers.
    * Regularly review and update pricing strategies to ensure they align with customer value perceptions.
    * Implement customer loyalty programs to incentivize repeat purchases and increase retention.
    
    """,
    "visualization_suggestions": """

    * Line charts showing NRR trends over time.
    * Stacked bar graphs comparing NRR by customer segment or product category.
    
    """,
    "risk_warnings": """

    * A declining NRR may lead to reduced overall revenue and profitability.
    * High NRR without corresponding customer acquisition efforts may indicate limited growth potential.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track customer interactions and identify retention opportunities.
    * Business intelligence tools for in-depth analysis of customer behavior and preferences.
    
    """,
    "integration_points": """

    * Integrate NRR tracking with sales and marketing systems to align retention efforts with customer acquisition strategies.
    * Link NRR data with customer feedback and satisfaction surveys to gain a comprehensive view of customer sentiment.
    
    """,
    "change_impact_analysis": """

    * Improving NRR can lead to increased customer lifetime value and overall business sustainability.
    * However, aggressive retention strategies may impact short-term profitability if not balanced with acquisition efforts.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Expansion Opportunity", "Revenue Forecast", "Sale", "Subscription"], "last_validated": "2025-11-10T13:43:23.676227"},
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
                        89479.95,
                        80758.42,
                        83356.84,
                        86489.02,
                        88572.89,
                        87713.53,
                        83192.79,
                        82797.05,
                        93789.12,
                        92234.04,
                        80488.97,
                        93360.67
                ],
                "unit": "$"
        },
        "current": {
                "value": 93360.67,
                "unit": "$",
                "change": 12871.7,
                "change_percent": 16.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 86852.77,
                "min": 80488.97,
                "max": 93789.12,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 21944.07,
                        "percentage": 23.5
                },
                {
                        "category": "Category B",
                        "value": 21990.08,
                        "percentage": 23.6
                },
                {
                        "category": "Category C",
                        "value": 8261.15,
                        "percentage": 8.8
                },
                {
                        "category": "Category D",
                        "value": 12190.43,
                        "percentage": 13.1
                },
                {
                        "category": "Other",
                        "value": 28974.94,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.676227",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Net Revenue Retention (NRR)"
        }
    },
}
