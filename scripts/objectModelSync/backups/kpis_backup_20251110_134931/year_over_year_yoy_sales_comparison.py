"""
Year-over-Year (YoY) Sales Comparison

A comparison of sales figures from one year to the same period in the previous year, indicating trends and growth patterns.
"""

YEAR_OVER_YEAR_YOY_SALES_COMPARISON = {
    "code": "YEAR_OVER_YEAR_YOY_SALES_COMPARISON",
    "name": "Year-over-Year (YoY) Sales Comparison",
    "description": "A comparison of sales figures from one year to the same period in the previous year, indicating trends and growth patterns.",
    "formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "calculation_formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Year-over-Year (YoY) Sales Comparison to be added.",
    "trend_analysis": """

    * Positive trends in YoY sales comparison may indicate successful marketing strategies or product innovations that are resonating with customers.
    * Negative trends could signal market saturation, increased competition, or economic downturns affecting consumer spending.
    
    """,
    "diagnostic_questions": """

    * Are there specific regions or customer segments driving the YoY sales growth or decline?
    * How do external factors such as industry trends or regulatory changes impact YoY sales performance?
    
    """,
    "actionable_tips": """

    * Invest in market research to identify emerging opportunities and customer preferences.
    * Adjust pricing strategies or promotional activities based on seasonal variations or competitive pressures.
    * Enhance sales team training and performance management to capitalize on growth opportunities and address declining sales trends.
    
    """,
    "visualization_suggestions": """

    * Line charts to visualize the trajectory of YoY sales comparison over time.
    * Stacked bar graphs to compare sales performance by product categories or geographic regions.
    
    """,
    "risk_warnings": """

    * Declining YoY sales may lead to revenue shortfalls and impact overall business profitability.
    * Rapid YoY sales growth without proper capacity planning can strain operational resources and lead to customer dissatisfaction.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track customer interactions and identify sales opportunities.
    * Business Intelligence (BI) tools for in-depth analysis of sales data and performance metrics.
    
    """,
    "integration_points": """

    * Integrate YoY sales comparison with inventory management systems to ensure adequate stock levels to meet demand.
    * Link sales performance with financial systems to analyze the impact on revenue and profitability.
    
    """,
    "change_impact_analysis": """

    * Improving YoY sales comparison can lead to increased market share and brand recognition.
    * Conversely, declining sales performance may necessitate cost-cutting measures or strategic repositioning to remain competitive.
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:25.292639"},
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
                        740.62,
                        796.95,
                        778.16,
                        805.56,
                        838.34,
                        821.77,
                        814.42,
                        783.14,
                        858.85,
                        745.48,
                        855.99,
                        799.49
                ],
                "unit": "units"
        },
        "current": {
                "value": 799.49,
                "unit": "units",
                "change": -56.5,
                "change_percent": -6.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 803.23,
                "min": 740.62,
                "max": 858.85,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 167.82,
                        "percentage": 21.0
                },
                {
                        "category": "Category B",
                        "value": 103.25,
                        "percentage": 12.9
                },
                {
                        "category": "Category C",
                        "value": 100.78,
                        "percentage": 12.6
                },
                {
                        "category": "Category D",
                        "value": 69.89,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 357.75,
                        "percentage": 44.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.292639",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Year-over-Year (YoY) Sales Comparison"
        }
    },
}
