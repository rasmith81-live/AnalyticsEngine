"""
Contract Utilization Rate

The percentage of contracted services or products that customers actually use.
"""

CONTRACT_UTILIZATION_RATE = {
    "code": "CONTRACT_UTILIZATION_RATE",
    "name": "Contract Utilization Rate",
    "description": "The percentage of contracted services or products that customers actually use.",
    "formula": "(Value of Services or Products Utilized / Total Contract Value) * 100",
    "calculation_formula": "(Value of Services or Products Utilized / Total Contract Value) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Contract Utilization Rate to be added.",
    "trend_analysis": """



    * An increasing contract utilization rate may indicate that customers are finding more value in the products or services, leading to higher usage.
    * A decreasing rate could signal dissatisfaction with the offerings, changes in customer needs, or ineffective communication about the benefits of the contracted items.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that have a consistently low utilization rate?
    * How does our contract utilization rate compare with industry benchmarks or with historical data?
    
    
    
    """,
    "actionable_tips": """



    * Regularly communicate the value and benefits of the contracted items to customers to encourage usage.
    * Offer training or support to customers to help them maximize the benefits of the products or services they have contracted.
    * Regularly review and update the offerings to ensure they align with customer needs and expectations.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend in contract utilization rates over time.
    * Pie charts to compare the utilization rates of different products or services.
    
    
    
    """,
    "risk_warnings": """



    * Low contract utilization rates may lead to customer churn and lost revenue.
    * High utilization rates without corresponding customer satisfaction may indicate that the offerings are not meeting customer needs effectively.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track customer interactions and feedback related to the contracted items.
    * Data analytics tools to identify patterns and trends in customer usage data.
    
    
    
    """,
    "integration_points": """



    * Integrate contract utilization data with customer feedback and satisfaction metrics to gain a comprehensive understanding of customer perceptions.
    * Link utilization rates with sales and marketing data to align messaging and promotions with customer needs and usage patterns.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving contract utilization rates can lead to increased customer satisfaction and loyalty, potentially impacting long-term revenue and profitability.
    * However, changes in offerings or communication strategies to improve utilization rates may require investment and could impact short-term profitability.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product"], "last_validated": "2025-11-10T13:49:32.717369"},
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
                        64.95,
                        58.77,
                        60.79,
                        66.47,
                        76.19,
                        67.85,
                        58.52,
                        61.32,
                        65.88,
                        66.7,
                        57.73,
                        57.66
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.66,
                "unit": "%",
                "change": -0.07,
                "change_percent": -0.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.57,
                "min": 57.66,
                "max": 76.19,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 13.13,
                        "percentage": 22.8
                },
                {
                        "category": "Product Line B",
                        "value": 12.21,
                        "percentage": 21.2
                },
                {
                        "category": "Product Line C",
                        "value": 5.86,
                        "percentage": 10.2
                },
                {
                        "category": "Services",
                        "value": 6.79,
                        "percentage": 11.8
                },
                {
                        "category": "Other",
                        "value": 19.67,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.513267",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Contract Utilization Rate"
        }
    },
}
