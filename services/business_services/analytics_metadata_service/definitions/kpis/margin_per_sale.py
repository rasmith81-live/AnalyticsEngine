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
                        81194.97,
                        80554.21,
                        86687.07,
                        83443.65,
                        92466.71,
                        88366.69,
                        83826.48,
                        80555.02,
                        79744.19,
                        79802.09,
                        89036.39,
                        90515.11
                ],
                "unit": "$"
        },
        "current": {
                "value": 90515.11,
                "unit": "$",
                "change": 1478.72,
                "change_percent": 1.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 84682.71,
                "min": 79744.19,
                "max": 92466.71,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19929.62,
                        "percentage": 22.0
                },
                {
                        "category": "Segment B",
                        "value": 16825.17,
                        "percentage": 18.6
                },
                {
                        "category": "Segment C",
                        "value": 11806.85,
                        "percentage": 13.0
                },
                {
                        "category": "Segment D",
                        "value": 8732.12,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 33221.35,
                        "percentage": 36.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.183859",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Margin per Sale"
        }
    },
}
