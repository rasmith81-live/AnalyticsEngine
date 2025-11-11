"""
Deal Cancellation Rate

The percentage of deals that are canceled after being initiated.
"""

DEAL_CANCELLATION_RATE = {
    "code": "DEAL_CANCELLATION_RATE",
    "name": "Deal Cancellation Rate",
    "description": "The percentage of deals that are canceled after being initiated.",
    "formula": "(Number of Deals Canceled / Total Number of Deals Initially Confirmed) * 100",
    "calculation_formula": "(Number of Deals Canceled / Total Number of Deals Initially Confirmed) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Cancellation Rate to be added.",
    "trend_analysis": """



    * An increasing deal cancellation rate may indicate issues with the sales process, product quality, or customer satisfaction.
    * A decreasing rate could signal improved sales strategies, better product offerings, or enhanced customer service.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common reasons why deals are being canceled, such as pricing, product fit, or customer expectations?
    * How does our deal cancellation rate compare with industry benchmarks or with specific sales teams or regions?
    
    
    
    """,
    "actionable_tips": """



    * Implement thorough qualification processes to ensure that potential deals are a good fit for the company and the customer.
    * Provide additional sales training and resources to address common reasons for deal cancellations.
    * Regularly review and update sales strategies and product offerings to better meet customer needs and expectations.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend in deal cancellation rates over time.
    * Pie charts to compare reasons for deal cancellations, such as pricing, product fit, or customer dissatisfaction.
    
    
    
    """,
    "risk_warnings": """



    * High deal cancellation rates can lead to lost revenue and impact sales team morale.
    * Consistently high cancellation rates may indicate deeper issues with product-market fit or sales processes.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and analyze deal cancellation reasons and trends.
    * Sales performance management software to identify areas for improvement and track the impact of sales strategies on deal cancellations.
    
    
    
    """,
    "integration_points": """



    * Integrate deal cancellation data with customer feedback systems to understand the reasons behind cancellations and improve customer satisfaction.
    * Link deal cancellation rates with sales forecasting and inventory management systems to adjust production and inventory levels accordingly.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing deal cancellation rates can lead to increased revenue and improved customer retention.
    * However, changes in sales strategies or product offerings to reduce cancellations may require additional resources and investment.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.908347"},
    "required_objects": [],
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
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
                        43.09,
                        55.2,
                        59.76,
                        47.54,
                        49.13,
                        58.35,
                        47.48,
                        42.28,
                        52.05,
                        42.81,
                        43.16,
                        48.66
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.66,
                "unit": "%",
                "change": 5.5,
                "change_percent": 12.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 49.13,
                "min": 42.28,
                "max": 59.76,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 9.1,
                        "percentage": 18.7
                },
                {
                        "category": "Segment B",
                        "value": 10.67,
                        "percentage": 21.9
                },
                {
                        "category": "Segment C",
                        "value": 9.06,
                        "percentage": 18.6
                },
                {
                        "category": "Segment D",
                        "value": 4.93,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 14.9,
                        "percentage": 30.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.873824",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Deal Cancellation Rate"
        }
    },
}
