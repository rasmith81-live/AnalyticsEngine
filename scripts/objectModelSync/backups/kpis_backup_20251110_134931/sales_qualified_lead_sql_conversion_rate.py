"""
Sales Qualified Lead (SQL) Conversion Rate

The percentage of sales qualified leads that convert into opportunities or sales.
"""

SALES_QUALIFIED_LEAD_SQL_CONVERSION_RATE = {
    "code": "SALES_QUALIFIED_LEAD_SQL_CONVERSION_RATE",
    "name": "Sales Qualified Lead (SQL) Conversion Rate",
    "description": "The percentage of sales qualified leads that convert into opportunities or sales.",
    "formula": "(Number of SQLs that Convert to Sales or Opportunities / Total Number of SQLs) * 100",
    "calculation_formula": "(Number of SQLs that Convert to Sales or Opportunities / Total Number of SQLs) * 100",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Qualified Lead (SQL) Conversion Rate to be added.",
    "trend_analysis": """

    * An increasing SQL conversion rate may indicate improved lead qualification processes or a higher demand for the product or service.
    * A decreasing rate could signal issues with lead quality, sales follow-up, or changes in market conditions.
    
    """,
    "diagnostic_questions": """

    * Are there specific criteria used to qualify leads as sales qualified? Are these criteria still relevant and effective?
    * What is the follow-up process for sales qualified leads? Are there any bottlenecks or gaps in the process?
    
    """,
    "actionable_tips": """

    * Regularly review and update the criteria for sales qualified leads to ensure they align with the ideal customer profile and current market conditions.
    * Provide ongoing training and support for sales representatives to improve their ability to convert sales qualified leads into opportunities or sales.
    * Implement lead nurturing strategies to maintain engagement with sales qualified leads that are not yet ready to make a purchase.
    
    """,
    "visualization_suggestions": """

    * Funnel charts to visualize the conversion rates at each stage of the sales process.
    * Line graphs to track the trend of SQL conversion rates over time.
    
    """,
    "risk_warnings": """

    * A low SQL conversion rate can lead to wasted resources and decreased sales effectiveness.
    * A high SQL conversion rate without corresponding sales growth may indicate issues with lead quality or sales tactics.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and manage sales qualified leads and their interactions with the sales team.
    * Sales enablement platforms to provide sales representatives with the tools and content they need to effectively engage and convert leads.
    
    """,
    "integration_points": """

    * Integrate the SQL conversion rate with marketing automation platforms to align lead generation efforts with the sales qualification process.
    * Connect the SQL conversion rate with revenue and pipeline metrics to understand the impact of lead quality on overall sales performance.
    
    """,
    "change_impact_analysis": """

    * Improving the SQL conversion rate can lead to more efficient use of sales resources and increased revenue generation.
    * However, a significant increase in the SQL conversion rate may require adjustments in sales capacity and resources to handle the higher volume of opportunities or sales.
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Lead Qualification", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.547189"},
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
                        79.55,
                        81.35,
                        67.59,
                        66.62,
                        67.56,
                        66.31,
                        81.43,
                        77.54,
                        72.51,
                        71.73,
                        64.6,
                        80.96
                ],
                "unit": "%"
        },
        "current": {
                "value": 80.96,
                "unit": "%",
                "change": 16.36,
                "change_percent": 25.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.15,
                "min": 64.6,
                "max": 81.43,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.0,
                        "percentage": 23.5
                },
                {
                        "category": "Category B",
                        "value": 12.14,
                        "percentage": 15.0
                },
                {
                        "category": "Category C",
                        "value": 14.14,
                        "percentage": 17.5
                },
                {
                        "category": "Category D",
                        "value": 9.25,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 26.43,
                        "percentage": 32.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.547189",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Qualified Lead (SQL) Conversion Rate"
        }
    },
}
