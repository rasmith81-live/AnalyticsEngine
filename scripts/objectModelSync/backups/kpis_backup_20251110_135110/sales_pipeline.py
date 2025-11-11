"""
Sales Pipeline

The total value of potential sales opportunities within the key accounts.
"""

SALES_PIPELINE = {
    "code": "SALES_PIPELINE",
    "name": "Sales Pipeline",
    "description": "The total value of potential sales opportunities within the key accounts.",
    "formula": "Listing of all active deals categorized by sales stage",
    "calculation_formula": "Listing of all active deals categorized by sales stage",
    "category": "Key Account Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Pipeline to be added.",
    "trend_analysis": """


    * Increasing sales pipeline value may indicate successful lead generation and account expansion efforts.
    * A decreasing pipeline value could signal challenges in converting leads or retaining existing business.
    
    
    """,
    "diagnostic_questions": """


    * What is the average time it takes to move opportunities through the sales pipeline?
    * Are there specific stages in the pipeline where opportunities tend to stall or drop off?
    
    
    """,
    "actionable_tips": """


    * Implement a structured sales process to move opportunities through the pipeline more efficiently.
    * Provide targeted training and resources to sales teams to improve their ability to qualify and close opportunities.
    * Regularly review and update the sales pipeline to ensure it accurately reflects the current state of potential opportunities.
    
    
    """,
    "visualization_suggestions": """


    * Funnel charts to visualize the progression of opportunities through different stages of the pipeline.
    * Line graphs to track changes in pipeline value over time.
    
    
    """,
    "risk_warnings": """


    * A stagnant or declining sales pipeline value may lead to missed revenue targets and decreased market share.
    * An overly optimistic pipeline may result in resource allocation to opportunities that are unlikely to close.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track and manage opportunities within the pipeline.
    * Sales analytics tools to gain insights into the health and movement of the sales pipeline.
    
    
    """,
    "integration_points": """


    * Integrate the sales pipeline with marketing automation systems to ensure a steady flow of qualified leads.
    * Connect the pipeline with financial forecasting and resource planning systems to align sales targets with operational capabilities.
    
    
    """,
    "change_impact_analysis": """


    * Improving the sales pipeline can lead to increased revenue and market share, but may also require additional resources and investment in sales and marketing efforts.
    * A declining pipeline value can impact overall business performance and may require strategic adjustments in sales and marketing strategies.
    
    
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Deal", "Key Account", "Key Account Manager", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.455259"},
    "required_objects": [],
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
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
                        850.02,
                        980.55,
                        896.16,
                        875.28,
                        970.48,
                        850.76,
                        988.3,
                        876.37,
                        934.19,
                        955.23,
                        869.63,
                        907.06
                ],
                "unit": "units"
        },
        "current": {
                "value": 907.06,
                "unit": "units",
                "change": 37.43,
                "change_percent": 4.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 912.84,
                "min": 850.02,
                "max": 988.3,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 158.6,
                        "percentage": 17.5
                },
                {
                        "category": "Category B",
                        "value": 246.35,
                        "percentage": 27.2
                },
                {
                        "category": "Category C",
                        "value": 115.15,
                        "percentage": 12.7
                },
                {
                        "category": "Category D",
                        "value": 94.67,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 292.29,
                        "percentage": 32.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.487923",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Pipeline"
        }
    },
}
