"""
Number of Active Channel Partners

The number of active channel partners in the network.
"""

NUMBER_OF_ACTIVE_CHANNEL_PARTNERS = {
    "code": "NUMBER_OF_ACTIVE_CHANNEL_PARTNERS",
    "name": "Number of Active Channel Partners",
    "description": "The number of active channel partners in the network.",
    "formula": "Total Count of Active Channel Partners",
    "calculation_formula": "Total Count of Active Channel Partners",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Number of Active Channel Partners to be added.",
    "trend_analysis": """

    * The number of active channel partners tends to increase as the company expands its market reach or introduces new products/services.
    * A decreasing number of active channel partners may indicate dissatisfaction with the partnership program or increased competition in the market.
    
    """,
    "diagnostic_questions": """

    * What factors contribute to the onboarding and retention of channel partners?
    * Are there specific regions or industries where the number of active channel partners is declining, and what could be the reasons behind it?
    
    """,
    "actionable_tips": """

    * Regularly review and update the value proposition for channel partners to ensure it aligns with their needs and market demands.
    * Provide comprehensive training and support to channel partners to help them effectively sell and promote the company's products/services.
    * Implement a robust communication and feedback mechanism to address the concerns and suggestions of channel partners in a timely manner.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the growth or decline in the number of active channel partners over time.
    * Map visualizations to identify geographical areas with the highest and lowest concentration of active channel partners.
    
    """,
    "risk_warnings": """

    * A decreasing number of active channel partners can lead to reduced market coverage and missed sales opportunities.
    * An excessively high number of channel partners without proper management can lead to channel conflict and diluted brand representation.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) systems to track and manage interactions with channel partners.
    * Partner Relationship Management (PRM) software to streamline partner onboarding, training, and collaboration.
    
    """,
    "integration_points": """

    * Integrate the number of active channel partners with sales performance data to assess the effectiveness of the channel partner network in driving revenue.
    * Link the channel partner KPI with marketing analytics to understand the impact of partner-driven promotions and campaigns.
    
    """,
    "change_impact_analysis": """

    * An increase in the number of active channel partners can lead to expanded market reach and potentially higher sales volumes.
    * However, a decrease in the number of active channel partners may require a reassessment of the partnership program and its value proposition.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.696363"},
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
                        187,
                        224,
                        175,
                        200,
                        217,
                        204,
                        220,
                        178,
                        199,
                        216,
                        186,
                        188
                ],
                "unit": "count"
        },
        "current": {
                "value": 188,
                "unit": "count",
                "change": 2,
                "change_percent": 1.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 199.5,
                "min": 175,
                "max": 224,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 46.06,
                        "percentage": 24.5
                },
                {
                        "category": "Category B",
                        "value": 21.91,
                        "percentage": 11.7
                },
                {
                        "category": "Category C",
                        "value": 19.42,
                        "percentage": 10.3
                },
                {
                        "category": "Category D",
                        "value": 19.4,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 81.21,
                        "percentage": 43.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.696363",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Number of Active Channel Partners"
        }
    },
}
