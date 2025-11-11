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
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Product Adoption", "Product Usage"], "last_validated": "2025-11-10T13:49:33.574830"},
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
                        13.4,
                        15.2,
                        10.0,
                        14.6,
                        16.3,
                        11.3,
                        12.9,
                        16.3,
                        10.7,
                        14.4,
                        9.8,
                        11.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 11.5,
                "unit": "days",
                "change": 1.7,
                "change_percent": 17.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 13.03,
                "min": 9.8,
                "max": 16.3,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.57,
                        "percentage": 22.3
                },
                {
                        "category": "Segment B",
                        "value": 1.88,
                        "percentage": 16.3
                },
                {
                        "category": "Segment C",
                        "value": 2.09,
                        "percentage": 18.2
                },
                {
                        "category": "Segment D",
                        "value": 0.67,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 4.29,
                        "percentage": 37.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.386691",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Social Media Sentiment Analysis"
        }
    },
}
