"""
Demo-to-Close Ratio

The percentage of product demos given to prospects that result in closed sales.
"""

DEMO_TO_CLOSE_RATIO = {
    "code": "DEMO_TO_CLOSE_RATIO",
    "name": "Demo-to-Close Ratio",
    "description": "The percentage of product demos given to prospects that result in closed sales.",
    "formula": "(Number of Closed Deals Post-Demo / Total Number of Demos Given) * 100",
    "calculation_formula": "(Number of Closed Deals Post-Demo / Total Number of Demos Given) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Demo-to-Close Ratio to be added.",
    "trend_analysis": """



    * An increasing demo-to-close ratio may indicate improved sales techniques or a better understanding of customer needs.
    * A decreasing ratio could signal issues with product quality, pricing, or the effectiveness of the sales team.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or sales reps that consistently have higher or lower demo-to-close ratios?
    * How does our demo-to-close ratio compare with industry benchmarks or with different customer segments?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional sales training and resources to improve the effectiveness of product demos.
    * Regularly review and update sales scripts and materials to ensure they align with customer needs and objections.
    * Implement a lead scoring system to prioritize prospects with a higher likelihood of closing.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of demo-to-close ratios over time.
    * Pie charts comparing demo-to-close ratios for different product categories or customer segments.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low demo-to-close ratio can lead to wasted resources and decreased sales effectiveness.
    * High fluctuations in the ratio may indicate inconsistent sales processes or customer targeting.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track and analyze the effectiveness of product demos and sales follow-ups.
    * Sales enablement platforms to provide sales reps with the necessary tools and content to improve their demo-to-close ratio.
    
    
    
    """,
    "integration_points": """



    * Integrate demo-to-close ratio tracking with marketing automation systems to align lead generation efforts with sales effectiveness.
    * Link with customer feedback systems to understand how product demos and sales interactions are perceived by prospects.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the demo-to-close ratio can lead to increased revenue and customer satisfaction, but may require additional resources for sales training and support.
    * Conversely, a declining ratio can negatively impact sales performance and overall business growth.
    
    
    
    """,
    "metadata_": {"modules": ["BUS_DEV", "INSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Demo", "Lead", "Lead Qualification", "Opportunity", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "replaces": ["DEMO_TO_CLOSING_RATE"], "last_validated": "2025-11-10T13:49:32.924094"},
    "required_objects": [],
    "modules": ["BUS_DEV", "INSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "BUS_DEV",
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
                        71.82,
                        66.16,
                        73.23,
                        60.61,
                        67.06,
                        75.72,
                        70.38,
                        77.65,
                        78.25,
                        68.61,
                        78.93,
                        67.8
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.8,
                "unit": "%",
                "change": -11.13,
                "change_percent": -14.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.35,
                "min": 60.61,
                "max": 78.93,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 23.53,
                        "percentage": 34.7
                },
                {
                        "category": "Segment B",
                        "value": 15.27,
                        "percentage": 22.5
                },
                {
                        "category": "Segment C",
                        "value": 6.81,
                        "percentage": 10.0
                },
                {
                        "category": "Segment D",
                        "value": 5.75,
                        "percentage": 8.5
                },
                {
                        "category": "Other",
                        "value": 16.44,
                        "percentage": 24.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.918965",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Demo-to-Close Ratio"
        }
    },
}
