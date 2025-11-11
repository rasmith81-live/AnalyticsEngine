"""
Partner Contribution Margin

A measure of how much each channel partner contributes to covering the company's fixed costs after variable costs are subtracted.
"""

PARTNER_CONTRIBUTION_MARGIN = {
    "code": "PARTNER_CONTRIBUTION_MARGIN",
    "name": "Partner Contribution Margin",
    "description": "A measure of how much each channel partner contributes to covering the company's fixed costs after variable costs are subtracted.",
    "formula": "(Total Revenue from Partners - Variable Costs Attributable to Partners) / Total Revenue from Partners * 100",
    "calculation_formula": "(Total Revenue from Partners - Variable Costs Attributable to Partners) / Total Revenue from Partners * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Contribution Margin to be added.",
    "trend_analysis": """

    * Increasing partner contribution margin may indicate improved efficiency in the channel partner network or better pricing strategies.
    * Decreasing margin could signal rising variable costs, ineffective pricing, or a decline in sales volume.
    
    """,
    "diagnostic_questions": """

    * Are there specific channel partners that consistently contribute more or less to covering fixed costs?
    * How does our partner contribution margin compare with industry benchmarks or historical performance?
    
    """,
    "actionable_tips": """

    * Provide channel partners with training and support to improve their sales effectiveness and reduce variable costs.
    * Regularly review pricing strategies to ensure they align with market conditions and partner capabilities.
    * Implement incentive programs to encourage channel partners to focus on high-margin products or services.
    
    """,
    "visualization_suggestions": """

    * Line charts showing partner contribution margin over time to identify trends and seasonality.
    * Pie charts to compare the contribution margin of different channel partners or regions.
    
    """,
    "risk_warnings": """

    * Low partner contribution margin may lead to increased reliance on company-owned sales channels, impacting overall profitability.
    * Highly variable contribution margins across partners may indicate inconsistent performance or potential issues with partner management.
    
    """,
    "tracking_tools": """

    * Channel management software to track and analyze partner performance and contribution margin.
    * Financial management systems to accurately allocate fixed and variable costs to each channel partner.
    
    """,
    "integration_points": """

    * Integrate partner contribution margin analysis with sales and marketing systems to identify opportunities for improved partner performance.
    * Link contribution margin data with supply chain and inventory management systems to ensure efficient cost allocation.
    
    """,
    "change_impact_analysis": """

    * Increasing partner contribution margin may lead to higher overall profitability but could require additional investment in partner support and resources.
    * Decreasing margin may impact the company's ability to cover fixed costs and maintain profitability, potentially leading to strategic shifts in the channel partner network.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.854946"},
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
                        31211.39,
                        33791.01,
                        32453.45,
                        29514.54,
                        40149.29,
                        35952.66,
                        27672.53,
                        29863.99,
                        32239.45,
                        35060.92,
                        35018.04,
                        31852.98
                ],
                "unit": "$"
        },
        "current": {
                "value": 31852.98,
                "unit": "$",
                "change": -3165.06,
                "change_percent": -9.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 32898.35,
                "min": 27672.53,
                "max": 40149.29,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10077.96,
                        "percentage": 31.6
                },
                {
                        "category": "Category B",
                        "value": 4814.67,
                        "percentage": 15.1
                },
                {
                        "category": "Category C",
                        "value": 4344.05,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 2536.19,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 10080.11,
                        "percentage": 31.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.854946",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Partner Contribution Margin"
        }
    },
}
