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
                        64.7,
                        68.4,
                        65.9,
                        65.9,
                        74.4,
                        65.4,
                        76.8,
                        77.4,
                        68.9,
                        76.1,
                        67.2,
                        70.7
                ],
                "unit": "score"
        },
        "current": {
                "value": 70.7,
                "unit": "score",
                "change": 3.5,
                "change_percent": 5.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 70.15,
                "min": 64.7,
                "max": 77.4,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 18.37,
                        "percentage": 26.0
                },
                {
                        "category": "Channel Sales",
                        "value": 8.57,
                        "percentage": 12.1
                },
                {
                        "category": "Online Sales",
                        "value": 12.6,
                        "percentage": 17.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.58,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 26.58,
                        "percentage": 37.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.156943",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Rep Engagement Index"
        }
    },
}
