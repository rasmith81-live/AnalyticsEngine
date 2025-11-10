"""
Sales Territory Performance KPI

The performance of sales within specific geographic areas, important for evaluating the effectiveness of territory management.
"""

SALES_TERRITORY_PERFORMANCE = {
    "code": "SALES_TERRITORY_PERFORMANCE",
    "name": "Sales Territory Performance",
    "description": "The performance of sales within specific geographic areas, important for evaluating the effectiveness of territory management.",
    "formula": "Total Sales by Territory / Number of Territories",
    "calculation_formula": "Total Sales by Territory / Number of Territories",
    "category": "Sales Strategy",
    "is_active": True,
    "kpi_definition": "The performance of sales within specific geographic areas, important for evaluating the effectiveness of territory management.",
    "expected_business_insights": "Helps identify high and low-performing regions, influencing resource allocation and territory management.",
    "measurement_approach": "Analyzes sales data by region or territory to measure performance.",
    "trend_analysis": """
    * Increasing sales territory performance may indicate successful expansion or improved sales strategies.
    * Decreasing performance could signal market saturation or ineffective territory management.
    """,
    "diagnostic_questions": """
    * Are there specific territories that consistently outperform or underperform?
    * How does our sales territory performance compare with industry benchmarks or competitor territories?
    """,
    "actionable_tips": """
    * Regularly review and adjust territory boundaries based on sales data and market analysis.
    * Provide additional training and support to sales teams in underperforming territories.
    * Implement incentive programs to motivate sales teams and drive performance in specific territories.
    """,
    "visualization_suggestions": """
    * Heat maps to visualize sales performance by geographic area.
    * Bar charts comparing sales figures across different territories.
    """,
    "risk_warnings": """
    * Low sales territory performance can lead to missed revenue opportunities and market share loss.
    * Highly variable performance across territories may indicate inconsistent sales management practices.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track and analyze sales data by territory.
    * Geospatial analytics tools to visualize and understand geographic sales patterns.
    """,
    "integration_points": """
    * Integrate sales territory performance data with marketing analytics to align sales and marketing efforts in specific regions.
    * Link territory performance with inventory management systems to ensure adequate product availability in high-performing territories.
    """,
    "change_impact_analysis": """
    * Improving sales territory performance can lead to increased market share and revenue growth.
    * However, changes in territory management may require adjustments in resource allocation and sales team structure.
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Territory Assignment"]},
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
}
