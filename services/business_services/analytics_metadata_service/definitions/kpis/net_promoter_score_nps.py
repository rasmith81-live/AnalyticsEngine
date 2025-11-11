"""
Net Promoter Score (NPS)

A metric that gauges how likely a customer is to recommend a product or service to others. This KPI measures the satisfaction level of customers with the company's product or service.
"""

NET_PROMOTER_SCORE_NPS = {
    "code": "NET_PROMOTER_SCORE_NPS",
    "name": "Net Promoter Score (NPS)",
    "description": "A metric that gauges how likely a customer is to recommend a product or service to others. This KPI measures the satisfaction level of customers with the company's product or service.",
    "formula": "(Percentage of Promoters - Percentage of Detractors) * 100",
    "calculation_formula": "(Percentage of Promoters - Percentage of Detractors) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Net Promoter Score (NPS) to be added.",
    "trend_analysis": """



    * An increasing NPS may indicate improved product quality or customer service, leading to higher customer satisfaction.
    * A decreasing NPS could signal issues with product performance, customer support, or overall customer experience.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific aspects of the product or service that customers frequently praise or criticize?
    * How does our NPS compare with industry benchmarks or competitors in the same market?
    
    
    
    """,
    "actionable_tips": """



    * Invest in customer feedback mechanisms to understand the root causes of high or low NPS scores.
    * Implement customer service training programs to improve interactions and resolve issues effectively.
    * Regularly review and act on customer feedback to address pain points and enhance positive experiences.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing NPS trends over time to identify patterns and changes in customer sentiment.
    * Word clouds to visualize common themes in customer feedback related to NPS scores.
    
    
    
    """,
    "risk_warnings": """



    * Low NPS scores can lead to customer churn and negative word-of-mouth, impacting future sales and brand reputation.
    * Consistently high NPS scores may create complacency, masking underlying issues that need attention.
    
    
    
    """,
    "tracking_tools": """



    * Customer feedback and survey platforms like SurveyMonkey or Qualtrics to collect and analyze NPS data.
    * CRM systems to track customer interactions and identify areas for improvement based on NPS feedback.
    
    
    
    """,
    "integration_points": """



    * Integrate NPS data with customer relationship management (CRM) systems to align customer feedback with individual customer profiles.
    * Link NPS scores with sales and marketing platforms to tailor messaging and offers based on customer sentiment.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving NPS can lead to increased customer retention and loyalty, positively impacting long-term revenue and profitability.
    * Conversely, declining NPS scores can result in reduced customer lifetime value and hinder the company's growth prospects.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:33.068691"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
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
                        73.79,
                        65.53,
                        60.25,
                        77.8,
                        62.45,
                        64.48,
                        71.81,
                        74.66,
                        73.93,
                        74.52,
                        68.73,
                        75.24
                ],
                "unit": "%"
        },
        "current": {
                "value": 75.24,
                "unit": "%",
                "change": 6.51,
                "change_percent": 9.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 70.27,
                "min": 60.25,
                "max": 77.8,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20.05,
                        "percentage": 26.6
                },
                {
                        "category": "Segment B",
                        "value": 10.97,
                        "percentage": 14.6
                },
                {
                        "category": "Segment C",
                        "value": 10.81,
                        "percentage": 14.4
                },
                {
                        "category": "Segment D",
                        "value": 3.99,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 29.42,
                        "percentage": 39.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.229003",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Net Promoter Score (NPS)"
        }
    },
}
