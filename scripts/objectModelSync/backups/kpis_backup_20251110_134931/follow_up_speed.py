"""
Follow-up Speed

How quickly the Sales Development team follows up with new leads. A shorter follow-up time can lead to better conversion rates and a higher likelihood of closing deals.
"""

FOLLOW_UP_SPEED = {
    "code": "FOLLOW_UP_SPEED",
    "name": "Follow-up Speed",
    "description": "How quickly the Sales Development team follows up with new leads. A shorter follow-up time can lead to better conversion rates and a higher likelihood of closing deals.",
    "formula": "Time from Initial Contact to Follow-up",
    "calculation_formula": "Time from Initial Contact to Follow-up",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Follow-up Speed to be added.",
    "trend_analysis": """

    * A decreasing follow-up speed may indicate a lack of urgency or capacity within the Sales Development team.
    * An increasing follow-up speed could signal improved efficiency or better utilization of resources.
    
    """,
    "diagnostic_questions": """

    * What are the current average response times for different lead sources or types?
    * Are there any bottlenecks or obstacles in the follow-up process that are causing delays?
    
    """,
    "actionable_tips": """

    * Implement automated lead distribution and follow-up systems to reduce manual delays.
    * Provide ongoing training and coaching to the Sales Development team to improve their responsiveness and time management.
    * Utilize lead scoring to prioritize follow-up on the most promising leads.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the average follow-up time over different time periods (e.g., daily, weekly, monthly).
    * Comparison bar charts to visualize follow-up speed across different team members or lead sources.
    
    """,
    "risk_warnings": """

    * Slow follow-up speed can result in missed opportunities and potential revenue loss.
    * Rapid follow-up without proper qualification can lead to wasted resources and decreased conversion rates.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) software with lead tracking and automated follow-up capabilities.
    * Lead management platforms that provide real-time alerts and notifications for new leads.
    
    """,
    "integration_points": """

    * Integrate follow-up speed data with lead generation and marketing systems to understand the impact of lead quality on response times.
    * Link follow-up speed with sales performance metrics to analyze the correlation between follow-up efficiency and deal closure rates.
    
    """,
    "change_impact_analysis": """

    * Improving follow-up speed can lead to increased lead-to-opportunity conversion rates and overall sales productivity.
    * However, overly aggressive follow-up tactics may negatively impact customer experience and brand reputation.
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Lead", "Lead Qualification", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.497417"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
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
                        383.47,
                        471.83,
                        459.78,
                        436.9,
                        395.42,
                        516.3,
                        404.87,
                        428.61,
                        516.17,
                        435.09,
                        425.38,
                        487.17
                ],
                "unit": "units"
        },
        "current": {
                "value": 487.17,
                "unit": "units",
                "change": 61.79,
                "change_percent": 14.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 446.75,
                "min": 383.47,
                "max": 516.3,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 81.13,
                        "percentage": 16.7
                },
                {
                        "category": "Category B",
                        "value": 95.2,
                        "percentage": 19.5
                },
                {
                        "category": "Category C",
                        "value": 87.58,
                        "percentage": 18.0
                },
                {
                        "category": "Category D",
                        "value": 65.73,
                        "percentage": 13.5
                },
                {
                        "category": "Other",
                        "value": 157.53,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.497417",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Follow-up Speed"
        }
    },
}
