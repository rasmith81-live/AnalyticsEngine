"""
Partner-Centric Productivity

The productivity of channel partners, often measured in revenue per partner or deals closed per partner.
"""

PARTNER_CENTRIC_PRODUCTIVITY = {
    "code": "PARTNER_CENTRIC_PRODUCTIVITY",
    "name": "Partner-Centric Productivity",
    "description": "The productivity of channel partners, often measured in revenue per partner or deals closed per partner.",
    "formula": "Total Revenue from Partners / Total Costs of Partner Support and Resources",
    "calculation_formula": "Total Revenue from Partners / Total Costs of Partner Support and Resources",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner-Centric Productivity to be added.",
    "trend_analysis": """



    * Increasing revenue per partner may indicate successful enablement and support programs.
    * Decreasing deals closed per partner could signal a lack of engagement or alignment with the partner channel.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific partners consistently driving high revenue, and what can be learned from their approach?
    * How does our partner-centric productivity compare with industry benchmarks or with top-performing partners in our network?
    
    
    
    """,
    "actionable_tips": """



    * Invest in partner training and enablement to improve their sales capabilities.
    * Align partner incentives with desired sales behaviors to drive better performance.
    * Regularly communicate with partners to understand their challenges and provide necessary support.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing revenue per partner over time to identify trends and patterns.
    * Pie charts comparing deals closed per partner to visualize the distribution of performance across the partner network.
    
    
    
    """,
    "risk_warnings": """



    * Low partner-centric productivity can lead to missed sales opportunities and revenue loss.
    * Over-reliance on a few high-performing partners can create vulnerability if they disengage or underperform.
    
    
    
    """,
    "tracking_tools": """



    * Partner relationship management (PRM) software to track partner performance and engagement.
    * Sales enablement platforms to provide partners with necessary resources and training materials.
    
    
    
    """,
    "integration_points": """



    * Integrate partner-centric productivity data with CRM systems to understand the full customer journey and partner involvement.
    * Link partner performance with incentive and compensation systems to drive desired behaviors.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving partner-centric productivity can lead to increased market coverage and customer reach.
    * However, changes in partner engagement and incentives may impact the overall sales strategy and resource allocation.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Deal", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.180868"},
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
                        583.94,
                        680.58,
                        546.43,
                        618.2,
                        566.54,
                        576.82,
                        648.15,
                        656.63,
                        621.9,
                        606.87,
                        629.51,
                        569.5
                ],
                "unit": "units"
        },
        "current": {
                "value": 569.5,
                "unit": "units",
                "change": -60.01,
                "change_percent": -9.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 608.76,
                "min": 546.43,
                "max": 680.58,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 134.81,
                        "percentage": 23.7
                },
                {
                        "category": "Product Line B",
                        "value": 76.17,
                        "percentage": 13.4
                },
                {
                        "category": "Product Line C",
                        "value": 101.72,
                        "percentage": 17.9
                },
                {
                        "category": "Services",
                        "value": 40.74,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 216.06,
                        "percentage": 37.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.444818",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Partner-Centric Productivity"
        }
    },
}
