"""
Training Hours per Rep

The total number of hours each sales representative spends in training.
"""

TRAINING_HOURS_PER_REP = {
    "code": "TRAINING_HOURS_PER_REP",
    "name": "Training Hours per Rep",
    "description": "The total number of hours each sales representative spends in training.",
    "formula": "Total Training Hours Completed / Number of Sales Reps",
    "calculation_formula": "Total Training Hours Completed / Number of Sales Reps",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Hours per Rep to be added.",
    "trend_analysis": """


    * Training hours per rep may increase over time as new products, services, or sales techniques are introduced.
    * A decrease in training hours could indicate a lack of investment in ongoing development or a need for more efficient training methods.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific areas or skills that sales reps consistently require more training in?
    * How do our training hours per rep compare with industry standards or benchmarks?
    
    
    """,
    "actionable_tips": """


    * Implement regular skills assessments to identify areas where reps need additional training.
    * Utilize e-learning platforms to provide flexible and ongoing training opportunities.
    * Encourage mentorship and peer-to-peer learning to supplement formal training programs.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing training hours per rep over time to identify trends and patterns.
    * Bar graphs comparing training hours by department, region, or product line to pinpoint areas needing more focus.
    
    
    """,
    "risk_warnings": """


    * Low training hours per rep may lead to decreased sales effectiveness and missed opportunities.
    * High training hours without corresponding improvements in performance may indicate ineffective training methods or lack of retention.
    
    
    """,
    "tracking_tools": """


    * Learning management systems (LMS) to track and manage training programs and progress.
    * Video conferencing and virtual training tools for remote or distributed sales teams.
    
    
    """,
    "integration_points": """


    * Integrate training hours data with sales performance metrics to assess the impact of training on results.
    * Link training hours with employee development plans and performance reviews for a holistic approach to talent management.
    
    
    """,
    "change_impact_analysis": """


    * Increasing training hours may initially impact productivity but can lead to long-term improvements in sales performance.
    * Decreasing training hours may result in short-term cost savings but could lead to decreased competitiveness and employee satisfaction.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.743428"},
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
                        103,
                        119,
                        106,
                        81,
                        117,
                        119,
                        125,
                        127,
                        93,
                        86,
                        96,
                        78
                ],
                "unit": "count"
        },
        "current": {
                "value": 78,
                "unit": "count",
                "change": -18,
                "change_percent": -18.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 104.17,
                "min": 78,
                "max": 127,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 21.36,
                        "percentage": 27.4
                },
                {
                        "category": "Category B",
                        "value": 9.8,
                        "percentage": 12.6
                },
                {
                        "category": "Category C",
                        "value": 7.67,
                        "percentage": 9.8
                },
                {
                        "category": "Category D",
                        "value": 10.39,
                        "percentage": 13.3
                },
                {
                        "category": "Other",
                        "value": 28.78,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.119429",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Training Hours per Rep"
        }
    },
}
