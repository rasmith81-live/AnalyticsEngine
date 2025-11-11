"""
Customer Retention Post-Training

The change in customer retention rates attributed to improved sales rep performance post-training.
"""

CUSTOMER_RETENTION_POST_TRAINING = {
    "code": "CUSTOMER_RETENTION_POST_TRAINING",
    "name": "Customer Retention Post-Training",
    "description": "The change in customer retention rates attributed to improved sales rep performance post-training.",
    "formula": "(Number of Customers Retained Post-Training / Total Number of Customers Engaged Post-Training) * 100",
    "calculation_formula": "(Number of Customers Retained Post-Training / Total Number of Customers Engaged Post-Training) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Retention Post-Training to be added.",
    "trend_analysis": """



    * An increasing customer retention rate post-training may indicate that the sales reps are effectively applying the skills and knowledge gained from the training.
    * A decreasing rate could signal that the training content or delivery method needs to be reassessed for effectiveness.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments or products that show a significant change in retention rates post-training?
    * How does the customer retention rate post-training compare with industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular follow-up sessions or refresher courses to reinforce the training and ensure continued application of new skills.
    * Provide ongoing coaching and support to sales reps to address specific challenges or areas for improvement identified post-training.
    * Collect feedback from customers to understand the impact of the training on their experience and satisfaction.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend in customer retention rates over time, pre and post-training.
    * Comparison bar charts to visualize the change in retention rates across different sales reps or teams.
    
    
    
    """,
    "risk_warnings": """



    * A decline in customer retention post-training may lead to lost revenue and damage to the company's reputation.
    * Consistently high retention rates without improvement may indicate a lack of impact from the training, leading to wasted resources.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze customer retention rates and feedback post-training.
    * Sales performance management platforms to monitor the application of training concepts and identify areas for improvement.
    
    
    
    """,
    "integration_points": """



    * Integrate customer retention data with sales training performance metrics to assess the direct impact of training on retention rates.
    * Link customer feedback systems with training evaluation to understand the correlation between customer satisfaction and training effectiveness.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving customer retention post-training can lead to increased sales, customer loyalty, and positive word-of-mouth referrals.
    * Conversely, a decline in retention rates may require additional resources to address customer dissatisfaction and potential loss of business.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.870654"},
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
                        67.39,
                        65.29,
                        60.27,
                        52.68,
                        68.79,
                        63.5,
                        52.09,
                        68.7,
                        59.0,
                        57.84,
                        60.14,
                        69.46
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.46,
                "unit": "%",
                "change": 9.32,
                "change_percent": 15.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 62.1,
                "min": 52.09,
                "max": 69.46,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 15.16,
                        "percentage": 21.8
                },
                {
                        "category": "Existing Customers",
                        "value": 10.86,
                        "percentage": 15.6
                },
                {
                        "category": "VIP Customers",
                        "value": 14.3,
                        "percentage": 20.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.76,
                        "percentage": 5.4
                },
                {
                        "category": "Other",
                        "value": 25.38,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.779839",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Retention Post-Training"
        }
    },
}
