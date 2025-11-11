"""
Sales Pipeline Coverage

The ratio of the sales pipeline to the sales quota, showing whether there is sufficient potential business to meet future sales targets.
"""

SALES_PIPELINE_COVERAGE = {
    "code": "SALES_PIPELINE_COVERAGE",
    "name": "Sales Pipeline Coverage",
    "description": "The ratio of the sales pipeline to the sales quota, showing whether there is sufficient potential business to meet future sales targets.",
    "formula": "Total Value of Sales Pipeline / Sales Quota",
    "calculation_formula": "Total Value of Sales Pipeline / Sales Quota",
    "category": "Sales Strategy",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Pipeline Coverage to be added.",
    "trend_analysis": """

    * An increasing sales pipeline coverage may indicate a growing potential for future sales, but it could also signal a lack of efficiency in converting leads into actual sales.
    * A decreasing ratio may suggest a lack of potential business opportunities or a need to reevaluate sales targets and strategies.
    
    """,
    "diagnostic_questions": """

    * What is the average time it takes for leads to progress through the sales pipeline?
    * Are there specific stages in the sales pipeline where leads tend to drop off or get stuck?
    
    """,
    "actionable_tips": """

    * Implement lead nurturing strategies to improve conversion rates at different stages of the sales pipeline.
    * Regularly review and update sales targets based on market trends and business opportunities.
    * Provide ongoing training and support for sales teams to improve their effectiveness in moving leads through the pipeline.
    
    """,
    "visualization_suggestions": """

    * Funnel charts to visualize the conversion rates at each stage of the sales pipeline.
    * Line graphs to track the changes in sales pipeline coverage over time.
    
    """,
    "risk_warnings": """

    * A high sales pipeline coverage without corresponding sales may lead to overestimation of future revenue and resource allocation.
    * A low ratio may indicate missed opportunities and potential revenue loss.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and manage leads throughout the sales pipeline.
    * Sales analytics tools to identify trends and patterns in the sales pipeline data.
    
    """,
    "integration_points": """

    * Integrate sales pipeline coverage data with marketing analytics to align lead generation efforts with sales targets.
    * Link the KPI with customer feedback systems to understand how the sales pipeline performance impacts customer satisfaction.
    
    """,
    "change_impact_analysis": """

    * Improving the sales pipeline coverage can lead to increased revenue and market share, but it may also require additional resources and investments in sales and marketing.
    * A declining ratio may indicate the need for strategic changes in sales and marketing approaches to remain competitive.
    
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Quarterly Business Review", "Quota Plan", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.508139"},
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
                        534.99,
                        501.6,
                        559.65,
                        582.95,
                        516.53,
                        562.45,
                        500.59,
                        483.3,
                        564.48,
                        504.71,
                        581.81,
                        611.64
                ],
                "unit": "units"
        },
        "current": {
                "value": 611.64,
                "unit": "units",
                "change": 29.83,
                "change_percent": 5.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 542.06,
                "min": 483.3,
                "max": 611.64,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 146.74,
                        "percentage": 24.0
                },
                {
                        "category": "Category B",
                        "value": 128.53,
                        "percentage": 21.0
                },
                {
                        "category": "Category C",
                        "value": 89.81,
                        "percentage": 14.7
                },
                {
                        "category": "Category D",
                        "value": 52.36,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 194.2,
                        "percentage": 31.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.508139",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Pipeline Coverage"
        }
    },
}
