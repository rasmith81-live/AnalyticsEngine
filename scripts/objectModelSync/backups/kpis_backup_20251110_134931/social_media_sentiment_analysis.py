"""
Social Media Sentiment Analysis

The evaluation of customer sentiment and satisfaction through social media channels.
"""

SOCIAL_MEDIA_SENTIMENT_ANALYSIS = {
    "code": "SOCIAL_MEDIA_SENTIMENT_ANALYSIS",
    "name": "Social Media Sentiment Analysis",
    "description": "The evaluation of customer sentiment and satisfaction through social media channels.",
    "formula": "Ratio or Score Based on Sentiment Analysis of Social Media Mentions",
    "calculation_formula": "Ratio or Score Based on Sentiment Analysis of Social Media Mentions",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Social Media Sentiment Analysis to be added.",
    "trend_analysis": """

    * An increase in negative sentiment on social media may indicate declining customer satisfaction or issues with product quality or service.
    * A decrease in positive sentiment could signal a shift in customer preferences, competitive pressures, or marketing effectiveness.
    
    """,
    "diagnostic_questions": """

    * What specific aspects of our products or services are being mentioned in customer sentiment analysis?
    * How does our sentiment analysis compare with competitors or industry benchmarks?
    
    """,
    "actionable_tips": """

    * Actively engage with customers on social media to address concerns and highlight positive feedback.
    * Implement changes based on customer feedback to improve overall satisfaction and sentiment.
    * Monitor trends in sentiment to proactively address potential issues before they escalate.
    
    """,
    "visualization_suggestions": """

    * Line charts showing sentiment trends over time.
    * Word clouds to visually represent the most frequently mentioned themes in customer sentiment.
    
    """,
    "risk_warnings": """

    * Negative sentiment can lead to customer churn and damage brand reputation.
    * Ignoring or mishandling negative sentiment can exacerbate issues and lead to public relations crises.
    
    """,
    "tracking_tools": """

    * Social media monitoring tools like Hootsuite or Sprout Social for real-time sentiment analysis.
    * Natural language processing (NLP) software to analyze and categorize customer comments and feedback.
    
    """,
    "integration_points": """

    * Integrate sentiment analysis with customer relationship management (CRM) systems to track sentiment at an individual customer level.
    * Link sentiment analysis with product development and marketing to align strategies with customer feedback.
    
    """,
    "change_impact_analysis": """

    * Improving customer sentiment can lead to increased customer loyalty and lifetime value.
    * However, changes in sentiment may also require adjustments in product offerings, customer service processes, or marketing strategies.
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Product Adoption", "Product Usage"], "last_validated": "2025-11-10T13:43:24.771350"},
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
                        15.7,
                        11.4,
                        11.6,
                        17.4,
                        17.5,
                        12.0,
                        16.2,
                        10.8,
                        12.0,
                        16.0,
                        14.0,
                        14.8
                ],
                "unit": "days"
        },
        "current": {
                "value": 14.8,
                "unit": "days",
                "change": 0.8,
                "change_percent": 5.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 14.12,
                "min": 10.8,
                "max": 17.5,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 2.58,
                        "percentage": 17.4
                },
                {
                        "category": "Category B",
                        "value": 2.49,
                        "percentage": 16.8
                },
                {
                        "category": "Category C",
                        "value": 2.87,
                        "percentage": 19.4
                },
                {
                        "category": "Category D",
                        "value": 1.01,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 5.85,
                        "percentage": 39.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.771350",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Social Media Sentiment Analysis"
        }
    },
}
