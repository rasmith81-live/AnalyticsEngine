"""
Partner Satisfaction Index

A composite metric that measures the overall satisfaction of channel partners with the support, products, and services provided by the company.
"""

PARTNER_SATISFACTION_INDEX = {
    "code": "PARTNER_SATISFACTION_INDEX",
    "name": "Partner Satisfaction Index",
    "description": "A composite metric that measures the overall satisfaction of channel partners with the support, products, and services provided by the company.",
    "formula": "(Sum of Partner Satisfaction Scores / Number of Survey Responses) * 100",
    "calculation_formula": "(Sum of Partner Satisfaction Scores / Number of Survey Responses) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Satisfaction Index to be added.",
    "trend_analysis": """

    * An increasing Partner Satisfaction Index may indicate improved product quality, better support, or expanded service offerings.
    * A decreasing index could signal issues with product availability, support responsiveness, or overall partner experience.
    
    """,
    "diagnostic_questions": """

    * Are there specific products or services that receive consistently lower satisfaction ratings from partners?
    * How does our Partner Satisfaction Index compare with industry benchmarks or with competitors?
    
    """,
    "actionable_tips": """

    * Regularly solicit feedback from partners and act on their suggestions to improve satisfaction.
    * Invest in partner training and enablement to ensure they are equipped to represent and sell the company's products effectively.
    * Provide incentives or rewards for high-performing partners to encourage continued satisfaction and loyalty.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of Partner Satisfaction Index over time.
    * Comparison bar charts to visualize the satisfaction levels across different products or services.
    
    """,
    "risk_warnings": """

    * Low Partner Satisfaction Index can lead to decreased sales and market share as partners may choose to represent competing products.
    * Consistently low satisfaction ratings may indicate systemic issues that could harm the company's reputation in the channel.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track partner interactions and feedback.
    * Partner portal platforms to provide easy access to resources and support materials for partners.
    
    """,
    "integration_points": """

    * Integrate Partner Satisfaction Index data with sales performance metrics to understand the impact of partner satisfaction on revenue.
    * Link partner feedback systems with product development and support teams to drive continuous improvement based on partner input.
    
    """,
    "change_impact_analysis": """

    * Improving Partner Satisfaction Index can lead to increased sales, market share, and overall channel performance.
    * Conversely, a declining index may result in decreased revenue and partner loyalty, impacting long-term channel relationships.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Feedback", "Enablement Feedback", "Key Account", "Key Account Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Partnership", "Product", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"], "last_validated": "2025-11-10T13:43:23.906238"},
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
                        376,
                        383,
                        411,
                        377,
                        370,
                        374,
                        388,
                        394,
                        389,
                        365,
                        387,
                        403
                ],
                "unit": "count"
        },
        "current": {
                "value": 403,
                "unit": "count",
                "change": 16,
                "change_percent": 4.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 384.75,
                "min": 365,
                "max": 411,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 64.89,
                        "percentage": 16.1
                },
                {
                        "category": "Category B",
                        "value": 112.83,
                        "percentage": 28.0
                },
                {
                        "category": "Category C",
                        "value": 77.73,
                        "percentage": 19.3
                },
                {
                        "category": "Category D",
                        "value": 33.46,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 114.09,
                        "percentage": 28.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.906238",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Partner Satisfaction Index"
        }
    },
}
