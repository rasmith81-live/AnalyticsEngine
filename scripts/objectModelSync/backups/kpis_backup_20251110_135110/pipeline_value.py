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
                        16968.26,
                        23814.09,
                        17992.94,
                        15512.39,
                        22772.56,
                        23744.5,
                        26154.6,
                        15138.48,
                        18085.38,
                        23123.29,
                        14784.74,
                        24255.46
                ],
                "unit": "$"
        },
        "current": {
                "value": 24255.46,
                "unit": "$",
                "change": 9470.72,
                "change_percent": 64.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 20195.56,
                "min": 14784.74,
                "max": 26154.6,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 6145.52,
                        "percentage": 25.3
                },
                {
                        "category": "Category B",
                        "value": 5966.63,
                        "percentage": 24.6
                },
                {
                        "category": "Category C",
                        "value": 2743.03,
                        "percentage": 11.3
                },
                {
                        "category": "Category D",
                        "value": 1901.92,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 7498.36,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.936602",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Pipeline Value"
        }
    },
}
