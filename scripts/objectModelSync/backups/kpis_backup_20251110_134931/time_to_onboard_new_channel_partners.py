"""
Time to Onboard New Channel Partners

The time taken to onboard new channel partners from initial contact to first sale.
"""

TIME_TO_ONBOARD_NEW_CHANNEL_PARTNERS = {
    "code": "TIME_TO_ONBOARD_NEW_CHANNEL_PARTNERS",
    "name": "Time to Onboard New Channel Partners",
    "description": "The time taken to onboard new channel partners from initial contact to first sale.",
    "formula": "Average Number of Days from Partner Agreement to First Sale",
    "calculation_formula": "Average Number of Days from Partner Agreement to First Sale",
    "category": "Channel Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Onboard New Channel Partners to be added.",
    "trend_analysis": """

    * Decreasing time to onboard new channel partners may indicate improved onboarding processes or increased demand for partnership.
    * An increasing time to onboard new channel partners could signal inefficiencies in the onboarding process or a decline in interest from potential partners.
    
    """,
    "diagnostic_questions": """

    * What are the common bottlenecks in the onboarding process for new channel partners?
    * How does our time to onboard new channel partners compare with industry benchmarks or with our competitors?
    
    """,
    "actionable_tips": """

    * Streamline the onboarding process by providing comprehensive training and support materials for new channel partners.
    * Invest in technology solutions that can automate and expedite the onboarding process, such as partner relationship management (PRM) software.
    * Regularly review and update the onboarding process based on feedback from new channel partners to identify and address any pain points.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average time to onboard new channel partners over time.
    * Comparison bar charts displaying the time to onboard new channel partners for different regions or product lines.
    
    """,
    "risk_warnings": """

    * Lengthy onboarding processes may result in potential partners seeking out competitors with faster onboarding procedures.
    * Rapidly increasing time to onboard new channel partners may indicate a need for immediate attention to prevent a negative impact on sales.
    
    """,
    "tracking_tools": """

    * Utilize customer relationship management (CRM) systems to track and manage the onboarding process for new channel partners.
    * Implement collaboration tools such as Slack or Microsoft Teams to facilitate communication and coordination during the onboarding process.
    
    """,
    "integration_points": """

    * Integrate the onboarding process with sales and marketing systems to ensure seamless transition from onboarding to sales activities.
    * Link the onboarding process with customer support systems to provide immediate assistance to new channel partners as they begin their sales activities.
    
    """,
    "change_impact_analysis": """

    * Improving the time to onboard new channel partners can lead to increased sales revenue and market expansion.
    * Conversely, a prolonged onboarding process may result in missed sales opportunities and decreased market competitiveness.
    
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Lost Sale", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:25.027048"},
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
                        444,
                        449,
                        453,
                        473,
                        436,
                        461,
                        458,
                        464,
                        442,
                        437,
                        479,
                        445
                ],
                "unit": "count"
        },
        "current": {
                "value": 445,
                "unit": "count",
                "change": -34,
                "change_percent": -7.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 453.42,
                "min": 436,
                "max": 479,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 70.18,
                        "percentage": 15.8
                },
                {
                        "category": "Category B",
                        "value": 105.38,
                        "percentage": 23.7
                },
                {
                        "category": "Category C",
                        "value": 68.63,
                        "percentage": 15.4
                },
                {
                        "category": "Category D",
                        "value": 48.09,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 152.72,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.027048",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Onboard New Channel Partners"
        }
    },
}
