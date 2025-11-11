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
                        63.54,
                        65.19,
                        71.44,
                        56.97,
                        68.56,
                        67.99,
                        54.0,
                        56.23,
                        60.13,
                        60.98,
                        72.65,
                        55.6
                ],
                "unit": "%"
        },
        "current": {
                "value": 55.6,
                "unit": "%",
                "change": -17.05,
                "change_percent": -23.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 62.77,
                "min": 54.0,
                "max": 72.65,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 14.9,
                        "percentage": 26.8
                },
                {
                        "category": "Channel Sales",
                        "value": 14.08,
                        "percentage": 25.3
                },
                {
                        "category": "Online Sales",
                        "value": 8.55,
                        "percentage": 15.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.33,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 12.74,
                        "percentage": 22.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.175711",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Retention Rate"
        }
    },
}
