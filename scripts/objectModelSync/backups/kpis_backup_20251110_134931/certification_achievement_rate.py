"""
Certification Achievement Rate

The proportion of sales reps who achieve certification if applicable, through the training program.
"""

CERTIFICATION_ACHIEVEMENT_RATE = {
    "code": "CERTIFICATION_ACHIEVEMENT_RATE",
    "name": "Certification Achievement Rate",
    "description": "The proportion of sales reps who achieve certification if applicable, through the training program.",
    "formula": "(Number of Sales Reps Achieving Certification / Number of Sales Reps Enrolled in the Certification Program) * 100",
    "calculation_formula": "(Number of Sales Reps Achieving Certification / Number of Sales Reps Enrolled in the Certification Program) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Certification Achievement Rate to be added.",
    "trend_analysis": """

    * An increasing certification achievement rate may indicate the effectiveness of the training program in preparing sales reps.
    * A decreasing rate could signal a need for program adjustments or changes in the sales team composition.
    
    """,
    "diagnostic_questions": """

    * Are there specific areas of the training program where sales reps struggle to achieve certification?
    * How does the certification achievement rate compare with industry benchmarks or with different cohorts of sales reps?
    
    """,
    "actionable_tips": """

    * Provide additional support and resources for sales reps who are struggling to achieve certification.
    * Regularly review and update the training program to ensure it aligns with the evolving needs and challenges of the sales team.
    * Implement mentorship or coaching programs to help sales reps prepare for certification.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the certification achievement rate over time.
    * Comparison bar charts to visualize the differences in certification achievement among different groups of sales reps.
    
    """,
    "risk_warnings": """

    * A consistently low certification achievement rate may indicate a need for a more comprehensive review of the training program.
    * High variability in certification achievement rates among different sales reps may point to inconsistencies in the training or coaching process.
    
    """,
    "tracking_tools": """

    * Learning management systems (LMS) to track and manage sales reps' progress in the training program.
    * Coaching and feedback tools to provide personalized support for sales reps aiming for certification.
    
    """,
    "integration_points": """

    * Integrate certification achievement data with performance management systems to identify correlations between certification and sales success.
    * Link certification achievement with individual development plans to ensure ongoing improvement and career growth for sales reps.
    
    """,
    "change_impact_analysis": """

    * Improving the certification achievement rate can lead to a more skilled and knowledgeable sales force, potentially increasing overall sales performance.
    * Conversely, a declining certification achievement rate may lead to decreased confidence and motivation among the sales team.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Certification", "Customer Advocacy Program", "Loyalty Program", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.081836"},
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
                        78.31,
                        76.5,
                        86.18,
                        78.76,
                        68.87,
                        72.19,
                        77.77,
                        75.31,
                        85.49,
                        71.17,
                        85.7,
                        67.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.89,
                "unit": "%",
                "change": -17.81,
                "change_percent": -20.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 77.01,
                "min": 67.89,
                "max": 86.18,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.57,
                        "percentage": 18.5
                },
                {
                        "category": "Category B",
                        "value": 17.96,
                        "percentage": 26.5
                },
                {
                        "category": "Category C",
                        "value": 6.64,
                        "percentage": 9.8
                },
                {
                        "category": "Category D",
                        "value": 8.31,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 22.41,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.081836",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Certification Achievement Rate"
        }
    },
}
