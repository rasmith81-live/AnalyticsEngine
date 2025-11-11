"""
Prospect Engagement Score

A measure of how involved and interested prospects are during sales interactions.
"""

PROSPECT_ENGAGEMENT_SCORE = {
    "code": "PROSPECT_ENGAGEMENT_SCORE",
    "name": "Prospect Engagement Score",
    "description": "A measure of how involved and interested prospects are during sales interactions.",
    "formula": "Sum of Engagement Activities Scores for Each Prospect",
    "calculation_formula": "Sum of Engagement Activities Scores for Each Prospect",
    "category": "Sales Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Prospect Engagement Score to be added.",
    "trend_analysis": """



    * An increasing prospect engagement score may indicate a growing interest in the products or services being offered.
    * A decreasing score could signal a lack of interest or ineffective sales interactions.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific sales tactics or communication channels that result in higher prospect engagement?
    * How does the prospect engagement score correlate with the conversion rate from prospects to customers?
    
    
    
    """,
    "actionable_tips": """



    * Train sales representatives on effective communication and relationship-building techniques.
    * Utilize customer relationship management (CRM) software to track and analyze prospect interactions.
    * Personalize sales pitches and interactions based on prospect behavior and preferences.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the prospect engagement score over time.
    * Scatter plots to visualize the relationship between prospect engagement and conversion rates.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low prospect engagement score may lead to missed sales opportunities and revenue loss.
    * Overly aggressive sales tactics to boost engagement could result in a negative brand image and potential customer alienation.
    
    
    
    """,
    "tracking_tools": """



    * CRM systems with engagement tracking capabilities, such as Salesforce or HubSpot.
    * Social listening tools to monitor prospect interactions and sentiment on social media platforms.
    
    
    
    """,
    "integration_points": """



    * Integrate prospect engagement data with marketing automation platforms to align sales and marketing efforts.
    * Link prospect engagement scores with customer feedback systems to gain a holistic view of customer satisfaction.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving prospect engagement can lead to higher conversion rates and increased sales revenue.
    * However, overly aggressive tactics may negatively impact brand reputation and long-term customer relationships.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT", "SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Prospect", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.294396"},
    "required_objects": [],
    "modules": ["SALES_DEVELOPMENT", "SALES_ENABLEMENT"],
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
                        73.6,
                        68.6,
                        71.2,
                        73.6,
                        67.5,
                        61.9,
                        69.7,
                        72.9,
                        65.4,
                        69.2,
                        70.6,
                        68.9
                ],
                "unit": "score"
        },
        "current": {
                "value": 68.9,
                "unit": "score",
                "change": -1.7,
                "change_percent": -2.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.42,
                "min": 61.9,
                "max": 73.6,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 23.41,
                        "percentage": 34.0
                },
                {
                        "category": "Segment B",
                        "value": 10.55,
                        "percentage": 15.3
                },
                {
                        "category": "Segment C",
                        "value": 7.93,
                        "percentage": 11.5
                },
                {
                        "category": "Segment D",
                        "value": 6.47,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 20.54,
                        "percentage": 29.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.691681",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Prospect Engagement Score"
        }
    },
}
