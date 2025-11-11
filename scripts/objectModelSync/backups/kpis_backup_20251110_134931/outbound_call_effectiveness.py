"""
Outbound Call Effectiveness

The effectiveness of outbound sales calls measured by metrics such as conversion rate and average call duration.
"""

OUTBOUND_CALL_EFFECTIVENESS = {
    "code": "OUTBOUND_CALL_EFFECTIVENESS",
    "name": "Outbound Call Effectiveness",
    "description": "The effectiveness of outbound sales calls measured by metrics such as conversion rate and average call duration.",
    "formula": "Total Positive Outcomes from Calls / Total Number of Calls Made",
    "calculation_formula": "Total Positive Outcomes from Calls / Total Number of Calls Made",
    "category": "Sales Strategy",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Outbound Call Effectiveness to be added.",
    "trend_analysis": """

    * An increasing outbound call conversion rate may indicate improved sales pitch effectiveness or better lead quality.
    * A decreasing average call duration could suggest more efficient communication or a decline in customer engagement.
    
    """,
    "diagnostic_questions": """

    * Are there specific customer segments that respond better to outbound calls?
    * How does our outbound call effectiveness compare with industry benchmarks or competitor performance?
    
    """,
    "actionable_tips": """

    * Provide targeted sales training to improve call quality and conversion rates.
    * Implement customer relationship management (CRM) systems to track and analyze call outcomes.
    * Regularly review and update call scripts to ensure relevance and effectiveness.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of conversion rates and call durations over time.
    * Pie charts to compare conversion rates across different sales representatives or teams.
    
    """,
    "risk_warnings": """

    * Low conversion rates may lead to wasted resources and demotivation among sales teams.
    * Long average call durations can indicate inefficiencies in the sales process or poor lead qualification.
    
    """,
    "tracking_tools": """

    * Call tracking and analytics software like CallRail or CallTrackingMetrics.
    * CRM systems with built-in call management features such as Salesforce or HubSpot.
    
    """,
    "integration_points": """

    * Integrate outbound call data with sales performance metrics to assess overall sales effectiveness.
    * Link call outcomes with customer data to personalize future outreach and improve conversion rates.
    
    """,
    "change_impact_analysis": """

    * Improving outbound call effectiveness can lead to increased sales revenue and customer acquisition.
    * However, overly aggressive outbound calling may negatively impact brand reputation and customer satisfaction.
    
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Appointment", "Call", "Deal", "Lead", "Lead Qualification", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.772649"},
    "required_objects": [],
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
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
                        211,
                        177,
                        200,
                        220,
                        207,
                        207,
                        187,
                        214,
                        175,
                        195,
                        204,
                        191
                ],
                "unit": "count"
        },
        "current": {
                "value": 191,
                "unit": "count",
                "change": -13,
                "change_percent": -6.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 199.0,
                "min": 175,
                "max": 220,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 55.69,
                        "percentage": 29.2
                },
                {
                        "category": "Category B",
                        "value": 22.37,
                        "percentage": 11.7
                },
                {
                        "category": "Category C",
                        "value": 17.76,
                        "percentage": 9.3
                },
                {
                        "category": "Category D",
                        "value": 21.61,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 73.57,
                        "percentage": 38.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.772649",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Outbound Call Effectiveness"
        }
    },
}
