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
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager"], "last_validated": "2025-11-10T13:43:23.333421"},
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
                        78.98,
                        69.37,
                        81.47,
                        63.19,
                        66.64,
                        67.48,
                        78.97,
                        73.57,
                        66.3,
                        74.84,
                        77.29,
                        79.94
                ],
                "unit": "%"
        },
        "current": {
                "value": 79.94,
                "unit": "%",
                "change": 2.65,
                "change_percent": 3.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.17,
                "min": 63.19,
                "max": 81.47,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.85,
                        "percentage": 17.3
                },
                {
                        "category": "Category B",
                        "value": 19.56,
                        "percentage": 24.5
                },
                {
                        "category": "Category C",
                        "value": 10.04,
                        "percentage": 12.6
                },
                {
                        "category": "Category D",
                        "value": 7.28,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 29.21,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.333421",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Referenceability Rate"
        }
    },
}
