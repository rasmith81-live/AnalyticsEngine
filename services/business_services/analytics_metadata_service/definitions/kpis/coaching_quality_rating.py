"""
Coaching Quality Rating

A measure of the quality of coaching sessions based on feedback from sales reps.
"""

COACHING_QUALITY_RATING = {
    "code": "COACHING_QUALITY_RATING",
    "name": "Coaching Quality Rating",
    "description": "A measure of the quality of coaching sessions based on feedback from sales reps.",
    "formula": "Average of Coaching Quality Scores Collected from Feedback Surveys",
    "calculation_formula": "Average of Coaching Quality Scores Collected from Feedback Surveys",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Coaching Quality Rating to be added.",
    "trend_analysis": """



    * An increasing coaching quality rating may indicate more effective coaching techniques being implemented by sales managers.
    * A decreasing rating could signal a decline in the effectiveness of coaching sessions or a lack of engagement from sales reps.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas or topics where sales reps consistently rate coaching sessions lower?
    * How does the coaching quality rating compare with sales performance metrics such as conversion rates or average deal size?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular feedback sessions with sales reps to understand their needs and preferences for coaching.
    * Provide training for sales managers on effective coaching techniques and communication skills.
    * Encourage peer-to-peer coaching and knowledge sharing among the sales team.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of coaching quality ratings over time.
    * Radar charts comparing different aspects of coaching quality (e.g., communication, motivation, skill development).
    
    
    
    """,
    "risk_warnings": """



    * Low coaching quality ratings may lead to decreased motivation and performance among sales reps.
    * Consistently low ratings could indicate a need for a complete overhaul of coaching strategies and techniques.
    
    
    
    """,
    "tracking_tools": """



    * Coaching and feedback platforms like Refract or LevelEleven to track coaching sessions and feedback from sales reps.
    * Performance management systems that integrate coaching quality ratings with sales performance data for a comprehensive view.
    
    
    
    """,
    "integration_points": """



    * Integrate coaching quality ratings with performance reviews and goal setting to align coaching efforts with individual development plans.
    * Link coaching quality data with sales training programs to identify areas where additional training or resources may be needed.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving coaching quality can lead to increased sales performance and overall team effectiveness.
    * Conversely, a decline in coaching quality may result in missed sales opportunities and decreased team morale.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer Feedback", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.702728"},
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
                        82.1,
                        80.8,
                        80.0,
                        78.9,
                        74.1,
                        84.0,
                        75.5,
                        82.8,
                        75.2,
                        85.5,
                        73.4,
                        82.4
                ],
                "unit": "score"
        },
        "current": {
                "value": 82.4,
                "unit": "score",
                "change": 9.0,
                "change_percent": 12.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 79.56,
                "min": 73.4,
                "max": 85.5,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.34,
                        "percentage": 18.6
                },
                {
                        "category": "Segment B",
                        "value": 16.98,
                        "percentage": 20.6
                },
                {
                        "category": "Segment C",
                        "value": 15.78,
                        "percentage": 19.2
                },
                {
                        "category": "Segment D",
                        "value": 9.37,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 24.93,
                        "percentage": 30.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.487811",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Coaching Quality Rating"
        }
    },
}
