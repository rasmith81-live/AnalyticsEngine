"""
Up-Sell/Cross-Sell Rate

The percentage increase in up-sell or cross-sell successes after sales training.
"""

UP_SELLCROSS_SELL_RATE = {
    "code": "UP_SELLCROSS_SELL_RATE",
    "name": "Up-Sell/Cross-Sell Rate",
    "description": "The percentage increase in up-sell or cross-sell successes after sales training.",
    "formula": "(Number of Transactions with Up-Sell or Cross-Sell / Total Number of Transactions) * 100",
    "calculation_formula": "(Number of Transactions with Up-Sell or Cross-Sell / Total Number of Transactions) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Up-Sell/Cross-Sell Rate to be added.",
    "trend_analysis": """

    * An increasing up-sell/cross-sell rate may indicate that the sales team is effectively implementing the training and coaching strategies.
    * A decreasing rate could signal a need for additional training or adjustments to the sales process.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or services that have a higher success rate in up-selling or cross-selling?
    * How does our up-sell/cross-sell rate compare with industry benchmarks or competitors?
    
    """,
    "actionable_tips": """

    * Provide targeted training on effective up-selling and cross-selling techniques.
    * Implement a structured follow-up process to ensure that opportunities for up-selling or cross-selling are not missed.
    * Utilize customer relationship management (CRM) tools to track and analyze up-sell/cross-sell opportunities.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of up-sell/cross-sell rates over time.
    * Pie charts to compare the success rates of different up-sell/cross-sell strategies or products.
    
    """,
    "risk_warnings": """

    * A low up-sell/cross-sell rate may result in missed revenue opportunities and underperformance.
    * An excessively high rate could indicate aggressive or pushy sales tactics that may harm customer relationships.
    
    """,
    "tracking_tools": """

    * CRM systems with built-in up-sell/cross-sell tracking and reporting capabilities.
    * Sales performance management software to monitor and analyze the effectiveness of training and coaching programs.
    
    """,
    "integration_points": """

    * Integrate up-sell/cross-sell data with customer feedback and satisfaction metrics to understand the impact on overall customer experience.
    * Link up-sell/cross-sell performance with inventory and supply chain systems to ensure availability of recommended products.
    
    """,
    "change_impact_analysis": """

    * An increase in up-sell/cross-sell rate can lead to higher revenue and customer lifetime value.
    * However, aggressive up-selling or cross-selling may negatively impact customer trust and loyalty.
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:25.166396"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
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
                        49.8,
                        43.74,
                        51.5,
                        46.59,
                        46.12,
                        44.02,
                        52.23,
                        51.28,
                        45.35,
                        44.45,
                        47.01,
                        54.96
                ],
                "unit": "%"
        },
        "current": {
                "value": 54.96,
                "unit": "%",
                "change": 7.95,
                "change_percent": 16.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 48.09,
                "min": 43.74,
                "max": 54.96,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.64,
                        "percentage": 32.1
                },
                {
                        "category": "Category B",
                        "value": 7.36,
                        "percentage": 13.4
                },
                {
                        "category": "Category C",
                        "value": 9.57,
                        "percentage": 17.4
                },
                {
                        "category": "Category D",
                        "value": 3.14,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 17.25,
                        "percentage": 31.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.166396",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Up-Sell/Cross-Sell Rate"
        }
    },
}
