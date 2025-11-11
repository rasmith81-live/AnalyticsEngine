"""
Coaching Impact Score

A metric that quantifies the impact of individual coaching sessions on sales performance.
"""

COACHING_IMPACT_SCORE = {
    "code": "COACHING_IMPACT_SCORE",
    "name": "Coaching Impact Score",
    "description": "A metric that quantifies the impact of individual coaching sessions on sales performance.",
    "formula": "Sum of Performance Improvement Measures Post-Coaching / Number of Coaching Sessions",
    "calculation_formula": "Sum of Performance Improvement Measures Post-Coaching / Number of Coaching Sessions",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Coaching Impact Score to be added.",
    "trend_analysis": """

    * An increasing coaching impact score may indicate more effective coaching methods or a higher quality of coaching interactions.
    * A decreasing score could signal a decline in the effectiveness of coaching sessions or a lack of follow-through on coaching recommendations.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales metrics that have shown improvement following coaching sessions?
    * How do sales representatives perceive the value and impact of the coaching they receive?
    
    """,
    "actionable_tips": """

    * Implement regular feedback loops to assess the impact of coaching on sales performance.
    * Provide additional training for sales managers to enhance their coaching skills and techniques.
    * Encourage sales managers to set clear, measurable goals for coaching sessions and track progress over time.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of coaching impact scores over time.
    * Comparison charts displaying the impact scores of different sales teams or individual sales managers.
    
    """,
    "risk_warnings": """

    * A consistently low coaching impact score may indicate a need for a reevaluation of coaching strategies and approaches.
    * Highly variable impact scores across different sales teams may point to inconsistencies in coaching practices that need to be addressed.
    
    """,
    "tracking_tools": """

    * Utilize sales performance management software that includes coaching impact score tracking and analysis features.
    * Implement customer relationship management (CRM) systems that can provide insights into the correlation between coaching and sales results.
    
    """,
    "integration_points": """

    * Integrate coaching impact score data with sales performance evaluations to gain a comprehensive view of individual and team effectiveness.
    * Link coaching impact scores with employee development plans to align coaching efforts with career growth opportunities.
    
    """,
    "change_impact_analysis": """

    * Improving coaching impact scores can lead to increased sales productivity and revenue generation.
    * Conversely, a decline in coaching impact may result in missed sales opportunities and decreased motivation among sales teams.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.122246"},
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
                        443,
                        413,
                        413,
                        430,
                        444,
                        430,
                        427,
                        446,
                        446,
                        441,
                        430,
                        422
                ],
                "unit": "count"
        },
        "current": {
                "value": 422,
                "unit": "count",
                "change": -8,
                "change_percent": -1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 432.08,
                "min": 413,
                "max": 446,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 134.53,
                        "percentage": 31.9
                },
                {
                        "category": "Category B",
                        "value": 54.68,
                        "percentage": 13.0
                },
                {
                        "category": "Category C",
                        "value": 40.6,
                        "percentage": 9.6
                },
                {
                        "category": "Category D",
                        "value": 19.51,
                        "percentage": 4.6
                },
                {
                        "category": "Other",
                        "value": 172.68,
                        "percentage": 40.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.122246",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Coaching Impact Score"
        }
    },
}
