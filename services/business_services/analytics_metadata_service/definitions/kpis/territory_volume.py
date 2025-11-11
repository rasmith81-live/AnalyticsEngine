"""
Territory Volume

The volume of sales within a defined sales territory, which can be used to assess market penetration and sales representative performance.
"""

TERRITORY_VOLUME = {
    "code": "TERRITORY_VOLUME",
    "name": "Territory Volume",
    "description": "The volume of sales within a defined sales territory, which can be used to assess market penetration and sales representative performance.",
    "formula": "Total Sales Volume per Territory",
    "calculation_formula": "Total Sales Volume per Territory",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Territory Volume to be added.",
    "trend_analysis": """



    * Increasing territory volume may indicate successful sales strategies or expanding market opportunities.
    * Decreasing volume could signal market saturation or ineffective sales representative performance.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that are driving the majority of sales within the territory?
    * How does the territory volume compare to historical data and industry benchmarks?
    
    
    
    """,
    "actionable_tips": """



    * Provide targeted sales training and support to representatives in underperforming territories.
    * Explore new market segments or potential partnerships to expand territory opportunities.
    * Regularly review and adjust sales territories based on changing market dynamics.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing territory volume over time to identify trends and seasonality.
    * Geospatial maps to visualize territory boundaries and sales distribution.
    
    
    
    """,
    "risk_warnings": """



    * High territory volume may lead to potential resource strain and difficulty in maintaining customer service levels.
    * Low territory volume could indicate missed opportunities or ineffective sales strategies.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track sales activities and customer interactions within each territory.
    * Data analytics tools to identify patterns and opportunities within territory sales data.
    
    
    
    """,
    "integration_points": """



    * Integrate territory volume data with sales forecasting systems to align resource allocation and inventory management.
    * Link territory volume with marketing analytics to understand the impact of promotional activities on sales performance.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing territory volume may require adjustments in supply chain management and customer support to meet growing demand.
    * Decreasing volume could impact revenue projections and overall business growth if not addressed proactively.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Penetration", "Channel Market", "Market Segment", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Territory Assignment"], "last_validated": "2025-11-10T13:49:33.703421"},
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
                        929.64,
                        938.84,
                        970.09,
                        946.42,
                        937.33,
                        1055.46,
                        998.29,
                        1069.32,
                        948.52,
                        958.72,
                        996.45,
                        947.49
                ],
                "unit": "units"
        },
        "current": {
                "value": 947.49,
                "unit": "units",
                "change": -48.96,
                "change_percent": -4.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 974.71,
                "min": 929.64,
                "max": 1069.32,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 229.18,
                        "percentage": 24.2
                },
                {
                        "category": "Channel Sales",
                        "value": 218.85,
                        "percentage": 23.1
                },
                {
                        "category": "Online Sales",
                        "value": 80.03,
                        "percentage": 8.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 74.69,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 344.74,
                        "percentage": 36.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.737447",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Territory Volume"
        }
    },
}
