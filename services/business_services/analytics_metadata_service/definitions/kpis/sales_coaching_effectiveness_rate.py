"""
Sales Coaching Effectiveness Rate

The effectiveness of sales coaching programs provided by the sales enablement team in terms of improving sales skills and performance.
"""

SALES_COACHING_EFFECTIVENESS_RATE = {
    "code": "SALES_COACHING_EFFECTIVENESS_RATE",
    "name": "Sales Coaching Effectiveness Rate",
    "description": "The effectiveness of sales coaching programs provided by the sales enablement team in terms of improving sales skills and performance.",
    "formula": "(Post-Coaching Sales Performance - Pre-Coaching Sales Performance) / Pre-Coaching Sales Performance",
    "calculation_formula": "(Post-Coaching Sales Performance - Pre-Coaching Sales Performance) / Pre-Coaching Sales Performance",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Coaching Effectiveness Rate to be added.",
    "trend_analysis": """



    * An increasing sales coaching effectiveness rate may indicate that the sales team is adopting and implementing the coaching feedback effectively.
    * A decreasing rate could signal a need for reevaluation of the coaching programs or a lack of engagement from the sales team.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales skills or areas where the coaching seems to have the most impact?
    * How do the sales coaching effectiveness rates align with the actual sales performance metrics?
    
    
    
    """,
    "actionable_tips": """



    * Regularly gather feedback from the sales team to understand the effectiveness of the coaching programs.
    * Customize coaching programs to address specific skill gaps or challenges identified in the sales team.
    * Provide ongoing support and reinforcement of the coaching to ensure long-term impact on sales performance.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of sales coaching effectiveness rates over time.
    * Comparison bar charts to visualize the impact of coaching on different sales skills or performance metrics.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low sales coaching effectiveness rate may lead to stagnant or declining sales performance.
    * High variability in the coaching effectiveness rate may indicate inconsistency in the coaching programs or their impact.
    
    
    
    """,
    "tracking_tools": """



    * Utilize sales performance management software to track the impact of coaching on individual sales team members.
    * Implement video coaching platforms to provide remote and personalized coaching to the sales team.
    
    
    
    """,
    "integration_points": """



    * Integrate sales coaching effectiveness data with individual sales performance metrics to understand the direct impact of coaching on results.
    * Link coaching effectiveness with employee development and training programs to create a holistic approach to skill improvement.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving sales coaching effectiveness can lead to increased sales productivity and revenue generation.
    * However, a lack of improvement in coaching effectiveness may result in missed sales opportunities and decreased team morale.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Enablement Feedback", "Enablement Platform", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.388434"},
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
                        65.98,
                        63.64,
                        83.24,
                        74.02,
                        66.42,
                        68.76,
                        74.43,
                        66.27,
                        76.54,
                        75.05,
                        73.79,
                        79.98
                ],
                "unit": "%"
        },
        "current": {
                "value": 79.98,
                "unit": "%",
                "change": 6.19,
                "change_percent": 8.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 72.34,
                "min": 63.64,
                "max": 83.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 22.51,
                        "percentage": 28.1
                },
                {
                        "category": "Channel Sales",
                        "value": 13.74,
                        "percentage": 17.2
                },
                {
                        "category": "Online Sales",
                        "value": 9.01,
                        "percentage": 11.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7.62,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 27.1,
                        "percentage": 33.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.899898",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Coaching Effectiveness Rate"
        }
    },
}
