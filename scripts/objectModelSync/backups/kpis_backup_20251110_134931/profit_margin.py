"""
Profit Margin

The percentage of revenue that turns into profit after accounting for all expenses, taxes, and interest.
"""

PROFIT_MARGIN = {
    "code": "PROFIT_MARGIN",
    "name": "Profit Margin",
    "description": "The percentage of revenue that turns into profit after accounting for all expenses, taxes, and interest.",
    "formula": "Net Income / Revenue",
    "calculation_formula": "Net Income / Revenue",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Profit Margin to be added.",
    "trend_analysis": """

    * Increasing profit margin over time may indicate improved cost management or pricing strategies.
    * A decreasing margin could signal rising expenses, pricing pressure, or declining sales.
    
    """,
    "diagnostic_questions": """

    * What are the main cost drivers that impact our profit margin?
    * How does our profit margin compare to industry benchmarks or competitors?
    
    """,
    "actionable_tips": """

    * Regularly review and optimize pricing strategies to maintain healthy margins.
    * Focus on cost control measures such as reducing waste, improving operational efficiency, or renegotiating supplier contracts.
    * Explore opportunities for upselling or cross-selling to increase revenue without significantly impacting costs.
    
    """,
    "visualization_suggestions": """

    * Line charts showing profit margin trends over time.
    * Pareto charts to identify the most significant cost drivers impacting margin.
    
    """,
    "risk_warnings": """

    * Declining profit margins can lead to financial instability and reduced investment capacity.
    * Excessively high margins may indicate pricing strategies that could alienate customers or attract regulatory scrutiny.
    
    """,
    "tracking_tools": """

    * Financial management software like QuickBooks or Xero for detailed expense tracking and analysis.
    * Business intelligence tools to identify patterns and correlations between expenses, revenue, and profit margin.
    
    """,
    "integration_points": """

    * Integrate profit margin analysis with sales and marketing systems to understand the impact of pricing and promotions on profitability.
    * Link with supply chain and procurement systems to optimize costs and reduce expenses.
    
    """,
    "change_impact_analysis": """

    * Improving profit margin can lead to increased financial stability and investment opportunities.
    * However, aggressive margin improvement may impact customer loyalty and brand perception if not managed carefully.
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.991064"},
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
                        62396.91,
                        62746.76,
                        54275.21,
                        59395.96,
                        60798.88,
                        53397.63,
                        52218.42,
                        55284.42,
                        53951.39,
                        58346.01,
                        60998.02,
                        50425.97
                ],
                "unit": "$"
        },
        "current": {
                "value": 50425.97,
                "unit": "$",
                "change": -10572.05,
                "change_percent": -17.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 57019.63,
                "min": 50425.97,
                "max": 62746.76,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10263.98,
                        "percentage": 20.4
                },
                {
                        "category": "Category B",
                        "value": 7201.45,
                        "percentage": 14.3
                },
                {
                        "category": "Category C",
                        "value": 7821.71,
                        "percentage": 15.5
                },
                {
                        "category": "Category D",
                        "value": 4997.14,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 20141.69,
                        "percentage": 39.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.991064",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Profit Margin"
        }
    },
}
