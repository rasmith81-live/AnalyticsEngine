"""
Customer Feedback on Sales Interactions

A measure of customer impressions and feedback regarding interactions with trained sales reps.
"""

CUSTOMER_FEEDBACK_ON_SALES_INTERACTIONS = {
    "code": "CUSTOMER_FEEDBACK_ON_SALES_INTERACTIONS",
    "name": "Customer Feedback on Sales Interactions",
    "description": "A measure of customer impressions and feedback regarding interactions with trained sales reps.",
    "formula": "Quality Score Derived from Customer Feedback Surveys",
    "calculation_formula": "Quality Score Derived from Customer Feedback Surveys",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Feedback on Sales Interactions to be added.",
    "trend_analysis": """

    * Increasing positive feedback may indicate improved sales rep performance or customer satisfaction.
    * Decreasing feedback or a rise in negative comments could signal declining sales rep effectiveness or customer dissatisfaction.
    
    """,
    "diagnostic_questions": """

    * Are there common themes or patterns in the feedback received from customers?
    * How do our sales reps' interactions compare with industry benchmarks or customer expectations?
    
    """,
    "actionable_tips": """

    * Provide ongoing training and coaching for sales reps to enhance their communication and relationship-building skills.
    * Implement a feedback loop for sales reps to receive and act upon customer feedback in real-time.
    * Utilize customer relationship management (CRM) tools to track and analyze customer interactions for continuous improvement.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of positive and negative feedback over time.
    * Word clouds to visually represent common themes or keywords in customer feedback.
    
    """,
    "risk_warnings": """

    * Consistently negative feedback may lead to customer churn and loss of revenue.
    * Ignoring or mishandling customer feedback can damage brand reputation and trust.
    
    """,
    "tracking_tools": """

    * CRM systems with built-in feedback management features, such as Salesforce or HubSpot.
    * Social listening tools to monitor and analyze customer sentiment across various channels.
    
    """,
    "integration_points": """

    * Integrate customer feedback data with sales performance metrics to identify correlations and areas for improvement.
    * Link customer feedback with employee performance evaluations to align incentives with customer satisfaction goals.
    
    """,
    "change_impact_analysis": """

    * Improving customer feedback can lead to increased customer retention and lifetime value.
    * However, focusing solely on positive feedback may neglect areas of improvement and hinder overall sales performance.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.264579"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
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
                        672.18,
                        606.87,
                        661.73,
                        602.33,
                        665.62,
                        676.44,
                        579.93,
                        651.43,
                        638.44,
                        674.06,
                        597.83,
                        621.97
                ],
                "unit": "units"
        },
        "current": {
                "value": 621.97,
                "unit": "units",
                "change": 24.14,
                "change_percent": 4.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 637.4,
                "min": 579.93,
                "max": 676.44,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 131.02,
                        "percentage": 21.1
                },
                {
                        "category": "Category B",
                        "value": 75.65,
                        "percentage": 12.2
                },
                {
                        "category": "Category C",
                        "value": 83.48,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 86.5,
                        "percentage": 13.9
                },
                {
                        "category": "Other",
                        "value": 245.32,
                        "percentage": 39.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.264579",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Feedback on Sales Interactions"
        }
    },
}
