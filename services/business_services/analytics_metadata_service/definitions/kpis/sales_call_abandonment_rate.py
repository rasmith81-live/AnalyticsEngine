"""
Sales Call Abandonment Rate

The rate at which potential customers abandon a sales call before it is completed.
"""

SALES_CALL_ABANDONMENT_RATE = {
    "code": "SALES_CALL_ABANDONMENT_RATE",
    "name": "Sales Call Abandonment Rate",
    "description": "The rate at which potential customers abandon a sales call before it is completed.",
    "formula": "(Number of Abandoned Sales Calls / Total Number of Sales Calls) * 100",
    "calculation_formula": "(Number of Abandoned Sales Calls / Total Number of Sales Calls) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Call Abandonment Rate to be added.",
    "trend_analysis": """



    * An increasing sales call abandonment rate may indicate a need for better sales training or a lack of understanding of customer needs.
    * A decreasing rate could signal improved sales techniques or better alignment between customer expectations and the sales process.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there common reasons why potential customers abandon sales calls, such as pricing, product fit, or timing?
    * How does our sales call abandonment rate compare with industry benchmarks or with different sales teams within our organization?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional sales training to address potential customer objections and improve sales techniques.
    * Implement a more targeted approach to qualifying leads to ensure better alignment between customer needs and the sales process.
    * Utilize customer feedback to understand common reasons for call abandonment and adjust sales strategies accordingly.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of sales call abandonment rate over time.
    * Pie charts to visualize the reasons for call abandonment, such as pricing, product fit, or timing issues.
    
    
    
    """,
    "risk_warnings": """



    * A high sales call abandonment rate can lead to lost sales opportunities and decreased revenue.
    * Frequent call abandonment may indicate a need for improvement in the sales process or product offerings.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze call abandonment rates and reasons.
    * Sales enablement platforms to provide sales teams with the necessary tools and resources to address customer objections and improve sales effectiveness.
    
    
    
    """,
    "integration_points": """



    * Integrate sales call abandonment rate with customer feedback systems to understand the reasons behind call abandonment and make necessary adjustments.
    * Link with sales performance management systems to identify trends and patterns in call abandonment across different sales teams and territories.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the sales call abandonment rate can lead to increased sales efficiency and customer satisfaction, but may require investment in sales training and resources.
    * A high call abandonment rate can impact the overall sales performance and customer perception of the brand, affecting long-term customer value and brand reputation.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Customer", "Lead", "Lead Qualification", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.376384"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS"],
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
                        45.97,
                        50.36,
                        63.36,
                        63.59,
                        54.37,
                        61.95,
                        48.81,
                        55.89,
                        48.6,
                        46.28,
                        46.22,
                        59.58
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.58,
                "unit": "%",
                "change": 13.36,
                "change_percent": 28.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 53.75,
                "min": 45.97,
                "max": 63.59,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 19.96,
                        "percentage": 33.5
                },
                {
                        "category": "Channel Sales",
                        "value": 13.42,
                        "percentage": 22.5
                },
                {
                        "category": "Online Sales",
                        "value": 8.27,
                        "percentage": 13.9
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.12,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 12.81,
                        "percentage": 21.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.872850",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Call Abandonment Rate"
        }
    },
}
