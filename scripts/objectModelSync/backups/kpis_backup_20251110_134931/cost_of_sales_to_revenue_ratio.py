"""
Cost of Sales to Revenue Ratio

The ratio of the cost of sales (including salaries, commissions, expenses) to the total revenue generated.
"""

COST_OF_SALES_TO_REVENUE_RATIO = {
    "code": "COST_OF_SALES_TO_REVENUE_RATIO",
    "name": "Cost of Sales to Revenue Ratio",
    "description": "The ratio of the cost of sales (including salaries, commissions, expenses) to the total revenue generated.",
    "formula": "Total Cost of Sales / Total Revenue",
    "calculation_formula": "Total Cost of Sales / Total Revenue",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost of Sales to Revenue Ratio to be added.",
    "trend_analysis": """

    * An increasing cost of sales to revenue ratio may indicate rising expenses relative to revenue, potentially signaling inefficiencies in the sales process or increased costs that are not being offset by revenue growth.
    * A decreasing ratio could suggest improved cost management, increased sales efficiency, or a decline in costs relative to revenue.
    
    """,
    "diagnostic_questions": """

    * What specific cost components are driving the increase in the cost of sales to revenue ratio?
    * How does our cost of sales to revenue ratio compare with industry benchmarks or historical performance?
    
    """,
    "actionable_tips": """

    * Implement cost control measures to reduce unnecessary expenses and improve sales efficiency.
    * Explore opportunities to increase revenue through upselling, cross-selling, or expanding into new markets.
    * Regularly review and optimize sales compensation and incentive structures to ensure alignment with revenue generation.
    
    """,
    "visualization_suggestions": """

    * Line charts to track the trend of the cost of sales to revenue ratio over time.
    * Stacked bar charts to visually represent the composition of the cost of sales and its relationship to revenue.
    
    """,
    "risk_warnings": """

    * A high cost of sales to revenue ratio can erode profitability and indicate potential financial challenges.
    * Chronic increases in the ratio may point to systemic issues in sales management, resource allocation, or pricing strategies.
    
    """,
    "tracking_tools": """

    * CRM systems with robust reporting capabilities to track sales-related expenses and revenue generation.
    * Business intelligence tools for in-depth analysis of cost components and revenue sources.
    
    """,
    "integration_points": """

    * Integrate cost of sales to revenue ratio analysis with financial reporting systems for a comprehensive view of sales performance.
    * Link with sales forecasting and planning systems to align resource allocation with revenue targets.
    
    """,
    "change_impact_analysis": """

    * Reducing the cost of sales to revenue ratio may lead to improved profitability but could require strategic shifts in sales operations and resource allocation.
    * Conversely, a high ratio can impact overall financial health and may necessitate changes in pricing, sales strategies, or cost management.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.162768"},
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
                        73.18,
                        71.46,
                        74.62,
                        67.92,
                        63.12,
                        58.11,
                        58.11,
                        64.72,
                        76.23,
                        76.25,
                        56.89,
                        62.07
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.07,
                "unit": "%",
                "change": 5.18,
                "change_percent": 9.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 66.89,
                "min": 56.89,
                "max": 76.25,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.31,
                        "percentage": 16.6
                },
                {
                        "category": "Category B",
                        "value": 17.56,
                        "percentage": 28.3
                },
                {
                        "category": "Category C",
                        "value": 11.16,
                        "percentage": 18.0
                },
                {
                        "category": "Category D",
                        "value": 4.65,
                        "percentage": 7.5
                },
                {
                        "category": "Other",
                        "value": 18.39,
                        "percentage": 29.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.162768",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Cost of Sales to Revenue Ratio"
        }
    },
}
