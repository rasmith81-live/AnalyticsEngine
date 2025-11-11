"""
Partner Support Ticket Resolution Time

The average time taken to resolve support tickets raised by channel partners, indicating the effectiveness of partner support.
"""

PARTNER_SUPPORT_TICKET_RESOLUTION_TIME = {
    "code": "PARTNER_SUPPORT_TICKET_RESOLUTION_TIME",
    "name": "Partner Support Ticket Resolution Time",
    "description": "The average time taken to resolve support tickets raised by channel partners, indicating the effectiveness of partner support.",
    "formula": "Average Time to Resolve Partner Support Tickets",
    "calculation_formula": "Average Time to Resolve Partner Support Tickets",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Support Ticket Resolution Time to be added.",
    "trend_analysis": """


    * Increasing resolution time may indicate a growing backlog of partner support tickets or inefficiencies in the support process.
    * Decreasing resolution time can signal improvements in support ticket prioritization, resource allocation, or issue resolution capabilities.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific types of support tickets that consistently take longer to resolve?
    * How does our partner support ticket resolution time compare to industry benchmarks or our own historical data?
    
    
    """,
    "actionable_tips": """


    * Implement a ticket prioritization system to address urgent partner issues more quickly.
    * Provide additional training or resources to support agents to improve their ability to resolve issues efficiently.
    * Regularly review and optimize support processes to identify and eliminate bottlenecks.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the average resolution time over time to identify trends.
    * Stacked bar charts comparing resolution times for different types of support tickets.
    
    
    """,
    "risk_warnings": """


    * Long resolution times can lead to partner dissatisfaction and strained relationships.
    * Consistently high resolution times may indicate systemic issues in partner support that could impact overall channel performance.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) systems with ticketing and support modules for tracking and managing partner support tickets.
    * Performance analytics tools to identify patterns and areas for improvement in the support process.
    
    
    """,
    "integration_points": """


    * Integrate partner support ticket data with overall channel performance metrics to understand the impact of support on partner satisfaction and sales.
    * Link support ticket resolution time with resource allocation and capacity planning to ensure adequate support coverage.
    
    
    """,
    "change_impact_analysis": """


    * Improving resolution time can enhance partner satisfaction and loyalty, leading to increased sales and revenue.
    * Conversely, prolonged resolution times can strain partner relationships and impact overall channel performance.
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"], "last_validated": "2025-11-10T13:49:33.219616"},
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
                        7.8,
                        5.3,
                        5.2,
                        10.6,
                        10.3,
                        8.1,
                        5.0,
                        9.9,
                        6.3,
                        6.5,
                        6.3,
                        6.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 6.0,
                "unit": "days",
                "change": -0.3,
                "change_percent": -4.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 7.27,
                "min": 5.0,
                "max": 10.6,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 1.32,
                        "percentage": 22.0
                },
                {
                        "category": "Category B",
                        "value": 1.29,
                        "percentage": 21.5
                },
                {
                        "category": "Category C",
                        "value": 0.57,
                        "percentage": 9.5
                },
                {
                        "category": "Category D",
                        "value": 0.5,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 2.32,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.909358",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Partner Support Ticket Resolution Time"
        }
    },
}
