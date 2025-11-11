"""
Sales Call-to-Appointment Ratio

The ratio of sales calls made to the number of appointments or follow-up meetings secured.
"""

SALES_CALL_TO_APPOINTMENT_RATIO = {
    "code": "SALES_CALL_TO_APPOINTMENT_RATIO",
    "name": "Sales Call-to-Appointment Ratio",
    "description": "The ratio of sales calls made to the number of appointments or follow-up meetings secured.",
    "formula": "Number of Appointments Set / Total Number of Sales Calls Made * 100",
    "calculation_formula": "Number of Appointments Set / Total Number of Sales Calls Made * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Call-to-Appointment Ratio to be added.",
    "trend_analysis": """

    * An increasing sales call-to-appointment ratio may indicate a more effective sales pitch or better targeting of potential clients.
    * A decreasing ratio could signal a decline in the quality of leads or a need for sales training and development.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales strategies or pitches that have led to a higher appointment ratio?
    * How does our appointment ratio compare with industry benchmarks or with different sales representatives?
    
    """,
    "actionable_tips": """

    * Provide sales training to improve the quality of sales pitches and increase the likelihood of securing appointments.
    * Implement a lead scoring system to prioritize higher quality leads for follow-up.
    * Regularly review and update the sales pitch based on feedback and performance data.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of appointment ratios over time for different sales representatives or regions.
    * Pie charts to compare the distribution of secured appointments across different lead sources or industries.
    
    """,
    "risk_warnings": """

    * A low appointment ratio may lead to missed sales opportunities and revenue loss.
    * Consistently high ratios may indicate that sales representatives are being too selective and missing out on potential clients.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software to track and analyze sales call outcomes and appointment conversions.
    * Sales enablement platforms to provide sales representatives with the necessary tools and resources to improve their appointment conversion rates.
    
    """,
    "integration_points": """

    * Integrate appointment ratio data with lead generation systems to identify which sources are providing the highest quality leads.
    * Link appointment ratio with customer relationship management systems to track the conversion of appointments into actual sales.
    
    """,
    "change_impact_analysis": """

    * Improving the appointment ratio can lead to increased sales revenue and customer acquisition.
    * However, a focus solely on increasing the ratio may lead to a decline in the quality of appointments and potential long-term customer relationships.
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Appointment", "Call", "Meeting", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:24.160423"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
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
                        54.52,
                        48.67,
                        49.47,
                        48.14,
                        45.72,
                        47.67,
                        43.81,
                        51.6,
                        46.49,
                        56.87,
                        57.02,
                        40.65
                ],
                "unit": "%"
        },
        "current": {
                "value": 40.65,
                "unit": "%",
                "change": -16.37,
                "change_percent": -28.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 49.22,
                "min": 40.65,
                "max": 57.02,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.33,
                        "percentage": 18.0
                },
                {
                        "category": "Category B",
                        "value": 6.8,
                        "percentage": 16.7
                },
                {
                        "category": "Category C",
                        "value": 4.67,
                        "percentage": 11.5
                },
                {
                        "category": "Category D",
                        "value": 4.59,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 17.26,
                        "percentage": 42.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.160423",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Call-to-Appointment Ratio"
        }
    },
}
