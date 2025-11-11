"""
Customer Churn Cost

The cost incurred by the company when a customer ceases to do business or discontinues the subscription.
"""

CUSTOMER_CHURN_COST = {
    "code": "CUSTOMER_CHURN_COST",
    "name": "Customer Churn Cost",
    "description": "The cost incurred by the company when a customer ceases to do business or discontinues the subscription.",
    "formula": "Sum of Lost Revenue and Additional Costs Due to Customer Churn",
    "calculation_formula": "Sum of Lost Revenue and Additional Costs Due to Customer Churn",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Churn Cost to be added.",
    "trend_analysis": """



    * An increasing customer churn cost may indicate issues with customer satisfaction, product quality, or customer service.
    * A decreasing cost could signal improved customer retention strategies, better product offerings, or enhanced customer support.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common reasons cited by customers for discontinuing their subscription or ceasing business with us?
    * How does our customer churn cost compare with industry benchmarks or with our competitors?
    
    
    
    """,
    "actionable_tips": """



    * Implement customer feedback mechanisms to understand the reasons behind customer churn and address them proactively.
    * Invest in customer success and support teams to ensure a positive customer experience throughout their journey.
    * Offer incentives or loyalty programs to encourage customer retention and reduce churn.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of customer churn cost over time.
    * Pareto charts to identify the most common reasons for customer churn.
    
    
    
    """,
    "risk_warnings": """



    * High customer churn cost can lead to revenue loss and impact the company's bottom line.
    * Consistently increasing churn cost may indicate systemic issues that need to be addressed to prevent further losses.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify potential churn risks.
    * Survey and feedback tools to gather insights from customers about their experience and reasons for churn.
    
    
    
    """,
    "integration_points": """



    * Integrate customer churn cost data with sales and marketing systems to identify patterns and potential causes of churn.
    * Link churn cost with customer lifetime value calculations to understand the impact of churn on overall customer value.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing customer churn cost can lead to increased customer lifetime value and overall revenue growth.
    * However, focusing solely on reducing churn cost may lead to neglecting other important aspects of customer satisfaction and retention.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Churn Event", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lost Sale", "Quarterly Business Review", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Subscription"], "last_validated": "2025-11-10T13:49:32.803902"},
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
                        94706.42,
                        91059.74,
                        93231.67,
                        89406.72,
                        95761.73,
                        100224.46,
                        89995.64,
                        102564.71,
                        96562.0,
                        90377.91,
                        93828.12,
                        101131.44
                ],
                "unit": "$"
        },
        "current": {
                "value": 101131.44,
                "unit": "$",
                "change": 7303.32,
                "change_percent": 7.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 94904.21,
                "min": 89406.72,
                "max": 102564.71,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 33381.08,
                        "percentage": 33.0
                },
                {
                        "category": "Existing Customers",
                        "value": 11560.04,
                        "percentage": 11.4
                },
                {
                        "category": "VIP Customers",
                        "value": 8734.99,
                        "percentage": 8.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4845.33,
                        "percentage": 4.8
                },
                {
                        "category": "Other",
                        "value": 42610.0,
                        "percentage": 42.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.603097",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Customer Churn Cost"
        }
    },
}
