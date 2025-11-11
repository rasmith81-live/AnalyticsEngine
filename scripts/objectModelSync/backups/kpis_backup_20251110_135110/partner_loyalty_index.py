"""
Partner Loyalty Index

A measure of the loyalty of channel partners, which can be determined through factors such as repeat business and long-term commitment.
"""

PARTNER_LOYALTY_INDEX = {
    "code": "PARTNER_LOYALTY_INDEX",
    "name": "Partner Loyalty Index",
    "description": "A measure of the loyalty of channel partners, which can be determined through factors such as repeat business and long-term commitment.",
    "formula": "Composite Score Based on Loyalty Metrics (e.g., NPS, Retention, Advocacy)",
    "calculation_formula": "Composite Score Based on Loyalty Metrics (e.g., NPS, Retention, Advocacy)",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Loyalty Index to be added.",
    "trend_analysis": """


    * An increasing partner loyalty index may indicate stronger relationships with channel partners and higher levels of trust and satisfaction.
    * A decreasing index could signal dissatisfaction, competition from other vendors, or changes in the partner's business strategy.
    
    
    """,
    "diagnostic_questions": """


    * What specific actions or programs have been implemented to strengthen relationships with channel partners?
    * Are there any recent changes in the market or industry that could be impacting partner loyalty?
    
    
    """,
    "actionable_tips": """


    * Regularly communicate with channel partners to understand their needs and challenges.
    * Provide training and support to help partners effectively sell and support your products or services.
    * Offer incentives or rewards for achieving sales targets and demonstrating loyalty.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend of partner loyalty index over time.
    * Pie charts to compare the distribution of loyalty levels among different partners or regions.
    
    
    """,
    "risk_warnings": """


    * Low partner loyalty can lead to decreased sales and market share as partners may shift their focus to other vendors.
    * High partner turnover can result in increased costs associated with recruiting and training new partners.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) systems to track interactions and engagement with channel partners.
    * Partner Relationship Management (PRM) software to streamline partner communication and collaboration.
    
    
    """,
    "integration_points": """


    * Integrate partner loyalty data with sales performance metrics to understand the impact of partner relationships on overall sales results.
    * Link partner loyalty index with marketing efforts to align promotional activities with partner needs and preferences.
    
    
    """,
    "change_impact_analysis": """


    * Improving partner loyalty can lead to increased sales, market share, and brand advocacy.
    * Conversely, declining partner loyalty may result in decreased revenue and negative word-of-mouth, impacting overall business performance.
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Loyalty Program", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.204838"},
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
                        82.7,
                        78.7,
                        90.4,
                        90.4,
                        91.2,
                        78.9,
                        83.9,
                        83.9,
                        78.8,
                        79.5,
                        89.6,
                        90.4
                ],
                "unit": "score"
        },
        "current": {
                "value": 90.4,
                "unit": "score",
                "change": 0.8,
                "change_percent": 0.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 84.87,
                "min": 78.7,
                "max": 91.2,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 29.45,
                        "percentage": 32.6
                },
                {
                        "category": "Category B",
                        "value": 10.1,
                        "percentage": 11.2
                },
                {
                        "category": "Category C",
                        "value": 15.31,
                        "percentage": 16.9
                },
                {
                        "category": "Category D",
                        "value": 4.72,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 30.82,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.880994",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Partner Loyalty Index"
        }
    },
}
