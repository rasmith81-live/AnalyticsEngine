"""
Sales Territory Performance

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
    "full_kpi_definition": "Complete definition for Sales Territory Performance to be added.",
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
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Territory Assignment"], "last_validated": "2025-11-10T13:43:24.656503"},
    "required_objects": [],
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
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
                        331,
                        315,
                        284,
                        328,
                        294,
                        329,
                        306,
                        292,
                        320,
                        326,
                        332,
                        299
                ],
                "unit": "count"
        },
        "current": {
                "value": 299,
                "unit": "count",
                "change": -33,
                "change_percent": -9.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 313.0,
                "min": 284,
                "max": 332,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 85.66,
                        "percentage": 28.6
                },
                {
                        "category": "Category B",
                        "value": 69.65,
                        "percentage": 23.3
                },
                {
                        "category": "Category C",
                        "value": 35.19,
                        "percentage": 11.8
                },
                {
                        "category": "Category D",
                        "value": 29.87,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 78.63,
                        "percentage": 26.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.656503",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Territory Performance"
        }
    },
}
