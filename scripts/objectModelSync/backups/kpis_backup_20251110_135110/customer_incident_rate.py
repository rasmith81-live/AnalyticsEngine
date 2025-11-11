"""
Customer Incident Rate

The frequency at which customers encounter issues or problems with the company's products or services.
"""

CUSTOMER_INCIDENT_RATE = {
    "code": "CUSTOMER_INCIDENT_RATE",
    "name": "Customer Incident Rate",
    "description": "The frequency at which customers encounter issues or problems with the company's products or services.",
    "formula": "Total Number of Incidents Reported / Total Number of Customers",
    "calculation_formula": "Total Number of Incidents Reported / Total Number of Customers",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Incident Rate to be added.",
    "trend_analysis": """


    * An increasing customer incident rate may indicate declining product quality or service levels.
    * A decreasing rate could signal improved customer support or product enhancements.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific products or services that are consistently causing customer incidents?
    * How does our customer incident rate compare with industry standards or benchmarks?
    
    
    """,
    "actionable_tips": """


    * Invest in customer service training to address and resolve issues more effectively.
    * Regularly gather and analyze customer feedback to identify areas for improvement.
    * Implement proactive communication strategies to manage customer expectations and prevent incidents.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer incident rates over time.
    * Pareto charts to identify the most common types of customer incidents.
    
    
    """,
    "risk_warnings": """


    * High customer incident rates can lead to customer churn and negative word-of-mouth.
    * Consistently high incident rates may indicate systemic issues that could damage the company's reputation.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track and manage customer incidents.
    * Quality management systems to identify and address root causes of customer incidents.
    
    
    """,
    "integration_points": """


    * Integrate customer incident data with product development processes to prioritize improvements.
    * Link customer incident tracking with customer satisfaction surveys to understand the impact of incidents on overall satisfaction.
    
    
    """,
    "change_impact_analysis": """


    * Reducing customer incident rates can lead to higher customer retention and loyalty.
    * However, addressing customer incidents may require increased resources and operational costs.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Sales Representative", "Service Level Agreement", "Support Ticket"], "last_validated": "2025-11-10T13:49:32.838149"},
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
                        69.38,
                        70.8,
                        76.14,
                        69.87,
                        72.63,
                        76.16,
                        76.2,
                        79.63,
                        80.65,
                        71.93,
                        77.81,
                        73.48
                ],
                "unit": "%"
        },
        "current": {
                "value": 73.48,
                "unit": "%",
                "change": -4.33,
                "change_percent": -5.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.56,
                "min": 69.38,
                "max": 80.65,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.03,
                        "percentage": 30.0
                },
                {
                        "category": "Category B",
                        "value": 10.53,
                        "percentage": 14.3
                },
                {
                        "category": "Category C",
                        "value": 10.16,
                        "percentage": 13.8
                },
                {
                        "category": "Category D",
                        "value": 3.39,
                        "percentage": 4.6
                },
                {
                        "category": "Other",
                        "value": 27.37,
                        "percentage": 37.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.282846",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Incident Rate"
        }
    },
}
