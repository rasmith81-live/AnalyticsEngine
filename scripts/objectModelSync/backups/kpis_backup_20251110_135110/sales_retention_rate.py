"""
Sales Retention Rate

The percentage of sales representatives who remain with the company over a given period, indicating the impact of sales enablement on job satisfaction.
"""

SALES_RETENTION_RATE = {
    "code": "SALES_RETENTION_RATE",
    "name": "Sales Retention Rate",
    "description": "The percentage of sales representatives who remain with the company over a given period, indicating the impact of sales enablement on job satisfaction.",
    "formula": "(Number of Sales Reps Remaining / Total Number of Sales Reps at Start of Period) * 100",
    "calculation_formula": "(Number of Sales Reps Remaining / Total Number of Sales Reps at Start of Period) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Retention Rate to be added.",
    "trend_analysis": """


    * Increasing sales retention rate may indicate improved job satisfaction and effectiveness of sales enablement efforts.
    * Decreasing retention rate could signal dissatisfaction with sales enablement support or changes in the company culture.
    
    
    """,
    "diagnostic_questions": """


    * What specific aspects of the sales enablement program are positively impacting sales representative retention?
    * Are there any common reasons or patterns behind the departure of sales representatives?
    
    
    """,
    "actionable_tips": """


    * Regularly gather feedback from sales representatives to understand their needs and challenges.
    * Provide ongoing training and development opportunities to keep sales representatives engaged and motivated.
    * Implement recognition and reward programs to acknowledge the contributions of sales representatives.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of sales retention rate over time.
    * Comparison charts to analyze retention rates across different sales teams or regions.
    
    
    """,
    "risk_warnings": """


    * Low sales retention rates can lead to increased recruitment and training costs.
    * High turnover may negatively impact team morale and overall sales performance.
    
    
    """,
    "tracking_tools": """


    * Employee engagement and feedback platforms to gather insights from sales representatives.
    * HR analytics software to track and analyze retention data.
    
    
    """,
    "integration_points": """


    * Integrate sales retention data with performance management systems to identify correlations between retention and sales performance.
    * Link retention data with training and development programs to tailor support based on retention trends.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales retention can lead to a more experienced and knowledgeable sales team, potentially impacting overall sales performance positively.
    * Conversely, high turnover rates can disrupt team dynamics and affect customer relationships, leading to potential revenue loss.
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.490400"},
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
                        36.79,
                        38.79,
                        37.33,
                        38.95,
                        39.53,
                        37.14,
                        47.42,
                        37.77,
                        39.95,
                        50.79,
                        41.91,
                        48.28
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.28,
                "unit": "%",
                "change": 6.37,
                "change_percent": 15.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 41.22,
                "min": 36.79,
                "max": 50.79,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.96,
                        "percentage": 18.6
                },
                {
                        "category": "Category B",
                        "value": 7.58,
                        "percentage": 15.7
                },
                {
                        "category": "Category C",
                        "value": 6.41,
                        "percentage": 13.3
                },
                {
                        "category": "Category D",
                        "value": 3.19,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 22.14,
                        "percentage": 45.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.588960",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Retention Rate"
        }
    },
}
