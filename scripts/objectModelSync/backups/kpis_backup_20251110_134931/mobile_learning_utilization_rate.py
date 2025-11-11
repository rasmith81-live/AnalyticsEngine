"""
Mobile Learning Utilization Rate

The percentage of training completed using mobile devices, indicating flexibility and accessibility.
"""

MOBILE_LEARNING_UTILIZATION_RATE = {
    "code": "MOBILE_LEARNING_UTILIZATION_RATE",
    "name": "Mobile Learning Utilization Rate",
    "description": "The percentage of training completed using mobile devices, indicating flexibility and accessibility.",
    "formula": "(Number of Mobile Learning Resources Accessed / Total Number of Mobile Learning Resources Available) * 100",
    "calculation_formula": "(Number of Mobile Learning Resources Accessed / Total Number of Mobile Learning Resources Available) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Mobile Learning Utilization Rate to be added.",
    "trend_analysis": """

    * Mobile learning utilization rate tends to increase over time as more employees adopt mobile training methods.
    * A decreasing trend may indicate issues with the accessibility or quality of mobile training platforms.
    
    """,
    "diagnostic_questions": """

    * Are there specific barriers or challenges that prevent employees from utilizing mobile learning for training?
    * How does the mobile learning utilization rate compare with traditional training completion rates?
    
    """,
    "actionable_tips": """

    * Invest in user-friendly mobile learning platforms to encourage higher utilization rates.
    * Provide incentives or rewards for employees who complete training using mobile devices.
    * Offer technical support and training for employees who may be unfamiliar with mobile learning methods.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the increase or decrease in mobile learning utilization rate over time.
    * Comparison bar charts between mobile and traditional training completion rates.
    
    """,
    "risk_warnings": """

    * Low mobile learning utilization rates may indicate a disconnect between the training content and the mobile platform.
    * Failure to address low utilization rates can lead to a lack of training completion and knowledge gaps among the sales team.
    
    """,
    "tracking_tools": """

    * Learning management systems with mobile compatibility for tracking and analyzing mobile learning utilization.
    * Mobile app analytics tools to understand user behavior and engagement with training content.
    
    """,
    "integration_points": """

    * Integrate mobile learning utilization data with performance management systems to assess the impact of training on sales results.
    * Link mobile learning utilization with employee development plans to track individual progress and identify areas for improvement.
    
    """,
    "change_impact_analysis": """

    * Increasing mobile learning utilization can lead to a more knowledgeable and adaptable sales team, potentially improving sales performance.
    * However, a lack of improvement in mobile learning utilization may result in stagnant or declining sales effectiveness.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.662272"},
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
                        78.01,
                        74.41,
                        75.18,
                        70.12,
                        83.12,
                        82.52,
                        79.68,
                        68.57,
                        86.99,
                        83.27,
                        69.9,
                        67.93
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.93,
                "unit": "%",
                "change": -1.97,
                "change_percent": -2.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 76.64,
                "min": 67.93,
                "max": 86.99,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.39,
                        "percentage": 22.7
                },
                {
                        "category": "Category B",
                        "value": 14.52,
                        "percentage": 21.4
                },
                {
                        "category": "Category C",
                        "value": 9.36,
                        "percentage": 13.8
                },
                {
                        "category": "Category D",
                        "value": 6.06,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 22.6,
                        "percentage": 33.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.662272",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Mobile Learning Utilization Rate"
        }
    },
}
