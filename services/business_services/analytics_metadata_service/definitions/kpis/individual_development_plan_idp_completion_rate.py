"""
Individual Development Plan (IDP) Completion Rate

The percentage of sales reps who complete their IDPs within the planned timeframe.
"""

INDIVIDUAL_DEVELOPMENT_PLAN_IDP_COMPLETION_RATE = {
    "code": "INDIVIDUAL_DEVELOPMENT_PLAN_IDP_COMPLETION_RATE",
    "name": "Individual Development Plan (IDP) Completion Rate",
    "description": "The percentage of sales reps who complete their IDPs within the planned timeframe.",
    "formula": "(Number of IDPs Completed / Total Number of IDPs Assigned) * 100",
    "calculation_formula": "(Number of IDPs Completed / Total Number of IDPs Assigned) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Individual Development Plan (IDP) Completion Rate to be added.",
    "trend_analysis": """



    * An increasing IDP completion rate may indicate a more engaged and proactive sales team.
    * A decreasing rate could signal disengagement, lack of motivation, or ineffective coaching and training.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common reasons why sales reps are not completing their IDPs on time?
    * How does the IDP completion rate correlate with sales performance and overall job satisfaction?
    
    
    
    """,
    "actionable_tips": """



    * Provide clear expectations and guidance for creating and completing IDPs.
    * Offer regular coaching and support to help sales reps identify and achieve their development goals.
    * Incorporate IDP progress into performance evaluations and recognition programs.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the IDP completion rate over time for individual sales reps and the team as a whole.
    * Comparison bar graphs to visualize completion rates across different sales territories or product lines.
    
    
    
    """,
    "risk_warnings": """



    * A low IDP completion rate may lead to decreased individual and team performance, as well as higher turnover.
    * Consistently high completion rates without corresponding improvements in sales performance could indicate a lack of meaningful development in the IDPs.
    
    
    
    """,
    "tracking_tools": """



    * Performance management software with IDP tracking and reporting capabilities.
    * Coaching and mentoring platforms to facilitate ongoing support and feedback for sales reps.
    
    
    
    """,
    "integration_points": """



    * Integrate IDP completion data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link IDP progress with learning and development systems to ensure alignment with broader training initiatives.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the IDP completion rate can lead to more skilled and motivated sales reps, potentially driving higher revenue and customer satisfaction.
    * However, focusing solely on completion rates without considering the quality and relevance of the IDPs may result in superficial development and limited impact on sales outcomes.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Plan", "Deal", "Lead", "Opportunity", "Partner Training", "Quota Plan", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.973139"},
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
                        66.96,
                        66.24,
                        65.55,
                        71.42,
                        77.1,
                        70.36,
                        66.71,
                        67.35,
                        67.6,
                        73.22,
                        67.29,
                        68.93
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.93,
                "unit": "%",
                "change": 1.64,
                "change_percent": 2.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 69.06,
                "min": 65.55,
                "max": 77.1,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.51,
                        "percentage": 15.2
                },
                {
                        "category": "Segment B",
                        "value": 15.65,
                        "percentage": 22.7
                },
                {
                        "category": "Segment C",
                        "value": 12.88,
                        "percentage": 18.7
                },
                {
                        "category": "Segment D",
                        "value": 6.13,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 23.76,
                        "percentage": 34.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.032519",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Individual Development Plan (IDP) Completion Rate"
        }
    },
}
