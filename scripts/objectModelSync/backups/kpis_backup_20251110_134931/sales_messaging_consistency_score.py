"""
Sales Messaging Consistency Score

A measure of how consistent the sales messaging is across different sales representatives and content.
"""

SALES_MESSAGING_CONSISTENCY_SCORE = {
    "code": "SALES_MESSAGING_CONSISTENCY_SCORE",
    "name": "Sales Messaging Consistency Score",
    "description": "A measure of how consistent the sales messaging is across different sales representatives and content.",
    "formula": "Average Score on Consistency Assessments",
    "calculation_formula": "Average Score on Consistency Assessments",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Messaging Consistency Score to be added.",
    "trend_analysis": """

    * Consistent messaging may initially show a positive trend, but if it remains stagnant, it could indicate a lack of innovation or adaptation to changing market needs.
    * A decreasing consistency score may suggest a need for better training or clearer communication of sales messaging standards.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales reps or regions that consistently deviate from the standard messaging?
    * How do customer feedback and conversion rates correlate with messaging consistency?
    
    """,
    "actionable_tips": """

    * Regularly review and update sales messaging guidelines to reflect market changes and customer feedback.
    * Provide ongoing training and coaching to ensure all sales reps understand and can effectively deliver the approved messaging.
    * Utilize sales enablement platforms to centralize and distribute approved messaging content to all reps.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the consistency score over time for each sales rep or region.
    * Comparison charts to visually represent the variance in messaging consistency across different content types or customer segments.
    
    """,
    "risk_warnings": """

    * Inconsistent messaging can lead to confusion and mistrust among potential customers.
    * Failure to address messaging inconsistencies may result in missed sales opportunities and decreased revenue.
    
    """,
    "tracking_tools": """

    * Sales enablement platforms with content management and tracking capabilities, such as Highspot or Seismic.
    * CRM systems that allow for tracking and analysis of customer interactions and messaging effectiveness.
    
    """,
    "integration_points": """

    * Integrate messaging consistency data with performance metrics to assess the impact on sales results.
    * Link messaging consistency with customer feedback systems to understand the correlation between messaging and customer satisfaction.
    
    """,
    "change_impact_analysis": """

    * Improving messaging consistency can lead to increased customer trust and loyalty, ultimately impacting long-term revenue and market share.
    * However, overly rigid messaging standards may stifle creativity and personalization, potentially affecting customer engagement.
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.428983"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        61.1,
                        61.5,
                        60.9,
                        67.4,
                        64.5,
                        68.2,
                        62.7,
                        60.4,
                        68.5,
                        70.2,
                        58.2,
                        69.2
                ],
                "unit": "score"
        },
        "current": {
                "value": 69.2,
                "unit": "score",
                "change": 11.0,
                "change_percent": 18.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 64.4,
                "min": 58.2,
                "max": 70.2,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.96,
                        "percentage": 26.0
                },
                {
                        "category": "Category B",
                        "value": 10.63,
                        "percentage": 15.4
                },
                {
                        "category": "Category C",
                        "value": 7.65,
                        "percentage": 11.1
                },
                {
                        "category": "Category D",
                        "value": 3.95,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 29.01,
                        "percentage": 41.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.428983",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Messaging Consistency Score"
        }
    },
}
