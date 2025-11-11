"""
Training Progress Tracking Efficiency

How effectively the sales training team tracks the progress of sales reps through training programs.
"""

TRAINING_PROGRESS_TRACKING_EFFICIENCY = {
    "code": "TRAINING_PROGRESS_TRACKING_EFFICIENCY",
    "name": "Training Progress Tracking Efficiency",
    "description": "How effectively the sales training team tracks the progress of sales reps through training programs.",
    "formula": "(Total Number of Completed Training Assignments / Total Number of Assigned Training Tasks) * 100",
    "calculation_formula": "(Total Number of Completed Training Assignments / Total Number of Assigned Training Tasks) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Progress Tracking Efficiency to be added.",
    "trend_analysis": """

    * Increasing training progress tracking efficiency may indicate a more structured and effective training program.
    * Decreasing efficiency could signal a lack of engagement or understanding among sales reps, or a need for better tracking tools.
    
    """,
    "diagnostic_questions": """

    * Are there specific training modules or topics where sales reps tend to progress more slowly?
    * How does the progress tracking efficiency compare with the actual performance improvement of sales reps post-training?
    
    """,
    "actionable_tips": """

    * Implement automated tracking systems to reduce manual data entry and improve accuracy.
    * Regularly review and update training materials to ensure relevance and engagement.
    * Provide incentives for sales reps to complete training modules in a timely manner.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average time taken to complete each training module over time.
    * Comparison bar charts displaying the progress tracking efficiency for different sales teams or regions.
    
    """,
    "risk_warnings": """

    * Low progress tracking efficiency may lead to gaps in knowledge and skills among sales reps, impacting overall performance.
    * Inaccurate tracking could result in misinformed decisions regarding training program improvements.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) with built-in progress tracking and reporting features.
    * CRM platforms that integrate with training progress tracking to provide a comprehensive view of sales rep performance.
    
    """,
    "integration_points": """

    * Integrate progress tracking data with performance management systems to align training progress with sales targets and goals.
    * Link progress tracking with coaching and mentoring programs to provide personalized support based on individual training needs.
    
    """,
    "change_impact_analysis": """

    * Improving training progress tracking efficiency can lead to better-prepared sales reps, potentially increasing sales performance and customer satisfaction.
    * However, overly stringent tracking methods may lead to disengagement and resistance among sales reps, impacting overall morale and retention.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:25.135535"},
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
                        512,
                        522,
                        515,
                        511,
                        519,
                        526,
                        496,
                        511,
                        507,
                        479,
                        479,
                        507
                ],
                "unit": "count"
        },
        "current": {
                "value": 507,
                "unit": "count",
                "change": 28,
                "change_percent": 5.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 507.0,
                "min": 479,
                "max": 526,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 87.99,
                        "percentage": 17.4
                },
                {
                        "category": "Category B",
                        "value": 88.47,
                        "percentage": 17.4
                },
                {
                        "category": "Category C",
                        "value": 98.52,
                        "percentage": 19.4
                },
                {
                        "category": "Category D",
                        "value": 28.44,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 203.58,
                        "percentage": 40.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.135535",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Training Progress Tracking Efficiency"
        }
    },
}
