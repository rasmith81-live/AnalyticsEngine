"""
Partner Renewal Rate

The rate at which channel partners renew their contracts or agreements with the company.
"""

PARTNER_RENEWAL_RATE = {
    "code": "PARTNER_RENEWAL_RATE",
    "name": "Partner Renewal Rate",
    "description": "The rate at which channel partners renew their contracts or agreements with the company.",
    "formula": "(Number of Partners Renewing / Number of Partners Up for Renewal) * 100",
    "calculation_formula": "(Number of Partners Renewing / Number of Partners Up for Renewal) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Renewal Rate to be added.",
    "trend_analysis": """


    * Increasing partner renewal rate may indicate improved satisfaction with the company's products or services.
    * Decreasing renewal rate could signal dissatisfaction, increased competition, or changes in the partner's business strategy.
    
    
    """,
    "diagnostic_questions": """


    * Are there specific reasons partners cite for not renewing their contracts?
    * How does our partner renewal rate compare with industry averages or with our competitors?
    
    
    """,
    "actionable_tips": """


    * Enhance partner support and communication to address any concerns or issues that may lead to non-renewal.
    * Regularly review and update the value proposition for partners to ensure it aligns with their evolving needs and market conditions.
    * Provide incentives for partners to renew, such as early renewal discounts or additional marketing support.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing the trend in partner renewal rates over time.
    * Pie charts comparing renewal rates across different partner segments or regions.
    
    
    """,
    "risk_warnings": """


    * Low partner renewal rates can result in loss of revenue and market share.
    * High partner churn can damage the company's reputation and make it less attractive to potential new partners.
    
    
    """,
    "tracking_tools": """


    * Customer Relationship Management (CRM) systems to track partner interactions and identify potential renewal risks.
    * Partner portal or management software to streamline communication and support for partners.
    
    
    """,
    "integration_points": """


    * Integrate partner renewal data with sales and marketing systems to identify opportunities for proactive engagement.
    * Link renewal rates with partner performance metrics to assess the overall impact on the company's sales and market presence.
    
    
    """,
    "change_impact_analysis": """


    * Improving partner renewal rates can lead to increased revenue and market stability.
    * Conversely, a decline in renewal rates may require adjustments in sales and marketing strategies to attract new partners and customers.
    
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Contract", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Renewal Management", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.215505"},
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
                        73.27,
                        76.65,
                        75.94,
                        63.23,
                        69.8,
                        76.9,
                        67.76,
                        65.87,
                        71.92,
                        58.64,
                        76.93,
                        75.65
                ],
                "unit": "%"
        },
        "current": {
                "value": 75.65,
                "unit": "%",
                "change": -1.28,
                "change_percent": -1.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 71.05,
                "min": 58.64,
                "max": 76.93,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 21.61,
                        "percentage": 28.6
                },
                {
                        "category": "Category B",
                        "value": 18.07,
                        "percentage": 23.9
                },
                {
                        "category": "Category C",
                        "value": 10.76,
                        "percentage": 14.2
                },
                {
                        "category": "Category D",
                        "value": 6.38,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 18.83,
                        "percentage": 24.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.899809",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Renewal Rate"
        }
    },
}
