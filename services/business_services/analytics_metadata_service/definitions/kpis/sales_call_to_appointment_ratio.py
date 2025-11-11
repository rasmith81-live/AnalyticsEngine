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
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Appointment", "Call", "Meeting", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.381670"},
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
                        67.24,
                        57.31,
                        67.43,
                        68.32,
                        66.9,
                        58.99,
                        54.63,
                        62.7,
                        58.72,
                        55.45,
                        62.83,
                        64.6
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.6,
                "unit": "%",
                "change": 1.77,
                "change_percent": 2.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 62.09,
                "min": 54.63,
                "max": 68.32,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 11.57,
                        "percentage": 17.9
                },
                {
                        "category": "Channel Sales",
                        "value": 10.78,
                        "percentage": 16.7
                },
                {
                        "category": "Online Sales",
                        "value": 7.84,
                        "percentage": 12.1
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7.24,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 27.17,
                        "percentage": 42.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.883620",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Call-to-Appointment Ratio"
        }
    },
}
