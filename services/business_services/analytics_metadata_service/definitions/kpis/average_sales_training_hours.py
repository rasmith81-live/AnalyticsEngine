"""
Average Sales Training Hours

The average number of training hours completed by each sales representative, indicating the level of investment in skills development.
"""

AVERAGE_SALES_TRAINING_HOURS = {
    "code": "AVERAGE_SALES_TRAINING_HOURS",
    "name": "Average Sales Training Hours",
    "description": "The average number of training hours completed by each sales representative, indicating the level of investment in skills development.",
    "formula": "Total Training Hours / Total Number of Sales Representatives",
    "calculation_formula": "Total Training Hours / Total Number of Sales Representatives",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Sales Training Hours to be added.",
    "trend_analysis": """



    * An increasing average sales training hours may indicate a focus on continuous learning and skill development within the sales team.
    * A decreasing average may suggest a lack of investment in training or potential skill stagnation among sales representatives.
    
    
    
    """,
    "diagnostic_questions": """



    * Are the training hours tailored to address specific skill gaps or areas of improvement for each sales representative?
    * How does the average training hours compare to industry benchmarks or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Implement personalized training plans for each sales representative based on their individual performance and development needs.
    * Utilize interactive and engaging training methods to maximize knowledge retention and application in real-world sales scenarios.
    * Regularly assess the effectiveness of training programs and make adjustments based on feedback and performance outcomes.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of average training hours over time for each sales representative.
    * Comparison bar charts to visualize the variance in training hours between different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * Low average training hours may lead to decreased sales effectiveness and missed opportunities for skill development.
    * High average training hours without tangible improvements in sales performance may indicate ineffective training programs or resource misallocation.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track and manage individual training progress and performance.
    * Sales enablement platforms that offer training modules and resources tailored to specific sales roles and responsibilities.
    
    
    
    """,
    "integration_points": """



    * Integrate training hours data with sales performance metrics to identify correlations between training investment and sales outcomes.
    * Link training hours with employee development plans and performance reviews to align training efforts with career growth and skill enhancement.
    
    
    
    """,
    "change_impact_analysis": """



    * Increased training hours may lead to improved sales effectiveness, customer satisfaction, and overall revenue growth.
    * However, excessive focus on training hours alone may neglect other factors influencing sales performance, such as market changes or product quality.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"], "last_validated": "2025-11-10T13:49:32.660717"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        200,
                        179,
                        169,
                        167,
                        191,
                        164,
                        205,
                        199,
                        190,
                        202,
                        196,
                        194
                ],
                "unit": "count"
        },
        "current": {
                "value": 194,
                "unit": "count",
                "change": -2,
                "change_percent": -1.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 188.0,
                "min": 164,
                "max": 205,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 55.82,
                        "percentage": 28.8
                },
                {
                        "category": "Channel Sales",
                        "value": 35.12,
                        "percentage": 18.1
                },
                {
                        "category": "Online Sales",
                        "value": 26.91,
                        "percentage": 13.9
                },
                {
                        "category": "Enterprise Sales",
                        "value": 16.27,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 59.88,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.394012",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Sales Training Hours"
        }
    },
}
