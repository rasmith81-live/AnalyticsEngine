"""
Sales Pipeline Velocity

The time it takes for a lead to move through the sales pipeline and convert into a sale.
"""

SALES_PIPELINE_VELOCITY = {
    "code": "SALES_PIPELINE_VELOCITY",
    "name": "Sales Pipeline Velocity",
    "description": "The time it takes for a lead to move through the sales pipeline and convert into a sale.",
    "formula": "(Number of Deals in Pipeline * Average Deal Size * Win Rate) / Length of Sales Cycle",
    "calculation_formula": "(Number of Deals in Pipeline * Average Deal Size * Win Rate) / Length of Sales Cycle",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Pipeline Velocity to be added.",
    "trend_analysis": """


    * Shortening sales pipeline velocity may indicate improved lead qualification and sales process efficiency.
    * An increasing time to convert may signal issues with lead quality, sales team performance, or market conditions.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific stages in the sales pipeline where leads tend to stall or drop off?
    * How does our sales pipeline velocity compare with industry benchmarks or historical data?
    
    
    """,
    "actionable_tips": """


    * Implement lead scoring to prioritize high-quality leads and focus sales efforts more effectively.
    * Provide targeted training and support for sales teams to improve their ability to move leads through the pipeline.
    * Regularly review and optimize the sales process to identify and remove bottlenecks.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the average time spent at each stage of the sales pipeline.
    * Funnel charts to visualize the drop-off rates between pipeline stages.
    
    
    """,
    "risk_warnings": """


    * Slow sales pipeline velocity can lead to missed revenue targets and reduced cash flow.
    * Rapid pipeline velocity without proper lead qualification can result in increased customer churn and decreased customer lifetime value.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track lead movement and identify areas for improvement.
    * Sales enablement tools to streamline the sales process and provide sales teams with the resources they need to move leads through the pipeline efficiently.
    
    
    """,
    "integration_points": """


    * Integrate sales pipeline velocity with marketing automation systems to ensure a smooth transition from marketing-qualified leads to sales-qualified leads.
    * Link sales pipeline velocity with customer relationship management (CRM) systems to track the impact of lead movement on customer interactions and conversions.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales pipeline velocity can lead to increased revenue and improved sales team morale, but may also require additional resources and support.
    * Slowing down sales pipeline velocity to focus on lead quality and customer relationships may result in lower short-term sales, but can lead to higher customer satisfaction and long-term loyalty.
    
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Lead", "Lead Qualification", "Lost Sale", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.463656"},
    "required_objects": [],
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
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
                        171,
                        183,
                        194,
                        183,
                        150,
                        148,
                        161,
                        172,
                        147,
                        193,
                        182,
                        184
                ],
                "unit": "count"
        },
        "current": {
                "value": 184,
                "unit": "count",
                "change": 2,
                "change_percent": 1.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 172.33,
                "min": 147,
                "max": 194,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 50.87,
                        "percentage": 27.6
                },
                {
                        "category": "Category B",
                        "value": 23.59,
                        "percentage": 12.8
                },
                {
                        "category": "Category C",
                        "value": 29.27,
                        "percentage": 15.9
                },
                {
                        "category": "Category D",
                        "value": 9.02,
                        "percentage": 4.9
                },
                {
                        "category": "Other",
                        "value": 71.25,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.518621",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Pipeline Velocity"
        }
    },
}
