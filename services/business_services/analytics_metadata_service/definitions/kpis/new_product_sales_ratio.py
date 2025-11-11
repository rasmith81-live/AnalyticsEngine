"""
New Product Sales Ratio

The percentage of total sales that come from new products, indicating the success of product launches.
"""

NEW_PRODUCT_SALES_RATIO = {
    "code": "NEW_PRODUCT_SALES_RATIO",
    "name": "New Product Sales Ratio",
    "description": "The percentage of total sales that come from new products, indicating the success of product launches.",
    "formula": "(New Product Sales / Total Sales) * 100",
    "calculation_formula": "(New Product Sales / Total Sales) * 100",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for New Product Sales Ratio to be added.",
    "trend_analysis": """



    * An increasing new product sales ratio may indicate successful product launches and a growing customer interest in new offerings.
    * A decreasing ratio could signal challenges in marketing or positioning new products, or a lack of innovation in the product development pipeline.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific new products that consistently contribute to a high sales ratio, and if so, what factors contribute to their success?
    * How does the new product sales ratio compare to historical data and industry benchmarks, and what insights can be gained from any deviations?
    
    
    
    """,
    "actionable_tips": """



    * Invest in market research and customer feedback to better understand the demand for new products and tailor marketing strategies accordingly.
    * Provide sales teams with targeted training and resources to effectively promote and sell new products to customers.
    * Regularly review and refine the new product development process to ensure a steady stream of successful product launches.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of new product sales ratio over time.
    * Pie charts comparing the contribution of new products to total sales in different time periods.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low new product sales ratio may indicate a lack of innovation or relevance in the product portfolio, leading to potential market stagnation.
    * Over-reliance on new product sales without a strong foundation of core product sales may lead to volatility in revenue and customer retention.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer preferences and feedback related to new products.
    * Product lifecycle management (PLM) tools to streamline the development and launch process of new products.
    
    
    
    """,
    "integration_points": """



    * Integrate new product sales data with product development and marketing systems to align efforts and resources for successful launches.
    * Link new product sales ratio with customer satisfaction metrics to understand the impact of new products on overall customer experience.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in new product sales ratio can lead to a more diverse product portfolio and potentially higher customer engagement and loyalty.
    * Conversely, a decrease in the ratio may impact the organization's ability to stay competitive and relevant in the market, affecting long-term growth and profitability.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.078490"},
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
                        64.04,
                        61.7,
                        49.89,
                        59.89,
                        48.15,
                        49.87,
                        61.27,
                        58.46,
                        56.89,
                        56.89,
                        57.8,
                        64.1
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.1,
                "unit": "%",
                "change": 6.3,
                "change_percent": 10.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 57.41,
                "min": 48.15,
                "max": 64.1,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 13.15,
                        "percentage": 20.5
                },
                {
                        "category": "Product Line B",
                        "value": 13.62,
                        "percentage": 21.2
                },
                {
                        "category": "Product Line C",
                        "value": 6.24,
                        "percentage": 9.7
                },
                {
                        "category": "Services",
                        "value": 4.63,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 26.46,
                        "percentage": 41.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.245783",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "New Product Sales Ratio"
        }
    },
}
