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
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Prospect", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.292835"},
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
                        325,
                        309,
                        312,
                        334,
                        309,
                        331,
                        303,
                        319,
                        307,
                        332,
                        333,
                        312
                ],
                "unit": "count"
        },
        "current": {
                "value": 312,
                "unit": "count",
                "change": -21,
                "change_percent": -6.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 318.83,
                "min": 303,
                "max": 334,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 60.96,
                        "percentage": 19.5
                },
                {
                        "category": "Segment B",
                        "value": 50.65,
                        "percentage": 16.2
                },
                {
                        "category": "Segment C",
                        "value": 65.99,
                        "percentage": 21.2
                },
                {
                        "category": "Segment D",
                        "value": 29.49,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 104.91,
                        "percentage": 33.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.687263",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Prospect Engagement Level"
        }
    },
}
