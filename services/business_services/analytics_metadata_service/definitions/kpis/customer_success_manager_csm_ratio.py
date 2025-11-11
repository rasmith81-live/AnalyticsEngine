"""
Customer Success Manager (CSM) Ratio

The ratio of customers to customer success managers, indicating the level of personalized attention provided.
"""

CUSTOMER_SUCCESS_MANAGER_CSM_RATIO = {
    "code": "CUSTOMER_SUCCESS_MANAGER_CSM_RATIO",
    "name": "Customer Success Manager (CSM) Ratio",
    "description": "The ratio of customers to customer success managers, indicating the level of personalized attention provided.",
    "formula": "Total Number of Customers / Number of Customer Success Managers",
    "calculation_formula": "Total Number of Customers / Number of Customer Success Managers",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Success Manager (CSM) Ratio to be added.",
    "trend_analysis": """



    * An increasing CSM ratio may indicate a growing customer base without a proportional increase in customer success managers, potentially leading to decreased personalized attention.
    * A decreasing ratio could signal improved efficiency in customer success management, but it could also mean that customer success managers are spread too thin to provide adequate support.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments or product lines that require more attention from customer success managers?
    * How does our CSM ratio compare to industry standards or benchmarks for similar companies?
    
    
    
    """,
    "actionable_tips": """



    * Implement customer segmentation to prioritize high-value customers for more personalized attention.
    * Invest in training and development for customer success managers to improve their efficiency and effectiveness.
    * Consider hiring additional customer success managers to maintain a healthy ratio as the customer base grows.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of the CSM ratio over time.
    * Bar graphs comparing the CSM ratio across different customer segments or product categories.
    
    
    
    """,
    "risk_warnings": """



    * A high CSM ratio may lead to decreased customer satisfaction and retention.
    * An excessively low ratio could result in increased operational costs without a proportional improvement in customer success.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify areas for improvement.
    * Workflow automation tools to streamline routine tasks and free up time for more personalized customer engagement.
    
    
    
    """,
    "integration_points": """



    * Integrate the CSM ratio with sales and marketing systems to align customer success efforts with overall business objectives.
    * Link the ratio with customer feedback and satisfaction metrics to understand the impact of customer success efforts on overall customer experience.
    
    
    
    """,
    "change_impact_analysis": """



    * An improved CSM ratio can lead to higher customer lifetime value and increased referrals, but it may also require additional investment in customer success resources.
    * A declining ratio could result in decreased customer retention and negative word-of-mouth, impacting overall sales and revenue.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account Manager", "Sales Representative", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.886154"},
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
                        65.97,
                        67.34,
                        69.25,
                        64.2,
                        66.59,
                        64.85,
                        65.27,
                        62.66,
                        66.55,
                        69.81,
                        66.55,
                        64.35
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.35,
                "unit": "%",
                "change": -2.2,
                "change_percent": -3.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 66.12,
                "min": 62.66,
                "max": 69.81,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 11.79,
                        "percentage": 18.3
                },
                {
                        "category": "Existing Customers",
                        "value": 17.58,
                        "percentage": 27.3
                },
                {
                        "category": "VIP Customers",
                        "value": 9.03,
                        "percentage": 14.0
                },
                {
                        "category": "At-Risk Customers",
                        "value": 7.56,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 18.39,
                        "percentage": 28.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.822378",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Success Manager (CSM) Ratio"
        }
    },
}
