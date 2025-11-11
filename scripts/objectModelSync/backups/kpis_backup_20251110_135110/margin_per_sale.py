"""
Margin per Sale

The profit margin for each sale, calculated as the selling price minus the cost of goods sold.
"""

MARGIN_PER_SALE = {
    "code": "MARGIN_PER_SALE",
    "name": "Margin per Sale",
    "description": "The profit margin for each sale, calculated as the selling price minus the cost of goods sold.",
    "formula": "(Revenue - Cost of Goods Sold) / Revenue",
    "calculation_formula": "(Revenue - Cost of Goods Sold) / Revenue",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Margin per Sale to be added.",
    "trend_analysis": """


    * Increasing margin per sale may indicate successful pricing strategies or cost-saving measures.
    * Decreasing margin could signal increased competition, rising production costs, or ineffective pricing strategies.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific products with consistently low margins that need reevaluation?
    * How does our margin per sale compare with industry benchmarks or changes in production costs?
    
    
    """,
    "actionable_tips": """


    * Regularly review and adjust pricing strategies based on market conditions and cost fluctuations.
    * Identify and address inefficiencies in the production process to reduce cost of goods sold.
    * Explore opportunities for upselling or cross-selling to increase the average selling price.
    
    
    """,
    "visualization_suggestions": """


    * Line charts to track the trend of margin per sale over time.
    * Pareto charts to identify which products contribute the most to overall margin.
    
    
    """,
    "risk_warnings": """


    * Low margins may lead to reduced profitability and financial instability.
    * Overly high margins could result in loss of competitiveness and customer attrition.
    
    
    """,
    "tracking_tools": """


    * Enterprise resource planning (ERP) systems to track production costs and pricing data.
    * Business intelligence tools for in-depth analysis of sales and cost data.
    
    
    """,
    "integration_points": """


    * Integrate margin per sale data with pricing and product development processes to optimize profitability.
    * Link with financial systems to understand the impact of margin changes on overall revenue and profit.
    
    
    """,
    "change_impact_analysis": """


    * Improving margin per sale can lead to increased profitability but may require strategic shifts in pricing and cost management.
    * Reducing margins to gain market share may impact short-term profitability but could lead to long-term growth and customer loyalty.
    
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lost Sale", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.038909"},
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
                        36982.96,
                        40901.63,
                        39595.29,
                        39397.44,
                        40933.52,
                        32456.14,
                        44326.51,
                        38136.62,
                        41670.12,
                        42634.52,
                        31848.46,
                        42659.04
                ],
                "unit": "$"
        },
        "current": {
                "value": 42659.04,
                "unit": "$",
                "change": 10810.58,
                "change_percent": 33.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 39295.19,
                "min": 31848.46,
                "max": 44326.51,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9842.34,
                        "percentage": 23.1
                },
                {
                        "category": "Category B",
                        "value": 5098.6,
                        "percentage": 12.0
                },
                {
                        "category": "Category C",
                        "value": 5700.59,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 4344.38,
                        "percentage": 10.2
                },
                {
                        "category": "Other",
                        "value": 17673.13,
                        "percentage": 41.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.636204",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Margin per Sale"
        }
    },
}
