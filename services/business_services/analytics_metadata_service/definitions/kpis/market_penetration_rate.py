"""
Market Penetration Rate

The rate at which new clients are acquired in new or existing markets, indicating expansion success.
"""

MARKET_PENETRATION_RATE = {
    "code": "MARKET_PENETRATION_RATE",
    "name": "Market Penetration Rate",
    "description": "The rate at which new clients are acquired in new or existing markets, indicating expansion success.",
    "formula": "(Number of Customers in Target Market / Total Size of Target Market) * 100",
    "calculation_formula": "(Number of Customers in Target Market / Total Size of Target Market) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Market Penetration Rate to be added.",
    "trend_analysis": """



    * Increasing market penetration rate may indicate successful expansion efforts or improved sales strategies.
    * A decreasing rate could signal market saturation or ineffective sales tactics.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific regions or demographics where market penetration is particularly low?
    * How does our market penetration rate compare with competitors or industry benchmarks?
    
    
    
    """,
    "actionable_tips": """



    * Invest in targeted marketing campaigns to reach untapped markets.
    * Provide additional sales training or resources to sales teams operating in underperforming markets.
    * Regularly review and adjust sales strategies to adapt to changing market conditions.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of market penetration rate over time for different markets.
    * Geospatial maps to visually represent market penetration by region or territory.
    
    
    
    """,
    "risk_warnings": """



    * Low market penetration rates may lead to missed revenue opportunities and hinder overall company growth.
    * Rapidly expanding into new markets without proper research and planning can result in wasted resources and potential brand damage.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track sales activities and customer interactions in different markets.
    * Data analytics tools to identify market trends and opportunities for expansion.
    
    
    
    """,
    "integration_points": """



    * Integrate market penetration data with customer relationship management systems to better understand customer behavior in different markets.
    * Link market penetration rate with inventory and supply chain systems to ensure adequate product availability in new markets.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing market penetration can lead to higher sales volume and revenue, but may also require additional resources for customer support and fulfillment.
    * Decreasing market penetration may result in reduced market share and potential loss of competitive advantage.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Penetration", "Channel Market", "Customer", "Customer Success Manager", "Expansion Opportunity", "Market Segment", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.039964"},
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
                        69.19,
                        61.52,
                        64.12,
                        60.28,
                        69.34,
                        69.55,
                        75.7,
                        72.66,
                        63.2,
                        72.47,
                        70.91,
                        67.01
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.01,
                "unit": "%",
                "change": -3.9,
                "change_percent": -5.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 68.0,
                "min": 60.28,
                "max": 75.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 18.77,
                        "percentage": 28.0
                },
                {
                        "category": "Existing Customers",
                        "value": 10.04,
                        "percentage": 15.0
                },
                {
                        "category": "VIP Customers",
                        "value": 6.99,
                        "percentage": 10.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.35,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 26.86,
                        "percentage": 40.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.186985",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Market Penetration Rate"
        }
    },
}
