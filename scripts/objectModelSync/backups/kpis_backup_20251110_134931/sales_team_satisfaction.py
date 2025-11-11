"""
Sales Team Satisfaction

A metric assessing the job satisfaction levels of sales personnel, as higher satisfaction is often correlated with better performance.
"""

SALES_TEAM_SATISFACTION = {
    "code": "SALES_TEAM_SATISFACTION",
    "name": "Sales Team Satisfaction",
    "description": "A metric assessing the job satisfaction levels of sales personnel, as higher satisfaction is often correlated with better performance.",
    "formula": "Qualitative and quantitative analysis, no standard formula",
    "calculation_formula": "Qualitative and quantitative analysis, no standard formula",
    "category": "Sales Strategy",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Team Satisfaction to be added.",
    "trend_analysis": """

    * Increasing sales team satisfaction may indicate better morale and motivation, leading to improved performance and retention.
    * Decreasing satisfaction levels could signal issues with leadership, compensation, or work environment that may impact sales outcomes.
    
    """,
    "diagnostic_questions": """

    * What specific factors contribute to the satisfaction or dissatisfaction of the sales team?
    * How does the sales team satisfaction compare to industry benchmarks or historical data?
    
    """,
    "actionable_tips": """

    * Regularly solicit feedback from the sales team and take action on their concerns to improve satisfaction.
    * Provide training and development opportunities to enhance skills and confidence within the sales team.
    * Implement recognition and reward programs to acknowledge and appreciate the efforts of the sales team.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of sales team satisfaction over time.
    * Comparison bar charts displaying satisfaction levels across different sales teams or regions.
    
    """,
    "risk_warnings": """

    * Low sales team satisfaction can lead to increased turnover and recruitment costs.
    * Unaddressed dissatisfaction may result in decreased productivity and ultimately, lower sales performance.
    
    """,
    "tracking_tools": """

    * Employee engagement platforms like Officevibe or TINYpulse for gathering and analyzing feedback from the sales team.
    * Performance management software to track individual and team satisfaction levels and identify areas for improvement.
    
    """,
    "integration_points": """

    * Integrate sales team satisfaction data with performance management systems to understand the impact on sales results.
    * Link satisfaction metrics with HR systems to align improvement initiatives with broader organizational goals.
    
    """,
    "change_impact_analysis": """

    * Improving sales team satisfaction can lead to higher customer satisfaction and loyalty, positively impacting overall business performance.
    * However, a focus solely on satisfaction without considering sales outcomes may lead to decreased efficiency and effectiveness.
    
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Competitive Analysis", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.648543"},
    "required_objects": [],
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
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
                        493.12,
                        469.31,
                        477.99,
                        504.63,
                        469.31,
                        484.23,
                        532.23,
                        503.97,
                        457.94,
                        592.03,
                        485.31,
                        463.7
                ],
                "unit": "units"
        },
        "current": {
                "value": 463.7,
                "unit": "units",
                "change": -21.61,
                "change_percent": -4.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 494.48,
                "min": 457.94,
                "max": 592.03,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 90.59,
                        "percentage": 19.5
                },
                {
                        "category": "Category B",
                        "value": 91.97,
                        "percentage": 19.8
                },
                {
                        "category": "Category C",
                        "value": 64.04,
                        "percentage": 13.8
                },
                {
                        "category": "Category D",
                        "value": 52.18,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 164.92,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.648543",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Team Satisfaction"
        }
    },
}
