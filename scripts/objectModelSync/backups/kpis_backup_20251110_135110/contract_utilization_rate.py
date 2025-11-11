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
                        69.49,
                        71.64,
                        61.95,
                        64.69,
                        59.83,
                        61.82,
                        62.95,
                        54.38,
                        63.46,
                        58.79,
                        69.1,
                        57.9
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.9,
                "unit": "%",
                "change": -11.2,
                "change_percent": -16.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 63.0,
                "min": 54.38,
                "max": 71.64,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.98,
                        "percentage": 32.8
                },
                {
                        "category": "Category B",
                        "value": 8.74,
                        "percentage": 15.1
                },
                {
                        "category": "Category C",
                        "value": 5.56,
                        "percentage": 9.6
                },
                {
                        "category": "Category D",
                        "value": 4.92,
                        "percentage": 8.5
                },
                {
                        "category": "Other",
                        "value": 19.7,
                        "percentage": 34.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.147254",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Contract Utilization Rate"
        }
    },
}
