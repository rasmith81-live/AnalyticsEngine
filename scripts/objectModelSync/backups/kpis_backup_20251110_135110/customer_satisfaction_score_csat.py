"""
Customer Satisfaction Score (CSAT)

A metric that assesses how satisfied customers are with a company's products or services.
"""

CUSTOMER_SATISFACTION_SCORE_CSAT = {
    "code": "CUSTOMER_SATISFACTION_SCORE_CSAT",
    "name": "Customer Satisfaction Score (CSAT)",
    "description": "A metric that assesses how satisfied customers are with a company's products or services.",
    "formula": "Average of Customer Satisfaction Ratings on a Scale (e.g., 1-5)",
    "calculation_formula": "Average of Customer Satisfaction Ratings on a Scale (e.g., 1-5)",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Satisfaction Score (CSAT) to be added.",
    "trend_analysis": """


    * Increasing CSAT scores may indicate improved product quality or customer service.
    * Decreasing scores could signal issues with product performance, customer support, or overall satisfaction.
    
    
    """,
    "diagnostic_questions": """


    * What specific aspects of our products or services are contributing to higher or lower CSAT scores?
    * Are there common themes or patterns in customer feedback that correlate with changes in CSAT scores?
    
    
    """,
    "actionable_tips": """


    * Regularly solicit and act on customer feedback to address pain points and improve satisfaction.
    * Invest in training and development for customer-facing teams to enhance service quality.
    * Implement quality control measures to ensure products meet or exceed customer expectations.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing CSAT scores over time to identify trends and fluctuations.
    * Pie charts to visualize the distribution of satisfaction levels across different products or services.
    
    
    """,
    "risk_warnings": """


    * Low CSAT scores can lead to customer churn and negative word-of-mouth, impacting revenue and brand reputation.
    * Ignoring or neglecting customer feedback can result in missed opportunities for improvement and long-term success.
    
    
    """,
    "tracking_tools": """


    * Customer feedback and survey platforms like SurveyMonkey or Qualtrics for collecting and analyzing satisfaction data.
    * CRM systems with built-in CSAT tracking and reporting capabilities for seamless integration with customer interactions.
    
    
    """,
    "integration_points": """


    * Integrate CSAT data with customer relationship management systems to personalize interactions and address individual satisfaction concerns.
    * Link CSAT scores with product development and quality assurance processes to align improvements with customer needs.
    
    
    """,
    "change_impact_analysis": """


    * Improving CSAT scores can lead to increased customer loyalty and lifetime value, offsetting initial investment costs.
    * Conversely, declining CSAT scores may result in higher customer acquisition costs as a result of churn and negative reviews.
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"], "last_validated": "2025-11-10T13:49:32.876796"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
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
                        85.8,
                        85.2,
                        82.6,
                        79.0,
                        80.8,
                        86.0,
                        80.3,
                        78.7,
                        76.3,
                        76.3,
                        79.9,
                        74.4
                ],
                "unit": "score"
        },
        "current": {
                "value": 74.4,
                "unit": "score",
                "change": -5.5,
                "change_percent": -6.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 80.44,
                "min": 74.4,
                "max": 86.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.78,
                        "percentage": 27.9
                },
                {
                        "category": "Category B",
                        "value": 13.72,
                        "percentage": 18.4
                },
                {
                        "category": "Category C",
                        "value": 7.54,
                        "percentage": 10.1
                },
                {
                        "category": "Category D",
                        "value": 3.72,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 28.64,
                        "percentage": 38.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.351024",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Customer Satisfaction Score (CSAT)"
        }
    },
}
