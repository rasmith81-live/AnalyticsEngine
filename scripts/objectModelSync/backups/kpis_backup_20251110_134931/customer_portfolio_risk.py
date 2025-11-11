"""
Customer Portfolio Risk

A measure of the risk associated with the customer portfolio, indicating the potential for churn or dissatisfaction.
"""

CUSTOMER_PORTFOLIO_RISK = {
    "code": "CUSTOMER_PORTFOLIO_RISK",
    "name": "Customer Portfolio Risk",
    "description": "A measure of the risk associated with the customer portfolio, indicating the potential for churn or dissatisfaction.",
    "formula": "Sum of Risk Scores Assigned to Each Customer / Total Number of Customers",
    "calculation_formula": "Sum of Risk Scores Assigned to Each Customer / Total Number of Customers",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Portfolio Risk to be added.",
    "trend_analysis": """

    * Increasing customer portfolio risk may indicate a higher likelihood of churn or dissatisfaction among customers.
    * Decreasing risk could signal improved customer satisfaction and loyalty, leading to lower churn rates.
    
    """,
    "diagnostic_questions": """

    * Are there specific customer segments or industries that contribute more to the overall portfolio risk?
    * How do customer feedback and satisfaction scores correlate with changes in the customer portfolio risk?
    
    """,
    "actionable_tips": """

    * Implement proactive customer success strategies to address potential churn risks and improve overall satisfaction.
    * Leverage data analytics to identify at-risk customers and personalize retention efforts.
    * Invest in customer relationship management (CRM) tools to better track and manage customer interactions and feedback.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of customer portfolio risk over time.
    * Pie charts to visualize the distribution of risk across different customer segments or industries.
    
    """,
    "risk_warnings": """

    * High customer portfolio risk may lead to increased customer churn and negative word-of-mouth, impacting future sales and revenue.
    * Persistent high risk levels could indicate systemic issues in customer management and require immediate attention.
    
    """,
    "tracking_tools": """

    * Customer success platforms like Gainsight or Totango for tracking and managing customer satisfaction and retention efforts.
    * Data analytics tools such as Tableau or Power BI for deeper insights into customer behavior and risk factors.
    
    """,
    "integration_points": """

    * Integrate customer portfolio risk data with sales and marketing systems to align customer retention efforts with sales strategies.
    * Link risk analysis with customer support systems to ensure a coordinated approach in addressing customer concerns and issues.
    
    """,
    "change_impact_analysis": """

    * Reducing customer portfolio risk can lead to higher customer lifetime value and improved overall sales performance.
    * However, investing in customer retention efforts may require additional resources and could impact short-term profitability.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Risk", "Churn Event", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Subscription"], "last_validated": "2025-11-10T13:43:23.323536"},
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
                        315,
                        317,
                        341,
                        326,
                        308,
                        338,
                        330,
                        331,
                        323,
                        343,
                        304,
                        298
                ],
                "unit": "count"
        },
        "current": {
                "value": 298,
                "unit": "count",
                "change": -6,
                "change_percent": -2.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 322.83,
                "min": 298,
                "max": 343,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 68.53,
                        "percentage": 23.0
                },
                {
                        "category": "Category B",
                        "value": 78.74,
                        "percentage": 26.4
                },
                {
                        "category": "Category C",
                        "value": 30.1,
                        "percentage": 10.1
                },
                {
                        "category": "Category D",
                        "value": 31.55,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 89.08,
                        "percentage": 29.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.323536",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Portfolio Risk"
        }
    },
}
