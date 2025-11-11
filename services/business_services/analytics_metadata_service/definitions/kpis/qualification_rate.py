"""
Qualification Rate

The percentage of new sales hires who pass the initial training and are deemed qualified to start selling.
"""

QUALIFICATION_RATE = {
    "code": "QUALIFICATION_RATE",
    "name": "Qualification Rate",
    "description": "The percentage of new sales hires who pass the initial training and are deemed qualified to start selling.",
    "formula": "(Number of Qualified Leads / Total Number of Leads) * 100",
    "calculation_formula": "(Number of Qualified Leads / Total Number of Leads) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Qualification Rate to be added.",
    "trend_analysis": """



    * A rising qualification rate may indicate improvements in the effectiveness of sales training programs or better hiring practices.
    * A decreasing rate could signal issues with the quality of training, changes in the market, or challenges in finding suitable candidates.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific aspects of the training program are contributing to the increase or decrease in qualification rates?
    * Are there any common characteristics or traits among new hires who do not pass the initial training?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and update training materials to ensure they align with the current market and sales strategies.
    * Provide additional support and resources for new hires who may be struggling to meet qualification standards.
    * Implement a mentorship or coaching program to help new hires integrate their training into practical sales skills.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing qualification rates over time to identify long-term trends.
    * Comparison charts to analyze qualification rates across different training cohorts or regions.
    
    
    
    """,
    "risk_warnings": """



    * Low qualification rates can lead to a decrease in overall sales performance and revenue.
    * Consistently high qualification rates may indicate that the training standards are not rigorous enough, leading to underprepared sales professionals.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track the progress and performance of new hires during training.
    * Sales performance management software to identify correlations between training outcomes and actual sales results.
    
    
    
    """,
    "integration_points": """



    * Integrate qualification rate data with HR systems to analyze the impact of hiring practices on training outcomes.
    * Link qualification rates with sales performance data to understand the long-term effectiveness of the training program.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving qualification rates can lead to a more skilled and effective sales team, ultimately driving higher revenue and customer satisfaction.
    * Conversely, a decline in qualification rates may result in decreased sales performance and potential turnover among new hires.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Lead Qualification", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.305082"},
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
                        49.68,
                        60.88,
                        58.76,
                        43.92,
                        44.93,
                        44.61,
                        59.71,
                        59.45,
                        51.87,
                        47.9,
                        52.32,
                        45.94
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.94,
                "unit": "%",
                "change": -6.38,
                "change_percent": -12.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 51.66,
                "min": 43.92,
                "max": 60.88,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.89,
                        "percentage": 32.4
                },
                {
                        "category": "Segment B",
                        "value": 5.6,
                        "percentage": 12.2
                },
                {
                        "category": "Segment C",
                        "value": 4.78,
                        "percentage": 10.4
                },
                {
                        "category": "Segment D",
                        "value": 4.89,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 15.78,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.714632",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Qualification Rate"
        }
    },
}
