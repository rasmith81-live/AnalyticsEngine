"""
Lost Sales Analysis

A review of lost sales opportunities to determine common factors or reasons for not winning the business.
"""

LOST_SALES_ANALYSIS = {
    "code": "LOST_SALES_ANALYSIS",
    "name": "Lost Sales Analysis",
    "description": "A review of lost sales opportunities to determine common factors or reasons for not winning the business.",
    "formula": "No Standard Formula - This KPI is typically a combination of various metrics and qualitative assessments.",
    "calculation_formula": "No Standard Formula - This KPI is typically a combination of various metrics and qualitative assessments.",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lost Sales Analysis to be added.",
    "trend_analysis": """


    * An increasing number of lost sales due to pricing issues may indicate a need to reevaluate pricing strategies or offer more competitive pricing.
    * A decrease in lost sales related to product availability could signal improvements in inventory management or supplier relationships.
    
    
    """,
    "diagnostic_questions": """


    * Are there common objections or reasons cited by potential customers for not choosing our products/services?
    * How do our lost sales compare to competitors, and what factors differentiate our offerings?
    
    
    """,
    "actionable_tips": """


    * Provide additional sales training to address common objections and improve sales techniques.
    * Conduct market research to understand customer needs and preferences better, allowing for more targeted sales approaches.
    * Implement a customer feedback system to gather insights on why sales opportunities are being lost.
    
    
    """,
    "visualization_suggestions": """


    * Pie charts showing the distribution of lost sales reasons.
    * Trend line graphs to track changes in lost sales reasons over time.
    
    
    """,
    "risk_warnings": """


    * Consistently losing sales due to the same reasons may indicate a need for significant changes in product offerings or sales strategies.
    * Ignoring common reasons for lost sales can lead to continued revenue loss and market share erosion.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) software to track and analyze reasons for lost sales.
    * Sales analytics tools to identify patterns and trends in lost sales data.
    
    
    """,
    "integration_points": """


    * Integrate lost sales analysis with customer feedback systems to gain a comprehensive understanding of customer preferences and objections.
    * Link lost sales data with sales performance metrics to identify areas for improvement in the sales process.
    
    
    """,
    "change_impact_analysis": """


    * Addressing common reasons for lost sales can lead to increased revenue and market share.
    * However, changes in sales strategies or product offerings may require initial investment and could impact short-term profitability.
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Call", "Competitive Analysis", "Lost Sale", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Strategic Review"], "last_validated": "2025-11-10T13:49:33.034185"},
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
                        931.85,
                        837.21,
                        896.73,
                        833.75,
                        823.39,
                        860.58,
                        885.6,
                        840.68,
                        823.24,
                        837.31,
                        929.65,
                        832.13
                ],
                "unit": "units"
        },
        "current": {
                "value": 832.13,
                "unit": "units",
                "change": -97.52,
                "change_percent": -10.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 861.01,
                "min": 823.24,
                "max": 931.85,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 126.34,
                        "percentage": 15.2
                },
                {
                        "category": "Category B",
                        "value": 126.85,
                        "percentage": 15.2
                },
                {
                        "category": "Category C",
                        "value": 141.88,
                        "percentage": 17.1
                },
                {
                        "category": "Category D",
                        "value": 76.18,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 360.88,
                        "percentage": 43.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.626916",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Lost Sales Analysis"
        }
    },
}
