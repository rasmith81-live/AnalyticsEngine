"""
Partner Profitability

A measure of the net profit a channel partner generates for the company, indicating the financial success of the partnership.
"""

PARTNER_PROFITABILITY = {
    "code": "PARTNER_PROFITABILITY",
    "name": "Partner Profitability",
    "description": "A measure of the net profit a channel partner generates for the company, indicating the financial success of the partnership.",
    "formula": "(Total Revenue from Partners - Total Costs Associated with Partners) / Total Revenue from Partners * 100",
    "calculation_formula": "(Total Revenue from Partners - Total Costs Associated with Partners) / Total Revenue from Partners * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Profitability to be added.",
    "trend_analysis": """



    * Increasing partner profitability may indicate successful sales strategies and strong customer relationships.
    * Decreasing profitability could signal issues with pricing, competition, or changes in customer demand.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors contribute to the profitability of our channel partners?
    * Are there specific products or services that are more profitable for our partners?
    
    
    
    """,
    "actionable_tips": """



    * Provide training and support to help partners effectively market and sell high-margin products.
    * Regularly review and adjust partner commission structures to align with company goals and market conditions.
    * Implement incentive programs to encourage partners to focus on selling more profitable products or services.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing partner profitability over time to identify trends and seasonal variations.
    * Pie charts to compare the contribution of different products or services to overall partner profitability.
    
    
    
    """,
    "risk_warnings": """



    * Declining partner profitability may lead to disengagement or seeking partnerships with competitors.
    * Over-reliance on a small number of highly profitable products or services may create vulnerability to market changes.
    
    
    
    """,
    "tracking_tools": """



    * Channel management software to track partner performance and profitability in real-time.
    * Customer relationship management (CRM) systems to analyze customer behavior and preferences, helping partners focus on more profitable opportunities.
    
    
    
    """,
    "integration_points": """



    * Integrate partner profitability data with sales and marketing systems to identify opportunities for improving partner performance.
    * Link partner profitability with inventory and supply chain management to ensure partners have access to profitable products in a timely manner.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving partner profitability can lead to increased revenue and market share for the company.
    * However, changes in partner profitability may also impact relationships with other channel partners and overall market competitiveness.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Success Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Partnership", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.209651"},
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
                        78.95,
                        72.41,
                        73.28,
                        73.98,
                        71.46,
                        66.24,
                        67.02,
                        66.82,
                        79.95,
                        64.72,
                        80.02,
                        66.56
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.56,
                "unit": "%",
                "change": -13.46,
                "change_percent": -16.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 71.78,
                "min": 64.72,
                "max": 80.02,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 22.29,
                        "percentage": 33.5
                },
                {
                        "category": "Segment B",
                        "value": 9.34,
                        "percentage": 14.0
                },
                {
                        "category": "Segment C",
                        "value": 8.49,
                        "percentage": 12.8
                },
                {
                        "category": "Segment D",
                        "value": 4.9,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 21.54,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.500785",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Partner Profitability"
        }
    },
}
