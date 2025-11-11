"""
Market Share Growth

The increase in a company's sales volume in relation to the total sales volume of all competitors in the market, indicating the company's growing dominance in the market.
"""

MARKET_SHARE_GROWTH = {
    "code": "MARKET_SHARE_GROWTH",
    "name": "Market Share Growth",
    "description": "The increase in a company's sales volume in relation to the total sales volume of all competitors in the market, indicating the company's growing dominance in the market.",
    "formula": "((Current Market Share - Previous Market Share) / Previous Market Share) * 100",
    "calculation_formula": "((Current Market Share - Previous Market Share) / Previous Market Share) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Market Share Growth to be added.",
    "trend_analysis": """



    * Market share growth tends to show a gradual increase over time as the company gains traction in the market.
    * Positive performance shifts may be indicated by consistent, steady growth in market share, while negative shifts could be seen in stagnant or declining growth rates.
    
    
    
    """,
    "diagnostic_questions": """



    * What specific strategies or initiatives have contributed to the increase in market share?
    * Are there any external factors or market conditions that could be influencing the market share growth?
    
    
    
    """,
    "actionable_tips": """



    * Invest in targeted marketing and sales efforts to capture a larger share of the market.
    * Focus on product differentiation and innovation to attract more customers and increase market share.
    * Explore strategic partnerships or acquisitions to expand market presence and gain a competitive edge.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts to visually represent the steady increase in market share over time.
    * Pie charts to compare the company's market share with that of competitors in a specific timeframe.
    
    
    
    """,
    "risk_warnings": """



    * Rapid market share growth may lead to increased competition and potential price wars.
    * Overreliance on a specific market segment for growth could pose risks if that segment becomes saturated or experiences a downturn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze customer acquisition and retention efforts.
    * Competitor analysis tools to monitor and compare market share data with industry competitors.
    
    
    
    """,
    "integration_points": """



    * Integrate market share data with sales and marketing systems to align strategies with growth opportunities.
    * Link market share metrics with financial systems to assess the impact of market share growth on revenue and profitability.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing market share can lead to economies of scale and potentially lower production costs.
    * However, aggressive tactics to gain market share may impact brand reputation and customer loyalty if not managed carefully.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Market Segment", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.042198"},
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
                        71.54,
                        78.34,
                        75.83,
                        63.41,
                        59.55,
                        70.97,
                        65.57,
                        67.51,
                        69.39,
                        59.45,
                        75.27,
                        77.2
                ],
                "unit": "%"
        },
        "current": {
                "value": 77.2,
                "unit": "%",
                "change": 1.93,
                "change_percent": 2.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 69.5,
                "min": 59.45,
                "max": 78.34,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.48,
                        "percentage": 18.8
                },
                {
                        "category": "Segment B",
                        "value": 12.84,
                        "percentage": 16.6
                },
                {
                        "category": "Segment C",
                        "value": 14.01,
                        "percentage": 18.1
                },
                {
                        "category": "Segment D",
                        "value": 10.4,
                        "percentage": 13.5
                },
                {
                        "category": "Other",
                        "value": 25.47,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.192338",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Market Share Growth"
        }
    },
}
