"""
Training Content Utilization

The frequency with which sales reps use the training materials and resources provided.
"""

TRAINING_CONTENT_UTILIZATION = {
    "code": "TRAINING_CONTENT_UTILIZATION",
    "name": "Training Content Utilization",
    "description": "The frequency with which sales reps use the training materials and resources provided.",
    "formula": "(Number of Accesses to Training Content / Number of Training Materials Available) * 100",
    "calculation_formula": "(Number of Accesses to Training Content / Number of Training Materials Available) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Content Utilization to be added.",
    "trend_analysis": """



    * Increasing utilization may indicate a positive response to the training content and improved sales performance.
    * Decreasing utilization could signal a need to reassess the relevance and effectiveness of the training materials.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific training modules or resources that are being underutilized?
    * How does the utilization of training content correlate with sales performance and quota attainment?
    
    
    
    """,
    "actionable_tips": """



    * Regularly update and refresh training materials to keep them relevant and engaging.
    * Provide incentives or recognition for reps who demonstrate strong utilization of training resources.
    * Seek feedback from sales reps on the effectiveness and helpfulness of the training content.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of training content utilization over time.
    * Pie charts comparing the utilization rates of different training modules or resources.
    
    
    
    """,
    "risk_warnings": """



    * Low utilization may lead to missed sales opportunities and decreased productivity.
    * High utilization without corresponding improvements in sales performance may indicate a need for more effective training content.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track and analyze the utilization of training materials.
    * Survey and feedback tools to gather insights from sales reps on the usefulness of the training content.
    
    
    
    """,
    "integration_points": """



    * Integrate training content utilization data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link utilization data with individual performance reviews and coaching sessions to address specific training needs.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving utilization can lead to better sales performance and increased revenue.
    * However, over-reliance on training materials without practical application may not translate to actual sales results.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.733298"},
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
                        80.35,
                        79.89,
                        75.48,
                        62.91,
                        74.97,
                        67.79,
                        69.49,
                        73.75,
                        62.94,
                        66.92,
                        70.47,
                        64.45
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.45,
                "unit": "%",
                "change": -6.02,
                "change_percent": -8.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 70.78,
                "min": 62.91,
                "max": 80.35,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.45,
                        "percentage": 25.5
                },
                {
                        "category": "Segment B",
                        "value": 15.22,
                        "percentage": 23.6
                },
                {
                        "category": "Segment C",
                        "value": 7.18,
                        "percentage": 11.1
                },
                {
                        "category": "Segment D",
                        "value": 7.21,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 18.39,
                        "percentage": 28.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.826690",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Training Content Utilization"
        }
    },
}
