"""
Multi-threaded Engagement Rate

The percentage of deals where multiple contacts or decision-makers at the prospect's organization are engaged in the sales process.
"""

MULTI_THREADED_ENGAGEMENT_RATE = {
    "code": "MULTI_THREADED_ENGAGEMENT_RATE",
    "name": "Multi-threaded Engagement Rate",
    "description": "The percentage of deals where multiple contacts or decision-makers at the prospect's organization are engaged in the sales process.",
    "formula": "(Number of Multi-threaded Deals / Total Number of Deals) * 100",
    "calculation_formula": "(Number of Multi-threaded Deals / Total Number of Deals) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Multi-threaded Engagement Rate to be added.",
    "trend_analysis": """



    * An increasing multi-threaded engagement rate may indicate a more collaborative and inclusive sales approach, leading to higher deal success rates.
    * A decreasing rate could signal a lack of buy-in from key decision-makers or a failure to effectively engage with multiple stakeholders in the sales process.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific deals or industries where multi-threaded engagement is more or less common?
    * How do our win rates compare between deals with single-threaded engagement versus multi-threaded engagement?
    
    
    
    """,
    "actionable_tips": """



    * Encourage sales teams to identify and engage with multiple stakeholders within the prospect's organization early in the sales process.
    * Provide training and resources to help sales reps navigate complex decision-making structures and build relationships with various contacts.
    * Implement a CRM system that tracks and encourages multi-threaded engagement throughout the sales cycle.
    
    
    
    """,
    "visualization_suggestions": """



    * Stacked bar charts comparing win rates between single-threaded and multi-threaded engagement deals.
    * Line graphs showing the correlation between the number of engaged contacts and deal progression.
    
    
    
    """,
    "risk_warnings": """



    * A low multi-threaded engagement rate may lead to missed opportunities and longer sales cycles.
    * Relying too heavily on a single point of contact within the prospect's organization can increase the risk of deals falling through if that contact leaves or changes their position.
    
    
    
    """,
    "tracking_tools": """



    * CRM platforms with robust contact management and relationship tracking features.
    * Sales enablement tools that provide insights into the engagement levels of various contacts within a prospect's organization.
    
    
    
    """,
    "integration_points": """



    * Integrate multi-threaded engagement data with sales forecasting and pipeline management systems to better predict deal outcomes.
    * Link engagement metrics with customer relationship management systems to ensure a cohesive and coordinated approach to customer interactions.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving multi-threaded engagement can lead to more comprehensive and effective sales strategies, potentially increasing overall revenue and customer satisfaction.
    * However, changes in engagement approaches may require adjustments in sales processes and resource allocation, impacting operational efficiency.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Prospect", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.064471"},
    "required_objects": [],
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
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
                        70.46,
                        83.09,
                        69.13,
                        77.45,
                        66.26,
                        64.05,
                        71.56,
                        78.17,
                        83.17,
                        72.17,
                        81.49,
                        67.54
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.54,
                "unit": "%",
                "change": -13.95,
                "change_percent": -17.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.71,
                "min": 64.05,
                "max": 83.17,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.16,
                        "percentage": 16.5
                },
                {
                        "category": "Segment B",
                        "value": 16.75,
                        "percentage": 24.8
                },
                {
                        "category": "Segment C",
                        "value": 13.35,
                        "percentage": 19.8
                },
                {
                        "category": "Segment D",
                        "value": 4.48,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 21.8,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.222392",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Multi-threaded Engagement Rate"
        }
    },
}
