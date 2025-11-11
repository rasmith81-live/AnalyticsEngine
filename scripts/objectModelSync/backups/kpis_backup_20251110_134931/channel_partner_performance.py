"""
Channel Partner Performance

The performance metrics of each channel partner in terms of sales volume and effectiveness.
"""

CHANNEL_PARTNER_PERFORMANCE = {
    "code": "CHANNEL_PARTNER_PERFORMANCE",
    "name": "Channel Partner Performance",
    "description": "The performance metrics of each channel partner in terms of sales volume and effectiveness.",
    "formula": "Revenue (or other relevant metrics) attributed to each channel partner",
    "calculation_formula": "Revenue (or other relevant metrics) attributed to each channel partner",
    "category": "Sales Operations",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Channel Partner Performance to be added.",
    "trend_analysis": """

    * An increasing channel partner performance may indicate successful onboarding of new partners or increased market demand.
    * A decreasing performance could signal issues with partner support, product availability, or market saturation.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or regions where certain channel partners excel or struggle?
    * How does the channel partner performance compare with industry benchmarks or competitors' partnerships?
    
    """,
    "actionable_tips": """

    * Provide additional training and support to underperforming channel partners.
    * Regularly review and update the partner incentive and commission structures to align with sales goals.
    * Implement a lead management system to distribute leads effectively among channel partners.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the performance trends of individual channel partners over time.
    * Pie charts to compare the contribution of each channel partner to the overall sales volume.
    
    """,
    "risk_warnings": """

    * Underperforming channel partners may lead to missed sales opportunities and market share loss.
    * Overreliance on a few high-performing partners can create vulnerability to market changes or partner turnover.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and manage partner interactions and performance.
    * Partner Relationship Management (PRM) platforms to streamline partner communication and collaboration.
    
    """,
    "integration_points": """

    * Integrate channel partner performance data with sales forecasting to align production and inventory with expected demand.
    * Link performance metrics with marketing automation systems to tailor support and resources to each partner's needs.
    
    """,
    "change_impact_analysis": """

    * Improving channel partner performance can lead to increased market share and revenue, but may require additional resources for support and training.
    * Conversely, declining performance can impact overall sales and market presence, affecting the company's competitive position.
    
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.093895"},
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
                        896.88,
                        886.39,
                        982.52,
                        903.26,
                        940.88,
                        841.9,
                        974.58,
                        845.86,
                        913.96,
                        874.49,
                        982.77,
                        869.35
                ],
                "unit": "units"
        },
        "current": {
                "value": 869.35,
                "unit": "units",
                "change": -113.42,
                "change_percent": -11.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 909.4,
                "min": 841.9,
                "max": 982.77,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 238.28,
                        "percentage": 27.4
                },
                {
                        "category": "Category B",
                        "value": 188.73,
                        "percentage": 21.7
                },
                {
                        "category": "Category C",
                        "value": 125.88,
                        "percentage": 14.5
                },
                {
                        "category": "Category D",
                        "value": 34.86,
                        "percentage": 4.0
                },
                {
                        "category": "Other",
                        "value": 281.6,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.093895",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Channel Partner Performance"
        }
    },
}
