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
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Lost Sale", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.712430"},
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
                        293,
                        275,
                        265,
                        296,
                        308,
                        275,
                        285,
                        296,
                        306,
                        300,
                        286,
                        312
                ],
                "unit": "count"
        },
        "current": {
                "value": 312,
                "unit": "count",
                "change": 26,
                "change_percent": 9.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 291.42,
                "min": 265,
                "max": 312,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 53.31,
                        "percentage": 17.1
                },
                {
                        "category": "Segment B",
                        "value": 90.4,
                        "percentage": 29.0
                },
                {
                        "category": "Segment C",
                        "value": 40.11,
                        "percentage": 12.9
                },
                {
                        "category": "Segment D",
                        "value": 18.87,
                        "percentage": 6.0
                },
                {
                        "category": "Other",
                        "value": 109.31,
                        "percentage": 35.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.762761",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Onboard New Channel Partners"
        }
    },
}
