"""
Customer Engagement Score

A metric that quantifies the degree of customer interaction with a brand through various touchpoints.
"""

CUSTOMER_ENGAGEMENT_SCORE = {
    "code": "CUSTOMER_ENGAGEMENT_SCORE",
    "name": "Customer Engagement Score",
    "description": "A metric that quantifies the degree of customer interaction with a brand through various touchpoints.",
    "formula": "Sum of Engagement Points (based on actions, frequency, etc.) / Total Number of Customers",
    "calculation_formula": "Sum of Engagement Points (based on actions, frequency, etc.) / Total Number of Customers",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Engagement Score to be added.",
    "trend_analysis": """

    * An increasing customer engagement score may indicate improved brand loyalty and customer satisfaction.
    * A decreasing score could signal a decline in customer interest or dissatisfaction with the brand.
    
    """,
    "diagnostic_questions": """

    * Which touchpoints are most effective in driving customer engagement?
    * Are there specific customer segments that show lower engagement scores, and if so, why?
    
    """,
    "actionable_tips": """

    * Personalize customer interactions to make them more relevant and engaging.
    * Implement loyalty programs or rewards to incentivize continued engagement.
    * Regularly analyze customer feedback and sentiment to identify areas for improvement.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of customer engagement scores over time.
    * Heat maps to visualize engagement levels across different touchpoints and customer segments.
    
    """,
    "risk_warnings": """

    * Low customer engagement scores may lead to decreased sales and customer retention.
    * Inconsistent engagement across touchpoints could indicate a lack of cohesive brand experience.
    
    """,
    "tracking_tools": """

    * Customer relationship management (CRM) software to track and analyze customer interactions.
    * Social media monitoring tools to gauge customer sentiment and engagement on digital platforms.
    
    """,
    "integration_points": """

    * Integrate customer engagement scores with sales and marketing systems to align efforts towards improving engagement.
    * Link engagement data with product development to create offerings that resonate with customers.
    
    """,
    "change_impact_analysis": """

    * Improving customer engagement can lead to increased customer lifetime value and brand advocacy.
    * However, a decline in engagement may result in decreased sales and market share.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Product", "Product Adoption", "Product Usage", "Prospect Engagement", "Service Level Agreement"], "last_validated": "2025-11-10T13:43:23.251163"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
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
                        98,
                        86,
                        81,
                        89,
                        118,
                        111,
                        82,
                        88,
                        95,
                        109,
                        82,
                        99
                ],
                "unit": "count"
        },
        "current": {
                "value": 99,
                "unit": "count",
                "change": 17,
                "change_percent": 20.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 94.83,
                "min": 81,
                "max": 118,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 31.99,
                        "percentage": 32.3
                },
                {
                        "category": "Category B",
                        "value": 18.76,
                        "percentage": 18.9
                },
                {
                        "category": "Category C",
                        "value": 16.71,
                        "percentage": 16.9
                },
                {
                        "category": "Category D",
                        "value": 9.38,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 22.16,
                        "percentage": 22.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.251163",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Engagement Score"
        }
    },
}
