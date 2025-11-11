"""
Follow-up Contact Rate

The frequency at which the sales team follows up with leads and prospects.
"""

FOLLOW_UP_CONTACT_RATE = {
    "code": "FOLLOW_UP_CONTACT_RATE",
    "name": "Follow-up Contact Rate",
    "description": "The frequency at which the sales team follows up with leads and prospects.",
    "formula": "(Number of Leads Followed Up / Total Number of Leads) * 100",
    "calculation_formula": "(Number of Leads Followed Up / Total Number of Leads) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Follow-up Contact Rate to be added.",
    "trend_analysis": """



    * An increasing follow-up contact rate may indicate a proactive sales team or a growing number of leads and prospects.
    * A decreasing rate could signal a lack of follow-up processes or a decline in the quality of leads.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific leads or prospects that are consistently followed up with, and are there others that are often neglected?
    * How does our follow-up contact rate compare with industry benchmarks or with the performance of top-performing sales teams?
    
    
    
    """,
    "actionable_tips": """



    * Implement a structured follow-up schedule to ensure all leads and prospects are consistently contacted.
    * Utilize customer relationship management (CRM) software to automate and track follow-up activities.
    * Provide regular training and coaching to the sales team on effective follow-up techniques and best practices.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of follow-up contact rates over time.
    * Pie charts comparing follow-up contact rates for different sales representatives or territories.
    
    
    
    """,
    "risk_warnings": """



    * A low follow-up contact rate can result in missed sales opportunities and decreased conversion rates.
    * An excessively high follow-up contact rate may lead to customer annoyance or perception of pushiness.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems such as Salesforce or HubSpot for tracking and managing follow-up activities.
    * Sales engagement platforms like Outreach or SalesLoft to automate and optimize follow-up processes.
    
    
    
    """,
    "integration_points": """



    * Integrate follow-up contact rate data with lead generation systems to identify the most responsive lead sources.
    * Link follow-up contact rate with customer feedback systems to understand the impact of follow-up on customer satisfaction.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the follow-up contact rate can lead to increased sales and revenue, but may also require additional resources and time from the sales team.
    * A declining follow-up contact rate can negatively impact the overall sales performance and the effectiveness of marketing efforts.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "replaces": ["RATE_OF_FOLLOW_UP_CONTACT"], "last_validated": "2025-11-10T13:49:32.958794"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_OPERATIONS"],
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
                        77.48,
                        64.49,
                        75.48,
                        75.92,
                        65.4,
                        73.84,
                        59.33,
                        69.71,
                        74.39,
                        59.77,
                        69.42,
                        63.87
                ],
                "unit": "%"
        },
        "current": {
                "value": 63.87,
                "unit": "%",
                "change": -5.55,
                "change_percent": -8.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 69.09,
                "min": 59.33,
                "max": 77.48,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.9,
                        "percentage": 17.1
                },
                {
                        "category": "Segment B",
                        "value": 13.07,
                        "percentage": 20.5
                },
                {
                        "category": "Segment C",
                        "value": 9.72,
                        "percentage": 15.2
                },
                {
                        "category": "Segment D",
                        "value": 7.93,
                        "percentage": 12.4
                },
                {
                        "category": "Other",
                        "value": 22.25,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.996499",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Follow-up Contact Rate"
        }
    },
}
