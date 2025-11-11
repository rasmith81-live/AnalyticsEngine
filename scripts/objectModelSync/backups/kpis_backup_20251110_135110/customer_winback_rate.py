"""
Customer Winback Rate

The percentage of former customers who have been reacquired.
"""

CUSTOMER_WINBACK_RATE = {
    "code": "CUSTOMER_WINBACK_RATE",
    "name": "Customer Winback Rate",
    "description": "The percentage of former customers who have been reacquired.",
    "formula": "(Number of Customers Regained / Number of Customers Who Left) * 100",
    "calculation_formula": "(Number of Customers Regained / Number of Customers Who Left) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Winback Rate to be added.",
    "trend_analysis": """


    * A rising customer winback rate may indicate improved customer retention strategies or enhanced product offerings that are attracting former customers back.
    * A decreasing rate could signal increased competition, declining customer satisfaction, or ineffective winback campaigns.
    
    
    """,
    "diagnostic_questions": """


    * What are the primary reasons why customers leave, and how can we address those issues to improve the winback rate?
    * Are our winback efforts targeted and personalized, or are they generic and ineffective in reacquiring former customers?
    
    
    """,
    "actionable_tips": """


    * Implement targeted winback campaigns based on customer behavior and preferences.
    * Enhance customer service and support to address any issues that led to customer attrition.
    * Offer incentives or promotions to entice former customers to return.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer winback rate over time.
    * Pie charts comparing the reasons for customer attrition and the success rates of different winback strategies.
    
    
    """,
    "risk_warnings": """


    * Low customer winback rates may indicate a lack of customer loyalty and could lead to long-term revenue loss.
    * Repeated failed winback attempts may result in negative brand perception and reputation among former customers.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track and manage winback campaigns and customer interactions.
    * Data analytics tools to identify patterns and preferences of former customers for targeted winback efforts.
    
    
    """,
    "integration_points": """


    * Integrate winback rate data with customer feedback and satisfaction metrics to understand the underlying reasons for customer attrition.
    * Link winback rate with sales and marketing systems to align winback campaigns with overall sales strategies.
    
    
    """,
    "change_impact_analysis": """


    * Improving the customer winback rate can lead to increased customer lifetime value and overall revenue growth.
    * However, aggressive winback strategies may impact current customer relationships and satisfaction if not executed carefully.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review"], "last_validated": "2025-11-10T13:49:32.895339"},
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
                        44.85,
                        49.98,
                        44.0,
                        51.98,
                        47.2,
                        52.14,
                        45.68,
                        39.58,
                        47.85,
                        39.42,
                        47.59,
                        51.16
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.16,
                "unit": "%",
                "change": 3.57,
                "change_percent": 7.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 46.79,
                "min": 39.42,
                "max": 52.14,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.66,
                        "percentage": 24.7
                },
                {
                        "category": "Category B",
                        "value": 7.43,
                        "percentage": 14.5
                },
                {
                        "category": "Category C",
                        "value": 9.73,
                        "percentage": 19.0
                },
                {
                        "category": "Category D",
                        "value": 2.81,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 18.53,
                        "percentage": 36.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.389509",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Winback Rate"
        }
    },
}
