"""
Customer Account Growth Rate

The rate at which customer accounts grow in terms of usage or added features over time.
"""

CUSTOMER_ACCOUNT_GROWTH_RATE = {
    "code": "CUSTOMER_ACCOUNT_GROWTH_RATE",
    "name": "Customer Account Growth Rate",
    "description": "The rate at which customer accounts grow in terms of usage or added features over time.",
    "formula": "(Total Revenue at the End of the Period - Total Revenue at the Start of the Period) / Total Revenue at the Start of the Period",
    "calculation_formula": "(Total Revenue at the End of the Period - Total Revenue at the Start of the Period) / Total Revenue at the Start of the Period",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Account Growth Rate to be added.",
    "trend_analysis": """



    * Increasing customer account growth rate may indicate higher customer satisfaction and loyalty.
    * A decreasing growth rate could signal a need for better customer engagement or a decline in the perceived value of the product or service.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific features or services that customers frequently request or inquire about?
    * How does our customer account growth rate compare with industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Regularly engage with customers to understand their evolving needs and preferences.
    * Offer incentives for customers to upgrade to higher-tiered plans or packages.
    * Provide personalized recommendations for additional features or services based on customer usage patterns.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the growth rate over time for individual customer accounts.
    * Stacked bar graphs comparing the growth rates of different customer segments or product categories.
    
    
    
    """,
    "risk_warnings": """



    * A stagnant or declining growth rate may lead to customer churn and reduced revenue.
    * Rapid growth without proper support or resources may strain customer service and operational capabilities.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify opportunities for growth.
    * Usage analytics tools to understand how customers are engaging with the product or service.
    
    
    
    """,
    "integration_points": """



    * Integrate customer account growth rate data with sales and marketing systems to align efforts towards customer expansion.
    * Link growth rate metrics with product development and innovation processes to prioritize features that drive customer adoption and retention.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the customer account growth rate can lead to increased lifetime value of customers and higher overall revenue.
    * Conversely, a declining growth rate may necessitate a reevaluation of the product or service offering and customer engagement strategies.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Product Usage", "Revenue Forecast", "Sale"], "last_validated": "2025-11-10T13:49:32.791613"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
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
                        46.41,
                        44.38,
                        55.07,
                        59.15,
                        43.0,
                        56.36,
                        45.52,
                        48.3,
                        58.74,
                        43.3,
                        44.49,
                        45.03
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.03,
                "unit": "%",
                "change": 0.54,
                "change_percent": 1.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 49.15,
                "min": 43.0,
                "max": 59.15,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 10.33,
                        "percentage": 22.9
                },
                {
                        "category": "Mid-Market",
                        "value": 11.8,
                        "percentage": 26.2
                },
                {
                        "category": "Small Business",
                        "value": 5.75,
                        "percentage": 12.8
                },
                {
                        "category": "Strategic Partners",
                        "value": 3.73,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 13.42,
                        "percentage": 29.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.584022",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Account Growth Rate"
        }
    },
}
