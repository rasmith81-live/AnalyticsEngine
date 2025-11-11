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
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Expansion Opportunity", "Revenue Forecast", "Sale", "Subscription"], "last_validated": "2025-11-10T13:49:33.070271"},
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
                        44.6,
                        50.09,
                        52.94,
                        57.79,
                        61.42,
                        51.19,
                        48.96,
                        61.25,
                        61.48,
                        58.34,
                        59.81,
                        45.06
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.06,
                "unit": "%",
                "change": -14.75,
                "change_percent": -24.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 54.41,
                "min": 44.6,
                "max": 61.48,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 14.15,
                        "percentage": 31.4
                },
                {
                        "category": "Channel Sales",
                        "value": 7.43,
                        "percentage": 16.5
                },
                {
                        "category": "Online Sales",
                        "value": 7.7,
                        "percentage": 17.1
                },
                {
                        "category": "Enterprise Sales",
                        "value": 1.97,
                        "percentage": 4.4
                },
                {
                        "category": "Other",
                        "value": 13.81,
                        "percentage": 30.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.232444",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Net Revenue Retention (NRR)"
        }
    },
}
