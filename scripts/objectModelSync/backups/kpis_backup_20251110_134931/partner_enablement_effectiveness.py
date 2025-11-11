"""
Partner Enablement Effectiveness

A measure of how effectively the company enables its partners through resources, tools, and support to maximize their sales efforts.
"""

PARTNER_ENABLEMENT_EFFECTIVENESS = {
    "code": "PARTNER_ENABLEMENT_EFFECTIVENESS",
    "name": "Partner Enablement Effectiveness",
    "description": "A measure of how effectively the company enables its partners through resources, tools, and support to maximize their sales efforts.",
    "formula": "Partner Sales Performance Before and After Enablement Programs",
    "calculation_formula": "Partner Sales Performance Before and After Enablement Programs",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Enablement Effectiveness to be added.",
    "trend_analysis": """

    * An increasing partner enablement effectiveness may indicate better utilization of resources and improved support for partners, leading to increased sales.
    * A decreasing effectiveness could signal a lack of relevant tools or resources for partners, resulting in missed sales opportunities.
    
    """,
    "diagnostic_questions": """

    * Are partners satisfied with the resources and support provided by the company?
    * What specific tools or training do partners feel would enhance their sales efforts?
    
    """,
    "actionable_tips": """

    * Regularly gather feedback from partners to understand their needs and challenges.
    * Invest in training programs and resources that are tailored to the specific needs of different partner segments.
    * Provide easy access to sales collateral, product information, and marketing materials for partners.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of partner enablement effectiveness over time.
    * Pie charts to compare the distribution of resources and support provided to different partner segments.
    
    """,
    "risk_warnings": """

    * Low partner enablement effectiveness may lead to decreased partner loyalty and engagement.
    * Ineffective partner enablement can result in missed sales opportunities and decreased market share.
    
    """,
    "tracking_tools": """

    * Partner relationship management (PRM) software to track partner interactions and resource utilization.
    * Learning management systems (LMS) for delivering training and educational materials to partners.
    
    """,
    "integration_points": """

    * Integrate partner feedback and performance data with the company's CRM system for a comprehensive view of partner relationships.
    * Link partner enablement effectiveness with sales performance metrics to understand the impact on overall sales results.
    
    """,
    "change_impact_analysis": """

    * Improving partner enablement effectiveness can lead to increased sales revenue and market expansion.
    * Conversely, a decline in partner enablement may result in decreased sales performance and market competitiveness.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Enablement Feedback", "Enablement Platform", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"], "last_validated": "2025-11-10T13:43:23.864479"},
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
                        378.08,
                        298.94,
                        296.36,
                        274.91,
                        299.11,
                        289.64,
                        271.41,
                        302.17,
                        328.76,
                        384.78,
                        395.69,
                        298.7
                ],
                "unit": "units"
        },
        "current": {
                "value": 298.7,
                "unit": "units",
                "change": -96.99,
                "change_percent": -24.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 318.21,
                "min": 271.41,
                "max": 395.69,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 80.43,
                        "percentage": 26.9
                },
                {
                        "category": "Category B",
                        "value": 45.01,
                        "percentage": 15.1
                },
                {
                        "category": "Category C",
                        "value": 34.25,
                        "percentage": 11.5
                },
                {
                        "category": "Category D",
                        "value": 15.41,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 123.6,
                        "percentage": 41.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.864479",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Partner Enablement Effectiveness"
        }
    },
}
