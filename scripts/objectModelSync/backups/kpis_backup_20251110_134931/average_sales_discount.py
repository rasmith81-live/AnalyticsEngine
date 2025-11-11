"""
Average Sales Discount

The average discount rate applied to sales during a particular period.
"""

AVERAGE_SALES_DISCOUNT = {
    "code": "AVERAGE_SALES_DISCOUNT",
    "name": "Average Sales Discount",
    "description": "The average discount rate applied to sales during a particular period.",
    "formula": "Sum of all Discount Percentages Offered / Number of Discounted Deals",
    "calculation_formula": "Sum of all Discount Percentages Offered / Number of Discounted Deals",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Sales Discount to be added.",
    "trend_analysis": """

    * Increasing average sales discount may indicate a need to move excess inventory or meet aggressive sales targets.
    * Decreasing average sales discount could signal improved pricing strategies or increased customer loyalty.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or customer segments that consistently receive higher discounts?
    * How does our average sales discount compare with industry benchmarks or competitor pricing?
    
    """,
    "actionable_tips": """

    * Implement dynamic pricing strategies based on customer behavior and market conditions.
    * Provide sales teams with negotiation training to maintain margins while meeting customer needs.
    * Analyze the impact of discounts on overall profitability to ensure they are strategic and sustainable.
    
    """,
    "visualization_suggestions": """

    * Line charts showing average sales discount over time to identify seasonal or cyclical patterns.
    * Pie charts comparing discount rates across different product categories or customer segments.
    
    """,
    "risk_warnings": """

    * Excessive discounting can erode profit margins and devalue the brand in the eyes of customers.
    * Consistently low discount rates may indicate an inability to compete effectively in the market.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track discounting trends by customer and sales representative.
    * Price optimization tools to analyze pricing elasticity and recommend optimal discount levels.
    
    """,
    "integration_points": """

    * Integrate average sales discount data with customer satisfaction metrics to understand the impact of discounts on customer loyalty.
    * Link discount rates with inventory management systems to ensure discounts are aligned with inventory levels and turnover.
    
    """,
    "change_impact_analysis": """

    * Increasing average sales discount may boost short-term sales but could impact long-term profitability and brand perception.
    * Decreasing average sales discount may improve margins but could require additional efforts to maintain customer satisfaction and loyalty.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.041051"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        268,
                        296,
                        280,
                        306,
                        284,
                        311,
                        317,
                        278,
                        298,
                        282,
                        277,
                        297
                ],
                "unit": "count"
        },
        "current": {
                "value": 297,
                "unit": "count",
                "change": 20,
                "change_percent": 7.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 291.17,
                "min": 268,
                "max": 317,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 84.9,
                        "percentage": 28.6
                },
                {
                        "category": "Category B",
                        "value": 34.96,
                        "percentage": 11.8
                },
                {
                        "category": "Category C",
                        "value": 35.17,
                        "percentage": 11.8
                },
                {
                        "category": "Category D",
                        "value": 15.21,
                        "percentage": 5.1
                },
                {
                        "category": "Other",
                        "value": 126.76,
                        "percentage": 42.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.041051",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Sales Discount"
        }
    },
}
