"""
Number of Demos Conducted

The total number of product demonstrations performed by the sales team.
"""

NUMBER_OF_DEMOS_CONDUCTED = {
    "code": "NUMBER_OF_DEMOS_CONDUCTED",
    "name": "Number of Demos Conducted",
    "description": "The total number of product demonstrations performed by the sales team.",
    "formula": "Total Number of Product Demonstrations Given",
    "calculation_formula": "Total Number of Product Demonstrations Given",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Demos Conducted to be added.",
    "trend_analysis": """



    * An increasing number of demos conducted may indicate a growing interest in the product or improved sales team performance.
    * A decreasing number of demos could signal market saturation, lack of product relevance, or sales team inefficiency.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or features that are consistently included in successful demos?
    * How does the number of demos conducted compare to the number of leads generated or deals closed?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional sales training or resources to improve demo quality and effectiveness.
    * Implement lead scoring to prioritize demos for the most promising prospects.
    * Regularly review and update demo scripts and materials to ensure relevance and impact.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of demos conducted over time.
    * Pie charts comparing the distribution of demos across different products or customer segments.
    
    
    
    """,
    "risk_warnings": """



    * A low number of demos may lead to missed sales opportunities and revenue loss.
    * Too many demos without corresponding sales may indicate a problem with the sales process or product-market fit.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with built-in demo scheduling and tracking capabilities.
    * Screen recording and analytics tools to assess the effectiveness of demos.
    
    
    
    """,
    "integration_points": """



    * Integrate demo data with lead management systems to track conversion rates from demos to deals.
    * Link demo performance with customer feedback and satisfaction metrics to gauge impact on overall sales experience.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing the number of demos may lead to higher sales volume but could also strain sales team resources and time.
    * Decreasing the number of demos may free up resources but could also limit exposure to potential customers and hinder market expansion.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Demo", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.089106"},
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
                        106,
                        111,
                        115,
                        114,
                        92,
                        97,
                        98,
                        132,
                        94,
                        98,
                        107,
                        112
                ],
                "unit": "count"
        },
        "current": {
                "value": 112,
                "unit": "count",
                "change": 5,
                "change_percent": 4.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 106.33,
                "min": 92,
                "max": 132,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 32.24,
                        "percentage": 28.8
                },
                {
                        "category": "Product Line B",
                        "value": 20.95,
                        "percentage": 18.7
                },
                {
                        "category": "Product Line C",
                        "value": 17.35,
                        "percentage": 15.5
                },
                {
                        "category": "Services",
                        "value": 9.75,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 31.71,
                        "percentage": 28.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.263921",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Number of Demos Conducted"
        }
    },
}
