"""
Mentorship Program Effectiveness

A measure of the impact of mentorship programs on new sales reps' performance and development.
"""

MENTORSHIP_PROGRAM_EFFECTIVENESS = {
    "code": "MENTORSHIP_PROGRAM_EFFECTIVENESS",
    "name": "Mentorship Program Effectiveness",
    "description": "A measure of the impact of mentorship programs on new sales reps' performance and development.",
    "formula": "Performance Metrics Pre and Post-Mentorship / Number of Mentees",
    "calculation_formula": "Performance Metrics Pre and Post-Mentorship / Number of Mentees",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Mentorship Program Effectiveness to be added.",
    "trend_analysis": """



    * An increasing mentorship program effectiveness may indicate better onboarding processes and more impactful mentorship relationships.
    * A decreasing effectiveness could signal a need for reevaluation of the program structure or mentorship training.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas where new sales reps consistently struggle despite mentorship?
    * How does the effectiveness of our mentorship program compare to industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional training for mentors to improve their coaching and leadership skills.
    * Regularly gather feedback from new sales reps to identify areas for improvement in the mentorship program.
    * Pair new sales reps with mentors who have a track record of successful coaching and development.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of new sales reps' performance over time in relation to the mentorship program effectiveness.
    * Comparison bar charts displaying the performance of new sales reps who have been through the mentorship program versus those who haven't.
    
    
    
    """,
    "risk_warnings": """



    * Low mentorship program effectiveness may result in higher turnover among new sales reps.
    * Ineffective mentorship can lead to missed sales opportunities and slower ramp-up times for new reps.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with performance tracking capabilities to monitor the impact of mentorship on new sales reps' development.
    * Learning management platforms to provide structured training and resources for mentors and new sales reps.
    
    
    
    """,
    "integration_points": """



    * Integrate mentorship program effectiveness data with performance reviews and sales metrics to understand the correlation between mentorship and results.
    * Link mentorship program data with HR systems to track the long-term success and retention of new sales reps.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving mentorship program effectiveness can lead to higher sales performance and increased job satisfaction among new sales reps.
    * Conversely, a decline in effectiveness may result in a negative impact on overall sales team morale and productivity.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Advocacy Program", "Customer Success Manager", "Loyalty Program", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.055300"},
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
                        445,
                        461,
                        459,
                        435,
                        465,
                        424,
                        440,
                        460,
                        458,
                        460,
                        441,
                        445
                ],
                "unit": "count"
        },
        "current": {
                "value": 445,
                "unit": "count",
                "change": 4,
                "change_percent": 0.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 449.42,
                "min": 424,
                "max": 465,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 152.58,
                        "percentage": 34.3
                },
                {
                        "category": "Segment B",
                        "value": 59.65,
                        "percentage": 13.4
                },
                {
                        "category": "Segment C",
                        "value": 38.66,
                        "percentage": 8.7
                },
                {
                        "category": "Segment D",
                        "value": 22.27,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 171.84,
                        "percentage": 38.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.210586",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Mentorship Program Effectiveness"
        }
    },
}
