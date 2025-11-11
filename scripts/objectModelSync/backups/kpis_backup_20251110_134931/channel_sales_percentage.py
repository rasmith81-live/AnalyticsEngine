"""
Channel Sales Percentage

The percentage of total sales that come through various distribution channels (e.g., online, retail, direct).
"""

CHANNEL_SALES_PERCENTAGE = {
    "code": "CHANNEL_SALES_PERCENTAGE",
    "name": "Channel Sales Percentage",
    "description": "The percentage of total sales that come through various distribution channels (e.g., online, retail, direct).",
    "formula": "(Total Sales per Channel / Total Sales) * 100",
    "calculation_formula": "(Total Sales per Channel / Total Sales) * 100",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Channel Sales Percentage to be added.",
    "trend_analysis": """

    * Increasing channel sales percentage may indicate successful expansion into new distribution channels or increased online sales.
    * Decreasing percentage could signal a shift in customer preferences towards other sales channels or a decline in retail sales.
    
    """,
    "diagnostic_questions": """

    * Which distribution channels are driving the majority of our sales?
    * Are there specific products that perform better in certain channels?
    
    """,
    "actionable_tips": """

    * Invest in marketing and promotions for underperforming channels to drive sales.
    * Optimize inventory allocation based on channel performance to meet demand effectively.
    * Explore partnerships or collaborations to expand into new sales channels.
    
    """,
    "visualization_suggestions": """

    * Stacked bar charts comparing sales percentage by different channels over time.
    * Line graphs showing the trend of each channel's sales percentage over time.
    
    """,
    "risk_warnings": """

    * Relying too heavily on a single channel may expose the business to risks if that channel experiences issues.
    * Ignoring underperforming channels may lead to missed opportunities for sales growth.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track sales by channel and customer preferences.
    * Business intelligence tools to analyze sales data and identify channel performance trends.
    
    """,
    "integration_points": """

    * Integrate sales channel data with inventory management systems to ensure adequate stock levels for each channel.
    * Link channel sales data with marketing platforms to align promotional efforts with channel performance.
    
    """,
    "change_impact_analysis": """

    * Increasing channel sales percentage may lead to higher overall sales revenue but could also require additional resources for managing multiple channels.
    * Decreasing percentage in a specific channel may impact relationships with retail partners or online platforms.
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.107214"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        65.28,
                        70.71,
                        67.27,
                        59.24,
                        58.71,
                        69.3,
                        66.08,
                        57.47,
                        68.43,
                        64.64,
                        66.04,
                        60.81
                ],
                "unit": "%"
        },
        "current": {
                "value": 60.81,
                "unit": "%",
                "change": -5.23,
                "change_percent": -7.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 64.5,
                "min": 57.47,
                "max": 70.71,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.63,
                        "percentage": 17.5
                },
                {
                        "category": "Category B",
                        "value": 9.1,
                        "percentage": 15.0
                },
                {
                        "category": "Category C",
                        "value": 12.68,
                        "percentage": 20.9
                },
                {
                        "category": "Category D",
                        "value": 4.2,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 24.2,
                        "percentage": 39.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.107214",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Channel Sales Percentage"
        }
    },
}
