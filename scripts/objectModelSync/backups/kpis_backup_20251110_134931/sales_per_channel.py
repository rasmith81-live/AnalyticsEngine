"""
Sales per Channel

The distribution of sales across different sales channels, which can include online, in-store, direct sales, or partner sales.
"""

SALES_PER_CHANNEL = {
    "code": "SALES_PER_CHANNEL",
    "name": "Sales per Channel",
    "description": "The distribution of sales across different sales channels, which can include online, in-store, direct sales, or partner sales.",
    "formula": "Total Sales Revenue per Sales Channel",
    "calculation_formula": "Total Sales Revenue per Sales Channel",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales per Channel to be added.",
    "trend_analysis": """

    * Shift towards online sales channels may indicate changing consumer preferences or market dynamics.
    * Decrease in direct sales could signal the need for improved sales team training or lead generation strategies.
    
    """,
    "diagnostic_questions": """

    * Which sales channels are driving the majority of our revenue, and are there untapped opportunities in other channels?
    * How do our sales per channel compare to industry benchmarks, and what factors may be influencing these differences?
    
    """,
    "actionable_tips": """

    * Invest in targeted marketing and promotions for underperforming sales channels.
    * Provide additional training and resources for sales teams operating in specific channels to improve performance.
    * Explore partnerships or collaborations to expand reach and access new sales channels.
    
    """,
    "visualization_suggestions": """

    * Pie charts to visually represent the distribution of sales across different channels.
    * Line graphs to track changes in sales per channel over time and identify trends.
    
    """,
    "risk_warnings": """

    * Overreliance on a single sales channel can create vulnerability to market shifts or disruptions in that channel.
    * Ignoring underperforming sales channels may result in missed revenue opportunities and market share loss.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track sales performance and customer interactions across channels.
    * Analytics tools to measure and analyze the effectiveness of different sales channels.
    
    """,
    "integration_points": """

    * Integrate sales per channel data with inventory management systems to ensure adequate stock levels for each channel.
    * Link sales channel performance with customer feedback and satisfaction metrics to understand the impact on overall customer experience.
    
    """,
    "change_impact_analysis": """

    * Shifting sales from in-store to online channels may reduce operational costs but require investment in e-commerce infrastructure.
    * Improving performance in specific sales channels can lead to increased market share and customer loyalty.
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.464867"},
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
                        1035.03,
                        922.66,
                        1043.35,
                        1034.16,
                        960.58,
                        1003.29,
                        989.87,
                        934.07,
                        999.99,
                        928.05,
                        991.5,
                        952.81
                ],
                "unit": "units"
        },
        "current": {
                "value": 952.81,
                "unit": "units",
                "change": -38.69,
                "change_percent": -3.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 982.95,
                "min": 922.66,
                "max": 1043.35,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 255.92,
                        "percentage": 26.9
                },
                {
                        "category": "Category B",
                        "value": 177.54,
                        "percentage": 18.6
                },
                {
                        "category": "Category C",
                        "value": 143.73,
                        "percentage": 15.1
                },
                {
                        "category": "Category D",
                        "value": 51.33,
                        "percentage": 5.4
                },
                {
                        "category": "Other",
                        "value": 324.29,
                        "percentage": 34.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.464867",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales per Channel"
        }
    },
}
