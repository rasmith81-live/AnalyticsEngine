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
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Lead", "Opportunity", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.721112"},
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
                        75.57,
                        73.69,
                        76.57,
                        83.82,
                        77.1,
                        71.89,
                        83.04,
                        66.29,
                        75.37,
                        66.04,
                        79.97,
                        77.93
                ],
                "unit": "%"
        },
        "current": {
                "value": 77.93,
                "unit": "%",
                "change": -2.04,
                "change_percent": -2.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 75.61,
                "min": 66.04,
                "max": 83.82,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 19.07,
                        "percentage": 24.5
                },
                {
                        "category": "Channel Sales",
                        "value": 16.42,
                        "percentage": 21.1
                },
                {
                        "category": "Online Sales",
                        "value": 13.4,
                        "percentage": 17.2
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.81,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 24.23,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.518769",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Conversion Rate from Training to Sales"
        }
    },
}
