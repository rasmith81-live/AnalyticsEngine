"""
Sales Pipeline Health

The status of the opportunities in the sales pipeline, which can include the number of deals, their value, and the average time for deals to move through the pipeline.
"""

SALES_PIPELINE_HEALTH = {
    "code": "SALES_PIPELINE_HEALTH",
    "name": "Sales Pipeline Health",
    "description": "The status of the opportunities in the sales pipeline, which can include the number of deals, their value, and the average time for deals to move through the pipeline.",
    "formula": "Total Value of Sales Pipeline / Number of Opportunities in Pipeline",
    "calculation_formula": "Total Value of Sales Pipeline / Number of Opportunities in Pipeline",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Pipeline Health to be added.",
    "trend_analysis": """


    * Increasing number of deals in the pipeline may indicate improved lead generation or sales efforts.
    * A decreasing average time for deals to move through the pipeline could signal more efficient sales processes or better-qualified leads.
    
    
    """,
    "diagnostic_questions": """


    * What are the main reasons for deals stalling or getting stuck in the pipeline?
    * How does our sales pipeline health compare to industry benchmarks or best practices?
    
    
    """,
    "actionable_tips": """


    * Implement a clear qualification process to ensure only high-potential opportunities enter the pipeline.
    * Regularly review and clean the pipeline to remove stale or low-value opportunities.
    * Provide ongoing training and support for sales reps to help them move deals through the pipeline more effectively.
    
    
    """,
    "visualization_suggestions": """


    * Funnel charts to visualize the progression of deals through different stages of the pipeline.
    * Line charts to track changes in the number of deals and their value over time.
    
    
    """,
    "risk_warnings": """


    * A bloated pipeline with low-quality opportunities can lead to wasted resources and decreased win rates.
    * Long average time for deals to move through the pipeline may indicate inefficiencies or bottlenecks in the sales process.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track and manage opportunities in the pipeline.
    * Sales analytics tools to gain insights into the health and performance of the sales pipeline.
    
    
    """,
    "integration_points": """


    * Integrate sales pipeline data with marketing and lead generation systems to ensure a steady flow of qualified opportunities.
    * Link pipeline health with sales forecasting and resource allocation for better sales management.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales pipeline health can lead to increased revenue and better sales team performance.
    * However, a sudden decrease in the number of deals in the pipeline may impact future revenue and require adjustments in sales strategies.
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Health Record", "Deal", "Lead", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.462586"},
    "required_objects": [],
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
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
                        351,
                        392,
                        392,
                        356,
                        349,
                        367,
                        378,
                        361,
                        370,
                        360,
                        342,
                        351
                ],
                "unit": "count"
        },
        "current": {
                "value": 351,
                "unit": "count",
                "change": 9,
                "change_percent": 2.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 364.08,
                "min": 342,
                "max": 392,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 109.1,
                        "percentage": 31.1
                },
                {
                        "category": "Category B",
                        "value": 37.72,
                        "percentage": 10.7
                },
                {
                        "category": "Category C",
                        "value": 68.81,
                        "percentage": 19.6
                },
                {
                        "category": "Category D",
                        "value": 24.03,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 111.34,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.515487",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Pipeline Health"
        }
    },
}
