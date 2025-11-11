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
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.439149"},
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
                        86.3,
                        74.9,
                        77.7,
                        78.3,
                        80.6,
                        83.1,
                        85.8,
                        76.5,
                        79.4,
                        78.7,
                        73.9,
                        74.7
                ],
                "unit": "score"
        },
        "current": {
                "value": 74.7,
                "unit": "score",
                "change": 0.8,
                "change_percent": 1.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 79.16,
                "min": 73.9,
                "max": 86.3,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 23.87,
                        "percentage": 32.0
                },
                {
                        "category": "Channel Sales",
                        "value": 17.6,
                        "percentage": 23.6
                },
                {
                        "category": "Online Sales",
                        "value": 10.32,
                        "percentage": 13.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.16,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 18.75,
                        "percentage": 25.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.030128",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Messaging Consistency Score"
        }
    },
}
