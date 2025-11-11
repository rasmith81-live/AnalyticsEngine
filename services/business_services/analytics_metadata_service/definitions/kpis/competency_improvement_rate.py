"""
Competency Improvement Rate

The rate at which sales reps improve their competencies and skills through training.
"""

COMPETENCY_IMPROVEMENT_RATE = {
    "code": "COMPETENCY_IMPROVEMENT_RATE",
    "name": "Competency Improvement Rate",
    "description": "The rate at which sales reps improve their competencies and skills through training.",
    "formula": "(Number of Competencies Improved Post-Training / Total Number of Competencies Targeted) * 100",
    "calculation_formula": "(Number of Competencies Improved Post-Training / Total Number of Competencies Targeted) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Competency Improvement Rate to be added.",
    "trend_analysis": """



    * Increasing competency improvement rate may indicate the effectiveness of training programs and coaching initiatives.
    * A decreasing rate could signal a need for reevaluation of training methods or a lack of engagement from sales reps.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific competencies or skills that sales reps struggle to improve?
    * How does the competency improvement rate align with the implementation of new training initiatives or coaching strategies?
    
    
    
    """,
    "actionable_tips": """



    * Provide personalized coaching and training plans tailored to individual sales reps' needs.
    * Implement regular feedback mechanisms to track progress and adjust training programs accordingly.
    * Encourage a culture of continuous learning and skill development within the sales team.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of competency improvement rate over time.
    * Comparison charts to visualize the competency improvement rate across different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * A stagnant or declining competency improvement rate may lead to decreased sales performance and missed opportunities.
    * An overly rapid improvement rate could indicate a lack of challenge or insufficient training depth.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track and manage individual sales reps' training progress.
    * Coaching and feedback platforms to facilitate ongoing communication between sales managers and reps.
    
    
    
    """,
    "integration_points": """



    * Integrate competency improvement data with performance management systems to correlate skill development with sales outcomes.
    * Link training and coaching programs with customer relationship management (CRM) systems to align skill development with customer needs.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving competency improvement rate can lead to increased sales effectiveness and customer satisfaction.
    * However, rapid improvement without proper reinforcement may lead to short-term gains but long-term skill degradation.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.706067"},
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
                        73.03,
                        76.49,
                        64.44,
                        62.79,
                        62.47,
                        57.72,
                        61.95,
                        58.94,
                        65.26,
                        77.03,
                        59.65,
                        68.49
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.49,
                "unit": "%",
                "change": 8.84,
                "change_percent": 14.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 65.69,
                "min": 57.72,
                "max": 77.03,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.6,
                        "percentage": 15.5
                },
                {
                        "category": "Segment B",
                        "value": 13.57,
                        "percentage": 19.8
                },
                {
                        "category": "Segment C",
                        "value": 7.9,
                        "percentage": 11.5
                },
                {
                        "category": "Segment D",
                        "value": 3.79,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 32.63,
                        "percentage": 47.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.492996",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Competency Improvement Rate"
        }
    },
}
