"""
Pipeline Velocity

The speed at which deals move through the sales pipeline.
"""

PIPELINE_VELOCITY = {
    "code": "PIPELINE_VELOCITY",
    "name": "Pipeline Velocity",
    "description": "The speed at which deals move through the sales pipeline.",
    "formula": "(Number of Opportunities * Deal Size * Conversion Rate) / Length of Sales Cycle",
    "calculation_formula": "(Number of Opportunities * Deal Size * Conversion Rate) / Length of Sales Cycle",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Pipeline Velocity to be added.",
    "trend_analysis": """



    * Increasing pipeline velocity may indicate improved sales processes or higher demand for products/services.
    * Decreasing velocity could signal inefficiencies in the sales pipeline or a decline in market interest.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific stages in the sales pipeline where deals tend to get stuck?
    * How does our pipeline velocity compare with industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Implement sales automation tools to streamline the sales process and reduce bottlenecks.
    * Provide additional training and support for sales representatives to improve their efficiency and effectiveness.
    * Regularly review and optimize the sales pipeline stages to remove any unnecessary steps or delays.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the average time deals spend in each stage of the pipeline over time.
    * Funnel charts to visualize the drop-off rates at each stage of the sales pipeline.
    
    
    
    """,
    "risk_warnings": """



    * High pipeline velocity without proper qualification may lead to an increase in unqualified leads and wasted resources.
    * Excessively low velocity may result in missed sales opportunities and revenue targets.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and manage the sales pipeline.
    * Sales performance analytics tools to identify bottlenecks and areas for improvement.
    
    
    
    """,
    "integration_points": """



    * Integrate pipeline velocity data with marketing analytics to align sales and marketing efforts more effectively.
    * Link with customer support systems to understand how post-sales activities impact pipeline velocity.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing pipeline velocity may lead to higher sales volume but could also strain resources if not managed effectively.
    * Decreasing velocity may indicate a need for process improvement but could also impact revenue and market share.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Lead", "Opportunity", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.244845"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        76,
                        86,
                        77,
                        62,
                        58,
                        64,
                        71,
                        52,
                        87,
                        43,
                        77,
                        54
                ],
                "unit": "count"
        },
        "current": {
                "value": 54,
                "unit": "count",
                "change": -23,
                "change_percent": -29.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.25,
                "min": 43,
                "max": 87,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 18.38,
                        "percentage": 34.0
                },
                {
                        "category": "Channel Sales",
                        "value": 9.89,
                        "percentage": 18.3
                },
                {
                        "category": "Online Sales",
                        "value": 8.48,
                        "percentage": 15.7
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.51,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 13.74,
                        "percentage": 25.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.580242",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Pipeline Velocity"
        }
    },
}
