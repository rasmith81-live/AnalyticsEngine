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
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.830862"},
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
                        317.69,
                        352.41,
                        347.1,
                        308.3,
                        284.13,
                        280.25,
                        275.13,
                        384.09,
                        316.78,
                        417.92,
                        330.27,
                        278.72
                ],
                "unit": "units"
        },
        "current": {
                "value": 278.72,
                "unit": "units",
                "change": -51.55,
                "change_percent": -15.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 324.4,
                "min": 275.13,
                "max": 417.92,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 43.03,
                        "percentage": 15.4
                },
                {
                        "category": "Existing Customers",
                        "value": 43.86,
                        "percentage": 15.7
                },
                {
                        "category": "VIP Customers",
                        "value": 54.46,
                        "percentage": 19.5
                },
                {
                        "category": "At-Risk Customers",
                        "value": 17.81,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 119.56,
                        "percentage": 42.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.665569",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Feedback on Sales Interactions"
        }
    },
}
