"""
Sales Growth Year-over-Year

The percentage increase in sales compared to the same period in the previous year.
"""

SALES_GROWTH_YEAR_OVER_YEAR = {
    "code": "SALES_GROWTH_YEAR_OVER_YEAR",
    "name": "Sales Growth Year-over-Year",
    "description": "The percentage increase in sales compared to the same period in the previous year.",
    "formula": "((Sales in Current Year - Sales in Previous Year) / Sales in Previous Year) * 100",
    "calculation_formula": "((Sales in Current Year - Sales in Previous Year) / Sales in Previous Year) * 100",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Growth Year-over-Year to be added.",
    "trend_analysis": """



    * Sales growth tends to fluctuate based on economic conditions, industry trends, and competitive landscape.
    * An upward trend in sales growth may indicate successful product launches, effective marketing campaigns, or improved sales strategies.
    * A downward trend could signal market saturation, increased competition, or shifts in consumer preferences.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors have contributed to the increase or decrease in sales growth compared to the previous year?
    * Are there specific product lines or customer segments driving the changes in sales growth?
    
    
    
    """,
    "actionable_tips": """



    * Invest in market research to identify emerging opportunities and customer needs.
    * Enhance sales training and coaching programs to improve the performance of the sales team.
    * Explore new distribution channels or partnerships to expand market reach.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing year-over-year sales growth by product category or geographic region.
    * Comparative bar graphs to visualize the performance of different sales teams or individual sales representatives.
    
    
    
    """,
    "risk_warnings": """



    * Rapid sales growth may strain operational resources and lead to issues with order fulfillment or customer service.
    * A decline in sales growth could impact revenue projections and shareholder confidence.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track sales activities and customer interactions.
    * Business intelligence tools for analyzing sales data and identifying trends or opportunities.
    
    
    
    """,
    "integration_points": """



    * Integrate sales growth data with inventory management systems to ensure adequate stock levels to meet demand.
    * Link sales growth metrics with financial reporting systems to assess the impact on overall revenue and profitability.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing sales growth may require additional investment in marketing and sales resources.
    * Declining sales growth could necessitate cost-cutting measures or strategic shifts in product offerings.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.432227"},
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
                        47.9,
                        46.78,
                        63.99,
                        48.87,
                        50.42,
                        65.96,
                        64.54,
                        63.57,
                        51.69,
                        63.37,
                        51.96,
                        64.1
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.1,
                "unit": "%",
                "change": 12.14,
                "change_percent": 23.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 56.93,
                "min": 46.78,
                "max": 65.96,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 20.97,
                        "percentage": 32.7
                },
                {
                        "category": "Channel Sales",
                        "value": 7.1,
                        "percentage": 11.1
                },
                {
                        "category": "Online Sales",
                        "value": 6.61,
                        "percentage": 10.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.55,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 24.87,
                        "percentage": 38.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.010402",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Growth Year-over-Year"
        }
    },
}
