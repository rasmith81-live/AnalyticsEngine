"""
Sales Team Attrition Rate

The rate at which sales personnel leave the sales team over a given period.
"""

SALES_TEAM_ATTRITION_RATE = {
    "code": "SALES_TEAM_ATTRITION_RATE",
    "name": "Sales Team Attrition Rate",
    "description": "The rate at which sales personnel leave the sales team over a given period.",
    "formula": "(Number of Sales Staff Departures / Average Number of Sales Staff) * 100",
    "calculation_formula": "(Number of Sales Staff Departures / Average Number of Sales Staff) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Team Attrition Rate to be added.",
    "trend_analysis": """



    * An increasing sales team attrition rate may indicate issues with employee satisfaction, training, or management.
    * A decreasing rate could signal successful retention strategies, improved hiring practices, or a shift in market conditions.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the primary reasons for sales team members leaving the organization?
    * Are there patterns or commonalities among the departing sales personnel?
    * How does our sales team attrition rate compare with industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Invest in ongoing training and development programs to enhance skills and career growth opportunities for sales team members.
    * Regularly review and update compensation and benefits packages to remain competitive and attractive to top sales talent.
    * Implement mentorship or coaching programs to provide support and guidance for new and existing sales team members.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of sales team attrition rate over time.
    * Bar graphs comparing attrition rates across different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * High sales team attrition can lead to a loss of institutional knowledge and disrupt team dynamics.
    * Consistently high attrition rates may indicate systemic issues within the organization that could affect overall performance and morale.
    
    
    
    """,
    "tracking_tools": """



    * Employee engagement and feedback platforms to gather insights and address concerns proactively.
    * HR management systems to track turnover, identify trends, and implement targeted retention strategies.
    
    
    
    """,
    "integration_points": """



    * Integrate sales team attrition data with performance reviews and feedback to identify potential areas for improvement.
    * Link attrition rates with sales productivity metrics to understand the impact of turnover on overall sales performance.
    
    
    
    """,
    "change_impact_analysis": """



    * High turnover can disrupt team dynamics and affect overall sales productivity and customer relationships.
    * Reducing attrition can lead to a more stable and motivated sales team, potentially improving customer satisfaction and revenue generation.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_DEVELOPMENT", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.505319"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT", "SALES_STRATEGY"],
    "module_code": "INSIDE_SALES",
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
                        60.35,
                        49.43,
                        64.51,
                        56.89,
                        46.04,
                        64.13,
                        59.82,
                        63.73,
                        53.08,
                        55.2,
                        47.32,
                        46.36
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.36,
                "unit": "%",
                "change": -0.96,
                "change_percent": -2.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 55.57,
                "min": 46.04,
                "max": 64.51,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 12.28,
                        "percentage": 26.5
                },
                {
                        "category": "Channel Sales",
                        "value": 7.69,
                        "percentage": 16.6
                },
                {
                        "category": "Online Sales",
                        "value": 7.86,
                        "percentage": 17.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.79,
                        "percentage": 8.2
                },
                {
                        "category": "Other",
                        "value": 14.74,
                        "percentage": 31.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.216930",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Team Attrition Rate"
        }
    },
}
