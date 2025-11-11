"""
Email Open Rate

The percentage of sales emails sent that are opened by recipients.
"""

EMAIL_OPEN_RATE = {
    "code": "EMAIL_OPEN_RATE",
    "name": "Email Open Rate",
    "description": "The percentage of sales emails sent that are opened by recipients.",
    "formula": "(Number of Emails Opened / Number of Emails Sent) * 100",
    "calculation_formula": "(Number of Emails Opened / Number of Emails Sent) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Email Open Rate to be added.",
    "trend_analysis": """



    * A rising email open rate may indicate improved email subject lines or more engaging content.
    * A decreasing rate could signal email deliverability issues or a decline in recipient interest.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific types of emails (e.g., promotional, informational) that have higher or lower open rates?
    * How does our email open rate compare with industry benchmarks or with different segments of our target audience?
    
    
    
    """,
    "actionable_tips": """



    * Optimize email subject lines and content to increase recipient engagement.
    * Regularly clean and update email lists to improve deliverability and engagement.
    * Segment email lists and tailor content to different audience preferences and behaviors.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of email open rates over time.
    * Comparison bar charts displaying open rates for different types of emails or audience segments.
    
    
    
    """,
    "risk_warnings": """



    * Low email open rates can lead to reduced sales opportunities and lower ROI on email marketing efforts.
    * Consistently declining open rates may indicate broader issues with email marketing strategy or audience targeting.
    
    
    
    """,
    "tracking_tools": """



    * Email marketing platforms like Mailchimp or HubSpot for tracking and analyzing open rates.
    * Data cleansing tools to maintain accurate and engaged email lists.
    
    
    
    """,
    "integration_points": """



    * Integrate email open rate data with CRM systems to better understand the impact on sales and customer engagement.
    * Link with marketing automation platforms to adjust email content and timing based on open rate performance.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving email open rates can lead to increased sales opportunities and better ROI on marketing efforts.
    * However, changes in email content or frequency may impact overall email deliverability and engagement metrics.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Email", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.940588"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "INSIDE_SALES",
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
                        67.26,
                        80.28,
                        72.96,
                        68.41,
                        67.32,
                        75.4,
                        77.66,
                        65.82,
                        67.22,
                        79.56,
                        72.02,
                        66.16
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.16,
                "unit": "%",
                "change": -5.86,
                "change_percent": -8.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.67,
                "min": 65.82,
                "max": 80.28,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.41,
                        "percentage": 24.8
                },
                {
                        "category": "Segment B",
                        "value": 10.17,
                        "percentage": 15.4
                },
                {
                        "category": "Segment C",
                        "value": 9.17,
                        "percentage": 13.9
                },
                {
                        "category": "Segment D",
                        "value": 4.59,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 25.82,
                        "percentage": 39.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.952559",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Email Open Rate"
        }
    },
}
