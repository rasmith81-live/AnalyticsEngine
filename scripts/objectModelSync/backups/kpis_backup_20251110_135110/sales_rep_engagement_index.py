"""
Sales Rep Engagement Index

A composite measure of how engaged sales reps are with their work and training.
"""

SALES_REP_ENGAGEMENT_INDEX = {
    "code": "SALES_REP_ENGAGEMENT_INDEX",
    "name": "Sales Rep Engagement Index",
    "description": "A composite measure of how engaged sales reps are with their work and training.",
    "formula": "Composite Score from Engagement Surveys",
    "calculation_formula": "Composite Score from Engagement Surveys",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Rep Engagement Index to be added.",
    "trend_analysis": """


    * An increasing Sales Rep Engagement Index may indicate a positive shift in the sales team's motivation and productivity.
    * A decreasing index could signal disengagement, potential turnover, or dissatisfaction with training and coaching programs.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific training modules or coaching methods that are receiving lower engagement from sales reps?
    * How does the Sales Rep Engagement Index compare with industry benchmarks or with historical data?
    
    
    """,
    "actionable_tips": """


    * Regularly solicit feedback from sales reps to understand their training and coaching needs.
    * Provide personalized coaching and training plans to address individual development areas and keep sales reps engaged.
    * Implement recognition and rewards programs to acknowledge and incentivize active participation in training and coaching activities.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of the Sales Rep Engagement Index over time.
    * Pie charts to visualize the distribution of engagement levels across different training and coaching programs.
    
    
    """,
    "risk_warnings": """


    * Low engagement may lead to decreased sales performance and missed targets.
    * Disengagement could also result in increased turnover and recruitment costs.
    
    
    """,
    "tracking_tools": """


    * Employee engagement platforms like Officevibe or 15Five to gather feedback and measure engagement levels.
    * Learning management systems (LMS) to track participation and completion rates of training modules.
    
    
    """,
    "integration_points": """


    * Integrate the Sales Rep Engagement Index with performance management systems to identify correlations between engagement and sales results.
    * Link engagement data with HR systems to understand the impact of engagement on turnover and retention.
    
    
    """,
    "change_impact_analysis": """


    * Improving the Sales Rep Engagement Index can lead to higher sales productivity and improved customer satisfaction.
    * Conversely, low engagement may result in missed sales opportunities and a negative impact on the overall sales team morale.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.483301"},
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
                        65.0,
                        65.8,
                        56.3,
                        67.3,
                        61.7,
                        68.9,
                        56.9,
                        64.0,
                        60.9,
                        67.6,
                        68.8,
                        58.8
                ],
                "unit": "score"
        },
        "current": {
                "value": 58.8,
                "unit": "score",
                "change": -10.0,
                "change_percent": -14.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.5,
                "min": 56.3,
                "max": 68.9,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.24,
                        "percentage": 24.2
                },
                {
                        "category": "Category B",
                        "value": 13.02,
                        "percentage": 22.1
                },
                {
                        "category": "Category C",
                        "value": 5.14,
                        "percentage": 8.7
                },
                {
                        "category": "Category D",
                        "value": 3.99,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 22.41,
                        "percentage": 38.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.566668",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Rep Engagement Index"
        }
    },
}
