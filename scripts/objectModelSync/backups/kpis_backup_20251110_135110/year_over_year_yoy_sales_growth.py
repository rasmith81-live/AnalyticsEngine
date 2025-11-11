"""
Year-over-Year (YoY) Sales Growth

The increase in sales revenue compared to the same period in the previous year.
"""

YEAR_OVER_YEAR_YOY_SALES_GROWTH = {
    "code": "YEAR_OVER_YEAR_YOY_SALES_GROWTH",
    "name": "Year-over-Year (YoY) Sales Growth",
    "description": "The increase in sales revenue compared to the same period in the previous year.",
    "formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "calculation_formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Year-over-Year (YoY) Sales Growth to be added.",
    "trend_analysis": """


    * Year-over-year sales growth tends to show seasonal fluctuations, with certain periods of the year consistently outperforming others.
    * A consistent upward trend in year-over-year sales growth may indicate successful product launches, market expansion, or improved sales strategies.
    
    
    """,
    "diagnostic_questions": """


    * What factors contributed to the increase or decrease in year-over-year sales growth during specific periods?
    * How does the year-over-year sales growth compare to industry averages and competitors' performance?
    
    
    """,
    "actionable_tips": """


    * Invest in targeted marketing campaigns to capitalize on peak sales periods and drive year-over-year growth.
    * Regularly assess and adjust pricing strategies to maximize revenue and stimulate sales growth.
    * Provide sales teams with ongoing training and support to enhance their ability to close deals and drive revenue growth.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing year-over-year sales growth by month or quarter to visualize seasonal trends.
    * Comparative bar charts to highlight year-over-year growth rates for different product categories or customer segments.
    
    
    """,
    "risk_warnings": """


    * A decline in year-over-year sales growth may indicate market saturation, increased competition, or shifts in customer preferences.
    * Rapid growth in year-over-year sales may strain operational capacity, leading to fulfillment and customer service challenges.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track and analyze sales performance and customer behavior.
    * Business Intelligence (BI) tools to identify patterns and correlations that contribute to year-over-year sales growth.
    
    
    """,
    "integration_points": """


    * Integrate year-over-year sales growth data with marketing analytics to evaluate the effectiveness of promotional efforts.
    * Link sales growth metrics with inventory management systems to ensure adequate stock levels to support increased demand.
    
    
    """,
    "change_impact_analysis": """


    * Improving year-over-year sales growth can lead to increased profitability and market share, but may require additional resources and investments.
    * A decline in year-over-year sales growth can impact cash flow, profitability, and overall business performance.
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "replaces": ["YEAR_OVER_YEAR_GROWTH"], "last_validated": "2025-11-10T13:49:33.827123"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_STRATEGY"],
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
                        329.05,
                        323.64,
                        434.12,
                        302.72,
                        410.96,
                        368.55,
                        343.8,
                        335.28,
                        412.83,
                        328.01,
                        334.59,
                        347.92
                ],
                "unit": "units"
        },
        "current": {
                "value": 347.92,
                "unit": "units",
                "change": 13.33,
                "change_percent": 4.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 355.96,
                "min": 302.72,
                "max": 434.12,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 66.74,
                        "percentage": 19.2
                },
                {
                        "category": "Category B",
                        "value": 73.1,
                        "percentage": 21.0
                },
                {
                        "category": "Category C",
                        "value": 47.77,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 20.26,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 140.05,
                        "percentage": 40.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.295933",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Year-over-Year (YoY) Sales Growth"
        }
    },
}
