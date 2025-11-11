"""
Customer Concentration Risk

The level of risk associated with dependency on a limited number of customers for a significant percentage of revenue.
"""

CUSTOMER_CONCENTRATION_RISK = {
    "code": "CUSTOMER_CONCENTRATION_RISK",
    "name": "Customer Concentration Risk",
    "description": "The level of risk associated with dependency on a limited number of customers for a significant percentage of revenue.",
    "formula": "Revenue from Top X Customers / Total Revenue",
    "calculation_formula": "Revenue from Top X Customers / Total Revenue",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Concentration Risk to be added.",
    "trend_analysis": """



    * An increasing customer concentration risk may indicate a growing dependency on a small number of clients, which could lead to vulnerability if any of them are lost.
    * A decreasing risk may signal successful efforts to diversify the customer base and reduce reliance on a few key clients.
    
    
    
    """,
    "diagnostic_questions": """



    * What percentage of our revenue comes from our top 5 customers?
    * Are there any specific industries or regions that our major customers belong to, and how does this impact our risk?
    
    
    
    """,
    "actionable_tips": """



    * Diversify the customer base by targeting new industries or regions.
    * Implement strategies to increase customer retention and loyalty across all customer segments.
    * Develop contingency plans for potential loss of major customers to mitigate the impact on revenue.
    
    
    
    """,
    "visualization_suggestions": """



    * Pie charts showing the revenue contribution from different customer segments.
    * Line graphs depicting the trend of revenue concentration over time.
    
    
    
    """,
    "risk_warnings": """



    * High customer concentration risk can make the business vulnerable to economic downturns or industry-specific challenges.
    * Loss of a major customer can have a significant negative impact on revenue and profitability.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze customer revenue contributions.
    * Data analytics tools to identify trends and patterns in customer revenue concentration.
    
    
    
    """,
    "integration_points": """



    * Integrate customer concentration risk analysis with sales forecasting to anticipate potential revenue impacts.
    * Link customer concentration risk with customer satisfaction metrics to understand the relationship between customer dependency and loyalty.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing customer concentration risk may require investment in sales and marketing efforts to target new customer segments.
    * Increased customer diversification can lead to improved revenue stability and reduced vulnerability to customer-specific challenges.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.810287"},
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
                        59.33,
                        47.57,
                        55.46,
                        59.42,
                        53.83,
                        62.27,
                        43.4,
                        56.19,
                        45.77,
                        56.63,
                        51.05,
                        55.48
                ],
                "unit": "%"
        },
        "current": {
                "value": 55.48,
                "unit": "%",
                "change": 4.43,
                "change_percent": 8.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 53.87,
                "min": 43.4,
                "max": 62.27,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 10.74,
                        "percentage": 19.4
                },
                {
                        "category": "Existing Customers",
                        "value": 6.93,
                        "percentage": 12.5
                },
                {
                        "category": "VIP Customers",
                        "value": 9.59,
                        "percentage": 17.3
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.74,
                        "percentage": 6.7
                },
                {
                        "category": "Other",
                        "value": 24.48,
                        "percentage": 44.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.620120",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Concentration Risk"
        }
    },
}
