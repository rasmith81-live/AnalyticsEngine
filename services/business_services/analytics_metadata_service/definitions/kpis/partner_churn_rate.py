"""
Partner Churn Rate

The rate at which channel partners cease doing business with the company over a specific period.
"""

PARTNER_CHURN_RATE = {
    "code": "PARTNER_CHURN_RATE",
    "name": "Partner Churn Rate",
    "description": "The rate at which channel partners cease doing business with the company over a specific period.",
    "formula": "(Number of Partners Lost Over Period / Number of Partners at Start of Period) * 100",
    "calculation_formula": "(Number of Partners Lost Over Period / Number of Partners at Start of Period) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Churn Rate to be added.",
    "trend_analysis": """



    * An increasing partner churn rate may indicate dissatisfaction with the company's support or lack of competitive incentives.
    * A decreasing rate could signal improved partner enablement programs or better alignment with partner business goals.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific regions or product lines where partner churn is more prevalent?
    * What feedback have we received from exiting partners, and are there common themes or issues?
    
    
    
    """,
    "actionable_tips": """



    * Invest in partner training and certification programs to increase partner loyalty and expertise.
    * Regularly review and update partner incentive programs to ensure they remain competitive and aligned with partner goals.
    * Implement a partner feedback mechanism to address issues and improve overall partner experience.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing partner churn rates over time by region or product line.
    * Pie charts to compare the distribution of partner churn reasons (e.g., lack of support, competitive factors, market changes).
    
    
    
    """,
    "risk_warnings": """



    * High partner churn rates can lead to loss of market share and revenue.
    * Frequent partner turnover may indicate underlying issues in the partner program or company support.
    
    
    
    """,
    "tracking_tools": """



    * Partner relationship management (PRM) software to track partner engagement and performance.
    * Customer relationship management (CRM) systems with partner modules to manage partner interactions and feedback.
    
    
    
    """,
    "integration_points": """



    * Integrate partner churn data with sales and revenue figures to understand the impact on overall business performance.
    * Link partner churn metrics with marketing efforts to assess the effectiveness of partner-focused campaigns and initiatives.
    
    
    
    """,
    "change_impact_analysis": """



    * Reducing partner churn can lead to increased sales and market share, but may require additional investment in partner support and incentives.
    * High partner churn rates can negatively impact customer satisfaction and brand reputation, affecting long-term business growth.
    
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Customer", "Lost Sale", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Subscription"], "last_validated": "2025-11-10T13:49:33.182109"},
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
                        66.9,
                        64.67,
                        68.46,
                        63.1,
                        66.32,
                        66.81,
                        60.43,
                        62.69,
                        61.65,
                        55.01,
                        59.15,
                        52.4
                ],
                "unit": "%"
        },
        "current": {
                "value": 52.4,
                "unit": "%",
                "change": -6.75,
                "change_percent": -11.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 62.3,
                "min": 52.4,
                "max": 68.46,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.36,
                        "percentage": 31.2
                },
                {
                        "category": "Segment B",
                        "value": 5.59,
                        "percentage": 10.7
                },
                {
                        "category": "Segment C",
                        "value": 6.99,
                        "percentage": 13.3
                },
                {
                        "category": "Segment D",
                        "value": 3.18,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 20.28,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.448511",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Churn Rate"
        }
    },
}
