"""
Coaching Session Frequency

The number of coaching sessions provided to each sales rep within a given time period.
"""

COACHING_SESSION_FREQUENCY = {
    "code": "COACHING_SESSION_FREQUENCY",
    "name": "Coaching Session Frequency",
    "description": "The number of coaching sessions provided to each sales rep within a given time period.",
    "formula": "Total Number of Coaching Sessions / Specified Time Period",
    "calculation_formula": "Total Number of Coaching Sessions / Specified Time Period",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Coaching Session Frequency to be added.",
    "trend_analysis": """

    * An increasing coaching session frequency may indicate a need for more support or development for sales reps.
    * A decreasing frequency could signal improved sales performance or a lack of focus on coaching from sales management.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales reps who consistently require more coaching sessions?
    * How does the coaching session frequency correlate with sales performance and targets?
    
    """,
    "actionable_tips": """

    * Implement regular one-on-one coaching sessions to provide personalized support for each sales rep.
    * Utilize coaching tools and resources to make sessions more effective and impactful.
    * Encourage a culture of continuous learning and improvement within the sales team.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of coaching session frequency over time for each sales rep.
    * Comparison bar charts to visualize the variance in coaching session frequency among different sales reps.
    
    """,
    "risk_warnings": """

    * Low coaching session frequency may lead to underperformance and missed sales opportunities.
    * High coaching session frequency without improvement in sales performance may indicate ineffective coaching methods or other underlying issues.
    
    """,
    "tracking_tools": """

    * Utilize sales coaching and training platforms such as Brainshark or Allego to track and analyze coaching session frequency.
    * Implement customer relationship management (CRM) systems to integrate coaching data with sales performance metrics.
    
    """,
    "integration_points": """

    * Integrate coaching session frequency data with performance reviews and goal setting processes to align coaching efforts with individual sales targets.
    * Link coaching session frequency with sales forecasting and pipeline management to identify areas for improvement and development.
    
    """,
    "change_impact_analysis": """

    * Increasing coaching session frequency may lead to improved sales performance and customer satisfaction, but could also require additional time and resources.
    * Conversely, a decrease in coaching session frequency may result in missed opportunities for development and growth within the sales team.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Deal", "Lead", "Opportunity", "Partner Training", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.126490"},
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
                        230,
                        212,
                        201,
                        225,
                        231,
                        194,
                        201,
                        193,
                        208,
                        214,
                        185,
                        191
                ],
                "unit": "count"
        },
        "current": {
                "value": 191,
                "unit": "count",
                "change": 6,
                "change_percent": 3.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 207.08,
                "min": 185,
                "max": 231,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 56.8,
                        "percentage": 29.7
                },
                {
                        "category": "Category B",
                        "value": 41.49,
                        "percentage": 21.7
                },
                {
                        "category": "Category C",
                        "value": 14.7,
                        "percentage": 7.7
                },
                {
                        "category": "Category D",
                        "value": 22.66,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 55.35,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.126490",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Coaching Session Frequency"
        }
    },
}
