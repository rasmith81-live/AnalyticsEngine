"""
Sales Rep Retention Rate

The percentage of sales reps who remain with the company over a specific period. A higher retention rate indicates effective training and coaching.
"""

SALES_REP_RETENTION_RATE = {
    "code": "SALES_REP_RETENTION_RATE",
    "name": "Sales Rep Retention Rate",
    "description": "The percentage of sales reps who remain with the company over a specific period. A higher retention rate indicates effective training and coaching.",
    "formula": "(Number of Sales Reps Retained / Total Number of Sales Reps at Start of Period) * 100",
    "calculation_formula": "(Number of Sales Reps Retained / Total Number of Sales Reps at Start of Period) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Rep Retention Rate to be added.",
    "trend_analysis": """


    * A rising sales rep retention rate may indicate effective training and coaching programs that are keeping employees engaged and satisfied.
    * A decreasing rate could signal issues with the training and coaching programs, leading to higher turnover and potential performance gaps.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific areas of the training and coaching programs that receive consistently positive feedback from sales reps?
    * How does our sales rep retention rate compare with industry benchmarks or turnover rates in similar organizations?
    
    
    """,
    "actionable_tips": """


    * Regularly solicit feedback from sales reps to identify areas for improvement in the training and coaching programs.
    * Provide ongoing professional development opportunities to keep sales reps engaged and motivated.
    * Implement mentorship programs to support the growth and success of new sales reps.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of sales rep retention rate over time.
    * Comparison bar charts displaying retention rates across different sales teams or regions.
    
    
    """,
    "risk_warnings": """


    * Low sales rep retention rates can lead to increased recruitment and training costs, as well as potential disruptions in sales team performance.
    * High turnover may also indicate dissatisfaction with the company culture or leadership, which can impact overall employee morale.
    
    
    """,
    "tracking_tools": """


    * Employee engagement and feedback platforms to gather insights from sales reps about their training and coaching experiences.
    * Performance management systems to track the progress and development of sales reps over time.
    
    
    """,
    "integration_points": """


    * Integrate sales rep retention rate data with HR systems to identify correlations between retention and factors such as compensation, benefits, and career development opportunities.
    * Link retention rate with sales performance metrics to understand the impact of training and coaching on sales outcomes.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales rep retention can lead to a more experienced and knowledgeable sales force, potentially resulting in increased sales and customer satisfaction.
    * Conversely, high turnover can disrupt team dynamics and impact overall sales team performance and morale.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.486529"},
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
                        33.35,
                        38.05,
                        43.64,
                        32.72,
                        49.67,
                        35.43,
                        44.08,
                        49.79,
                        48.11,
                        46.96,
                        43.7,
                        43.76
                ],
                "unit": "%"
        },
        "current": {
                "value": 43.76,
                "unit": "%",
                "change": 0.06,
                "change_percent": 0.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 42.44,
                "min": 32.72,
                "max": 49.79,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.0,
                        "percentage": 25.1
                },
                {
                        "category": "Category B",
                        "value": 8.31,
                        "percentage": 19.0
                },
                {
                        "category": "Category C",
                        "value": 8.13,
                        "percentage": 18.6
                },
                {
                        "category": "Category D",
                        "value": 4.86,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 11.46,
                        "percentage": 26.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.579485",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Rep Retention Rate"
        }
    },
}
