"""
Partner Geographic Expansion

The extent to which channel partners are able to expand the company's reach into new geographic markets.
"""

PARTNER_GEOGRAPHIC_EXPANSION = {
    "code": "PARTNER_GEOGRAPHIC_EXPANSION",
    "name": "Partner Geographic Expansion",
    "description": "The extent to which channel partners are able to expand the company's reach into new geographic markets.",
    "formula": "Number of New Geographic Markets Entered by Partners",
    "calculation_formula": "Number of New Geographic Markets Entered by Partners",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Geographic Expansion to be added.",
    "trend_analysis": """

    * Increasing number of new geographic markets entered by channel partners over time may indicate positive performance in partner geographic expansion.
    * Declining trend in the expansion of new markets could signal potential challenges or limitations in the partner network's ability to reach new regions.
    
    """,
    "diagnostic_questions": """

    * What are the specific barriers or challenges that channel partners face when trying to expand into new geographic markets?
    * Are there any patterns or commonalities among successful expansions into new regions that can be replicated or leveraged?
    
    """,
    "actionable_tips": """

    * Provide targeted training and support to channel partners on market research and entry strategies for new geographic regions.
    * Develop incentive programs or rewards for channel partners who successfully expand the company's reach into new markets.
    * Invest in market intelligence tools and resources to identify potential opportunities for geographic expansion.
    
    """,
    "visualization_suggestions": """

    * Map visualizations showing the geographic locations where channel partners have successfully expanded the company's reach.
    * Line charts tracking the number of new geographic markets entered by channel partners over time.
    
    """,
    "risk_warnings": """

    * Inadequate understanding of local market dynamics and customer needs in new geographic regions can lead to ineffective expansion efforts.
    * Overreliance on a small number of channel partners for geographic expansion may create vulnerability to market fluctuations or partner turnover.
    
    """,
    "tracking_tools": """

    * Geospatial analytics tools to identify potential new markets and assess their suitability for expansion.
    * Customer relationship management (CRM) systems to track and manage partner activities related to geographic expansion.
    
    """,
    "integration_points": """

    * Integrate partner geographic expansion data with sales and marketing systems to align go-to-market strategies with new market opportunities.
    * Link geographic expansion efforts with supply chain and logistics systems to ensure seamless product availability in new regions.
    
    """,
    "change_impact_analysis": """

    * Successful geographic expansion can lead to increased sales revenue and market share, impacting overall business growth.
    * Unsuccessful or haphazard expansion efforts may strain resources and damage the company's reputation in new markets, affecting long-term success.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Expansion Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.868354"},
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
                        473,
                        502,
                        496,
                        477,
                        459,
                        478,
                        494,
                        460,
                        465,
                        497,
                        506,
                        456
                ],
                "unit": "count"
        },
        "current": {
                "value": 456,
                "unit": "count",
                "change": -50,
                "change_percent": -9.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 480.25,
                "min": 456,
                "max": 506,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 101.41,
                        "percentage": 22.2
                },
                {
                        "category": "Category B",
                        "value": 92.9,
                        "percentage": 20.4
                },
                {
                        "category": "Category C",
                        "value": 88.62,
                        "percentage": 19.4
                },
                {
                        "category": "Category D",
                        "value": 33.79,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 139.28,
                        "percentage": 30.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.868354",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Partner Geographic Expansion"
        }
    },
}
