"""
Partner Program Compliance Rate

The rate at which channel partners comply with the terms and conditions of the partner program.
"""

PARTNER_PROGRAM_COMPLIANCE_RATE = {
    "code": "PARTNER_PROGRAM_COMPLIANCE_RATE",
    "name": "Partner Program Compliance Rate",
    "description": "The rate at which channel partners comply with the terms and conditions of the partner program.",
    "formula": "(Number of Compliant Partners / Total Number of Partners) * 100",
    "calculation_formula": "(Number of Compliant Partners / Total Number of Partners) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Partner Program Compliance Rate to be added.",
    "trend_analysis": """

    * An increasing partner program compliance rate may indicate better understanding and adherence to the program's terms and conditions.
    * A decreasing rate could signal a lack of clarity or communication regarding the program requirements, leading to non-compliance.
    
    """,
    "diagnostic_questions": """

    * Are there specific aspects of the partner program that partners struggle to comply with?
    * How does our partner program compliance rate compare with industry benchmarks or with historical data?
    
    """,
    "actionable_tips": """

    * Provide regular training and resources to ensure partners fully understand and can comply with the program requirements.
    * Implement a clear and transparent communication strategy to keep partners informed about any updates or changes to the program.
    * Offer incentives for maintaining high compliance rates to motivate partners to adhere to the program terms.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of compliance rates over time.
    * Pie charts comparing compliance rates across different partner segments or regions.
    
    """,
    "risk_warnings": """

    * Low compliance rates can lead to inconsistent branding and customer experience, impacting overall sales performance.
    * Inconsistent compliance may also result in legal or financial risks for the organization.
    
    """,
    "tracking_tools": """

    * Partner relationship management (PRM) software to track and manage partner program compliance.
    * Learning management systems (LMS) to deliver training and educational materials to partners.
    
    """,
    "integration_points": """

    * Integrate compliance data with sales performance metrics to understand the impact of partner program adherence on overall sales results.
    * Link compliance tracking with contract management systems to ensure partners are meeting contractual obligations.
    
    """,
    "change_impact_analysis": """

    * Improving partner program compliance can lead to a more consistent and positive customer experience, potentially increasing customer retention and loyalty.
    * However, stringent compliance requirements may also deter potential partners from joining the program, impacting partner acquisition and network growth.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Advocacy Program", "Loyalty Program", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.892285"},
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
                        58.84,
                        54.78,
                        66.25,
                        54.89,
                        70.5,
                        57.25,
                        58.41,
                        60.99,
                        69.26,
                        59.09,
                        65.98,
                        50.83
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.83,
                "unit": "%",
                "change": -15.15,
                "change_percent": -23.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 60.59,
                "min": 50.83,
                "max": 70.5,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.93,
                        "percentage": 15.6
                },
                {
                        "category": "Category B",
                        "value": 7.51,
                        "percentage": 14.8
                },
                {
                        "category": "Category C",
                        "value": 10.03,
                        "percentage": 19.7
                },
                {
                        "category": "Category D",
                        "value": 3.98,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 21.38,
                        "percentage": 42.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.892285",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Partner Program Compliance Rate"
        }
    },
}
