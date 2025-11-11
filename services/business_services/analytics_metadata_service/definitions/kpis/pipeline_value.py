"""
Pipeline Value

The total value of the sales pipeline. A higher pipeline value indicates effective training and coaching.
"""

PIPELINE_VALUE = {
    "code": "PIPELINE_VALUE",
    "name": "Pipeline Value",
    "description": "The total value of the sales pipeline. A higher pipeline value indicates effective training and coaching.",
    "formula": "Sum of the Value of All Opportunities in the Sales Pipeline",
    "calculation_formula": "Sum of the Value of All Opportunities in the Sales Pipeline",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Pipeline Value to be added.",
    "trend_analysis": """



    * An increasing pipeline value may indicate successful lead generation and effective sales strategies.
    * A decreasing pipeline value could signal challenges in converting leads or a decline in overall sales opportunities.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the main sources of leads contributing to the pipeline value?
    * Are there specific stages in the sales process where leads are dropping off, impacting the pipeline value?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional sales training and coaching focused on lead conversion and closing techniques.
    * Implement lead nurturing strategies to maintain and advance leads through the sales pipeline.
    * Regularly review and update the sales pipeline to ensure accuracy and relevance of opportunities.
    
    
    
    """,
    "visualization_suggestions": """



    * Funnel charts to visualize the progression of leads through the sales pipeline.
    * Line graphs to track changes in pipeline value over time.
    
    
    
    """,
    "risk_warnings": """



    * A stagnant or declining pipeline value may lead to missed sales targets and revenue goals.
    * An inflated pipeline value without corresponding sales may indicate inaccurate or inflated opportunity tracking.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and manage leads throughout the sales pipeline.
    * Sales analytics tools to gain insights into lead behavior and pipeline performance.
    
    
    
    """,
    "integration_points": """



    * Integrate pipeline value tracking with sales forecasting to align sales strategies with anticipated revenue.
    * Link pipeline value with marketing analytics to assess the effectiveness of lead generation efforts.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving pipeline value can lead to increased revenue and sales team motivation.
    * However, a declining pipeline value may require adjustments in sales and marketing strategies, potentially impacting resource allocation.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.242793"},
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
                        80690.57,
                        78679.32,
                        88626.16,
                        78447.3,
                        82652.51,
                        84421.22,
                        75167.01,
                        74022.18,
                        80638.35,
                        74159.29,
                        87559.11,
                        83713.16
                ],
                "unit": "$"
        },
        "current": {
                "value": 83713.16,
                "unit": "$",
                "change": -3845.95,
                "change_percent": -4.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 80731.35,
                "min": 74022.18,
                "max": 88626.16,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 16079.66,
                        "percentage": 19.2
                },
                {
                        "category": "Channel Sales",
                        "value": 22315.45,
                        "percentage": 26.7
                },
                {
                        "category": "Online Sales",
                        "value": 10351.5,
                        "percentage": 12.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5096.75,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 29869.8,
                        "percentage": 35.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.576081",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Pipeline Value"
        }
    },
}
