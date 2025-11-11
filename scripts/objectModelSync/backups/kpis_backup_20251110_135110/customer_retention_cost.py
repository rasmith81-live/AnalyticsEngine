"""
Customer Retention Cost

The total cost associated with retaining an existing customer.
"""

CUSTOMER_RETENTION_COST = {
    "code": "CUSTOMER_RETENTION_COST",
    "name": "Customer Retention Cost",
    "description": "The total cost associated with retaining an existing customer.",
    "formula": "Total Retention Costs / Number of Customers Retained",
    "calculation_formula": "Total Retention Costs / Number of Customers Retained",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Retention Cost to be added.",
    "trend_analysis": """


    * Increasing customer retention cost may indicate higher expenses in loyalty programs or customer support.
    * Decreasing cost could signal improved customer satisfaction and loyalty, leading to lower retention efforts.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific customer segments that require higher retention costs?
    * How does our customer retention cost compare with industry averages or benchmarks?
    
    
    """,
    "actionable_tips": """


    * Invest in customer relationship management (CRM) systems to better understand and target high-cost segments.
    * Implement customer loyalty programs to increase retention without significantly increasing costs.
    * Regularly review and optimize customer support processes to reduce associated expenses.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer retention cost over time.
    * Pie charts to compare the distribution of retention costs across different customer segments.
    
    
    """,
    "risk_warnings": """


    * High customer retention costs may erode profitability if not aligned with the value derived from retained customers.
    * Significant fluctuations in retention costs may indicate inconsistent customer experiences or ineffective retention strategies.
    
    
    """,
    "tracking_tools": """


    * CRM software like Salesforce or HubSpot for tracking and managing customer retention efforts.
    * Customer loyalty platforms such as Smile.io or Yotpo to implement and monitor loyalty programs.
    
    
    """,
    "integration_points": """


    * Integrate customer retention cost analysis with financial systems to understand its impact on overall profitability.
    * Link retention cost data with customer feedback and satisfaction metrics to identify areas for improvement.
    
    
    """,
    "change_impact_analysis": """


    * Reducing customer retention costs may lead to improved profitability, but it should not compromise the quality of customer experience.
    * Increasing retention costs without a corresponding increase in customer value may indicate inefficiencies in retention strategies.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Sale"], "replaces": ["ACCOUNT_RETENTION_COSTS"], "last_validated": "2025-11-10T13:49:32.869485"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "OUTSIDE_SALES"],
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
                        274,
                        301,
                        311,
                        312,
                        293,
                        312,
                        273,
                        294,
                        302,
                        305,
                        318,
                        284
                ],
                "unit": "count"
        },
        "current": {
                "value": 284,
                "unit": "count",
                "change": -34,
                "change_percent": -10.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 298.25,
                "min": 273,
                "max": 318,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 48.8,
                        "percentage": 17.2
                },
                {
                        "category": "Category B",
                        "value": 77.77,
                        "percentage": 27.4
                },
                {
                        "category": "Category C",
                        "value": 50.76,
                        "percentage": 17.9
                },
                {
                        "category": "Category D",
                        "value": 27.8,
                        "percentage": 9.8
                },
                {
                        "category": "Other",
                        "value": 78.87,
                        "percentage": 27.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.341443",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Retention Cost"
        }
    },
}
