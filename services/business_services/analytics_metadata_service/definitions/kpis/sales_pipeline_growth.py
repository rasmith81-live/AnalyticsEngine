"""
Sales Pipeline Growth

The increase in the number of potential deals in the sales pipeline over a given period.
"""

SALES_PIPELINE_GROWTH = {
    "code": "SALES_PIPELINE_GROWTH",
    "name": "Sales Pipeline Growth",
    "description": "The increase in the number of potential deals in the sales pipeline over a given period.",
    "formula": "(Current Pipeline Value - Previous Pipeline Value) / Previous Pipeline Value",
    "calculation_formula": "(Current Pipeline Value - Previous Pipeline Value) / Previous Pipeline Value",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Pipeline Growth to be added.",
    "trend_analysis": """



    * An increasing sales pipeline growth may indicate improved lead generation and marketing efforts.
    * A decreasing growth rate could signal challenges in converting leads to opportunities or a decrease in market demand.
    
    
    
    """,
    "diagnostic_questions": """



    * What is the average time it takes for a lead to progress through the sales pipeline?
    * Are there specific stages in the pipeline where leads tend to drop off or stagnate?
    
    
    
    """,
    "actionable_tips": """



    * Implement lead nurturing strategies to move potential deals through the pipeline more effectively.
    * Regularly review and update the qualification criteria for opportunities to ensure a healthy pipeline.
    * Provide ongoing training and support for sales representatives to improve their ability to move leads through the pipeline.
    
    
    
    """,
    "visualization_suggestions": """



    * Funnel charts to visualize the progression of leads through each stage of the sales pipeline.
    * Line graphs to track the growth of the pipeline over time and identify any fluctuations.
    
    
    
    """,
    "risk_warnings": """



    * A stagnant or declining sales pipeline growth can lead to reduced sales opportunities and revenue.
    * An excessively large pipeline without proper management can result in inefficiencies and wasted resources.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and manage leads throughout the pipeline.
    * Sales analytics tools to gain insights into the performance of the sales pipeline and identify areas for improvement.
    
    
    
    """,
    "integration_points": """



    * Integrate the sales pipeline data with marketing automation systems to align lead generation efforts with the needs of the sales team.
    * Connect the pipeline with customer support systems to ensure a seamless transition from sales to post-sales service.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the sales pipeline growth can lead to increased revenue and a more predictable sales process.
    * However, rapid growth without proper management can strain resources and lead to decreased quality of customer interactions.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.460981"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
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
                        660.38,
                        593.85,
                        632.1,
                        644.72,
                        573.39,
                        688.66,
                        644.03,
                        589.63,
                        682.82,
                        675.21,
                        625.05,
                        615.87
                ],
                "unit": "units"
        },
        "current": {
                "value": 615.87,
                "unit": "units",
                "change": -9.18,
                "change_percent": -1.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 635.48,
                "min": 573.39,
                "max": 688.66,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 110.43,
                        "percentage": 17.9
                },
                {
                        "category": "Channel Sales",
                        "value": 155.26,
                        "percentage": 25.2
                },
                {
                        "category": "Online Sales",
                        "value": 112.35,
                        "percentage": 18.2
                },
                {
                        "category": "Enterprise Sales",
                        "value": 36.2,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 201.63,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.094979",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Pipeline Growth"
        }
    },
}
