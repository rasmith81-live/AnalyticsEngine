"""
Sales Role Play Effectiveness Score

A measure of the effectiveness of role-play exercises in improving sales skills and performance.
"""

SALES_ROLE_PLAY_EFFECTIVENESS_SCORE = {
    "code": "SALES_ROLE_PLAY_EFFECTIVENESS_SCORE",
    "name": "Sales Role Play Effectiveness Score",
    "description": "A measure of the effectiveness of role-play exercises in improving sales skills and performance.",
    "formula": "Average Improvement Score Post-Role Play Exercises",
    "calculation_formula": "Average Improvement Score Post-Role Play Exercises",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Role Play Effectiveness Score to be added.",
    "trend_analysis": """


    * An increasing effectiveness score may indicate that sales skills are improving and positively impacting performance.
    * A decreasing score could signal a need for reevaluation of role-play exercises or a decline in sales performance.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific sales skills or scenarios where role-play exercises are particularly effective or ineffective?
    * How does the effectiveness score align with actual sales performance and customer feedback?
    
    
    """,
    "actionable_tips": """


    * Regularly update and refresh role-play scenarios to keep them relevant and challenging for sales teams.
    * Provide constructive feedback and coaching to sales representatives based on their performance in role-play exercises.
    * Use technology to simulate real-world sales scenarios and provide a more immersive role-play experience.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of the effectiveness score over time.
    * Comparison charts to visualize the effectiveness scores of different sales teams or individuals.
    
    
    """,
    "risk_warnings": """


    * A consistently low effectiveness score may indicate a need for more comprehensive sales training and development.
    * High variability in the effectiveness score could suggest inconsistency in the quality of role-play exercises across different teams or regions.
    
    
    """,
    "tracking_tools": """


    * Simulation software and virtual reality tools to create more realistic and engaging role-play scenarios.
    * Sales performance management platforms that can track and analyze the impact of role-play exercises on actual sales outcomes.
    
    
    """,
    "integration_points": """


    * Integrate the effectiveness score with individual performance reviews and coaching sessions to align development efforts with specific needs.
    * Link the score with sales forecasting and pipeline management to identify potential areas for improvement in sales strategies.
    
    
    """,
    "change_impact_analysis": """


    * Improving the effectiveness score can lead to increased sales productivity and better customer interactions.
    * Conversely, a declining score may indicate a negative impact on sales performance and customer satisfaction.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.495143"},
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
                        82.1,
                        79.8,
                        84.6,
                        81.2,
                        81.3,
                        76.7,
                        80.3,
                        83.0,
                        74.6,
                        81.0,
                        78.7,
                        85.5
                ],
                "unit": "score"
        },
        "current": {
                "value": 85.5,
                "unit": "score",
                "change": 6.8,
                "change_percent": 8.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 80.73,
                "min": 74.6,
                "max": 85.5,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.86,
                        "percentage": 20.9
                },
                {
                        "category": "Category B",
                        "value": 20.52,
                        "percentage": 24.0
                },
                {
                        "category": "Category C",
                        "value": 10.14,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 5.92,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 31.06,
                        "percentage": 36.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.601749",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Role Play Effectiveness Score"
        }
    },
}
