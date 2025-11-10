"""
Sales per Channel KPI

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
    "kpi_definition": "The distribution of sales across different sales channels, which can include online, in-store, direct sales, or partner sales.",
    "expected_business_insights": "Identifies the most effective sales channels and opportunities for channel optimization.",
    "measurement_approach": "Assesses sales revenue generated from each distribution channel.",
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
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
}
