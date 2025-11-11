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
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.185936"},
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
                        61.1,
                        69.24,
                        73.48,
                        73.62,
                        79.93,
                        68.26,
                        61.5,
                        74.27,
                        79.86,
                        78.2,
                        68.48,
                        73.73
                ],
                "unit": "%"
        },
        "current": {
                "value": 73.73,
                "unit": "%",
                "change": 5.25,
                "change_percent": 7.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 71.81,
                "min": 61.1,
                "max": 79.93,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.06,
                        "percentage": 19.1
                },
                {
                        "category": "Segment B",
                        "value": 20.0,
                        "percentage": 27.1
                },
                {
                        "category": "Segment C",
                        "value": 9.8,
                        "percentage": 13.3
                },
                {
                        "category": "Segment D",
                        "value": 6.99,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 22.88,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.454350",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Partner Contribution Margin"
        }
    },
}
