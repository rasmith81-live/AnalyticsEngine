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
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.692567"},
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
                        659.44,
                        681.78,
                        646.76,
                        700.37,
                        722.5,
                        673.89,
                        612.25,
                        637.14,
                        731.86,
                        733.13,
                        709.94,
                        641.15
                ],
                "unit": "units"
        },
        "current": {
                "value": 641.15,
                "unit": "units",
                "change": -68.79,
                "change_percent": -9.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 679.18,
                "min": 612.25,
                "max": 733.13,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 108.43,
                        "percentage": 16.9
                },
                {
                        "category": "Category B",
                        "value": 142.83,
                        "percentage": 22.3
                },
                {
                        "category": "Category C",
                        "value": 80.61,
                        "percentage": 12.6
                },
                {
                        "category": "Category D",
                        "value": 89.42,
                        "percentage": 13.9
                },
                {
                        "category": "Other",
                        "value": 219.86,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.692567",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Volume"
        }
    },
}
