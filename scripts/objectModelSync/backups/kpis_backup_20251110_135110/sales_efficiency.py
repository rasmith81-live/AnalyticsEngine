"""
Sales Efficiency

The ratio of revenue generated to the cost of sales and marketing efforts.
"""

SALES_EFFICIENCY = {
    "code": "SALES_EFFICIENCY",
    "name": "Sales Efficiency",
    "description": "The ratio of revenue generated to the cost of sales and marketing efforts.",
    "formula": "Revenue Generated / Cost of Sales Activities",
    "calculation_formula": "Revenue Generated / Cost of Sales Activities",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Efficiency to be added.",
    "trend_analysis": """


    * Increasing sales efficiency may indicate improved targeting and effectiveness of sales and marketing efforts.
    * Decreasing sales efficiency could signal increased competition, market saturation, or inefficiencies in the sales process.
    
    
    """,
    "diagnostic_questions": """


    * What specific sales and marketing activities contribute most to revenue generation?
    * Are there any market or competitive factors impacting the cost-effectiveness of our sales efforts?
    
    
    """,
    "actionable_tips": """


    * Regularly review and optimize sales and marketing strategies to ensure maximum impact for the cost incurred.
    * Invest in training and development for sales teams to improve their effectiveness and efficiency.
    * Utilize customer relationship management (CRM) software to better track and manage sales activities and customer interactions.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of sales efficiency over time.
    * Pie charts comparing the proportion of revenue generated to the cost of different sales and marketing activities.
    
    
    """,
    "risk_warnings": """


    * Declining sales efficiency may lead to reduced profitability and financial performance.
    * High sales efficiency without corresponding revenue growth may indicate missed opportunities for investment and expansion.
    
    
    """,
    "tracking_tools": """


    * Sales analytics platforms like Tableau or Power BI to track and analyze sales efficiency metrics.
    * Marketing automation tools to streamline and optimize marketing efforts for better cost-effectiveness.
    
    
    """,
    "integration_points": """


    * Integrate sales efficiency data with financial reporting systems to understand its impact on overall profitability.
    * Link sales efficiency with customer relationship management (CRM) systems to identify the most cost-effective customer acquisition channels.
    
    
    """,
    "change_impact_analysis": """


    * Improving sales efficiency can lead to increased profitability and better resource allocation.
    * However, a singular focus on sales efficiency may neglect the quality of customer interactions and long-term customer relationships.
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.408446"},
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
                        600.82,
                        709.43,
                        708.18,
                        581.59,
                        684.16,
                        630.73,
                        621.62,
                        697.77,
                        671.35,
                        603.24,
                        645.13,
                        723.81
                ],
                "unit": "units"
        },
        "current": {
                "value": 723.81,
                "unit": "units",
                "change": 78.68,
                "change_percent": 12.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 656.49,
                "min": 581.59,
                "max": 723.81,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 230.04,
                        "percentage": 31.8
                },
                {
                        "category": "Category B",
                        "value": 168.04,
                        "percentage": 23.2
                },
                {
                        "category": "Category C",
                        "value": 95.81,
                        "percentage": 13.2
                },
                {
                        "category": "Category D",
                        "value": 28.28,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 201.64,
                        "percentage": 27.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.364175",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Efficiency"
        }
    },
}
