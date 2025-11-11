"""
Lost Sale Analysis

The evaluation of deals that were not won to understand the reasons behind the loss.
"""

LOST_SALE_ANALYSIS = {
    "code": "LOST_SALE_ANALYSIS",
    "name": "Lost Sale Analysis",
    "description": "The evaluation of deals that were not won to understand the reasons behind the loss.",
    "formula": "Variables vary; often a qualitative analysis",
    "calculation_formula": "Variables vary; often a qualitative analysis",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lost Sale Analysis to be added.",
    "trend_analysis": """

    * An increasing lost sale analysis may indicate issues with the sales process, product quality, or market competition.
    * A decreasing analysis could signal improved sales strategies, product enhancements, or better customer relationship management.
    
    """,
    "diagnostic_questions": """

    * Are there common reasons or patterns behind the lost sales? (e.g., pricing, product features, competitor actions)
    * How do our lost sales compare with industry benchmarks or historical data? Are there any emerging trends?
    
    """,
    "actionable_tips": """

    * Implement regular win/loss analysis to gather feedback from lost opportunities and identify areas for improvement.
    * Provide additional sales training or resources to address common objections or concerns raised by potential customers.
    * Consider revising pricing strategies, product offerings, or sales approaches based on the insights gained from the lost sale analysis.
    
    """,
    "visualization_suggestions": """

    * Funnel charts to visualize the stages where potential sales are being lost in the sales process.
    * Comparison charts to highlight the reasons for lost sales across different time periods or product categories.
    
    """,
    "risk_warnings": """

    * Consistently high lost sale rates can impact revenue and market share, leading to long-term business implications.
    * Ignoring the reasons behind lost sales may result in continued inefficiencies and missed opportunities for improvement.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and analyze lost sales data and customer interactions.
    * Sales analytics tools to identify patterns and trends in lost sale data, enabling targeted improvements.
    
    """,
    "integration_points": """

    * Integrate lost sale analysis with customer feedback systems to gain a comprehensive understanding of customer needs and preferences.
    * Link analysis with sales forecasting and inventory management systems to align production and sales efforts with market demand.
    
    """,
    "change_impact_analysis": """

    * Improving the lost sale analysis can lead to more targeted sales efforts, increased customer satisfaction, and higher conversion rates.
    * However, changes in sales strategies or product offerings may require additional resources and could impact short-term sales performance.
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Competitive Analysis", "Deal", "Lost Sale", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.624777"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "INSIDE_SALES",
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
                        255.33,
                        251.67,
                        228.13,
                        177.8,
                        194.68,
                        132.64,
                        140.12,
                        241.4,
                        206.97,
                        204.72,
                        242.39,
                        270.47
                ],
                "unit": "units"
        },
        "current": {
                "value": 270.47,
                "unit": "units",
                "change": 28.08,
                "change_percent": 11.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 212.19,
                "min": 132.64,
                "max": 270.47,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 75.31,
                        "percentage": 27.8
                },
                {
                        "category": "Category B",
                        "value": 48.25,
                        "percentage": 17.8
                },
                {
                        "category": "Category C",
                        "value": 24.23,
                        "percentage": 9.0
                },
                {
                        "category": "Category D",
                        "value": 18.33,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 104.35,
                        "percentage": 38.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.624777",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Lost Sale Analysis"
        }
    },
}
