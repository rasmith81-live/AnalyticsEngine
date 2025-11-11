"""
Discount Percentage

The average discount percentage applied to sales during a specific period.
"""

DISCOUNT_PERCENTAGE = {
    "code": "DISCOUNT_PERCENTAGE",
    "name": "Discount Percentage",
    "description": "The average discount percentage applied to sales during a specific period.",
    "formula": "(Total Discounts Given / Total Sales Revenue Before Discounts) * 100",
    "calculation_formula": "(Total Discounts Given / Total Sales Revenue Before Discounts) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Discount Percentage to be added.",
    "trend_analysis": """


    * Increasing discount percentage may indicate a need to boost sales or clear excess inventory.
    * Decreasing discount percentage could signal improved pricing strategies or stronger customer loyalty.
    
    
    """,
    "diagnostic_questions": """


    * What factors are driving the need for higher discounts?
    * Are there specific customer segments or products that consistently require discounts?
    
    
    """,
    "actionable_tips": """


    * Implement targeted marketing campaigns to attract new customers and reduce the need for broad discounts.
    * Analyze customer buying patterns to identify opportunities for personalized pricing or bundling.
    * Train sales teams to effectively communicate the value of products and services to reduce reliance on discounts.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing discount percentage trends over time.
    * Pie charts comparing discount percentages across different sales channels or customer segments.
    
    
    """,
    "risk_warnings": """


    * Excessive discounting can erode profit margins and devalue products in the eyes of customers.
    * Consistently high discount percentages may indicate pricing or product issues that need to be addressed.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems to track customer behavior and preferences.
    * Pricing optimization software to analyze market data and recommend competitive pricing strategies.
    
    
    """,
    "integration_points": """


    * Integrate discount percentage data with sales performance metrics to understand the impact on revenue and profitability.
    * Link with inventory management systems to align discount strategies with inventory levels and turnover.
    
    
    """,
    "change_impact_analysis": """


    * Increasing discounts may boost short-term sales but could impact long-term brand perception and profitability.
    * Reducing discounts may lead to higher margins and improved brand value, but could require a shift in sales and marketing strategies.
    
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Deal", "Lost Sale", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.931061"},
    "required_objects": [],
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
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
                        46.03,
                        43.89,
                        36.64,
                        47.13,
                        42.57,
                        37.12,
                        44.53,
                        33.35,
                        41.91,
                        31.81,
                        47.05,
                        36.4
                ],
                "unit": "%"
        },
        "current": {
                "value": 36.4,
                "unit": "%",
                "change": -10.65,
                "change_percent": -22.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 40.7,
                "min": 31.81,
                "max": 47.13,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.25,
                        "percentage": 25.4
                },
                {
                        "category": "Category B",
                        "value": 7.5,
                        "percentage": 20.6
                },
                {
                        "category": "Category C",
                        "value": 6.49,
                        "percentage": 17.8
                },
                {
                        "category": "Category D",
                        "value": 3.93,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 9.23,
                        "percentage": 25.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.443926",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Discount Percentage"
        }
    },
}
