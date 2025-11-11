"""
Sales Call Success Rate

The percentage of sales calls that result in a positive outcome, such as moving a lead to the next stage in the pipeline.
"""

SALES_CALL_SUCCESS_RATE = {
    "code": "SALES_CALL_SUCCESS_RATE",
    "name": "Sales Call Success Rate",
    "description": "The percentage of sales calls that result in a positive outcome, such as moving a lead to the next stage in the pipeline.",
    "formula": "(Number of Successful Sales Calls / Total Number of Sales Calls) * 100",
    "calculation_formula": "(Number of Successful Sales Calls / Total Number of Sales Calls) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Call Success Rate to be added.",
    "trend_analysis": """



    * An increasing sales call success rate may indicate improved lead qualification or more effective sales strategies.
    * A decreasing rate could signal issues with lead quality, sales team performance, or changes in the market.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales tactics or scripts that consistently lead to positive outcomes?
    * How does our sales call success rate compare with industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Provide ongoing sales training and coaching to improve communication and closing skills.
    * Regularly review and update lead qualification criteria to ensure sales calls are focused on high-potential leads.
    * Implement a customer relationship management (CRM) system to track and analyze sales call outcomes.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend in sales call success rate over time.
    * Pie charts comparing success rates across different sales teams or regions.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low success rate can lead to wasted resources and demotivated sales teams.
    * A sudden drop in success rate may indicate external factors affecting the market or customer behavior.
    
    
    
    """,
    "tracking_tools": """



    * CRM software with call tracking and analytics capabilities to monitor and analyze sales call outcomes.
    * Sales enablement platforms to provide sales teams with the tools and resources needed to improve success rates.
    
    
    
    """,
    "integration_points": """



    * Integrate sales call success rate data with lead generation and marketing systems to understand the quality of leads being generated.
    * Link success rate metrics with individual sales performance data to identify coaching and training opportunities.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the sales call success rate can lead to increased revenue and customer satisfaction.
    * However, a focus solely on success rate may neglect the quality of customer interactions and long-term relationships.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Appointment", "Call", "Customer Success Manager", "Lead", "Lead Qualification", "Lost Sale", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.380058"},
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
                        72.45,
                        55.01,
                        65.46,
                        64.01,
                        59.28,
                        70.62,
                        71.2,
                        63.08,
                        54.09,
                        53.89,
                        62.63,
                        63.52
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.52,
                "unit": "%",
                "change": 0.89,
                "change_percent": 1.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 62.94,
                "min": 53.89,
                "max": 72.45,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 15.9,
                        "percentage": 25.0
                },
                {
                        "category": "Channel Sales",
                        "value": 8.79,
                        "percentage": 13.8
                },
                {
                        "category": "Online Sales",
                        "value": 10.21,
                        "percentage": 16.1
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.07,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 23.55,
                        "percentage": 37.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.878942",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Call Success Rate"
        }
    },
}
