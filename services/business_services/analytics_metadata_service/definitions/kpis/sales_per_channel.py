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
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.449912"},
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
                        645.88,
                        589.81,
                        600.81,
                        524.43,
                        499.89,
                        626.02,
                        505.07,
                        516.17,
                        519.36,
                        577.66,
                        575.54,
                        567.68
                ],
                "unit": "units"
        },
        "current": {
                "value": 567.68,
                "unit": "units",
                "change": -7.86,
                "change_percent": -1.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 562.36,
                "min": 499.89,
                "max": 645.88,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 90.88,
                        "percentage": 16.0
                },
                {
                        "category": "Channel Sales",
                        "value": 135.33,
                        "percentage": 23.8
                },
                {
                        "category": "Online Sales",
                        "value": 68.08,
                        "percentage": 12.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 37.66,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 235.73,
                        "percentage": 41.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.064315",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales per Channel"
        }
    },
}
