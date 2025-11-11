"""
Operating Margin

A measure of what portion of a company's revenue is left over after paying for variable costs of production like wages and raw materials.
"""

OPERATING_MARGIN = {
    "code": "OPERATING_MARGIN",
    "name": "Operating Margin",
    "description": "A measure of what portion of a company's revenue is left over after paying for variable costs of production like wages and raw materials.",
    "formula": "Operating Income / Net Sales",
    "calculation_formula": "Operating Income / Net Sales",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Operating Margin to be added.",
    "trend_analysis": """



    * Operating margin tends to increase when there is efficient cost management and pricing strategies.
    * A declining trend may indicate rising production costs or pricing pressures in the market.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the main cost drivers impacting our operating margin?
    * How does our operating margin compare to industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Implement cost-saving measures such as lean production or renegotiating supplier contracts.
    * Regularly review pricing strategies to ensure they align with cost structures and market conditions.
    * Invest in technologies that can automate processes and reduce variable costs.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of operating margin over time.
    * Stacked bar charts comparing operating margin by product lines or business segments.
    
    
    
    """,
    "risk_warnings": """



    * A declining operating margin may lead to reduced profitability and financial instability.
    * High operating margins without corresponding investment in growth initiatives may limit long-term business expansion.
    
    
    
    """,
    "tracking_tools": """



    * Financial management software like QuickBooks or SAP for accurate tracking and analysis of cost and revenue data.
    * Business intelligence tools to identify cost-saving opportunities and optimize pricing strategies.
    
    
    
    """,
    "integration_points": """



    * Integrate operating margin analysis with budgeting and forecasting systems to align financial goals with operational performance.
    * Link with sales and marketing systems to understand the impact of pricing and promotions on operating margin.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving operating margin can lead to increased profitability but may require changes in cost structures and pricing strategies.
    * Conversely, a declining operating margin can affect investment capacity and shareholder confidence.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.104637"},
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
                        77016.22,
                        82029.41,
                        74527.36,
                        67829.29,
                        69044.0,
                        68548.09,
                        74704.23,
                        77170.41,
                        68262.5,
                        71626.81,
                        69995.34,
                        75668.63
                ],
                "unit": "$"
        },
        "current": {
                "value": 75668.63,
                "unit": "$",
                "change": 5673.29,
                "change_percent": 8.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 73035.19,
                "min": 67829.29,
                "max": 82029.41,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 23824.77,
                        "percentage": 31.5
                },
                {
                        "category": "Channel Sales",
                        "value": 15629.96,
                        "percentage": 20.7
                },
                {
                        "category": "Online Sales",
                        "value": 7014.21,
                        "percentage": 9.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4702.92,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 24496.77,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.288736",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Operating Margin"
        }
    },
}
