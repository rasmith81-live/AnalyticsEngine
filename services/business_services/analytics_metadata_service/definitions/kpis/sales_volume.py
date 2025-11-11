"""
Sales Volume

The total number of sales made by the outside sales team.
"""

SALES_VOLUME = {
    "code": "SALES_VOLUME",
    "name": "Sales Volume",
    "description": "The total number of sales made by the outside sales team.",
    "formula": "Sum of all Products Sold or Total Revenue from Sales",
    "calculation_formula": "Sum of all Products Sold or Total Revenue from Sales",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Volume to be added.",
    "trend_analysis": """



    * Increasing sales volume may indicate growing market demand or improved sales strategies.
    * Decreasing sales volume could signal market saturation, ineffective sales tactics, or economic downturn.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors have contributed to the changes in sales volume over time?
    * Are there specific products or regions driving the changes in sales volume?
    
    
    
    """,
    "actionable_tips": """



    * Invest in sales training and development programs to improve the effectiveness of the sales team.
    * Explore new markets or customer segments to expand the potential customer base.
    * Implement customer relationship management (CRM) software to better track and manage sales activities.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts to visualize the trend in sales volume over time.
    * Pie charts to compare sales volume by product category or region.
    
    
    
    """,
    "risk_warnings": """



    * Low sales volume can lead to revenue shortfalls and financial instability.
    * High sales volume without proper capacity planning can result in fulfillment challenges and customer dissatisfaction.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems like Salesforce or HubSpot for tracking and managing sales activities.
    * Data analytics tools to identify patterns and insights related to sales volume.
    
    
    
    """,
    "integration_points": """



    * Integrate sales volume data with inventory management systems to ensure adequate stock levels to meet demand.
    * Link sales volume with customer relationship management platforms to understand customer buying behavior and preferences.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing sales volume may require additional resources and infrastructure to support higher demand.
    * Decreasing sales volume can impact cash flow and profitability, potentially leading to cost-cutting measures.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.539490"},
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
                        372.5,
                        416.68,
                        307.96,
                        383.64,
                        334.06,
                        362.94,
                        405.21,
                        357.6,
                        389.85,
                        284.21,
                        361.43,
                        338.38
                ],
                "unit": "units"
        },
        "current": {
                "value": 338.38,
                "unit": "units",
                "change": -23.05,
                "change_percent": -6.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 359.54,
                "min": 284.21,
                "max": 416.68,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 81.27,
                        "percentage": 24.0
                },
                {
                        "category": "Product Line B",
                        "value": 66.07,
                        "percentage": 19.5
                },
                {
                        "category": "Product Line C",
                        "value": 39.11,
                        "percentage": 11.6
                },
                {
                        "category": "Services",
                        "value": 27.44,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 124.49,
                        "percentage": 36.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.299674",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Volume"
        }
    },
}
