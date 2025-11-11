"""
Product Performance

The sales success of individual products or services, which helps in analyzing which items are performing well and which are not.
"""

PRODUCT_PERFORMANCE = {
    "code": "PRODUCT_PERFORMANCE",
    "name": "Product Performance",
    "description": "The sales success of individual products or services, which helps in analyzing which items are performing well and which are not.",
    "formula": "Varies Depending on Specific Product Metrics Analyzed",
    "calculation_formula": "Varies Depending on Specific Product Metrics Analyzed",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Performance to be added.",
    "trend_analysis": """



    * Identifying which products or services are consistently top performers over time.
    * Analyzing the trend of underperforming products to determine if there are common factors contributing to their lack of success.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that consistently outperform others?
    * What factors contribute to the success or failure of individual products or services?
    
    
    
    """,
    "actionable_tips": """



    * Regularly review and update product or service offerings based on performance data.
    * Invest in marketing and promotional efforts for underperforming products to boost sales.
    * Consider adjusting pricing or packaging for products based on their performance.
    
    
    
    """,
    "visualization_suggestions": """



    * Pareto charts to identify the most significant contributors to overall sales performance.
    * Line graphs to track the performance of individual products or services over time.
    
    
    
    """,
    "risk_warnings": """



    * Over-reliance on a few top-performing products may lead to vulnerability if their sales decline.
    * Ignoring underperforming products may result in missed opportunities for improvement or innovation.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems to track customer preferences and purchasing behavior for different products or services.
    * Market research tools to gather insights on consumer trends and preferences.
    
    
    
    """,
    "integration_points": """



    * Integrate product performance data with inventory management systems to ensure adequate stock levels for top-performing items.
    * Link product performance with marketing and sales systems to align promotional efforts with successful products.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the performance of underperforming products can lead to increased overall sales and revenue.
    * Shifting focus away from top-performing products may impact short-term sales but could lead to long-term diversification and stability.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Market", "Customer Success Manager", "Market Segment", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.269150"},
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
                        954.74,
                        1025.45,
                        931.84,
                        985.77,
                        949.09,
                        894.66,
                        1035.55,
                        930.69,
                        984.29,
                        954.05,
                        966.77,
                        960.85
                ],
                "unit": "units"
        },
        "current": {
                "value": 960.85,
                "unit": "units",
                "change": -5.92,
                "change_percent": -0.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 964.48,
                "min": 894.66,
                "max": 1035.55,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 287.08,
                        "percentage": 29.9
                },
                {
                        "category": "Product Line B",
                        "value": 219.22,
                        "percentage": 22.8
                },
                {
                        "category": "Product Line C",
                        "value": 146.23,
                        "percentage": 15.2
                },
                {
                        "category": "Services",
                        "value": 39.52,
                        "percentage": 4.1
                },
                {
                        "category": "Other",
                        "value": 268.8,
                        "percentage": 28.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.639748",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Product Performance"
        }
    },
}
