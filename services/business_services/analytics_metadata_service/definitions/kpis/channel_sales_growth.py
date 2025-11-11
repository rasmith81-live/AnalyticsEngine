"""
Channel Sales Growth

The year-over-year growth in revenue from channel partner sales.
"""

CHANNEL_SALES_GROWTH = {
    "code": "CHANNEL_SALES_GROWTH",
    "name": "Channel Sales Growth",
    "description": "The year-over-year growth in revenue from channel partner sales.",
    "formula": "((Current Period Channel Sales - Previous Period Channel Sales) / Previous Period Channel Sales) * 100",
    "calculation_formula": "((Current Period Channel Sales - Previous Period Channel Sales) / Previous Period Channel Sales) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Channel Sales Growth to be added.",
    "trend_analysis": """



    * Channel Sales Growth tends to show seasonal fluctuations, with higher growth during peak sales periods and lower growth during off-peak times.
    * An overall upward trend in Channel Sales Growth may indicate successful partner recruitment and enablement, while a downward trend could signal issues with partner performance or market saturation.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific products or services are driving the most growth through channel partners?
    * Are there any common factors among underperforming channel partners that could be addressed to improve overall growth?
    
    
    
    """,
    "actionable_tips": """



    * Invest in targeted partner training and enablement programs to improve sales effectiveness.
    * Regularly review and optimize the partner portfolio to ensure alignment with market demand and company objectives.
    * Implement incentive programs to motivate and reward high-performing channel partners.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing year-over-year revenue growth from channel sales.
    * Pie charts illustrating the contribution of different partners or regions to overall channel sales growth.
    
    
    
    """,
    "risk_warnings": """



    * Over-reliance on a small number of channel partners may create vulnerability to market changes or partner performance issues.
    * Insufficient support for channel partners could lead to missed sales opportunities and decreased overall growth.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) systems to track and manage partner interactions and performance.
    * Partner Relationship Management (PRM) platforms to streamline partner communication and collaboration.
    
    
    
    """,
    "integration_points": """



    * Integrate Channel Sales Growth data with overall sales performance metrics to gain a comprehensive view of revenue generation.
    * Link Channel Sales Growth with marketing analytics to assess the effectiveness of partner-focused marketing efforts.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving Channel Sales Growth can lead to increased market share and revenue, but may also require additional resources for partner support and management.
    * A decline in Channel Sales Growth could impact overall company performance and market competitiveness, especially if direct sales are not able to compensate for the decrease.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.692472"},
    "required_objects": [],
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
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
                        62.39,
                        78.51,
                        63.35,
                        68.19,
                        69.15,
                        73.19,
                        64.25,
                        74.53,
                        70.21,
                        80.2,
                        78.31,
                        76.74
                ],
                "unit": "%"
        },
        "current": {
                "value": 76.74,
                "unit": "%",
                "change": -1.57,
                "change_percent": -2.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 71.59,
                "min": 62.39,
                "max": 80.2,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 21.65,
                        "percentage": 28.2
                },
                {
                        "category": "Channel Sales",
                        "value": 11.82,
                        "percentage": 15.4
                },
                {
                        "category": "Online Sales",
                        "value": 9.31,
                        "percentage": 12.1
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.58,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 28.38,
                        "percentage": 37.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.460433",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Channel Sales Growth"
        }
    },
}
