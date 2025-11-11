"""
Conversion Rate from Training to Sales

The percentage of sales reps who complete training and coaching and go on to achieve sales targets. A higher conversion rate indicates effective training and coaching.
"""

CONVERSION_RATE_FROM_TRAINING_TO_SALES = {
    "code": "CONVERSION_RATE_FROM_TRAINING_TO_SALES",
    "name": "Conversion Rate from Training to Sales",
    "description": "The percentage of sales reps who complete training and coaching and go on to achieve sales targets. A higher conversion rate indicates effective training and coaching.",
    "formula": "(Number of Sales Made by Trained Reps / Number of Trained Reps) * 100",
    "calculation_formula": "(Number of Sales Made by Trained Reps / Number of Trained Reps) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Conversion Rate from Training to Sales to be added.",
    "trend_analysis": """

    * A rising conversion rate may indicate the effectiveness of new training and coaching methods.
    * A decreasing rate could signal a need for reevaluation of the training content or coaching techniques.
    
    """,
    "diagnostic_questions": """

    * Are there specific areas of the training program where sales reps tend to struggle?
    * How does the conversion rate compare with industry benchmarks or with the performance of top-performing sales reps?
    
    """,
    "actionable_tips": """

    * Provide personalized coaching and mentoring for sales reps who are struggling to meet targets.
    * Regularly update training materials to ensure they reflect the latest sales techniques and product knowledge.
    * Implement a peer-to-peer learning program where successful sales reps can share their strategies with others.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of conversion rates over time.
    * Comparison bar charts to visualize the performance of different sales reps or teams.
    
    """,
    "risk_warnings": """

    * A declining conversion rate may lead to missed sales targets and revenue loss.
    * Consistently low conversion rates could indicate a need for a complete overhaul of the training and coaching program.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track the performance of individual sales reps and identify areas for improvement.
    * Learning management systems (LMS) to deliver and track the completion of training modules.
    
    """,
    "integration_points": """

    * Integrate with performance management systems to align training and coaching efforts with individual sales goals.
    * Link with sales forecasting tools to understand the impact of training and coaching on future sales projections.
    
    """,
    "change_impact_analysis": """

    * Improving the conversion rate can lead to increased revenue and higher overall sales team performance.
    * Conversely, a declining conversion rate may indicate a need for a reevaluation of the entire sales management process.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Lead", "Opportunity", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.152207"},
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
                        51.74,
                        59.75,
                        49.54,
                        57.47,
                        52.76,
                        50.9,
                        59.23,
                        50.81,
                        50.73,
                        57.48,
                        57.52,
                        51.81
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.81,
                "unit": "%",
                "change": -5.71,
                "change_percent": -9.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 54.15,
                "min": 49.54,
                "max": 59.75,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.98,
                        "percentage": 15.4
                },
                {
                        "category": "Category B",
                        "value": 7.63,
                        "percentage": 14.7
                },
                {
                        "category": "Category C",
                        "value": 11.85,
                        "percentage": 22.9
                },
                {
                        "category": "Category D",
                        "value": 2.95,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 21.4,
                        "percentage": 41.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.152207",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Conversion Rate from Training to Sales"
        }
    },
}
