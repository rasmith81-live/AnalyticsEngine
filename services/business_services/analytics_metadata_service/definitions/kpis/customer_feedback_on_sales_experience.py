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
                        940.04,
                        841.62,
                        932.38,
                        805.88,
                        862.0,
                        809.89,
                        912.07,
                        830.6,
                        879.9,
                        929.9,
                        878.83,
                        883.25
                ],
                "unit": "units"
        },
        "current": {
                "value": 883.25,
                "unit": "units",
                "change": 4.42,
                "change_percent": 0.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 875.53,
                "min": 805.88,
                "max": 940.04,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 193.12,
                        "percentage": 21.9
                },
                {
                        "category": "Existing Customers",
                        "value": 190.57,
                        "percentage": 21.6
                },
                {
                        "category": "VIP Customers",
                        "value": 155.22,
                        "percentage": 17.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 103.13,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 241.21,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.661538",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Feedback on Sales Experience"
        }
    },
}
