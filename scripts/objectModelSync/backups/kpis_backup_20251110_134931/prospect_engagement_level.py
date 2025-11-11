"""
Prospect Engagement Level

The level of interaction and interest shown by prospects during the sales process.
"""

PROSPECT_ENGAGEMENT_LEVEL = {
    "code": "PROSPECT_ENGAGEMENT_LEVEL",
    "name": "Prospect Engagement Level",
    "description": "The level of interaction and interest shown by prospects during the sales process.",
    "formula": "Engagement Metrics (e.g., page views, downloads) / Number of Prospects",
    "calculation_formula": "Engagement Metrics (e.g., page views, downloads) / Number of Prospects",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Prospect Engagement Level to be added.",
    "trend_analysis": """

    * An increasing prospect engagement level may indicate a growing interest in the product or service being offered.
    * A decreasing engagement level could signal a need for adjustments in the sales approach or a lack of alignment between the product and the target audience.
    
    """,
    "diagnostic_questions": """

    * Are there specific stages in the sales process where prospects tend to disengage?
    * What feedback have the sales team received from prospects regarding their level of engagement?
    
    """,
    "actionable_tips": """

    * Provide sales training to improve communication and relationship-building skills.
    * Personalize the sales approach to better resonate with the needs and interests of prospects.
    * Implement a lead nurturing strategy to maintain engagement throughout the sales process.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of prospect engagement level over time.
    * Funnel charts to visualize the drop-off points in the sales process where engagement decreases.
    
    """,
    "risk_warnings": """

    * Low prospect engagement levels can lead to longer sales cycles and decreased conversion rates.
    * Consistently low engagement may indicate a need for reevaluation of the target audience or product positioning.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and analyze prospect interactions.
    * Sales engagement platforms to automate and optimize outreach efforts.
    
    """,
    "integration_points": """

    * Integrate prospect engagement data with marketing analytics to understand the effectiveness of lead generation efforts.
    * Link engagement levels with customer feedback systems to gather insights on the sales process from the prospect's perspective.
    
    """,
    "change_impact_analysis": """

    * Increasing prospect engagement can lead to higher conversion rates and improved sales performance.
    * However, overly aggressive sales tactics to boost engagement may negatively impact brand reputation and long-term customer relationships.
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Prospect", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:24.003975"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
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
                        81,
                        71,
                        59,
                        58,
                        43,
                        73,
                        61,
                        69,
                        81,
                        68,
                        65,
                        67
                ],
                "unit": "count"
        },
        "current": {
                "value": 67,
                "unit": "count",
                "change": 2,
                "change_percent": 3.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 66.33,
                "min": 43,
                "max": 81,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.02,
                        "percentage": 20.9
                },
                {
                        "category": "Category B",
                        "value": 15.07,
                        "percentage": 22.5
                },
                {
                        "category": "Category C",
                        "value": 11.36,
                        "percentage": 17.0
                },
                {
                        "category": "Category D",
                        "value": 4.07,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 22.48,
                        "percentage": 33.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.003975",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Prospect Engagement Level"
        }
    },
}
