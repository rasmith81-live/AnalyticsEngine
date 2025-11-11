"""
Customer Feedback on Sales Experience

Customer perceptions of their buying experience, which can influence satisfaction, loyalty, and future sales.
"""

CUSTOMER_FEEDBACK_ON_SALES_EXPERIENCE = {
    "code": "CUSTOMER_FEEDBACK_ON_SALES_EXPERIENCE",
    "name": "Customer Feedback on Sales Experience",
    "description": "Customer perceptions of their buying experience, which can influence satisfaction, loyalty, and future sales.",
    "formula": "Qualitative analysis, no standard formula",
    "calculation_formula": "Qualitative analysis, no standard formula",
    "category": "Sales Strategy",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Feedback on Sales Experience to be added.",
    "trend_analysis": """


    * An increasing customer feedback on sales experience may indicate a decline in customer satisfaction and loyalty.
    * A decreasing feedback may signal improved sales processes and customer interactions.
    
    
    """,
    "diagnostic_questions": """


    * Are there common themes or issues mentioned in customer feedback?
    * How does our customer feedback compare with industry benchmarks or competitors?
    
    
    """,
    "actionable_tips": """


    * Implement regular customer feedback surveys to gather insights and identify areas for improvement.
    * Train sales teams to actively listen to customer concerns and address them effectively.
    * Use customer relationship management (CRM) software to track and analyze customer interactions and feedback.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of customer feedback over time.
    * Word clouds to visually represent common themes or issues mentioned in customer feedback.
    
    
    """,
    "risk_warnings": """


    * Low customer feedback scores can lead to decreased customer retention and negative word-of-mouth.
    * Consistently negative feedback may indicate systemic issues in the sales process that need to be addressed.
    
    
    """,
    "tracking_tools": """


    * Customer feedback management platforms like Medallia or Qualtrics to collect and analyze feedback data.
    * CRM systems with built-in feedback tracking and reporting capabilities.
    
    
    """,
    "integration_points": """


    * Integrate customer feedback data with sales performance metrics to understand the impact on overall sales effectiveness.
    * Link customer feedback with employee performance evaluations to align incentives with customer satisfaction goals.
    
    
    """,
    "change_impact_analysis": """


    * Improving customer feedback can lead to increased customer retention and higher lifetime value.
    * Conversely, consistently low feedback scores can impact brand reputation and market competitiveness.
    
    
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Loyalty Program", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.829815"},
    "required_objects": [],
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
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
                        524.43,
                        540.06,
                        519.31,
                        545.86,
                        486.12,
                        565.62,
                        537.73,
                        504.75,
                        577.63,
                        529.67,
                        471.01,
                        459.1
                ],
                "unit": "units"
        },
        "current": {
                "value": 459.1,
                "unit": "units",
                "change": -11.91,
                "change_percent": -2.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 521.77,
                "min": 459.1,
                "max": 577.63,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 157.39,
                        "percentage": 34.3
                },
                {
                        "category": "Category B",
                        "value": 104.35,
                        "percentage": 22.7
                },
                {
                        "category": "Category C",
                        "value": 46.02,
                        "percentage": 10.0
                },
                {
                        "category": "Category D",
                        "value": 29.97,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 121.37,
                        "percentage": 26.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.261242",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Feedback on Sales Experience"
        }
    },
}
