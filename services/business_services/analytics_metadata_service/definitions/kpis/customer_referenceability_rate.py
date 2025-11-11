"""
Customer Referenceability Rate

The percentage of customers who agree to act as a reference or case study for the company's marketing efforts.
"""

CUSTOMER_REFERENCEABILITY_RATE = {
    "code": "CUSTOMER_REFERENCEABILITY_RATE",
    "name": "Customer Referenceability Rate",
    "description": "The percentage of customers who agree to act as a reference or case study for the company's marketing efforts.",
    "formula": "(Number of Customers Willing to be References / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Willing to be References / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Referenceability Rate to be added.",
    "trend_analysis": """



    * An increasing customer referenceability rate may indicate higher satisfaction and loyalty among customers.
    * A decreasing rate could signal dissatisfaction with the company's products or services.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the common reasons customers agree or refuse to act as references or case studies?
    * Are there specific customer segments or product lines with higher or lower referenceability rates?
    
    
    
    """,
    "actionable_tips": """



    * Provide exceptional customer service and support to increase the likelihood of customers agreeing to be references.
    * Regularly solicit feedback from customers to address any issues that may be affecting their willingness to act as references.
    * Offer incentives or rewards for customers who agree to participate in reference activities.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend in customer referenceability rates over time.
    * Pie charts to compare referenceability rates across different customer segments or product categories.
    
    
    
    """,
    "risk_warnings": """



    * A low customer referenceability rate may indicate a lack of advocacy and potential negative word-of-mouth in the market.
    * Over-reliance on a small number of customer references may lead to limited diversity in marketing materials.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and manage customer interactions and feedback.
    * Survey and feedback tools to gather insights into customer satisfaction and willingness to participate in reference activities.
    
    
    
    """,
    "integration_points": """



    * Integrate customer referenceability data with sales and marketing systems to identify opportunities for leveraging references in the sales process.
    * Link referenceability rates with customer satisfaction metrics to understand the correlation between satisfaction and willingness to act as a reference.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the customer referenceability rate can enhance the credibility and trustworthiness of the company's marketing efforts.
    * Conversely, a declining referenceability rate may impact the effectiveness of sales and marketing campaigns that rely on customer references.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager"], "last_validated": "2025-11-10T13:49:32.865122"},
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
                        60.06,
                        55.89,
                        59.17,
                        52.24,
                        56.95,
                        51.3,
                        66.41,
                        58.53,
                        50.41,
                        53.93,
                        60.0,
                        65.5
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.5,
                "unit": "%",
                "change": 5.5,
                "change_percent": 9.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 57.53,
                "min": 50.41,
                "max": 66.41,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 15.26,
                        "percentage": 23.3
                },
                {
                        "category": "Existing Customers",
                        "value": 13.66,
                        "percentage": 20.9
                },
                {
                        "category": "VIP Customers",
                        "value": 10.76,
                        "percentage": 16.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.0,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 21.82,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.765650",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Referenceability Rate"
        }
    },
}
