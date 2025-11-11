"""
Email Click-Through Rate (CTR)

The percentage of recipients who click on a link contained in a sales email.
"""

EMAIL_CLICK_THROUGH_RATE_CTR = {
    "code": "EMAIL_CLICK_THROUGH_RATE_CTR",
    "name": "Email Click-Through Rate (CTR)",
    "description": "The percentage of recipients who click on a link contained in a sales email.",
    "formula": "(Number of Clicks / Number of Delivered Emails) * 100",
    "calculation_formula": "(Number of Clicks / Number of Delivered Emails) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Email Click-Through Rate (CTR) to be added.",
    "trend_analysis": """



    * A rising email click-through rate may indicate more engaging email content or improved targeting of recipients.
    * A decreasing rate could signal email fatigue among recipients or a need for better segmentation and personalization.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific types of content or subject lines that consistently result in higher click-through rates?
    * How does our email click-through rate compare with industry benchmarks or with different segments of our target audience?
    
    
    
    """,
    "actionable_tips": """



    * Experiment with different types of content, visuals, and calls-to-action in emails to see what resonates best with recipients.
    * Segment email lists based on recipient behavior and interests to deliver more personalized and relevant content.
    * Regularly clean and update email lists to remove inactive or unengaged recipients.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of click-through rates over time.
    * Heat maps to identify which links within emails are generating the most clicks.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low click-through rate may lead to decreased sales opportunities and revenue.
    * High click-through rates without corresponding conversion rates may indicate a disconnect between email content and the sales process.
    
    
    
    """,
    "tracking_tools": """



    * Email marketing platforms like Mailchimp or HubSpot that provide detailed analytics on email performance.
    * A/B testing tools to experiment with different email elements and measure their impact on click-through rates.
    
    
    
    """,
    "integration_points": """



    * Integrate email click-through rate data with CRM systems to track the impact on lead generation and sales opportunities.
    * Link with marketing automation platforms to adjust email content and targeting based on recipient behavior and engagement.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the email click-through rate can lead to increased lead generation and sales opportunities, but may also require investment in content creation and audience segmentation.
    * Conversely, a declining click-through rate can signal the need for a reassessment of email marketing strategies and potentially impact overall marketing ROI.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Email", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:32.939061"},
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
                        76.6,
                        74.83,
                        76.55,
                        68.22,
                        64.99,
                        59.46,
                        57.7,
                        66.18,
                        59.11,
                        63.63,
                        71.91,
                        72.24
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.24,
                "unit": "%",
                "change": 0.33,
                "change_percent": 0.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.62,
                "min": 57.7,
                "max": 76.6,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17.79,
                        "percentage": 24.6
                },
                {
                        "category": "Segment B",
                        "value": 13.27,
                        "percentage": 18.4
                },
                {
                        "category": "Segment C",
                        "value": 12.08,
                        "percentage": 16.7
                },
                {
                        "category": "Segment D",
                        "value": 7.88,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 21.22,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.948996",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Email Click-Through Rate (CTR)"
        }
    },
}
