"""
Customer Renewal Intent

The expressed intent of customers to renew their contracts or continue their subscription at the end of the current term.
"""

CUSTOMER_RENEWAL_INTENT = {
    "code": "CUSTOMER_RENEWAL_INTENT",
    "name": "Customer Renewal Intent",
    "description": "The expressed intent of customers to renew their contracts or continue their subscription at the end of the current term.",
    "formula": "(Number of Customers Indicating Positive Renewal Intent / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Indicating Positive Renewal Intent / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Renewal Intent to be added.",
    "trend_analysis": """



    * Increasing customer renewal intent may indicate higher satisfaction with the product or service.
    * Decreasing renewal intent could signal issues with product quality, customer support, or competitive pressures.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the main reasons customers cite for their intent to renew or not renew?
    * How does our customer renewal intent compare with industry benchmarks or with our historical data?
    
    
    
    """,
    "actionable_tips": """



    * Enhance customer support and engagement to address any concerns or issues that may be impacting renewal intent.
    * Regularly solicit feedback from customers to understand their needs and expectations, and make necessary adjustments.
    * Offer incentives or loyalty programs to encourage renewal and reward long-term customers.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of renewal intent over time.
    * Segmented bar charts comparing renewal intent across different customer segments or product categories.
    
    
    
    """,
    "risk_warnings": """



    * Low renewal intent may lead to revenue loss and indicate potential churn in the customer base.
    * High renewal intent without continuous improvement may lead to complacency and missed opportunities for growth.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and analyze customer interactions and feedback.
    * Survey and feedback tools to gather and analyze customer sentiment and satisfaction data.
    
    
    
    """,
    "integration_points": """



    * Integrate renewal intent data with sales and marketing systems to align efforts in retaining customers.
    * Link renewal intent with product development and improvement processes to address any recurring issues.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving renewal intent can lead to increased customer lifetime value and overall revenue growth.
    * Conversely, declining renewal intent may require additional resources to win back customers or acquire new ones.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Renewal Management", "Subscription"], "last_validated": "2025-11-10T13:49:32.866851"},
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
                        47.86,
                        60.79,
                        57.75,
                        59.44,
                        63.53,
                        49.38,
                        53.46,
                        59.07,
                        49.73,
                        58.88,
                        66.26,
                        48.56
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.56,
                "unit": "%",
                "change": -17.7,
                "change_percent": -26.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.23,
                "min": 47.86,
                "max": 66.26,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 9.08,
                        "percentage": 18.7
                },
                {
                        "category": "Existing Customers",
                        "value": 6.69,
                        "percentage": 13.8
                },
                {
                        "category": "VIP Customers",
                        "value": 5.68,
                        "percentage": 11.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.59,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 22.52,
                        "percentage": 46.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.769027",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Renewal Intent"
        }
    },
}
