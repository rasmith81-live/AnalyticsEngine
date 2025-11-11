"""
Sales Training Attendance Rate

The percentage of eligible sales representatives who attend scheduled sales training sessions.
"""

SALES_TRAINING_ATTENDANCE_RATE = {
    "code": "SALES_TRAINING_ATTENDANCE_RATE",
    "name": "Sales Training Attendance Rate",
    "description": "The percentage of eligible sales representatives who attend scheduled sales training sessions.",
    "formula": "(Number of Reps Attending Training / Total Number of Reps Expected to Attend) * 100",
    "calculation_formula": "(Number of Reps Attending Training / Total Number of Reps Expected to Attend) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Training Attendance Rate to be added.",
    "trend_analysis": """

    * Increasing sales training attendance rate may indicate a more engaged and motivated sales team.
    * Decreasing attendance could signal a lack of interest in the training content or a need for more engaging training methods.
    
    """,
    "diagnostic_questions": """

    * Are there specific topics or areas of training that consistently have lower attendance?
    * How does the attendance rate vary between new hires and more experienced sales representatives?
    
    """,
    "actionable_tips": """

    * Offer incentives or rewards for attending training sessions to boost participation.
    * Provide more interactive and hands-on training experiences to increase engagement.
    * Regularly survey sales representatives to gather feedback on training content and delivery.
    
    """,
    "visualization_suggestions": """

    * Line charts showing attendance rates over time to identify trends and patterns.
    * Comparison bar charts to visualize attendance rates for different training topics or regions.
    
    """,
    "risk_warnings": """

    * Low attendance rates may lead to gaps in knowledge and skills among the sales team, impacting overall performance.
    * Consistently low attendance could indicate a need for reevaluation of training content and methods.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) to track and analyze attendance data for training sessions.
    * Survey and feedback tools to gather insights from sales representatives about their training experiences.
    
    """,
    "integration_points": """

    * Integrate attendance data with performance metrics to assess the impact of training on sales results.
    * Link attendance tracking with HR systems to identify any correlations between training participation and employee satisfaction or turnover.
    
    """,
    "change_impact_analysis": """

    * Improving attendance rates can lead to better-equipped sales representatives, potentially increasing sales performance and customer satisfaction.
    * However, increased attendance may also require additional resources for training delivery and content development.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:24.676150"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        76.08,
                        77.09,
                        83.41,
                        76.67,
                        80.16,
                        78.43,
                        79.06,
                        75.61,
                        67.45,
                        73.08,
                        76.93,
                        68.48
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.48,
                "unit": "%",
                "change": -8.45,
                "change_percent": -11.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 76.04,
                "min": 67.45,
                "max": 83.41,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.39,
                        "percentage": 28.3
                },
                {
                        "category": "Category B",
                        "value": 12.46,
                        "percentage": 18.2
                },
                {
                        "category": "Category C",
                        "value": 9.95,
                        "percentage": 14.5
                },
                {
                        "category": "Category D",
                        "value": 6.26,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 20.42,
                        "percentage": 29.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.676150",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Training Attendance Rate"
        }
    },
}
